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

## Funzionalità

- **Rilevamento indipendente dalla lingua** — trova testo leggibile in QUALSIASI lingua (francese, inglese, vietnamita, arabo, CJK, cirillico…)
- **Modalità specifica per francese** — ottimizzata per progetti francesi, meno falsi positivi
- **Report markdown condivisibile** — perfetto per revisioni di team o artefatti CI
- **Auto-patching sicuro** — aggiunge `import { useTranslations }`, dichiara `const t = useTranslations(...)`, sostituisce testo JSX, verifica la sintassi
- **Pipeline di traduzione** — inserisce chiavi in `fr.json`, poi traduce in tutte le 20 lingue tramite DeepSeek
- **Nessun passaggio di build** — singolo file Python, zero dipendenze (stdlib + `httpx` opzionale)

---

## Struttura del progetto

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Lo scanner (file singolo, autonomo)
├── scripts/
│   ├── sync-i18n.py            # Script di traduzione batch DeepSeek
│   └── no-emoji-i18n.sh        # Hook pre-commit per file locale senza emoji
├── readmes/                    # README tradotti
├── pyproject.toml              # Pacchettizzazione Python (opzionale)
├── LICENSE                     # MIT
└── README.md                   # Questo file
```

## Avvio rapido

```bash
# Clona ed esegui (dry-run — nessuna chiave API necessaria)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## Chiave API — DeepSeek (opzionale)

La pipeline di traduzione (`--auto`, `--translate`, `--update-stale`) utilizza DeepSeek per tradurre le chiavi in 20 lingue. Hai bisogno di una chiave API **solo** per queste funzionalità.

```bash
# 1. Ottieni una chiave: https://platform.deepseek.com/api_keys
# 2. Forniscila tramite variabile d'ambiente:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Oppure crea ~/.hermes/auth.json (rilevato automaticamente):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Dry-run, inject, patch-safe, ci, check-stale** — nessuna di queste necessita di una chiave API.

---

---

## Utilizzo

### Modalità di scansione

```bash
# Specifica per francese (più precisa, meno risultati)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Tutte le lingue (esaustiva, cattura tutto)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Report

```bash
# Genera scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh con candidati patch per file
```

### Inietta e traduci

```bash
# Inietta le chiavi scoperte in fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Traduci in tutte le 20 lingue tramite DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Pipeline completa: inject + translate
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Patching sicuro

```bash
# Dry-run (mostra le differenze, non scrive nulla)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Applica (aggiunge import, t(), sostituisce testo JSX, verifica sintassi)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Solo i nodi di testo JSX (`>testo<`) vengono sostituiti automaticamente. Gli array di dati e gli attributi stringa vengono segnalati per revisione manuale.

---

## Come funziona

Lo scanner **non** utilizza dizionari specifici per lingua. Invece, cerca **pattern tecnici** che distinguono il testo UI dal codice:

### Cosa cattura

| Pattern | Esempio | Rileva |
|---------|---------|--------|
| Caratteri latini accentati | `é`, `ñ`, `ü` | Francese, Spagnolo, Tedesco, Vietnamita… |
| Scritture non latine | 你好, Привет, العربية | CJK, Cirillico, Arabo… |
| Frasi multi-parola | `"Caricamento file..."` | Qualsiasi lingua con spazi |
| Punteggiatura di frase | `"Fatto!"`, `"Continuare?"` | Termina con `.`, `!`, `?`, `:` |
| Parole in maiuscolo | `"Dashboard"`, `"Paramètres"` | Nomi propri, titoli di sezione |
| Emoji nel testo | `"✅ Copiato"` | Emoji misto + testo |

### Cosa salta

| Pattern | Esempio | Motivo |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | Identificatori JS |
| Classi CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Stile, non testo UI |
| URL e percorsi file | `https://...`, `./components/` | Import, risorse |
| Istruzioni di codice | `const t =`, `return null` | Codice JS |
| Costanti MAIUSCOLE | `API_URL`, `MAX_RETRIES` | Configurazione |
| Numeri puri / hex | `#fff`, `42` | Valori tecnici |

### Pipeline di rilevamento per file

```
Riga per riga → 
  ① È un nodo di testo JSX (>testo<? 
     → Controlla se sembra leggibile → Segnala come JSX
  ② C'è una stringa tra virgolette ("..." o '...')? 
     → È un identificatore JS? → Salta
     → È tecnico? → Salta
     → È leggibile? → Segnala come STRINGA
```

---

## Convenzioni di denominazione delle chiavi

Lo scanner genera automaticamente chiavi camelCase dal testo francese/inglese:

| Testo originale | Chiave generata |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Collisioni** ricevono un suffisso `_N` (`title_2`, `title_3`). Le chiavi dovrebbero essere revisionate dopo la generazione.

---

## Garanzie di sicurezza

Ogni auto-patch passa attraverso questi controlli:

1. **Import aggiunto** — `import { useTranslations } from "next-intl"` se mancante
2. **Dichiarazione aggiunta** — `const t = useTranslations("Namespace")` dopo gli import
3. **Parentesi bilanciate** — `{}[]()` verifica che non ci siano JSX rotti
4. **t() rilevato all'interno di stringhe** — `placeholder="{t("key")}"` verrebbe renderizzato come testo letterale
5. **Scrittura atomica** — il file viene scritto solo se tutti i controlli passano

---

## Contributi della comunità benvenuti

Questo strumento è **open source e guidato dalla comunità**. Fai il fork, miglioralo, condividilo.
Ogni contributo — che sia un nuovo pattern linguistico, un adattatore per framework o una correzione di bug — aiuta a rendere il web più accessibile.

Accogliamo con favore soprattutto PR da sviluppatori che parlano lingue attualmente sottorappresentate negli strumenti i18n.

### 1. Aggiungi rilevamento per la tua lingua

La modalità `--universal` cattura tutte le scritture, ma pattern specifici