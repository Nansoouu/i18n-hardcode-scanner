<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/i18n_Hardcode_Scanner-00A86B?style=for-the-badge&logo=github&logoColor=white">
    <img alt="i18n Hardcode Scanner" src="https://img.shields.io/badge/i18n_Hardcode_Scanner-00A86B?style=for-the-badge&logo=github&logoColor=white" width="300">
  </picture>
</p>

<h1 align="center">i18n Hardcode Scanner</h1>

<p align="center">
  <strong>Scan your Next.js project for untranslated UI text in ANY language.</strong><br/>
  Automatic detection → translation key injection → 20-locale sync. Built for <a href="https://github.com/Nansoouu/subvox">Subvox</a>.
</p>

<p align="center">
  <a href="readmes/README.fr.md"><img src="https://img.shields.io/badge/Français-FR-blue" alt="Français"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/English-GB-white" alt="English"></a>
  <a href="readmes/README.es.md"><img src="https://img.shields.io/badge/Español-ES-green" alt="Español"></a>
  <a href="readmes/README.de.md"><img src="https://img.shields.io/badge/Deutsch-DE-orange" alt="Deutsch"></a>
  <a href="readmes/README.it.md"><img src="https://img.shields.io/badge/Italiano-IT-red" alt="Italiano"></a>
  <a href="readmes/README.pt.md"><img src="https://img.shields.io/badge/Português-PT-brightgreen" alt="Português"></a>
  <a href="readmes/README.nl.md"><img src="https://img.shields.io/badge/Nederlands-NL-brightblue" alt="Nederlands"></a>
  <a href="readmes/README.pl.md"><img src="https://img.shields.io/badge/Polski-PL-purple" alt="Polski"></a>
  <a href="readmes/README.ru.md"><img src="https://img.shields.io/badge/Русский-RU-purple" alt="Русский"></a>
  <a href="readmes/README.uk.md"><img src="https://img.shields.io/badge/Українська-UA-yellow" alt="Українська"></a>
  <a href="readmes/README.tr.md"><img src="https://img.shields.io/badge/Türkçe-TR-important" alt="Türkçe"></a>
  <a href="readmes/README.ar.md"><img src="https://img.shields.io/badge/العربية-SA-lightgrey" alt="العربية"></a>
  <a href="readmes/README.fa.md"><img src="https://img.shields.io/badge/فارسی-IR-green1" alt="فارسی"></a>
  <a href="readmes/README.he.md"><img src="https://img.shields.io/badge/עברית-IL-blue" alt="עברית"></a>
  <a href="readmes/README.hi.md"><img src="https://img.shields.io/badge/हिन्दी-IN-orange" alt="हिन्दी"></a>
  <a href="readmes/README.zh.md"><img src="https://img.shields.io/badge/中文-CN-critical" alt="中文"></a>
  <a href="readmes/README.ja.md"><img src="https://img.shields.io/badge/日本語-JP-blueviolet" alt="日本語"></a>
  <a href="readmes/README.ko.md"><img src="https://img.shields.io/badge/한국어-KR-violet" alt="한국어"></a>
  <a href="readmes/README.id.md"><img src="https://img.shields.io/badge/Bahasa Indonesia-ID-teal" alt="Bahasa Indonesia"></a>
  <a href="readmes/README.vi.md"><img src="https://img.shields.io/badge/Tiếng Việt-VN-success" alt="Tiếng Việt"></a>
</p>

---

## Funktionen

- **Sprachunabhängige Erkennung** — findet lesbaren Text in JEDER Sprache (Französisch, Englisch, Vietnamesisch, Arabisch, CJK, Kyrillisch…)
- **Französisch-spezifischer Modus** — optimiert für französische Projekte, weniger Fehlalarme
- **Teilbarer Markdown-Bericht** — perfekt für Team-Reviews oder CI-Artefakte
- **Sicheres automatisches Patchen** — fügt `import { useTranslations }` hinzu, deklariert `const t = useTranslations(...)`, ersetzt JSX-Text, überprüft Syntax
- **Übersetzungspipeline** — fügt Schlüssel in `fr.json` ein, übersetzt dann in alle 20 Locales via DeepSeek
- **Kein Build-Schritt** — einzelne Python-Datei, keine Abhängigkeiten (stdlib + optionales `httpx`)

---

## Schnellstart

```bash
# Klonen und ausführen
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Projekt scannen (Probelauf, keine Änderungen)
python3 i18n_hardcode_scanner.py --project /pfad/zu/ihrem/frontend --universal --dry-run
```

---

## Verwendung

### Scan-Modi

```bash
# Französisch-spezifisch (präziser, weniger Ergebnisse)
python3 i18n_hardcode_scanner.py --project ./meine-app --dry-run

# Alle Sprachen (vollständig, erfasst alles)
python3 i18n_hardcode_scanner.py --project ./meine-app --universal --dry-run
```

### Bericht

```bash
# Erzeugt scripts/i18n-reports/hardcode-scan-{zeitstempel}.md
# + scripts/i18n-replacements.sh mit Patch-Kandidaten pro Datei
```

### Einfügen & Übersetzen

```bash
# Entdeckte Schlüssel in fr.json einfügen
python3 i18n_hardcode_scanner.py --project ./meine-app --inject

# In alle 20 Locales via DeepSeek übersetzen
python3 i18n_hardcode_scanner.py --project ./meine-app --translate

# Vollständige Pipeline: einfügen + übersetzen
python3 i18n_hardcode_scanner.py --project ./meine-app --auto
```

### Sicheres Patchen

```bash
# Probelauf (zeigt Unterschiede, schreibt nichts)
python3 i18n_hardcode_scanner.py --project ./meine-app --patch-safe --dry-run

# Anwenden (fügt Imports, t() hinzu, ersetzt JSX-Text, überprüft Syntax)
python3 i18n_hardcode_scanner.py --project ./meine-app --patch-safe
```

