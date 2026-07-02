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

## Fitur

- **Deteksi agnostik bahasa** — menemukan teks yang dapat dibaca manusia dalam BAHASA APAPUN (Prancis, Inggris, Vietnam, Arab, CJK, Sirilik…)
- **Mode khusus Prancis** — disesuaikan untuk proyek Prancis, lebih sedikit positif palsu
- **Laporan markdown yang dapat dibagikan** — sempurna untuk tinjauan tim atau artefak CI
- **Penambalan otomatis yang aman** — menambahkan `import { useTranslations }`, mendeklarasikan `const t = useTranslations(...)`, mengganti teks JSX, memverifikasi sintaks
- **Pipeline terjemahan** — menyuntikkan kunci ke `fr.json`, kemudian menerjemahkan ke semua 20 lokal melalui DeepSeek
- **Tanpa langkah build** — file Python tunggal, tanpa dependensi (stdlib + `httpx` opsional)

---

## Mulai Cepat

```bash
# Clone dan jalankan
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Pindai proyek Anda (dry-run, tanpa perubahan)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

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
# + scripts/i18n-replacements.sh dengan kandidat patch per file
```

### Suntik & terjemahkan

```bash
# Suntikkan kunci yang ditemukan ke fr.json
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

Hanya node teks JSX (`>text<`) yang diganti secara otomatis. Array data dan string atribut ditandai untuk tinjauan manual.

---

## Cara kerjanya

Pemindai **tidak** menggunakan kamus khusus bahasa. Sebaliknya, ia mencari **pola teknis** yang membedakan teks UI dari kode:

### Apa yang ditangkap

| Pola | Contoh | Mendeteksi |
|---------|---------|---------|
| Karakter Latin beraksen | `é`, `ñ`, `ü` | Prancis, Spanyol, Jerman, Vietnam… |
| Skrip non-Latin | 你好, Привет, العربية | CJK, Sirilik, Arab… |
| Frasa multi-kata | `"Uploading file..."` | Bahasa apa pun dengan spasi |
| Tanda baca kalimat | `"Done!"`, `"Continue?"` | Diakhiri dengan `.`, `!`, `?`, `:` |
| Kata dengan huruf kapital judul | `"Dashboard"`, `"Paramètres"` | Kata benda khusus, judul bagian |
| Emoji dalam teks | `"✅ Copié"` | Campuran emoji + teks |

### Apa yang dilewati

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
     → Periksa apakah terlihat seperti teks yang dapat dibaca manusia → Tandai sebagai JSX
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

Setiap patch otomatis melalui pemeriksaan berikut:

1. **Impor ditambahkan** — `import { useTranslations } from "next-intl"` jika tidak ada
2. **Deklarasi ditambahkan** — `const t = useTranslations("Namespace")` setelah impor
3. **Kurung seimbang** — `{}[]()` memverifikasi tidak ada JSX yang rusak
4. **t() di dalam string terdeteksi** — `placeholder="{t("key")}"` akan dirender sebagai teks literal
5. **Penulisan bersifat atomik** — file hanya ditulis jika semua pemeriksaan lolos

---

## Kontribusi komunitas diinginkan

Alat ini menjadi lebih baik dengan lebih banyak pola deteksi bahasa. Berikut beberapa cara untuk membantu:

### 1. Tambahkan deteksi untuk bahasa Anda

Mode `--universal` menangkap semua skrip, tetapi pola spesifik meningkatkan akurasi. Tambahkan:

- **Set karakter beraksen** — Vietnam (ăâđêôơư), Polandia (łężźć), Rumania (ăâîșț), dll.
- **Kata henti non-Latin** — Kata umum Arab, Hindi, Thai, Yunani yang merupakan teks UI, bukan kode
- **Deteksi CJK** — Rentang karakter Cina/Jepang/Korea (sudah termasuk, tetapi penyesuaian sub-bahasa membantu)

### 2. Adaptor kerangka kerja

- Dukung sintaks `react-i18next` / `i18next` (saat ini hanya next-intl)
- Deteksi pola `formatMessage()`, `intl.formatMessage()`, `$t()`
- Tambahkan dukungan Vue.js / Svelte / Angular

### 3. Peningkatan penamaan kunci

- Inferensi namespace yang lebih baik dari struktur direktori
- Saran kunci multi-bahasa (tidak hanya dari bahasa Prancis)
- Integrasi dengan sistem manajemen terjemahan yang ada

### 4. Integrasi CI/CD

- GitHub Action untuk menjalankan pemindaian pada PR
- Gagalkan CI jika teks hardcode baru diperkenalkan
- Komentar otomatis pada PR dengan hasil pemindaian

### 5. Plugin IDE

- Ekstensi VS Code untuk menyorot teks hardcode secara inline
- Perbaikan cepat yang disarankan untuk membungkus dalam panggilan `t()`
- Penjelajah file lokal

---

## Bangun untuk proyek Anda

Pemindai ini dibuat untuk proyek **[Subvox](https://github.com/Nansoouu/subvox)** — platform subtitle video sumber terbuka yang mendukung 150+ bahasa subtitle dan 20 bahasa UI.

Pemindai bekerja dengan proyek Next.js APAPUN yang menggunakan next-intl. Cukup arahkan