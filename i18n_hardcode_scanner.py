#!/usr/bin/env python3
"""
Subvox i18n Hardcode Scanner  —  Scan, suggest, inject, translate.

A shareable tool that finds hardcoded French text across the entire
Next.js frontend, suggests i18n key names, and optionally injects them
into all 20 locale files + translates via DeepSeek.

Usage:

    # Dry-run (scan only, no changes — shareable report)
    python3 scripts/i18n-hardcode-scanner.py --dry-run

    # Full auto mode (inject + translate all locales)
    python3 scripts/i18n-hardcode-scanner.py --auto

    # Just inject keys into fr.json (no translation)
    python3 scripts/i18n-hardcode-scanner.py --inject

    # Translate existing fr.json changes to all locales
    python3 scripts/i18n-hardcode-scanner.py --translate

About namespace inference:
    Uses the file path to guess the next-intl namespace (BillingPage, HistoryPage, …).
    Always verify the guess — the script emits a warning when confidence is low.

About key naming:
    Converts French text to camelCase keys. Collisions get a _N suffix.
    Review and rename before using — automated naming is not perfect.

About the report:
    --dry-run generates a complete markdown report at
    scripts/i18n-reports/hardcode-scan-{timestamp}.md
    ready to share with the team.

Author: Nans
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import textwrap
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────────────────
PROJECT_ROOT = None  # Set via --project CLI arg
APP_DIR: Path | None = None
MSGS_DIR: Path | None = None
REPORTS_DIR: Path | None = None
# MSGS_DIR = PROJECT_ROOT / "app" / "messages"  # Set via --project
# REPORTS_DIR set via --project

# ── French detection ─────────────────────────────────────────────────────
FR_ACCENTS = re.compile(r"[éèêëàâçœùûüÿÉÈÊËÀÂÇŒÙÛÜŸ]", re.I)

# French-specific words — matched ONLY when the whole word is present.
# These are unaccented French words that would otherwise be invisible to
# the accent-based scanner.
FR_WORDS: set[str] = {
    "accueil", "aucun", "cout", "duree", "exporter", "plateforme",
    "precedent", "prive", "recherche", "retour", "suivant", "termine",
    "traduisez", "filigrane", "abonnement", "decouverte",
    "bibliotheque", "documentation", "gratuit", "passion",
    "inscription", "essai", "telecharger", "supprimer", "modifier",
    "ajouter", "creer", "choisir", "valider", "envoyer", "recevoir",
    "afficher", "masquer", "fermer", "annuler", "sauvegarder",
    "publier", "partager", "membre", "invite", "tableau", "projet",
    "parametre", "messagerie", "fichier", "confirmation",
    "videotheque", "sous-titres", "voix off", "tiers", "forfait",
}

# Words that LOOK French (have accents) but are actually:
#   - English / shared vocabulary
#   - JS variable/property names (camelCase identifiers)
#   - Other language names
FALSE_POSITIVES: set[str] = {
    # English / international
    "active", "video", "analyse", "description", "generation",
    "elements", "serie", "categorie", "regions", "administration",
    "archive", "commentaire", "client", "contact", "service",
    "studio", "credit", "format", "groupe", "mobile", "nature",
    "option", "passage", "poste", "presente", "produit",
    "programme", "proposition", "question", "reference",
    "reserve", "role", "signale", "structure", "technique",
    "version", "edition", "etape", "premiere",
    # Language names (not hardcoded FR)
    "francais", "française", "portugais", "turc", "turkce",
    "cest", "cette", "etes", "etre", "donnees", "faites",
    # JS identifiers / API fields (accented keys, not UI text)
    "duree", "video_count", "duree_totale", "scorequalite",
    "qualite", "visagesdetectes", "plaquesdetectes",
    "scenesdetectes", "editionliste", "tlcharger",
    "copie", "copier", "deja", "donne", "etat", "exemple",
    "fixe", "global", "grace", "image", "interet", "limite",
    "livre", "marche", "marque", "memoire", "metre",
    "modele", "nombre", "note", "ordre", "origine", "partie",
    "pensee", "pere", "place", "planete", "premiere",
    "presence", "pret", "probleme", "proche", "propre",
    "puis", "raison", "rapide", "reel", "reponse", "reste",
    "reunion", "revue", "risque", "scene", "secteur",
    "sensible", "seule", "seul", "signe", "simple",
    "solution", "souhait", "soumis", "sujet", "superieur",
    "surface", "surveiller", "symbole", "systeme", "table",
    "tache", "taille", "tard", "taux", "telephone",
    "temperature", "tendance", "tenir", "terre", "tete",
    "theme", "timbre", "titre", "toile", "tomber",
    "totalite", "tour", "trace", "traite", "tranche",
    "travail", "tresor", "triangle", "tribune", "triste",
    "trois", "tromper", "trop", "trouble", "trouver",
    "type", "unique", "usage", "valeur", "vaste",
    "vehicule", "vendredi", "venir", "vente", "verbe",
    "verre", "vers", "vert", "veste", "veteran",
    "viande", "victime", "vide", "vie", "vieux", "village",
    "ville", "vin", "visage", "visite", "visuel", "vite",
    "vitesse", "vivable", "vivant", "vivre", "vocal",
    "voici", "voie", "voir", "voisin", "voiture", "voix",
    "volume", "votre", "vouloir", "voyage", "vrai", "vue",
    "zero", "zone",
}

JUNK_WORDS: set[str] = {
    "août", "septembre", "octobre", "novembre", "decembre",
    "janvier", "fevrier", "mars", "avril", "mai", "juin",
    "juillet", "aout",
}

SKIP_LINE = re.compile(
    r"^(import |//|/\*|\* |type |interface |"
    r"export (type|interface)|\s*className=|\s*tailwind=|"
    r".*\.css|\s*@apply|use client|use server)"
)

SKIP_PATH_PATTERNS = [
    re.compile(p) for p in [
        r"node_modules", r"\.next", r"\.git",
    ]
]

# ── Key generation ───────────────────────────────────────────────────────

VOWELS: set[str] = {"a", "e", "i", "o", "u", "y", "é", "è", "ê", "ë", "à", "â"}


def _trim_accents(text: str) -> str:
    """Remove accents for slug generation, but keep letters readable."""
    mapping = {
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a",
        "ç": "c",
        "ù": "u", "û": "u", "ü": "u",
        "ô": "o", "ö": "o",
        "î": "i", "ï": "i",
        "É": "E", "È": "E", "Ê": "E", "Ë": "E",
        "À": "A", "Â": "A",
        "Ç": "C",
        "Ù": "U", "Û": "U", "Ü": "U",
        "Ô": "O", "Ö": "O",
        "Î": "I", "Ï": "I",
    }
    for a, b in mapping.items():
        text = text.replace(a, b)
    return text


def slugify(text: str) -> str:
    """Convert French text to a camelCase i18n key.

    Rules:
      - Remove punctuation, keep letters and digits
      - De-accent
      - First word lowercase, subsequent words capitalized
      - Max 45 chars
      - Strip leading digits
    """
    # De-accent first
    clean = _trim_accents(text)
    # Remove special chars except spaces, letters, digits
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", clean)
    words = clean.strip().lower().split()
    if not words:
        return "unnamed"
    key = words[0] + "".join(w.capitalize() for w in words[1:])
    # Strip leading digits
    key = re.sub(r"^\d+", "", key)
    if not key:
        key = "unnamed"
    # Trim to 45 chars
    return key[:45]


def infer_namespace(filepath: str) -> tuple[str, bool]:
    """Guess the next-intl namespace from the file path.

    Returns (namespace, high_confidence) where high_confidence is False
    when the guess is uncertain (component files, nested routes).
    """
    path = filepath.replace("app/", "").replace(".tsx", "")
    parts = [p for p in path.split("/") if p not in ("", ".")]

    # ── Page routes ────────────────────────────────────────────
    # app/page.tsx                        → HomePage (confident)
    # app/billing/page.tsx                → BillingPage (confident)
    # app/billing/history/page.tsx        → BillingHistoryPage (confident)
    # app/[locale]/fonctionnalites/…      → FonctionnalitesPage (confident)
    if parts and parts[-1] == "page":
        # Skip [locale] parameter
        route_parts = [p for p in parts[:-1] if not re.match(r"^\[.+\]$", p)]
        if route_parts:
            name = "".join(
                p[0].upper() + p[1:] for p in route_parts
            )
            return name + "Page", True
        return "HomePage", True

    # ── Component files ────────────────────────────────────────
    # components/Navbar.tsx               → Navbar (low confidence)
    # components/job/AnalysisBadges.tsx    → AnalysisBadges (low confidence)
    # We strip common suffixes for better grouping
    if parts:
        fname = parts[-1]
        fname = re.sub(
            r"(Card|Bar|List|Item|Form|Modal|Button|Input|"
            r"Select|Dropdown|Section|Row|Table|Chip|Badge)$",
            "",
            fname,
        )
        if fname:
            return fname[0].upper() + fname[1:], False
    return "Common", False


# ── Scanning engine ──────────────────────────────────────────────────────

ScanEntry = tuple[str, int, str, str, str]
"""
(relative_path, line_number, raw_text, suggested_key, detection_type)