Nur JSX-Textknoten (`>text<`) werden automatisch ersetzt. Datenarrays und Attributstrings werden zur manuellen Überprüfung markiert.

---

## Funktionsweise

Der Scanner verwendet **keine** sprachspezifischen Wörterbücher. Stattdessen sucht er nach **technischen Mustern**, die UI-Text von Code unterscheiden:

### Was er erfasst

| Muster | Beispiel | Erkennt |
|--------|----------|---------|
| Akzentuierte lateinische Zeichen | `é`, `ñ`, `ü` | Französisch, Spanisch, Deutsch, Vietnamesisch… |
| Nicht-lateinische Schriften | 你好, Привет, العربية | CJK, Kyrillisch, Arabisch… |
| Mehrwort-Phrasen | `"Datei hochladen..."` | Jede Sprache mit Leerzeichen |
| Satzzeichen | `"Fertig!"`, `"Fortfahren?"` | Endet mit `.`, `!`, `?`, `:` |
| Großgeschriebene Wörter | `"Dashboard"`, `"Paramètres"` | Eigennamen, Abschnittstitel |
| Emoji im Text | `"✅ Kopiert"` | Gemischt Emoji + Text |

### Was er überspringt

| Muster | Beispiel | Grund |
|--------|----------|-------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS-Bezeichner |
| CSS / Tailwind-Klassen | `py-3 px-4`, `text-gray-500` | Styling, kein UI-Text |
| URLs und Dateipfade | `https://...`, `./components/` | Importe, Ressourcen |
| Code-Anweisungen | `const t =`, `return null` | JS-Code |
| ALL_CAPS-Konstanten | `API_URL`, `MAX_RETRIES` | Konfiguration |
| Reine Zahlen / Hex | `#fff`, `42` | Technische Werte |

### Erkennungspipeline pro Datei

```
Zeile für Zeile → 
  ① Ist dies ein JSX-Textknoten (>text<)? 
     → Prüfen, ob es lesbar aussieht → Als JSX markieren
  ② Gibt es einen in Anführungszeichen gesetzten String ("..." oder '...')? 
     → Ist es ein JS-Bezeichner? → Überspringen
     → Ist es technisch? → Überspringen
     → Ist es lesbar? → Als STRING markieren
```

---

## Schlüsselbenennungskonventionen

Der Scanner generiert automatisch camelCase-Schlüssel aus dem französischen/englischen Text:

| Originaltext | Generierter Schlüssel |
|-------------|----------------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Kollisionen** erhalten ein `_N`-Suffix (`title_2`, `title_3`). Schlüssel sollten nach der Generierung überprüft werden.

---

## Sicherheitsgarantien

Jeder automatische Patch durchläuft diese Prüfungen:

1. **Import hinzugefügt** — `import { useTranslations } from "next-intl"` falls fehlend
2. **Deklaration hinzugefügt** — `const t = useTranslations("Namespace")` nach Imports
3. **Klammern ausgeglichen** — `{}[]()` überprüft auf defektes JSX
4. **t() innerhalb von Strings erkannt** — `placeholder="{t("key")}"` würde als Literaltext gerendert
5. **Schreiben ist atomar** — Datei wird nur geschrieben, wenn alle Prüfungen bestanden sind

---

## Community-Beiträge erwünscht

Dieses Tool wird mit mehr Spracherkennungsmustern besser. Hier sind einige Möglichkeiten zu helfen:

### 1. Erkennung für Ihre Sprache hinzufügen

Der `--universal`-Modus erfasst alle Schriften, aber spezifische Muster verbessern die Genauigkeit. Fügen Sie hinzu:

- **Akzentuierte Zeichensätze** — Vietnamesisch (ăâđêôơư), Polnisch (łężźć), Rumänisch (ăâîșț) usw.
- **Nicht-lateinische Stoppwörter** — Häufige arabische, Hindi-, Thai-, griechische Wörter, die UI-Text sind, kein Code
- **CJK-Erkennung** — Chinesische/japanische/koreanische Zeichenbereiche (bereits enthalten, aber Untersprachen-Tuning hilft)

### 2. Framework-Adapter

- Unterstützung für `react-i18next` / `i18next`-Syntax (derzeit nur next-intl)
- Erkennung von `formatMessage()`, `intl.formatMessage()`, `$t()`-Mustern
- Vue.js / Svelte / Angular-Unterstützung hinzufügen

### 3. Verbesserungen der Schlüsselbenennung

- Bessere Namespace-Ableitung aus der Verzeichnisstruktur
- Mehrsprachige Schlüsselvorschläge (nicht nur aus Französisch)
- Integration mit bestehenden Übersetzungsmanagementsystemen

### 4. CI/CD-Integrationen

- GitHub-Aktion zum Scannen bei PRs
- CI fehlschlagen lassen, wenn neuer hartcodierter Text eingeführt wird
- Automatische Kommentare bei PRs mit Scan-Ergebnissen

### 5. IDE-Plugins

- VS Code-Erweiterung zur Inline-Hervorhebung von hartcodiertem Text
- Vorgeschlagene Schnellkorrektur zum Einwickeln in `t()`-Aufruf
- Locale-Datei-Explorer

---

## Für Ihr Projekt erstellen

Dieser Scanner wurde für das **[Subvox](https://github.com/Nansoouu/subvox)**-Projekt entwickelt — eine Open-Source-Videountertitel-Plattform mit Unterstützung für 150+ Untertitelsprachen und 20 UI-Sprachen.

Der Scanner funktioniert mit JEDEM Next.js-Projekt, das next-intl verwendet. Geben Sie einfach den