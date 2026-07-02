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

> **Support the author** — if this tool saves you time, send a donation to:

> ```
> 6bHv6bgWg5ZdD5GupvtdobFJBhVPihYhY7KyNA7qAigu
> ```

---

## Fonctionnalités

- **Détection indépendante de la langue** — trouve du texte lisible par l'humain dans TOUTE langue (français, anglais, vietnamien, arabe, CJK, cyrillique…)
- **Mode spécifique au français** — optimisé pour les projets français, moins de faux positifs
- **Rapport markdown partageable** — parfait pour la révision en équipe ou les artefacts CI
- **Correction automatique sécurisée** — ajoute `import { useTranslations }`, déclare `const t = useTranslations(...)`, remplace le texte JSX, vérifie la syntaxe
- **Pipeline de traduction** — injecte les clés dans `fr.json`, puis traduit vers les 20 locales via DeepSeek
- **Aucune étape de build** — fichier Python unique, zéro dépendance (stdlib + `httpx` optionnel)

---

## Structure du projet

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Le scanner (fichier unique, autonome)
├── scripts/
│   ├── sync-i18n.py            # Script de traduction batch DeepSeek
│   └── no-emoji-i18n.sh        # Hook pre-commit pour les fichiers de locale sans emoji
├── readmes/                    # READMEs traduits
├── pyproject.toml              # Empaquetage Python (optionnel)
├── LICENSE                     # MIT
└── README.md                   # Ce fichier
```

## Démarrage rapide

```bash
# Cloner et exécuter (simulation — aucune clé API nécessaire)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /chemin/vers/votre/frontend --universal --dry-run
```

---

## Clé API — DeepSeek (optionnel)

Le pipeline de traduction (`--auto`, `--translate`, `--update-stale`) utilise DeepSeek pour traduire les clés en 20 langues. Vous avez besoin d'une clé API **uniquement** pour ces fonctionnalités.

```bash
# 1. Obtenez une clé : https://platform.deepseek.com/api_keys
# 2. Fournissez-la via une variable d'environnement :
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./mon-app --translate

# Ou créez ~/.hermes/auth.json (détection automatique) :
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Simulation, injection, correction sécurisée, ci, vérification des obsolètes** — aucune de ces options n'a besoin d'une clé API.

---

---

## Utilisation

### Modes d'analyse

```bash
# Spécifique au français (plus précis, moins de résultats)
python3 i18n_hardcode_scanner.py --project ./mon-app --dry-run

# Toutes les langues (exhaustif, détecte tout)
python3 i18n_hardcode_scanner.py --project ./mon-app --universal --dry-run
```

### Rapport

```bash
# Génère scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh avec les correctifs par fichier
```

### Injection et traduction

```bash
# Injecte les clés découvertes dans fr.json
python3 i18n_hardcode_scanner.py --project ./mon-app --inject

# Traduit vers les 20 locales via DeepSeek
python3 i18n_hardcode_scanner.py --project ./mon-app --translate

# Pipeline complet : injection + traduction
python3 i18n_hardcode_scanner.py --project ./mon-app --auto
```

### Correction sécurisée

```bash
# Simulation (affiche les différences, n'écrit rien)
python3 i18n_hardcode_scanner.py --project ./mon-app --patch-safe --dry-run

# Application (ajoute les imports, t(), remplace le texte JSX, vérifie la syntaxe)
python3 i18n_hardcode_scanner.py --project ./mon-app --patch-safe
```

Seuls les nœuds de texte JSX (`>texte<`) sont automatiquement remplacés. Les tableaux de données et les chaînes d'attributs sont signalés pour révision manuelle.

---

## Comment ça fonctionne

Le scanner **n'utilise pas** de dictionnaires spécifiques à une langue. Au lieu de cela, il recherche des **motifs techniques** qui distinguent le texte d'interface du code :

### Ce qu'il détecte

| Motif | Exemple | Détecte |
|---------|---------|---------|
| Caractères latins accentués | `é`, `ñ`, `ü` | Français, espagnol, allemand, vietnamien… |
| Écritures non latines | 你好, Привет, العربية | CJK, cyrillique, arabe… |
| Phrases multi-mots | `"Téléchargement du fichier..."` | Toute langue avec des espaces |
| Ponctuation de phrase | `"Terminé !"`, `"Continuer ?"` | Se termine par `.`, `!`, `?`, `:` |
| Mots en casse titre | `"Tableau de bord"`, `"Paramètres"` | Noms propres, titres de sections |
| Emoji dans le texte | `"✅ Copié"` | Mélange emoji + texte |

### Ce qu'il ignore

| Motif | Exemple | Raison |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | Identifiants JS |
| Classes CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Style, pas texte d'interface |
| URLs et chemins de fichiers | `https://...`, `./components/` | Imports, ressources |
| Instructions de code | `const t =`, `return null` | Code JS |
| Constantes en MAJUSCULES | `API_URL`, `MAX_RETRIES` | Configuration |
| Nombres purs / hexadécimaux | `#fff`, `42` | Valeurs techniques |

### Pipeline de détection par fichier

```
Ligne par ligne → 
  ① Est-ce un nœud de texte JSX (>texte<) ? 
     → Vérifier s'il semble lisible par l'humain → Marquer comme JSX
  ② Y a-t-il une chaîne entre guillemets ("..." ou '...') ? 
     → Est-ce un identifiant JS ? → Ignorer
     → Est-ce technique ? → Ignorer
     → Est-ce lisible par l'humain ? → Marquer comme CHAÎNE
```

---

## Conventions de nommage des clés

Le scanner génère automatiquement des clés en camelCase à partir du texte français/anglais :

| Texte original | Clé générée |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Les collisions** reçoivent un suffixe `_N` (`title_2`, `title_3`). Les clés doivent être révisées après la génération.

---

## Garanties de sécurité

Chaque correction automatique passe par ces vérifications :

1. **Import ajouté** — `import { useTranslations } from "next-intl"` si manquant
2. **Déclaration ajoutée** — `const t = useTranslations("Namespace")` après les imports
3. **Accolades équilibrées** — `{}[]()` vérifie qu'aucun JSX n'est cassé
4. **t() dans les chaînes détecté** — `placeholder="{t("key")}"` serait rendu comme texte littéral
5. **Écriture atomique** — le fichier n'est écrit que si toutes les vérifications réussissent

---

## Contributions de la communauté recherchées

Cet outil est **open source et piloté par la communauté**. Forkez-le, améliorez-le, partagez-le.
Chaque contribution — qu'il s'agisse d'un nouveau motif linguistique, d'un adaptateur de framework ou d'une correction de bug — contribue à rendre le web plus accessible.

Nous accueillons particulièrement les PR des développeurs parlant des langues actuellement sous-représentées dans les outils d'internationalisation.

### 1. Ajouter la détection pour votre langue

Le mode `--universal` détecte toutes les écritures, mais les motifs spécifiques