detection_type is one of:
  JSX     — Text inside JSX tags (> text <)
  STRING  — String value in data definition / attribute
  ATTR    — Attribute value like placeholder=
  JSID    — JS camelCase identifier (low confidence, likely variable name)
"""


def _is_french_word(word: str) -> bool:
    """Check if a word looks French — either accented or known non-accented FR."""
    w = word.lower().strip(",.!?;:\"'()[]{}<>")
    if not w or len(w) < 2:
        return False
    if w in FALSE_POSITIVES:
        return False
    if w in JUNK_WORDS:
        return True
    if FR_ACCENTS.search(w):
        return True
    if w in FR_WORDS:
        return True
    return False


def _looks_like_js_id(text: str) -> bool:
    """Check if a string is likely a JS identifier (camelCase, snake_case, PascalCase)."""
    if " " in text or "\n" in text:
        return False
    # camelCase: starts lowercase, has uppercase mid-word
    if re.match(r"^[a-z][a-zA-Z0-9éèêëàâçùü_]*[A-Z]", text):
        return True
    # PascalCase: starts uppercase, has another uppercase later
    if re.match(r"^[A-Z][a-z]+[A-Z]", text):
        return True
    # snake_case: has underscores
    if "_" in text:
        return True
    # kebab-case
    if "-" in text:
        return True
    return False


def _is_technical_value(text: str) -> bool:
    """Check if a string is a technical value, not human-readable text.

    Returns True for: URLs, paths, CSS classes, hex colors, numbers,
    import specifiers, file extensions, single words that are identifiers.
    """
    t = text.strip()
    if not t or len(t) < 2:
        return True
    
    # URLs and paths
    if t.startswith(("http://", "https://", "/", "./", "../", "#")):
        return True
    if "." in t and not t.endswith((".", "!", "?")):
        # Could be a URL or file extension
        ext_patterns = (".com", ".org", ".io", ".png", ".jpg", ".svg", ".mp4",
                       ".ts", ".tsx", ".js", ".json", ".css", ".py", ".md")
        if any(t.lower().endswith(e) for e in ext_patterns):
            return True
    
    # Hex colors
    if re.match(r"^#[0-9a-fA-F]{3,8}$", t):
        return True
    
    # Pure numbers, dimensions
    if re.match(r"^[\d.,\s%]+$", t):
        return True

    # CSS/Tailwind class names — single or multiple space-separated
    # Each word must be a CSS class (lowercase, hyphens, colons, numbers, dots)
    css_words = t.split()
    if len(css_words) > 0:
        is_css = True
        for w in css_words:
            if not re.match(r"^[a-z][a-z0-9\-:/\[\]\(\)%.]*$", w) or len(w) < 2:
                is_css = False
                break
        if is_css:
            return True

    # Import-like or module paths
    if re.match(r"^[@a-z_][\w/@.-]*$", t) and "/" in t:
        return True

    # camelCase / snake_case single words (likely code identifiers)
    if _looks_like_js_id(t):
        return True
    
    # ALL_CAPS single word (constants, env vars)
    if re.match(r"^[A-Z][A-Z0-9_]+$", t) and " " not in t and len(t) > 1:
        return True
    
    # Code statements: const, let, var, function, import, export, return
    code_keywords = {"const", "let", "var", "function", "import", "export", "return",
                     "if", "else", "for", "while", "switch", "case", "break", "continue"}
    first_word = t.split()[0].lower().rstrip(";:,") if t.split() else ""
    if first_word in code_keywords:
        return True
    
    # Contains assignment operators (code, not text)
    if re.search(r"[=!<>]=|=>|->", t):
        return True
    
    # Indices like [0], [1], ...
    if re.match(r"^\[?\d+\]?$", t):
        return True
    
    return False


def _is_human_readable(text: str) -> bool:
    """Language-agnostic check: does this string look like human-readable UI text?

    Returns True if the string has properties of natural language text
    in ANY human language (French, Vietnamese, Arabic, CJK, etc.).
    """
    if _is_technical_value(text):
        return False

    # Strings with accents from any language (French, Spanish, German, etc.)
    # Includes Vietnamese: ăâđêôơư
    if re.search(r"[éèêëàâçùüôöîïÉÈÊËÀÂÇÙÜÔÖÎÏñÑßüÜäÄöÖăâđêôơưỠẪẨẲẴẶẤẦẬẮẰẲẴẶẾỀỂỄỆỐỒỔỖỘỚỜỞỠỢỨỪỬỮỰáạảãàâấầậắằẳẵặéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ]", text):
        return True

    # Strings with non-Latin scripts (Cyrillic, CJK, Arabic, etc.)
    if re.search(r"[А-Яа-яЁё]", text):  # Cyrillic
        return True
    if re.search(r"[\u4e00-\u9fff\u3400-\u4dbf]", text):  # CJK
        return True
    if re.search(r"[\u0600-\u06ff\u0750-\u077f]", text):  # Arabic
        return True
    if re.search(r"[\u0900-\u097f]", text):  # Devanagari
        return True
    if re.search(r"[\u0e00-\u0e7f]", text):  # Thai
        return True
    if re.search(r"[\u1f00-\u1fff]", text):  # Greek
        return True

    # Multi-word strings with mixed case (sentence-like)
    words = text.split()
    if len(words) >= 3:
        # 3+ words = very likely human text
        return True
    
    if len(words) == 2:
        # 2 words: check it's not a composite identifier
        accent_lower = r"a-zéèêëàâçùüôöîïñûœăâđêôơưáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
        # "Coût SUBVOX" pattern: capitalized word + uppercase/shout word
        if re.match(rf"^[A-Z][{accent_lower}]+ [A-Z][A-Z0-9]+$", text):
            return True
        # "Paiement annulé" pattern: two capitalized words
        if re.match(rf"^[A-Z][{accent_lower}]+ [A-Z]?[{accent_lower}]+$", text):
            return True
        # "Hello world" pattern: capitalized + lowercase
        if re.match(rf"^[A-Z][a-z]+ [{accent_lower}]+$", text):
            return True

    # Single word that starts uppercase followed by lowercase (proper noun / title)
    if re.match(r"^[A-Z][a-zéèêëàâçùüôöîïñûœăâđêôơưáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ]{3,}$", text):
        return True

    # Contains sentence punctuation
    if re.search(r"[.!?:;]$", text):
        return True
    
    # Contains emoji
    if re.search(r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U00002702-\U000027B0]", text):
        return True

    return False


def _is_french_word(word: str) -> bool:
    """Check if a word looks French — either accented or known non-accented FR."""
    w = word.lower().strip(",.!?;:\"'()[]{}<>")
    if not w or len(w) < 2:
        return False
    if w in FALSE_POSITIVES:
        return False
    if w in JUNK_WORDS:
        return True
    if FR_ACCENTS.search(w):
        return True
    if w in FR_WORDS:
        return True
    return False


def _has_french_text(text: str) -> bool:
    """Check if a string contains any French-looking text."""
    words = re.findall(r"\w+", text)
    french_count = sum(1 for w in words if _is_french_word(w))
    if french_count >= 2:
        return True
    if french_count == 1 and any(FR_ACCENTS.search(w) for w in words):
        return True
    return False


def _is_language_name(text: str) -> bool:
    langs = {
        "français", "francaise", "française", "anglais", "anglaise",
        "espagnol", "allemand", "italien", "portugais", "português",
        "turc", "türkçe", "russe", "arabe", "chinois", "japonais",
        "coreen", "neerlandais", "polonais", "ukrainien", "vietnamien",
        "persan", "hebreu", "hindi", "indonesien",
    }
    return text.strip().lower().rstrip("s") in langs


def _assertive_scan(line: str, mode: str = "french") -> list[tuple[str, str]]:
    """Find hardcoded strings inside quotes, skipping JS identifiers.

    mode="french" — detect French-specific text (accents, FR_WORDS).
    mode="universal" — detect any human-readable text (language-agnostic).

    Returns [(full_string_value, detection_type)].
    """
    results: list[tuple[str, str]] = []
    # Find quoted strings
    for m in re.finditer(r'"([^"]{2,100})"', line):
        val = m.group(1)
        if _looks_like_js_id(val):
            results.append((val, "JSID"))
        elif mode == "universal":
            if _is_human_readable(val):
                results.append((val, "STRING"))
        else:
            if _has_french_text(val) and not _is_language_name(val):
                results.append((val, "STRING"))
    # Find single-quoted strings
    for m in re.finditer(r"'([^']{2,100})'", line):
        val = m.group(1)
        if _looks_like_js_id(val):
            results.append((val, "JSID"))
        elif mode == "universal":
            if _is_human_readable(val):
                results.append((val, "STRING"))
        else:
            if _has_french_text(val) and not _is_language_name(val):
                results.append((val, "STRING"))
    return results
def scan_file(filepath: Path, mode: str = "french") -> list[ScanEntry]:
    """Scan a single .tsx file. Returns deduplicated entries."""
    relative = str(filepath.relative_to(PROJECT_ROOT))
    for pat in SKIP_PATH_PATTERNS:
        if pat.search(relative):
            return []

    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return []

    lines = content.split("\n")
    seen: set[tuple[int, str]] = set()
    results: list[ScanEntry] = []

    for i, line in enumerate(lines, 1):
        # ── Pass 1: JSX text nodes ──────────────────────────────
        # > text <  where text is 3–80 chars and not a JS expression
        for m in re.finditer(r">([^<]{3,80})<", line):
            text = m.group(1).strip()
            if not text or "{" in text:
                continue
            if mode == "universal":
                if not _is_human_readable(text):
                    continue
            else:
                if not _has_french_text(text):
                    continue
                if _is_language_name(text):
                    continue
            key = (i, text)
            if key in seen:
                continue
            seen.add(key)
            sk = slugify(text)
            results.append((relative, i, text, sk, "JSX"))

        # ── Pass 2: Quoted strings (French text in data, attrs) ─
        if SKIP_LINE.match(line.lstrip()):
            continue
        for val, det_type in _assertive_scan(line, mode):
            key = (i, val)
            if key in seen:
                continue
            seen.add(key)
            sk = slugify(val)
            if val.startswith(".") or val.startswith("/") or val.startswith("http"):
                continue
            # Skip pure JS identifiers (false positives from camelCase)
            if det_type == "JSID":
                continue
            results.append((relative, i, val, sk, "STRING"))

    return results


def scan_all(mode: str = "french") -> list[ScanEntry]:
    """Scan all .tsx and .ts files under app/."""
    all_results: list[ScanEntry] = []
    for root, dirs, files in os.walk(APP_DIR):
        for pat in ("node_modules", ".next", ".git"):
            if pat in root:
                dirs[:] = []
                break
        else:
            for fname in files:
                if not (fname.endswith(".tsx") or fname.endswith(".ts")):
                    continue
                all_results.extend(scan_file(Path(root) / fname, mode))
    return all_results


# ── Grouping ─────────────────────────────────────────────────────────────

def group_by_file(entries: list[ScanEntry]) -> dict[str, list[ScanEntry]]:
    grouped: dict[str, list[ScanEntry]] = defaultdict(list)
    for e in entries:
        grouped[e[0]].append(e)
    return dict(sorted(grouped.items()))


def group_by_namespace(entries: list[ScanEntry]) -> dict[str, list[ScanEntry]]:
    grouped: dict[str, list[ScanEntry]] = defaultdict(list)
    for e in entries:
        ns, _ = infer_namespace(e[0])
        grouped[ns].append(e)
    return dict(sorted(grouped.items()))


# ── Key collision resolution ─────────────────────────────────────────────

def resolve_keys(entries: list[ScanEntry], existing_fr: dict) -> dict[str, str]:
    """Map original text → final key, handling collisions within fr.json.

    Uses incremental _N suffix (text_alreadyExists → textAlreadyExists_2 → …).
    """
    mapping: dict[str, str] = {}
    used: set[str] = set()
    # Pre-populate with existing keys
    for ns_keys in existing_fr.values():
        if isinstance(ns_keys, dict):
            used.update(ns_keys.keys())

    for _, _, text, sk, _ in entries:
        if text in mapping:
            continue
        final = sk
        while final in used:
            # Try _2, _3, …
            num = 2
            while f"{sk}_{num}" in used:
                num += 1
            final = f"{sk}_{num}"
        mapping[text] = final
        used.add(final)

    return mapping


# ── Report generation ────────────────────────────────────────────────────

def _ns_summary(entries: list[ScanEntry]) -> dict:
    """Build a namespace summary from entries."""
    by_ns: dict[str, int] = defaultdict(int)
    by_file: dict[str, int] = defaultdict(int)
    by_type: dict[str, int] = defaultdict(int)
    for e in entries:
        ns, _ = infer_namespace(e[0])
        by_ns[ns] += 1
        by_file[e[0]] += 1
        by_type[e[4]] += 1
    return {
        "total": len(entries),
        "files": len(by_file),
        "namespaces": len(by_ns),
        "by_ns": dict(sorted(by_ns.items())),
        "by_type": dict(by_type),
    }


def generate_markdown_report(
    entries: list[ScanEntry],
    ns_keys: dict[str, list[tuple[str, str, str]]] | None = None,
    dry_run: bool = True,
) -> str:
    """Generate a beautiful, shareable markdown report."""
    summary = _ns_summary(entries)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = [
        f"# Subvox i18n — Hardcoded French Scan Report",
        f"",
        f"**Date:** {timestamp}  ",
        f"**Mode:** {'Dry-run (no changes)' if dry_run else 'Auto'}  ",
        f"**Total:** {summary['total']} occurrences · {summary['files']} files · {summary['namespaces']} namespaces  ",
        f"",
        f"---",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Files affected | {summary['files']} |",
        f"| Total hardcoded strings | {summary['total']} |",
        f"| Namespaces needed | {summary['namespaces']} |",
        f"| JSX text nodes | {summary['by_type'].get('JSX', 0)} |",
        f"| String/attr values | {summary['by_type'].get('STRING', 0)} |",
        f"",
        f"### Per-namespace breakdown",
        f"",
        f"| Namespace | Count | Status |",
        f"|-----------|-------|--------|",
    ]

    for ns, count in sorted(summary["by_ns"].items()):
        status = "✅ keys injected"
        if ns_keys and ns in ns_keys:
            status = f"✅ {len(ns_keys[ns])} keys injected"
        elif dry_run:
            status = "🔍 scanned"
        lines.append(f"| `{ns}` | {count} | {status} |")

    lines.extend([
        "",
        "---",
        "",
        "## Detailed findings",
        "",
    ])

    grouped = group_by_namespace(entries)
    by_file_grouped = group_by_file(entries)

    for ns in sorted(grouped):
        ns_entries = grouped[ns]
        ns_ci, confident = infer_namespace(ns_entries[0][0])
        confidence = "" if confident else " ⚠️ inferred (verify)"
        lines.append(f"### {ns}{confidence}")
        lines.append("")
        lines.append(f"`{len(ns_entries)} strings across {len(set(e[0] for e in ns_entries))} files`")
        lines.append("")

        # Table header
        lines.append("| File | Line | Text | Suggested key | Detected as |")
        lines.append("|------|------|------|---------------|-------------|")

        for e in ns_entries:
            rel, ln, text, sk, dtype = e
            fname = rel.replace("app/", "")
            type_icon = {
                "JSX": "`JSX`",
                "STRING": "`string`",
            }.get(dtype, f"`{dtype}`")
            text_esc = text.replace("|", "\\|").replace("\n", " ").strip()
            lines.append(f"| `{fname}` | `{ln}` | {text_esc} | `{sk}` | {type_icon} |")

        lines.append("")

    # ── Replacement code suggestions ──────────────────────────
    lines.extend([
        "---",
        "",
        "## Replacement guide",
        "",
        "For each file, add `const t = useTranslations(\"Namespace\")` and replace:",
        "",
    ])

    current_ns = None
    for ns in sorted(grouped):
        for e in grouped[ns]:
            rel, ln, text, sk, dtype = e
            ns_shown, _ = infer_namespace(rel)
            if ns_shown != current_ns:
                current_ns = ns_shown
                lines.append(f"### {ns_shown}")
                lines.append("")
                lines.append("```tsx")
                lines.append(f"const t = useTranslations(\"{ns_shown}\");")
                lines.append("```")
                lines.append("")

            t_call = f'{{t("{sk}")}}'
            lines.append(f"- **`{rel}` L{ln}**: `{text[:50]}` → `{t_call}`")

    lines.extend([
        "",
        "---",
        "",
        "*Report generated by `scripts/i18n-hardcode-scanner.py`*",
        "",
    ])

    return "\n".join(lines)


def print_report(entries: list[ScanEntry], ns_keys: dict | None = None, dry_run: bool = True):
    """Print the report to stdout."""
    md = generate_markdown_report(entries, ns_keys, dry_run)
    print(md)

    # Also save to file
    if dry_run:
        if REPORTS_DIR is not None:
            REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = Path(f"hardcode-scan-{ts}.md") if REPORTS_DIR is None else REPORTS_DIR / f"hardcode-scan-{ts}.md"
        report_path.write_text(md, encoding="utf-8")
        print(f"\n📄 Report saved to: {report_path.relative_to(PROJECT_ROOT)}\n")


# ── Key injection into fr.json ──────────────────────────────────────────

INJECT_WARN = """\
⚠️  DRY-RUN MODE — no files modified.
   Pass --inject or --auto to apply changes.
