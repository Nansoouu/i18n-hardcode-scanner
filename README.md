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

A language-agnostic scanner that finds hardcoded UI text in your codebase and helps you wire it through next-intl translation keys. Built for and battle-tested on **[Subvox](https://github.com/Nansoouu/subvox)** — the open-source video subtitle platform.

```
🔍 Scan → 📋 Report → 💉 Inject keys → 🌍 Translate 20 locales → ✅ Safe patch
```

> **Support the author** — if this tool saves you time, send a donation to:

> ```
> 6bHv6bgWg5ZdD5GupvtdobFJBhVPihYhY7KyNA7qAigu
> ```

> (Solana / USDC / any SPL token)

---

## Features

- **Language-agnostic detection** — finds human-readable text in ANY language (French, English, Vietnamese, Arabic, CJK, Cyrillic…)
- **French-specific mode** — tuned for French projects, fewer false positives
- **Shareable markdown report** — perfect for team review or CI artifacts
- **Safe auto-patching** — adds `import { useTranslations }`, declares `const t = useTranslations(...)`, replaces JSX text, verifies syntax
- **Translation pipeline** — injects keys into `fr.json`, then translates to all 20 locales via DeepSeek
- **No build step** — single Python file, zero dependencies (stdlib + optional `httpx`)

---

## Quick Start

```bash
# Clone and run
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Scan your project (dry-run, no changes)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## Usage

### Scan modes

```bash
# French-specific (more precise, fewer results)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# All languages (exhaustive, catches everything)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Report

```bash
# Generates scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh with per-file patch candidates
```

### Inject & translate

```bash
# Inject discovered keys into fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Translate to all 20 locales via DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Full pipeline: inject + translate
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Safe patching

```bash
# Dry-run (shows diffs, writes nothing)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Apply (adds imports, t(), replaces JSX text, verifies syntax)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Only JSX text nodes (`>text<`) are auto-replaced. Data arrays and attribute strings are flagged for manual review.

---

## How it works

The scanner does **not** use language-specific dictionaries. Instead, it looks for **technical patterns** that distinguish UI text from code:

### What it catches

| Pattern | Example | Detects |
|---------|---------|---------|
| Accented Latin chars | `é`, `ñ`, `ü` | French, Spanish, German, Vietnamese… |
| Non-Latin scripts | 你好, Привет, العربية | CJK, Cyrillic, Arabic… |
| Multi-word phrases | `"Uploading file..."` | Any language with spaces |
| Sentence punctuation | `"Done!"`, `"Continue?"` | Ends with `.`, `!`, `?`, `:` |
| Title-case words | `"Dashboard"`, `"Paramètres"` | Proper nouns, section titles |
| Emoji in text | `"✅ Copié"` | Mixed emoji + text |

### What it skips

| Pattern | Example | Reason |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS identifiers |
| CSS / Tailwind classes | `py-3 px-4`, `text-gray-500` | Styling, not UI text |
| URLs and file paths | `https://...`, `./components/` | Imports, resources |
| Code statements | `const t =`, `return null` | JS code |
| ALL_CAPS constants | `API_URL`, `MAX_RETRIES` | Configuration |
| Pure numbers / hex | `#fff`, `42` | Technical values |

### Detection pipeline per file

```
Line by line → 
  ① Is this a JSX text node (>text<)? 
     → Check if it looks human-readable → Flag as JSX
  ② Is there a quoted string ("..." or '...')? 
     → Is it a JS identifier? → Skip
     → Is it technical? → Skip
     → Is it human-readable? → Flag as STRING
```

---

## Key naming conventions

The scanner auto-generates camelCase keys from the French/English text:

| Original text | Generated key |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Collisions** get a `_N` suffix (`title_2`, `title_3`). Keys should be reviewed after generation.

---

## Safety guarantees

Every auto-patch goes through these checks:

1. **Import added** — `import { useTranslations } from "next-intl"` if missing
2. **Declaration added** — `const t = useTranslations("Namespace")` after imports
3. **Braces balanced** — `{}[]()` verifies no broken JSX
4. **t() inside strings detected** — `placeholder="{t("key")}"` would render as literal text
5. **Write is atomic** — file is only written if all checks pass

---

## Community contributions wanted

This tool is **open source and community-driven**. Fork it, improve it, share it.
Every contribution — whether a new language pattern, a framework adapter, or a bug fix — helps make the web more accessible.

We especially welcome PRs from developers who speak languages currently underrepresented in i18n tooling.

### 1. Add detection for your language

The `--universal` mode catches all scripts, but specific patterns improve accuracy. Fork the repo and submit a PR adding:

- **Accented character sets** — Vietnamese (ăâđêôơư), Polish (łężźć), Romanian (ăâîșț), etc.
- **Non-Latin stopwords** — Common Arabic, Hindi, Thai, Greek words that are UI text, not code
- **CJK detection** — Chinese/Japanese/Korean character ranges (already included, but sub-language tuning helps)

### 2. Framework adapters

- Support `react-i18next` / `i18next` syntax (currently next-intl only)
- Detect `formatMessage()`, `intl.formatMessage()`, `$t()` patterns
- Add Vue.js / Svelte / Angular support

### 3. Key naming improvements

- Better namespace inference from directory structure
- Multi-language key suggestions (not just from French)
- Integration with existing translation management systems

### 4. CI/CD integrations

- GitHub Action to run scan on PRs
- Fail CI if new hardcoded text is introduced
- Auto-comment on PRs with scan results

### 5. IDE plugins

- VS Code extension to highlight hardcoded text inline
- Suggested quick-fix to wrap in `t()` call
- Locale file explorer

---

## Frontend integration examples

This repo includes the complete language selector system from Subvox — ready to copy into your project.

```
examples/
├── i18n.ts                   # 20-locale config, localStorage helpers
├── I18nProvider.tsx           # Context provider, dynamic message loading
├── LanguageSelector.tsx       # Navbar dropdown selector
├── LanguagePicker.tsx         # Advanced multi-language picker (150+ langs)
└── README.md                  # Integration guide
```

See [`examples/README.md`](examples/README.md) for the full integration guide.

---

## Build for your project

This scanner was built for the **[Subvox](https://github.com/Nansoouu/subvox)** project — an open-source video subtitle platform supporting 150+ subtitle languages and 20 UI languages.

The scanner works with ANY Next.js project using next-intl. Just point `--project` at your frontend root.

---

## License

MIT — use it, modify it, share it. If you build something cool with it, we'd love to hear about it.

## Project structure

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # The scanner (single file, self-contained)
├── scripts/
│   ├── sync-i18n.py            # DeepSeek batch translation script
│   └── no-emoji-i18n.sh        # Pre-commit hook for emoji-free locale files
├── readmes/                    # Translated READMEs
├── pyproject.toml              # Python packaging (optional)
├── LICENSE                     # MIT
└── README.md                   # This file
```
