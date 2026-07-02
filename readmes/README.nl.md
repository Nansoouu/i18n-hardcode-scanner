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

## Functies

- **Taalonafhankelijke detectie** — vindt leesbare tekst in ELKE taal (Frans, Engels, Vietnamees, Arabisch, CJK, Cyrillisch…)
- **Frans-specifieke modus** — afgestemd op Franse projecten, minder valse positieven
- **Deelbaar markdown-rapport** — perfect voor teamreview of CI-artefacten
- **Veilige automatische patching** — voegt `import { useTranslations }` toe, declareert `const t = useTranslations(...)`, vervangt JSX-tekst, verifieert syntax
- **Vertalingspijplijn** — injecteert sleutels in `fr.json`, vertaalt vervolgens naar alle 20 talen via DeepSeek
- **Geen buildstap** — enkel Python-bestand, nul afhankelijkheden (stdlib + optioneel `httpx`)

---

## Snel starten

```bash
# Kloon en voer uit
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Scan je project (proefdraai, geen wijzigingen)
python3 i18n_hardcode_scanner.py --project /pad/naar/jouw/frontend --universal --dry-run
```

---

## Gebruik

### Scanmodi

```bash
# Frans-specifiek (preciezer, minder resultaten)
python3 i18n_hardcode_scanner.py --project ./mijn-app --dry-run

# Alle talen (uitputtend, vangt alles)
python3 i18n_hardcode_scanner.py --project ./mijn-app --universal --dry-run
```

### Rapport

```bash
# Genereert scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh met per-bestand patchkandidaten
```

### Injecteren & vertalen

```bash
# Injecteer gevonden sleutels in fr.json
python3 i18n_hardcode_scanner.py --project ./mijn-app --inject

# Vertaal naar alle 20 talen via DeepSeek
python3 i18n_hardcode_scanner.py --project ./mijn-app --translate

# Volledige pijplijn: injecteren + vertalen
python3 i18n_hardcode_scanner.py --project ./mijn-app --auto
```

### Veilig patchen

```bash
# Proefdraai (toont verschillen, schrijft niets)
python3 i18n_hardcode_scanner.py --project ./mijn-app --patch-safe --dry-run

# Toepassen (voegt imports, t() toe, vervangt JSX-tekst, verifieert syntax)
python3 i18n_hardcode_scanner.py --project ./mijn-app --patch-safe
```

Alleen JSX-tekstknooppunten (`>tekst<`) worden automatisch vervangen. Gegevensarrays en attribuutstrings worden gemarkeerd voor handmatige controle.

---

## Hoe het werkt

De scanner gebruikt **geen** taalspecifieke woordenboeken. In plaats daarvan zoekt het naar **technische patronen** die UI-tekst onderscheiden van code:

### Wat het vangt

| Patroon | Voorbeeld | Detecteert |
|---------|-----------|------------|
| Accenttekens Latijnse karakters | `é`, `ñ`, `ü` | Frans, Spaans, Duits, Vietnamees… |
| Niet-Latijnse schriften | 你好, Привет, العربية | CJK, Cyrillisch, Arabisch… |
| Meerwoordige zinnen | `"Bestand uploaden..."` | Elke taal met spaties |
| Zinsleestekens | `"Klaar!"`, `"Doorgaan?"` | Eindigt met `.`, `!`, `?`, `:` |
| Titelwoordhoofdletters | `"Dashboard"`, `"Paramètres"` | Eigennamen, sectietitels |
| Emoji in tekst | `"✅ Gekopieerd"` | Gemengde emoji + tekst |

### Wat het overslaat

| Patroon | Voorbeeld | Reden |
|---------|-----------|-------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS-identifiers |
| CSS / Tailwind-klassen | `py-3 px-4`, `text-gray-500` | Opmaak, geen UI-tekst |
| URL's en bestandspaden | `https://...`, `./componenten/` | Imports, bronnen |
| Codeverklaringen | `const t =`, `return null` | JS-code |
| ALL_CAPS-constanten | `API_URL`, `MAX_RETRIES` | Configuratie |
| Pure getallen / hex | `#fff`, `42` | Technische waarden |

### Detectiepijplijn per bestand

```
Regel voor regel → 
  ① Is dit een JSX-tekstknooppunt (>tekst<)? 
     → Controleer of het leesbaar is → Markeer als JSX
  ② Is er een geciteerde string ("..." of '...')? 
     → Is het een JS-identifier? → Overslaan
     → Is het technisch? → Overslaan
     → Is het leesbaar? → Markeer als STRING
```

---

## Sleutelnaamconventies

De scanner genereert automatisch camelCase-sleutels uit de Franse/Engelse tekst:

| Originele tekst | Gegenereerde sleutel |
|-----------------|----------------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Botsingen** krijgen een `_N`-achtervoegsel (`title_2`, `title_3`). Sleutels moeten na generatie worden gecontroleerd.

---

## Veiligheidsgaranties

Elke automatische patch doorloopt deze controles:

1. **Import toegevoegd** — `import { useTranslations } from "next-intl"` indien ontbrekend
2. **Declaratie toegevoegd** — `const t = useTranslations("Namespace")` na imports
3. **Accolades in balans** — `{}[]()` verifieert geen gebroken JSX
4. **t() binnen strings gedetecteerd** — `placeholder="{t("sleutel")}"` zou als letterlijke tekst worden weergegeven
5. **Schrijven is atomair** — bestand wordt alleen geschreven als alle controles slagen

---

## Communitybijdragen gewenst

Dit hulpmiddel wordt beter met meer taaldetectiepatronen. Hier zijn enkele manieren om te helpen:

### 1. Voeg detectie toe voor jouw taal

De `--universal`-modus vangt alle schriften, maar specifieke patronen verbeteren de nauwkeurigheid. Voeg toe:

- **Accenttekensets** — Vietnamees (ăâđêôơư), Pools (łężźć), Roemeens (ăâîșț), enz.
- **Niet-Latijnse stopwoorden** — Veelvoorkomende Arabische, Hindi, Thaise, Griekse woorden die UI-tekst zijn, geen code
- **CJK-detectie** — Chinese/Japanse/Koreaanse karakterreeksen (al inbegrepen, maar subtaalafstemming helpt)

### 2. Frameworkadapters

- Ondersteuning voor `react-i18next` / `i18next`-syntax (momenteel alleen next-intl)
- Detecteer `formatMessage()`, `intl.formatMessage()`, `$t()`-patronen
- Voeg Vue.js / Svelte / Angular-ondersteuning toe

### 3. Sleutelnaamverbeteringen

- Betere namespace-afleiding uit directorystructuur
- Meertalige sleutelsuggesties (niet alleen uit het Frans)
- Integratie met bestaande vertaalbeheersystemen

### 4. CI/CD-integraties

- GitHub Action om scan op PR's uit te voeren
- CI laten falen als nieuwe hardcoded tekst wordt geïntroduceerd
- Automatisch commentaar op PR's met scanresultaten

### 5. IDE-plugins

- VS Code-extensie om hardcoded tekst inline te markeren
- Voorgestelde snelle oplossing om in `t()`-aanroep te wrappen
- Taalbestandsverkenner

---

## Bouw voor jouw project

Deze scanner is gebouwd voor het **[Subvox](https://github.com/Nansoouu/subvox)** -project — een open-source videobijschriftenplatform dat 150+ ondertiteltalen en 20 UI-talen ondersteunt.

De scanner werkt met ELK Next.js-project dat next-intl gebruikt. Wijs gewoon `