"""


def inject_keys(
    entries: list[ScanEntry],
    dry_run: bool = True,
) -> dict[str, list[tuple[str, str, str]]] | None:
    """Inject new keys into fr.json, grouped by namespace.

    Returns mapping: namespace → [(key, french_text, source_file)].
    None when dry_run (no changes).
    """
    if dry_run:
        print(INJECT_WARN)
        return None

    fp = MSGS_DIR / "fr.json"
    with open(fp, encoding="utf-8") as f:
        fr = json.load(f)

    mapping = resolve_keys(entries, fr)
    namespace_keys: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    injected = 0
    errors = 0

    for e in entries:
        rel, _, text, _, _ = e
        ns, confident = infer_namespace(rel)
        key = mapping[text]

        if ns not in fr:
            fr[ns] = {}
            print(f"  📁 Created namespace `{ns}`")

        if key in fr[ns]:
            if fr[ns][key] == text:
                continue  # Already exists with same value
            else:
                # Key collision: same key, different FR value — add suffix
                num = 2
                while f"{key}_{num}" in fr[ns]:
                    num += 1
                key = f"{key}_{num}"
                print(f"  ⚠️  Collision `{key}` → renamed to `{key}`")

        if not confident:
            print(f"  ⚠️  Low-confidence namespace `{ns}` for {rel} — verify.")

        fr[ns][key] = text
        namespace_keys[ns].append((key, text, rel))
        injected += 1

    with open(fp, "w", encoding="utf-8") as f:
        json.dump(fr, f, indent=2, ensure_ascii=False)
    print(f"\n  ✅ {injected} keys injected into fr.json")

    return dict(namespace_keys)


# ── DeepSeek translation ──────────────────────────────────────────────────

LOCALE_NAMES: dict[str, str] = {
    "ar": "Arabic",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fa": "Persian",
    "he": "Hebrew",
    "hi": "Hindi",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "nl": "Dutch",
    "pl": "Polish",
    "pt": "Portuguese",
    "ru": "Russian",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh": "Chinese",
}

DEEPSEEK_API = "https://api.deepseek.com/v1/chat/completions"


def _read_deepseek_key() -> str | None:
    """Read DeepSeek from Hermes auth.json → credential_pool.deepseek[0].access_token."""
    auth_path = os.path.expanduser("~/.hermes/auth.json")
    try:
        with open(auth_path) as f:
            auth = json.load(f)
        for entry in auth.get("credential_pool", {}).get("deepseek", []):
            key = entry.get("access_token") or entry.get("api_key")
            if key:
                return key
    except Exception:
        pass
    return os.environ.get("DEEPSEEK_API_KEY")


def _translate_batch(
    texts: list[str],
    lang_name: str,
    api_key: str,
) -> dict[str, str]:
    """Translate a batch of FR texts → target language via DeepSeek.

    Returns {french_text: translated_text}.
    Falls back to original French on failure.
    """
    items = "\n".join(f"<{i}> {t}" for i, t in enumerate(texts))
    prompt = (
        f"Translate these French texts to {lang_name}.\n"
        f"Preserve {{placeholder}} variables exactly.\n"
        f"Return each translation on its own line, preserving the <id> markers.\n\n"
        f"FR:\n{items}\n\n"
        f"{lang_name}:"
    )
    for attempt in range(3):
        try:
            import httpx
            r = httpx.post(
                DEEPSEEK_API,
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {
                            "role": "system",
                            "content": f"You are a translator FR→{lang_name}. Return ONLY translations, numbered.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.1,
                    "max_tokens": 3000,
                },
                timeout=120,
            )
            content = r.json()["choices"][0]["message"]["content"]
            result: dict[str, str] = {}
            for line in content.strip().split("\n"):
                m = re.match(r"<(\d+)>\s*(.*)", line.strip())
                if m:
                    idx = int(m.group(1))
                    if idx < len(texts):
                        result[texts[idx]] = m.group(2).strip()
            for t in texts:
                if t not in result:
                    result[t] = t  # fallback to FR
            return result
        except Exception as e:
            print(f"      ⚠️  Retry {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(3)
    return {t: t for t in texts}


def translate_all(
    namespace_keys: dict[str, list[tuple[str, str, str]]],
    dry_run: bool = True,
) -> None:
    """Translate newly injected keys to all 19 non-FR locales."""
    if dry_run:
        print(INJECT_WARN)
        return

    api_key = _read_deepseek_key()
    if not api_key:
        print("❌ DeepSeek key not found. Could not translate.")
        print(
            "   Check ~/.hermes/auth.json → credential_pool.deepseek[0].access_token"
        )
        sys.exit(1)

    print("\n🌍 Translating to all locales…\n")

    total_keys = sum(len(v) for v in namespace_keys.values())
    done = 0

    # Collect all unique (ns, key, fr_value) triples
    all_pending: list[tuple[str, str, str]] = []
    for ns, keys in namespace_keys.items():
        for k, v, _ in keys:
            all_pending.append((ns, k, v))

    for locale, lang_name in sorted(LOCALE_NAMES.items()):
        fp = MSGS_DIR / f"{locale}.json"
        with open(fp, encoding="utf-8") as f:
            data = json.load(f)

        missing: list[tuple[str, str, str]] = [
            (ns, k, v) for ns, k, v in all_pending
            if ns not in data or k not in data.get(ns, {})
        ]

        if not missing:
            print(f"  ⏭️  {locale} ({lang_name}) — already up to date")
            continue

        texts = [v for _, _, v in missing]
        print(f"  → {locale} ({lang_name}) — {len(texts)} keys…", end=" ", flush=True)

        if locale == "en":
            # English: copy FR as placeholder
            for ns, k, v in missing:
                if ns not in data:
                    data[ns] = {}
                data[ns][k] = v
            print("✅ (copied from FR)")
        else:
            translations = _translate_batch(texts, lang_name, api_key)
            for ns, k, v in missing:
                if ns not in data:
                    data[ns] = {}
                data[ns][k] = translations.get(v, v)
            print("✅")

        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        done += len(missing)
        time.sleep(0.3)  # rate limit

    print(f"\n✅ {done} keys translated across {len(LOCALE_NAMES)} locales")


# ── Replacement script generator ─────────────────────────────────────────

def generate_replacement_script(entries: list[ScanEntry]) -> str:
    """Generate a shell script with commented patch() calls for review."""
    by_file = group_by_file(entries)
    lines: list[str] = [
        "#!/bin/bash",
        "# =======================================================================",
        "# i18n-replacements.sh — Auto-generated i18n replacement candidates",
        "#",
        "# HOW TO USE:",
        "#   1. Review each patch line (they are COMMENTED OUT)",
        "#   2. Uncomment the ones you want to apply",
        "#   3. Run: bash scripts/i18n-replacements.sh",
        "#",
        "# IMPORTANT:",
        "#   - Add `import { useTranslations } from \"next-intl\"` to each file",
        "#   - Add `const t = useTranslations(\"Namespace\")` in the component body",
        "#   - The patches below only replace INLINE text, not add imports",
        "# =======================================================================",
        "",
    ]

    for path in sorted(by_file):
        entries_list = by_file[path]
        ns, confident = infer_namespace(path)
        lines.append(f"# ── {path} ─────────────────────────────────────")
        lines.append(f"#   Namespace: {ns} {'⚠️  (verify)' if not confident else ''}")
        lines.append(f"#   Add: const t = useTranslations(\"{ns}\");")
        lines.append("")

        for e in entries_list:
            rel, ln, text, sk, dtype = e
            t_call = f'{{t("{sk}")}}'
            # Build a safe old_string/new_string pair
            escaped = text.replace("'", "\\'")
            lines.append(f"# L{ln}: \"{text[:60]}\" → {t_call}")
            if len(text) > 3:
                # Produce a patch command
                lines.append(
                    f"# patch --path \"{rel}\" \\"
                )
                lines.append(
                    f"#       --old-string '{escaped}' \\"
                )
                lines.append(
                    f"#       --new-string '{t_call}'"
                )
            lines.append("")

        lines.append("")

    return "\n".join(lines)


# ── Safe patching ─────────────────────────────────────────────────────────

def _has_tsx_syntax_error(content: str, filepath: str = "<file>") -> list[str]:
    """Basic TSX syntax check — bracket balance + JSX tag balance.

    Returns a list of errors found (empty = OK).
    This is NOT a full TypeScript check, but catches the most common
    mistakes: unbalanced braces, broken JSX, t() inside strings.
    """
    errors: list[str] = []

    # 1. Brace balance
    stack: list[str] = []
    for i, ch in enumerate(content):
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            expected = {"(": ")", "{": "}", "[": "]"}.get(
                stack[-1] if stack else ""
            )
            if ch != expected:
                errors.append(
                    f"  L~{content[:i].count(chr(10)) + 1}: "
                    f"Unbalanced brace: expected '{expected}', got '{ch}'"
                )
                return errors
            stack.pop()

    if stack:
        errors.append(f"  Unclosed braces: {''.join(stack)} remaining")

    # 2. Detect t() calls inside HTML attribute values
    for i, line in enumerate(content.split("\n"), 1):
        tag_match = re.search(r'<([^>]*)>', line)
        if not tag_match:
            continue
        tag_body = tag_match.group(1)
        if re.search(r'=[\'"][^\'"]*\{t\(', tag_body):
            errors.append(
                f"  L{i}: t() call INSIDE HTML attribute — will render as "
                f"literal text: {line.strip()[:70]}"
            )

    return errors

def _add_import_use_translations(content: str) -> tuple[str, bool]:
    """Add `import { useTranslations } from "next-intl"` if missing.

    Returns (modified_content, was_modified).
    Insertion point: after the last existing import, or at the top of the file.
    """
    if 'from "next-intl"' in content or "from 'next-intl'" in content:
        return content, False  # already imported

    lines = content.split("\n")
    last_import_idx = -1
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("import ") and (
            '"next-intl' in stripped or "'next-intl" in stripped
        ):
            return content, False  # already imported (catches next-intl/server etc)
        if stripped.startswith("import "):
            last_import_idx = i

    insert_at = last_import_idx + 1 if last_import_idx >= 0 else 0
    lines.insert(insert_at, 'import { useTranslations } from "next-intl";')
    return "\n".join(lines), True


def _add_t_declaration(content: str, namespace: str, filepath: str) -> tuple[str, bool]:
    """Add `const t = useTranslations("Namespace")` after the last import.

    Returns (modified_content, was_modified).
    The user may need to move it inside their component body.
    """
    if f'const t = useTranslations("' in content or f"const t = useTranslations('" in content:
        return content, False  # already has a t() declaration

    # Check if already has t from props or other context
    if re.search(r'\bt\b', content.split("export")[0] if "export" in content else ""):
        # t might be used as prop — skip to be safe
        return content, False

    lines = content.split("\n")
    # Find last import line
    last_import = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("import ") or line.strip().startswith("//"):
            last_import = i

    # Find "use client" or "use server" directives
    use_directives_end = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('"use ') or line.strip().startswith("'use "):
            use_directives_end = i + 1

    insert_at = max(last_import + 1, use_directives_end)
    # Fast-forward past blank lines
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1

    indent = ""
    if insert_at < len(lines):
        leading = re.match(r"^(\s*)", lines[insert_at])
        if leading:
            indent = leading.group(1)
    if not indent:
        indent = ""

    decl = f"{indent}const t = useTranslations(\"{namespace}\");"
    lines.insert(insert_at, decl)

    return "\n".join(lines), True


def patch_file_safe(
    filepath: str,
    entries: list[ScanEntry],
    namespace: str,
    dry_run: bool = True,
) -> dict:
    """Safely patch a single file: add import, add t(), replace JSX text.

    Returns a dict with:
      - modified: bool
      - errors: list[str]
      - replacements: list[tuple[old_text, new_text, line]]
      - diff_lines: list[str]
    """
    abs_path = PROJECT_ROOT / filepath
    if not abs_path.exists():
        return {"modified": False, "errors": [f"File not found: {filepath}"], "replacements": [], "diff_lines": []}

    with open(abs_path, encoding="utf-8") as f:
        original = f.read()

    content = original
    result: dict = {
        "modified": False,
        "errors": [],
        "replacements": [],
        "diff_lines": [],
    }

    # 1. Add import if needed
    content, import_added = _add_import_use_translations(content)
    if import_added:
        result["replacements"].append(("(import)", 'import { useTranslations } from "next-intl"', 1))

    # 2. Add t() declaration — but only for JSX entries (safe)
    jsx_entries = [e for e in entries if e[4] == "JSX"]
    if jsx_entries:
        content, t_added = _add_t_declaration(content, namespace, filepath)
        if t_added:
            result["replacements"].append(
                ("(t declaration)", f'const t = useTranslations("{namespace}")', 1)
            )

    # 3. Replace JSX text: >text< → >{t("key")}<
    lines = content.split("\n")
    modified_lines = list(lines)
    replacement_count = 0

    for e in entries:
        rel, ln, text, sk, dtype = e
        if dtype != "JSX":
            continue  # Skip data arrays — too risky to auto-replace

        idx = ln - 1
        if idx >= len(modified_lines):
            continue

        old_line = modified_lines[idx]
        t_call = f'{{t("{sk}")}}'

        # Replace JSX text node: >text< → >{t("key")}<
        # Only replace the EXACT occurrence
        if f">{text}<" in old_line:
            new_line = old_line.replace(f">{text}<", f">{t_call}<", 1)
            if new_line != old_line:
                modified_lines[idx] = new_line
                replacement_count += 1
                result["replacements"].append((text, t_call, ln))

    content = "\n".join(modified_lines)

    # 4. Syntax check
    syntax_errors = _has_tsx_syntax_error(content, filepath)
    if syntax_errors:
        result["errors"].extend(syntax_errors)
        # Don't save if there are errors
        return result

    # 5. Write
    if content != original and not dry_run:
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
        result["modified"] = True
    elif content != original:
        result["modified"] = True  # would have been modified

    # Generate diff
    if content != original:
        orig_lines = original.split("\n")
        new_lines = content.split("\n")
        for i, (ol, nl) in enumerate(zip(orig_lines, new_lines)):
            if ol != nl:
                result["diff_lines"].append(f"  L{i+1}: -{ol[:80]}")
                result["diff_lines"].append(f"         +{nl[:80]}")
        # Handle added/removed lines
        if len(new_lines) > len(orig_lines):
            for i in range(len(orig_lines), len(new_lines)):
                result["diff_lines"].append(f"  L{i+1}: +{new_lines[i][:80]}")
        elif len(new_lines) < len(orig_lines):
            for i in range(len(new_lines), len(orig_lines)):
                result["diff_lines"].append(f"  L{i+1}: -{orig_lines[i][:80]}")

    return result


def patch_all_safe(
    entries: list[ScanEntry],
    dry_run: bool = True,
) -> dict:
    """Safely patch all files with JSX text replacements.

    Returns a summary dict with per-file results.
    """
    by_file = group_by_file(entries)
    summary: dict = {
        "files_scanned": len(by_file),
        "files_modified": 0,
        "files_with_errors": 0,
        "total_replacements": 0,
        "total_errors": 0,
        "details": {},
    }

    for filepath in sorted(by_file):
        file_entries = by_file[filepath]
        ns, _ = infer_namespace(filepath)
        jsx_count = sum(1 for e in file_entries if e[4] == "JSX")
        string_count = sum(1 for e in file_entries if e[4] == "STRING")

        if jsx_count == 0:
            summary["details"][filepath] = {
                "status": "skipped",
                "reason": f"No JSX text to replace ({string_count} STRING entries need manual migration)",
                "jsx_count": jsx_count,
                "string_count": string_count,
            }
            continue

        result = patch_file_safe(filepath, file_entries, ns, dry_run=dry_run)
        summary["details"][filepath] = result

        if result["errors"]:
            summary["files_with_errors"] += 1
            summary["total_errors"] += len(result["errors"])
        if result["modified"]:
            summary["files_modified"] += 1
            summary["total_replacements"] += len(result["replacements"])

    return summary


def print_patch_summary(summary: dict, dry_run: bool):
    """Print a human-readable summary of the safe patching results."""
    mode = "🔍 DRY-RUN" if dry_run else "💉 APPLIED"
    print(f"\n{'=' * 70}")
    print(f"  PATCH SUMMARY — {mode}")
    print(f"  {summary['files_scanned']} files · "
          f"{summary['files_modified']} modified · "
          f"{summary['files_with_errors']} with errors")
    print(f"  {summary['total_replacements']} replacements · "
          f"{summary['total_errors']} errors")
    print(f"{'=' * 70}")

    for filepath, result in sorted(summary["details"].items()):
        if isinstance(result, dict) and result.get("status") == "skipped":
            continue

        status = (
            "✅" if isinstance(result, dict) and result.get("modified") and not result.get("errors")
            else "⚠️ " if isinstance(result, dict) and result.get("errors")
            else "⏭️ "
        )
        label = filepath.replace("app/", "")
        replacements = len(result["replacements"])
        errors = len(result["errors"])
        print(f"\n  {status} {label} ({replacements} replacements{', ' + str(errors) + ' errors' if errors else ''})")

        if result["errors"]:
            for err in result["errors"]:
                print(f"     ❌ {err}")

        if result["diff_lines"]:
            for dl in result["diff_lines"][:8]:  # limit to first 8 diff lines
                print(f"     {dl}")
            if len(result["diff_lines"]) > 8:
                print(f"     ... ({len(result['diff_lines']) - 8} more lines)")

    skipped = sum(
        1 for v in summary["details"].values()
        if isinstance(v, dict) and v.get("status") == "skipped"
    )
    if skipped:
        print(f"\n  ⏭️  {skipped} files skipped (no JSX text, STRING-only — needs manual migration)")
    print()



# ── CI & stale detection ───────────────────────────────────────────────

BASELINE_FILE = ".i18n-baseline.json"


def _baseline_path() -> Path:
    """Path to the baseline file in the project root."""
    if PROJECT_ROOT is None:
        return Path.cwd() / BASELINE_FILE
    return PROJECT_ROOT / BASELINE_FILE


def _load_baseline() -> dict:
    bp = _baseline_path()
    if bp.exists():
        with open(bp, encoding="utf-8") as f:
            return json.load(f)
    return {"hardcoded": {}, "fr_values": {}, "timestamp": None}


def _save_baseline(data: dict):
    bp = _baseline_path()
    with open(bp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  💾 Baseline saved: {bp}")


def _build_baseline(entries: list[ScanEntry]) -> dict:
    """Build a baseline snapshot from scan results."""
    hardcoded: dict[str, list[dict]] = {}
    for e in entries:
        rel, ln, text, sk, dtype = e
        hardcoded.setdefault(rel, []).append({
            "line": ln, "text": text, "key": sk, "type": dtype
        })
    # Snapshot fr.json values
    fr_values: dict[str, dict[str, str]] = {}
    if MSGS_DIR is not None and (MSGS_DIR / "fr.json").exists():
        with open(MSGS_DIR / "fr.json", encoding="utf-8") as f:
            fr = json.load(f)
        for ns, keys in fr.items():
            if isinstance(keys, dict):
                fr_values[ns] = {k: v for k, v in keys.items() if isinstance(v, str)}
    return {
        "hardcoded": hardcoded,
        "fr_values": fr_values,
        "timestamp": datetime.now().isoformat(),
    }


def ci_save(entries: list[ScanEntry]):
    """Save current scan as baseline. Run after cleaning all hardcoded text."""
    data = _build_baseline(entries)
    _save_baseline(data)
    print(f"  📊 {len(entries)} entries baseline saved "
          f"({len(data['fr_values'])} namespaces in fr.json)")
    return data


def ci_check(entries: list[ScanEntry]) -> int:
    """Compare current scan against baseline. Returns number of NEW hardcoded texts."""
    baseline = _load_baseline()
    if not baseline.get("hardcoded"):
        print("  ⚠️  No baseline found. Run --ci-save first.")
        return 0

    # Build lookup of baseline texts per file
    baseline_texts: dict[str, set[str]] = {}
    for rel, texts in baseline.get("hardcoded", {}).items():
        baseline_texts[rel] = {t["text"] for t in texts}

    new_entries: list[ScanEntry] = []
    for e in entries:
        rel, ln, text, sk, dtype = e
        baseline_set = baseline_texts.get(rel, set())
        if text not in baseline_set:
            new_entries.append(e)

    if not new_entries:
        print(f"  ✅ Baseline: {len(baseline['hardcoded'])} occurrences — no regressions")
        return 0

    print(f"\n  ❌ {len(new_entries)} NEW hardcoded texts found since baseline!\n")
    by_file: dict[str, list[ScanEntry]] = {}
    for e in new_entries:
        by_file.setdefault(e[0], []).append(e)
    for path in sorted(by_file):
        for e in by_file[path]:
            print(f"      {e[0]}:{e[1]} → {e[2][:60]}")
    return len(new_entries)


def check_stale() -> int:
    """Compare current fr.json values against baseline. Returns count of changed keys."""
    baseline = _load_baseline()
    if not baseline.get("fr_values"):
        print("  ⚠️  No baseline found. Run --ci-save first.")
        return 0

    if MSGS_DIR is None or not (MSGS_DIR / "fr.json").exists():
        print("  ⚠️  fr.json not found.")
        return 0

    with open(MSGS_DIR / "fr.json", encoding="utf-8") as f:
        current_fr = json.load(f)

    stale_count = 0
    baseline_fr = baseline["fr_values"]

    for ns, keys in current_fr.items():
        if not isinstance(keys, dict):
            continue
        baseline_ns = baseline_fr.get(ns, {})
        for k, v in keys.items():
            if not isinstance(v, str):
                continue
            old_v = baseline_ns.get(k)
            if old_v is not None and old_v != v:
                if stale_count == 0:
                    print(f"\n  🔄 Stale translations detected (FR value changed):\n")
                print(f"      {ns}.{k}")
                print(f"        was: {old_v[:60]}")
                print(f"        now: {v[:60]}")
                stale_count += 1

    if stale_count == 0:
        print(f"  ✅ All {sum(len(v) for v in baseline_fr.values() if isinstance(v, dict))} FR keys unchanged")
    return stale_count


def update_stale(api_key: str) -> int:
    """Retranslate stale keys (where FR value changed) via DeepSeek."""
    import httpx
    stale_count = check_stale()
    if stale_count == 0:
        return 0

    baseline = _load_baseline()
    baseline_fr = baseline.get("fr_values", {})

    if MSGS_DIR is None:
        return 0

    with open(MSGS_DIR / "fr.json", encoding="utf-8") as f:
        current_fr = json.load(f)

    # Collect stale (ns, key, new_fr_value) per namespace
    stale_by_ns: dict[str, list[tuple[str, str]]] = {}
    for ns, keys in current_fr.items():
        if not isinstance(keys, dict):
            continue
        baseline_ns = baseline_fr.get(ns, {})
        for k, v in keys.items():
            if not isinstance(v, str):
                continue
            old_v = baseline_ns.get(k)
            if old_v is not None and old_v != v:
                stale_by_ns.setdefault(ns, []).append((k, v))

    total_updated = 0
    for locale, lang_name in sorted(LOCALE_NAMES.items()):
        fp = MSGS_DIR / f"{locale}.json"
        
        # English: just copy new FR
        if locale == "en":
            with open(fp, encoding="utf-8") as f:
                en_data = json.load(f)
            for ns, keys in stale_by_ns.items():
                if ns not in en_data:
                    en_data[ns] = {}
                for k, v in keys:
                    en_data[ns][k] = v
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(en_data, f, indent=2, ensure_ascii=False)
            total_updated += sum(len(v) for v in stale_by_ns.values())
            print(f"  → en — {sum(len(v) for v in stale_by_ns.values())} keys (copied FR)")
            continue

        # Other locales: translate via DeepSeek
        all_texts = [v for keys in stale_by_ns.values() for _, v in keys]
        if not all_texts:
            continue

        print(f"  → {locale} ({lang_name}) — {len(all_texts)} keys...", end=" ", flush=True)
        translations = _translate_batch(all_texts, lang_name, api_key)
        
        with open(fp, encoding="utf-8") as f:
            data = json.load(f)

        idx = 0
        for ns, keys in stale_by_ns.items():
            if ns not in data:
                data[ns] = {}
            for k, v in keys:
                data[ns][k] = translations.get(v, v)
                idx += 1

        with open(fp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("✅")
        total_updated += len(all_texts)

    # Update baseline with new fr values
    new_baseline = _build_baseline([])  # Get fresh timestamp + fr snapshot
    with open(_baseline_path(), encoding="utf-8") as f:
        existing = json.load(f)
    existing["fr_values"] = new_baseline["fr_values"]
    existing["timestamp"] = new_baseline["timestamp"]
    _save_baseline(existing)

    print(f"\n  ✅ {total_updated} keys updated across {len(LOCALE_NAMES)} locales")
    return total_updated


# ── Main CLI ─────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Subvox i18n Hardcode Scanner — scan, suggest, inject, translate.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              %(prog)s --dry-run            # Scan only, generate report
              %(prog)s --inject              # Inject keys into fr.json only
              %(prog)s --translate           # Translate fr.json changes to all locales
              %(prog)s --auto                # Full pipeline: inject + translate
        """),
    )
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="Path to your Next.js project root (e.g. ./my-app)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scan only — generate report, no file modifications (default if no mode given)",
    )
    parser.add_argument(
        "--universal",
        action="store_true",
        help="Scan for hardcoded text in ANY language (not just French)",
    )
    parser.add_argument(
        "--patch-safe", "--patch",
        action="store_true",
        dest="patch_safe",
        help="Apply safe patches: add import/t(), replace JSX text, verify syntax",
    )
    parser.add_argument(
        "--inject",
        action="store_true",
        help="Inject discovered keys into fr.json",
    )
    parser.add_argument(
        "--translate",
        action="store_true",
        help="Translate existing fr.json changes to all locales",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Full pipeline: scan → inject → translate (equivalent to --inject + --translate)",
    )
    parser.add_argument(
        "--ci-save",
        action="store_true",
        help="Save current scan as baseline for CI comparison",
    )
    parser.add_argument(
        "--ci",
        action="store_true",
        help="CI mode: compare scan against baseline, exit 1 if new hardcoded text found",
    )
    parser.add_argument(
        "--check-stale",
        action="store_true",
        help="Check for FR keys whose value changed since baseline (stale translations)",
    )
    parser.add_argument(
        "--update-stale",
        action="store_true",
        help="Retranslate stale FR keys to all locales via DeepSeek",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default=None,
        help="Save report to specific path (default: scripts/i18n-reports/hardcode-scan-{timestamp}.md)",
    )

    args = parser.parse_args()

    if not args.project:
        print("\n  ❌ --project is required. Point it to your Next.js frontend root.")
        print("     Example: python3 i18n_hardcode_scanner.py --project ./my-app --dry-run\n")
        sys.exit(1)

    project_path = Path(args.project).resolve()
    if not (project_path / "app").exists() or not (project_path / "app" / "messages").exists():
        print(f"\n  ❌ {project_path / 'app'} or {project_path / 'app' / 'messages'} not found.")
        print("     Make sure --project points to a Next.js frontend with app/ and app/messages/\n")
        sys.exit(1)

    # Set module-level paths
    mod_vars = globals()
    mod_vars["PROJECT_ROOT"] = project_path
    mod_vars["APP_DIR"] = project_path / "app"
    mod_vars["MSGS_DIR"] = project_path / "app" / "messages"
    mod_vars["REPORTS_DIR"] = project_path / "scripts" / "i18n-reports"

    # If no mode given, default to dry-run
    mode = "dry-run"
    if args.inject:
        mode = "inject"
    if args.translate:
        mode = "translate"
    if args.auto:
        mode = "auto"
    if args.patch_safe:
        mode = "patch"
    if args.universal:
        mode = "universal"
    if args.ci_save:
        mode = "ci-save"
    if args.ci:
        mode = "ci"
    if args.check_stale:
        mode = "check-stale"
    if args.update_stale:
        mode = "update-stale"

    print(f"\n╔══════════════════════════════════════════════════════════╗")
    print(f"║      Subvox i18n — Hardcoded French Scanner             ║")
    print(f"╚══════════════════════════════════════════════════════════╝")
    print(f"")
    mode_label = {
        "dry-run": "🔍 Dry-run", "inject": "💉 Inject", "translate": "🌍 Translate",
        "auto": "🚀 Auto", "patch": "🛠️  Patch", "universal": "🌍 Universal",
        "ci-save": "💾 CI Save baseline", "ci": "🔬 CI Check",
        "check-stale": "🔍 Check stale", "update-stale": "🔄 Update stale",
    }.get(mode, mode)
    print(f"  Mode:     {mode_label}")
    print(f"  Scan dir: {APP_DIR}")
    print(f"")

    # ── Scan ───────────────────────────────────────────────────
    print("🔍 Scanning files…")
    entries = scan_all(mode)
    if not entries:
        print("  No hardcoded French text found.")
        return

    # ── Mode-specific actions ──────────────────────────────────
    dry_run = mode == "dry-run"

    if mode == "dry-run":
        print(f"  Found {len(entries)} occurrences in {len(set(e[0] for e in entries))} files\n")
        print_report(entries, dry_run=True)
        script_content = generate_replacement_script(entries)
        script_path = PROJECT_ROOT / "scripts" / "i18n-replacements.sh"
        script_path.write_text(script_content, encoding="utf-8")
        os.chmod(script_path, 0o755)
        print(f"📝 Replacement script: {script_path.relative_to(PROJECT_ROOT)}")
        print(f"    Open it in your editor, review, uncomment — then run.")
        print()

    elif mode == "patch":
        print(f"  Found {len(entries)} occurrences in {len(set(e[0] for e in entries))} files\n")
        print_report(entries, dry_run=True)
        is_dry = args.dry_run
        print(f"\n{'=' * 70}")
        print(f"  🛠️  MODE PATCH — Applying safe auto-fixes")
        print(f"  {'🔍 DRY-RUN' if is_dry else '💉 LIVE'}")
        print(f"  Only JSX text nodes will be replaced (STRING/data arrays skipped).")
        print(f"  Syntax checked after each file.\n")
        summary = patch_all_safe(entries, dry_run=is_dry)
        print_patch_summary(summary, dry_run=is_dry)
        if is_dry:
            print(f"  ⚠️  This was a dry-run. Re-run without --dry-run to apply.")
        print()

    elif mode == "ci-save":
        print(f"  Found {len(entries)} occurrences in {len(set(e[0] for e in entries))} files\n")
        data = ci_save(entries)
        print(f"\n  💡 Run --ci on your next scan to detect regressions.")
        print()

    elif mode == "ci":
        print(f"  Found {len(entries)} occurrences in {len(set(e[0] for e in entries))} files\n")
        new_count = ci_check(entries)
        if new_count > 0:
            print(f"\n  ❌ {new_count} regression(s) — run --dry-run to review, fix them, then --ci-save\n")
            sys.exit(1)
        print()

    elif mode == "check-stale":
        stale_count = check_stale()
        if stale_count > 0:
            print(f"\n  💡 Run --update-stale to retranslate changed keys via DeepSeek\n")
        print()

    elif mode == "update-stale":
        api_key = _read_deepseek_key()
        if not api_key:
            print("❌ DeepSeek key not found.")
            sys.exit(1)
        update_stale(api_key)
        print()

    elif mode == "inject" or mode == "auto":
        ns_keys = inject_keys(entries, dry_run=False)
        if ns_keys:
            print_report(entries, ns_keys, dry_run=False)
            script_content = generate_replacement_script(entries)
            script_path = PROJECT_ROOT / "scripts" / "i18n-replacements.sh"
            script_path.write_text(script_content, encoding="utf-8")
            os.chmod(script_path, 0o755)
            print(f"📝 Replacement script: {script_path.relative_to(PROJECT_ROOT)}")
            print()
        if mode == "auto" and ns_keys:
            translate_all(ns_keys, dry_run=False)
            print(f"\n✅ Full pipeline complete!")
            print(f"   Next: open scripts/i18n-replacements.sh and apply the patches.")

    elif mode == "translate":
        # Read fr.json, find keys that exist in FR but not in other locales
        with open(MSGS_DIR / "fr.json", encoding="utf-8") as f:
            fr_data = json.load(f)
        # Build a pseudo namespace_keys from fr.json
        ns_keys: dict[str, list[tuple[str, str, str]]] = {}  # type: ignore
        for ns, keys in fr_data.items():
            if isinstance(keys, dict):
                entries_list = [
                    (k, v, "fr.json") for k, v in keys.items()
                    if isinstance(v, str)
                ]
                if entries_list:
                    ns_keys[ns] = entries_list
        translate_all(ns_keys, dry_run=False)


if __name__ == "__main__":
    main()
