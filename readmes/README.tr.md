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

## Özellikler

- **Dil bağımsız algılama** — HERHANGİ bir dilde (Fransızca, İngilizce, Vietnamca, Arapça, Çince, Kiril…) insan tarafından okunabilir metin bulur
- **Fransızca özel mod** — Fransızca projeler için ayarlanmış, daha az yanlış pozitif
- **Paylaşılabilir markdown raporu** — ekip incelemesi veya CI yapıtları için mükemmel
- **Güvenli otomatik yama** — `import { useTranslations }` ekler, `const t = useTranslations(...)` bildirir, JSX metnini değiştirir, sözdizimini doğrular
- **Çeviri hattı** — anahtarları `fr.json` dosyasına ekler, ardından DeepSeek aracılığıyla 20 yerel ayara çevirir
- **Derleme adımı yok** — tek Python dosyası, sıfır bağımlılık (stdlib + isteğe bağlı `httpx`)

---

## Proje yapısı

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Tarayıcı (tek dosya, kendi kendine yeterli)
├── scripts/
│   ├── sync-i18n.py            # DeepSeek toplu çeviri betiği
│   └── no-emoji-i18n.sh        # Emoji içermeyen yerel dosyalar için ön işleme kancası
├── readmes/                    # Çevrilmiş README'ler
├── pyproject.toml              # Python paketleme (isteğe bağlı)
├── LICENSE                     # MIT
└── README.md                   # Bu dosya
```

## Hızlı Başlangıç

```bash
# Kopyala ve çalıştır (deneme modu — API anahtarı gerekmez)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## API anahtarı — DeepSeek (isteğe bağlı)

Çeviri hattı (`--auto`, `--translate`, `--update-stale`) anahtarları 20 dile çevirmek için DeepSeek kullanır. Bu özellikler için **yalnızca** bir API anahtarına ihtiyacınız vardır.

```bash
# 1. Anahtar al: https://platform.deepseek.com/api_keys
# 2. Ortam değişkeni aracılığıyla sağla:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Veya ~/.hermes/auth.json oluştur (otomatik algılanır):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Deneme modu, ekleme, güvenli yama, ci, güncel olmayanları kontrol** — bunların hiçbiri API anahtarı gerektirmez.

---

---

## Kullanım

### Tarama modları

```bash
# Fransızca özel (daha hassas, daha az sonuç)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Tüm diller (kapsamlı, her şeyi yakalar)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Rapor

```bash
# scripts/i18n-reports/hardcode-scan-{timestamp}.md oluşturur
# + dosya başına yama adaylarıyla scripts/i18n-replacements.sh
```

### Ekle ve çevir

```bash
# Bulunan anahtarları fr.json dosyasına ekle
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# DeepSeek aracılığıyla 20 yerel ayara çevir
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Tam hat: ekle + çevir
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Güvenli yama

```bash
# Deneme modu (farkları gösterir, hiçbir şey yazmaz)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Uygula (import'ları, t()'yi ekler, JSX metnini değiştirir, sözdizimini doğrular)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Yalnızca JSX metin düğümleri (`>text<`) otomatik olarak değiştirilir. Veri dizileri ve öznitelik dizeleri manuel inceleme için işaretlenir.

---

## Nasıl çalışır

Tarayıcı, dile özgü sözlükler **kullanmaz**. Bunun yerine, UI metnini koddan ayıran **teknik kalıpları** arar:

### Neyi yakalar

| Kalıp | Örnek | Algılar |
|---------|---------|---------|
| Aksanlı Latin karakterler | `é`, `ñ`, `ü` | Fransızca, İspanyolca, Almanca, Vietnamca… |
| Latin olmayan yazılar | 你好, Привет, العربية | Çince, Kiril, Arapça… |
| Çok kelimeli ifadeler | `"Dosya yükleniyor..."` | Boşluklu herhangi bir dil |
| Cümle noktalama işaretleri | `"Bitti!"`, `"Devam et?"` | `.`, `!`, `?`, `:` ile biter |
| Başlık büyük harfli kelimeler | `"Kontrol Paneli"`, `"Paramètres"` | Özel isimler, bölüm başlıkları |
| Metinde emoji | `"✅ Kopyalandı"` | Karışık emoji + metin |

### Neyi atlar

| Kalıp | Örnek | Neden |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS tanımlayıcıları |
| CSS / Tailwind sınıfları | `py-3 px-4`, `text-gray-500` | Stil, UI metni değil |
| URL'ler ve dosya yolları | `https://...`, `./components/` | İçe aktarmalar, kaynaklar |
| Kod ifadeleri | `const t =`, `return null` | JS kodu |
| TAMAMI_BÜYÜK_HARF sabitleri | `API_URL`, `MAX_RETRIES` | Yapılandırma |
| Saf sayılar / hex | `#fff`, `42` | Teknik değerler |

### Dosya başına algılama hattı

```
Satır satır → 
  ① Bu bir JSX metin düğümü mü (>metin<)? 
     → İnsan tarafından okunabilir görünüyor mu? → JSX olarak işaretle
  ② Tırnak içinde bir dize var mı ("..." veya '...')? 
     → Bu bir JS tanımlayıcısı mı? → Geç
     → Teknik mi? → Geç
     → İnsan tarafından okunabilir mi? → STRING olarak işaretle
```

---

## Anahtar adlandırma kuralları

Tarayıcı, Fransızca/İngilizce metinden otomatik olarak camelCase anahtarlar oluşturur:

| Orijinal metin | Oluşturulan anahtar |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Çakışmalar** `_N` son eki alır (`title_2`, `title_3`). Anahtarlar oluşturulduktan sonra gözden geçirilmelidir.

---

## Güvenlik garantileri

Her otomatik yama şu kontrollerden geçer:

1. **İçe aktarma eklendi** — eksikse `import { useTranslations } from "next-intl"`
2. **Bildirim eklendi** — içe aktarmalardan sonra `const t = useTranslations("Namespace")`
3. **Parantezler dengeli** — `{}[]()` kırık JSX olmadığını doğrular
4. **Dizeler içinde t() algılandı** — `placeholder="{t("key")}"` değişmez metin olarak işlenir
5. **Yazma atomiktir** — dosya yalnızca tüm kontroller geçerse yazılır

---

## Topluluk katkıları aranıyor

Bu araç **açık kaynaklı ve topluluk odaklıdır**. Çatallayın, geliştirin, paylaşın.
Her katkı — ister yeni bir dil kalıbı, ister bir çerçeve bağdaştırıcısı veya bir hata düzeltmesi olsun — web'i daha erişilebilir kılmaya yardımcı olur.

Özellikle i18n araçlarında yeterince temsil edilmeyen dilleri konuşan geliştiricilerden gelen PR'ları memnuniyetle karşılıyoruz.

### 1. Diliniz için algılama ekleyin

`--universal` modu tüm yazıları yakalar, ancak belirli kalıplar