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

## Fitur

- **Deteksi agnostik bahasa** — menemukan teks yang dapat dibaca manusia dalam bahasa APAPUN (Prancis, Inggris, Vietnam, Arab, CJK, Sirilik…)
- **Mode khusus Prancis** — disesuaikan untuk proyek Prancis, lebih sedikit positif palsu
- **Laporan markdown yang dapat dibagikan** — sempurna untuk tinjauan tim atau artefak CI
- **Penambalan otomatis yang aman** — menambahkan `import { useTranslations }`, mendeklarasikan `const t = useTranslations(...)`, mengganti teks JSX, memverifikasi sintaks
- **Pipeline penerjemahan** — menyuntikkan kunci ke dalam `fr.json`, lalu menerjemahkan ke semua 20 lokal melalui DeepSeek
- **Tidak ada langkah build** — file Python tunggal, tanpa dependensi (stdlib + `httpx` opsional)

---

## Struktur proyek

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Pemindai (file tunggal, mandiri)
├── scripts/
│   ├── sync-i18n.py            # Skrip penerjemahan batch DeepSeek
│   └── no-emoji-i18n.sh        # Hook pre-commit untuk file lokal tanpa emoji
├── readmes/                    # README yang diterjemahkan
├── pyproject.toml              # Pengemasan Python (opsional)
├── LICENSE                     # MIT
└── README.md                   # File ini
```

## Mulai Cepat

```bash
# Clone dan jalankan (dry-run — tidak perlu API key)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## API key — DeepSeek (opsional)

Pipeline penerjemahan (`--auto`, `--translate`, `--update-stale`) menggunakan DeepSeek untuk menerjemahkan kunci ke dalam 20 bahasa. Anda memerlukan API key **hanya** untuk fitur-fitur ini.

```bash
# 1. Dapatkan kunci: https://platform.deepseek.com/api_keys
# 2. Berikan melalui variabel lingkungan:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Atau buat ~/.hermes/auth.json (terdeteksi otomatis):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Dry-run, inject, patch-safe, ci, check-stale** — tidak ada yang memerlukan API key.

---

---

## Penggunaan

### Mode pemindaian

```bash
# Khusus Prancis (lebih presisi, lebih sedikit hasil)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Semua bahasa (menyeluruh, menangkap semuanya)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Laporan

```bash
# Menghasilkan scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh dengan kandidat tambalan per file
```

### Suntik & terjemahkan

```bash
# Suntikkan kunci yang ditemukan ke dalam fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Terjemahkan ke semua 20 lokal melalui DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Pipeline lengkap: suntik + terjemahkan
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Penambalan yang aman

```bash
# Dry-run (menampilkan perbedaan, tidak menulis apa pun)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Terapkan (menambahkan impor, t(), mengganti teks JSX, memverifikasi sintaks)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Hanya node teks JSX (`>text<`) yang diganti secara otomatis. Array data dan string atribut ditandai untuk ditinjau secara manual.

---

## Cara kerjanya

Pemindai **tidak** menggunakan kamus khusus bahasa. Sebaliknya, ia mencari **pola teknis** yang membedakan teks UI dari kode:

### Apa yang ditangkapnya

| Pola | Contoh | Mendeteksi |
|---------|---------|---------|
| Karakter Latin beraksen | `é`, `ñ`, `ü` | Prancis, Spanyol, Jerman, Vietnam… |
| Skrip non-Latin | 你好, Привет, العربية | CJK, Sirilik, Arab… |
| Frasa multi-kata | `"Uploading file..."` | Bahasa apa pun dengan spasi |
| Tanda baca kalimat | `"Done!"`, `"Continue?"` | Diakhiri dengan `.`, `!`, `?`, `:` |
| Kata dengan huruf kapital judul | `"Dashboard"`, `"Paramètres"` | Kata benda khusus, judul bagian |
| Emoji dalam teks | `"✅ Copié"` | Campuran emoji + teks |

### Apa yang dilewatinya

| Pola | Contoh | Alasan |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | Pengenal JS |
| Kelas CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Styling, bukan teks UI |
| URL dan jalur file | `https://...`, `./components/` | Impor, sumber daya |
| Pernyataan kode | `const t =`, `return null` | Kode JS |
| Konstanta ALL_CAPS | `API_URL`, `MAX_RETRIES` | Konfigurasi |
| Angka murni / heks | `#fff`, `42` | Nilai teknis |

### Pipeline deteksi per file

```
Baris per baris → 
  ① Apakah ini node teks JSX (>text<)? 
     → Periksa apakah terlihat dapat dibaca manusia → Tandai sebagai JSX
  ② Apakah ada string yang dikutip ("..." atau '...')? 
     → Apakah itu pengenal JS? → Lewati
     → Apakah itu teknis? → Lewati
     → Apakah itu dapat dibaca manusia? → Tandai sebagai STRING
```

---

## Konvensi penamaan kunci

Pemindai secara otomatis menghasilkan kunci camelCase dari teks Prancis/Inggris:

| Teks asli | Kunci yang dihasilkan |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Tabrakan** mendapatkan akhiran `_N` (`title_2`, `title_3`). Kunci harus ditinjau setelah pembuatan.

---

## Jaminan keamanan

Setiap tambalan otomatis melalui pemeriksaan berikut:

1. **Impor ditambahkan** — `import { useTranslations } from "next-intl"` jika tidak ada
2. **Deklarasi ditambahkan** — `const t = useTranslations("Namespace")` setelah impor
3. **Kurung seimbang** — `{}[]()` memverifikasi tidak ada JSX yang rusak
4. **t() di dalam string terdeteksi** — `placeholder="{t("key")}"` akan dirender sebagai teks literal
5. **Penulisan bersifat atomik** — file hanya ditulis jika semua pemeriksaan lolos

---

## Kontribusi komunitas diharapkan

Alat ini **open source dan digerakkan oleh komunitas**. Fork, tingkatkan, bagikan.
Setiap kontribusi — baik pola bahasa baru, adaptor kerangka kerja, atau perbaikan bug — membantu membuat web lebih mudah diakses.

Kami terutama menyambut PR dari pengembang yang berbicara dalam bahasa yang saat ini kurang terwakili dalam perangkat i18n.

### 1. Tambahkan deteksi untuk bahasa Anda

Mode `--universal` menangkap semua skrip, tetapi pola spesifik