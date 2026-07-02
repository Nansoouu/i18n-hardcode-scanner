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

## Özellikler

- **Dilden bağımsız algılama** — HERHANGİ bir dildeki (Fransızca, İngilizce, Vietnamca, Arapça, Çince-Japonca-Korece, Kiril…) insan tarafından okunabilir metni bulur
- **Fransızca özel modu** — Fransızca projeler için ayarlanmış, daha az yanlış pozitif
- **Paylaşılabilir markdown raporu** — ekip incelemesi veya CI yapıtları için mükemmel
- **Güvenli otomatik yama** — `import { useTranslations }` ekler, `const t = useTranslations(...)` bildirir, JSX metnini değiştirir, sözdizimini doğrular
- **Çeviri hattı** — anahtarları `fr.json` dosyasına enjekte eder, ardından DeepSeek aracılığıyla 20 yerel ayarın tamamına çevirir
- **Derleme adımı yok** — tek bir Python dosyası, sıfır bağımlılık (stdlib + isteğe bağlı `httpx`)

---

## Hızlı Başlangıç

```bash
# Kopyala ve çalıştır
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Projenizi tarayın (kuru çalıştırma, değişiklik yok)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

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
# scripts/i18n-reports/hardcode-scan-{timestamp}.md dosyasını oluşturur
# + dosya başına yama adaylarıyla birlikte scripts/i18n-replacements.sh dosyasını oluşturur
```

### Enjekte et ve çevir

```bash
# Bulunan anahtarları fr.json dosyasına enjekte et
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# DeepSeek aracılığıyla 20 yerel ayarın tamamına çevir
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Tam hat: enjekte et + çevir
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Güvenli yama

```bash
# Kuru çalıştırma (farkları gösterir, hiçbir şey yazmaz)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Uygula (içe aktarmaları, t() fonksiyonunu ekler, JSX metnini değiştirir, sözdizimini doğrular)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Yalnızca JSX metin düğümleri (`>metin<`) otomatik olarak değiştirilir. Veri dizileri ve öznitelik dizeleri manuel inceleme için işaretlenir.

---

## Nasıl çalışır

Tarayıcı, dile özgü sözlükler **kullanmaz**. Bunun yerine, UI metnini koddan ayıran **teknik kalıpları** arar:

### Neyi yakalar

| Kalıp | Örnek | Algılar |
|---------|---------|---------|
| Aksanlı Latin karakterler | `é`, `ñ`, `ü` | Fransızca, İspanyolca, Almanca, Vietnamca… |
| Latin olmayan yazılar | 你好, Привет, العربية | Çince-Japonca-Korece, Kiril, Arapça… |
| Çok kelimeli ifadeler | `"Dosya yükleniyor..."` | Boşluklu herhangi bir dil |
| Cümle noktalama işaretleri | `"Bitti!"`, `"Devam et?"` | `.`, `!`, `?`, `:` ile biter |
| Başlık büyük harfli kelimeler | `"Kontrol Paneli"`, `"Paramètres"` | Özel isimler, bölüm başlıkları |
| Metin içinde emoji | `"✅ Kopyalandı"` | Karışık emoji + metin |

### Neyi atlar

| Kalıp | Örnek | Neden |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS tanımlayıcıları |
| CSS / Tailwind sınıfları | `py-3 px-4`, `text-gray-500` | Stil, UI metni değil |
| URL'ler ve dosya yolları | `https://...`, `./components/` | İçe aktarmalar, kaynaklar |
| Kod ifadeleri | `const t =`, `return null` | JS kodu |
| TAMAMI_BÜYÜK_HARF sabitleri | `API_URL`, `MAX_RETRIES` | Yapılandırma |
| Saf sayılar / onaltılık | `#fff`, `42` | Teknik değerler |

### Dosya başına algılama hattı

```
Satır satır → 
  ① Bu bir JSX metin düğümü mü (>metin<)? 
     → İnsan tarafından okunabilir görünüyor mu diye kontrol et → JSX olarak işaretle
  ② Tırnak içinde bir dize var mı ("..." veya '...')? 
     → Bir JS tanımlayıcısı mı? → Atla
     → Teknik mi? → Atla
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

**Çakışmalar** bir `_N` son eki alır (`title_2`, `title_3`). Anahtarlar oluşturulduktan sonra gözden geçirilmelidir.

---

## Güvenlik garantileri

Her otomatik yama şu kontrollerden geçer:

1. **İçe aktarma eklendi** — eksikse `import { useTranslations } from "next-intl"` eklenir
2. **Bildirim eklendi** — içe aktarmalardan sonra `const t = useTranslations("Namespace")` eklenir
3. **Köşeli parantezler dengeli** — `{}[]()` ile JSX'in bozulmadığı doğrulanır
4. **Dizeler içindeki t() algılandı** — `placeholder="{t("key")}"` gerçek metin olarak işlenir
5. **Yazma atomiktir** — dosya yalnızca tüm kontroller geçilirse yazılır

---

## Topluluk katkıları aranıyor

Bu araç, daha fazla dil algılama kalıbıyla daha iyi hale gelir. İşte yardımcı olmanın bazı yolları:

### 1. Diliniz için algılama ekleyin

`--universal` modu tüm yazıları yakalar, ancak belirli kalıplar doğruluğu artırır. Şunları ekleyin:

- **Aksanlı karakter kümeleri** — Vietnamca (ăâđêôơư), Lehçe (łężźć), Rumence (ăâîșț) vb.
- **Latin olmayan durdurma kelimeleri** — Kod değil, UI metni olan yaygın Arapça, Hintçe, Tayca, Yunanca kelimeler
- **Çince-Japonca-Korece algılama** — Çince/Japonca/Korece karakter aralıkları (zaten dahil, ancak alt dil ayarlaması yardımcı olur)

### 2. Çerçeve bağdaştırıcıları

- `react-i18next` / `i18next` sözdizimi desteği (şu anda yalnızca next-intl)
- `formatMessage()`, `intl.formatMessage()`, `$t()` kalıplarını algılama
- Vue.js / Svelte / Angular desteği ekleme

### 3. Anahtar adlandırma iyileştirmeleri

- Dizin yapısından daha iyi ad alanı çıkarımı
- Çok dilli anahtar önerileri (yalnızca Fransızcadan değil)
- Mevcut çeviri yönetim sistemleriyle entegrasyon

### 4. CI/CD entegrasyonları

- PR'lerde tarama çalıştırmak için GitHub Eylemi
- Yeni sabit kodlanmış metin eklenirse CI'yi başarısız kılma
- Tarama sonuçlarıyla PR'lara otomatik yorum yapma

### 5. IDE eklentileri

- Sabit kodlanmış metni satır içinde vurgulamak için VS Code uzantısı
- `t()` çağrısına sarmak için önerilen hızlı düzeltme
- Yerel ayar dosyası gezgini

---

## Projeniz için oluşturun

Bu tarayıcı, **[Subvox](https://github.com/Nansoouu/subvox)** projesi için oluşturulmuştur — 150'den fazla altyazı dili ve 20 UI dilini destekleyen açık kaynaklı bir video altyazı platformu.

Tarayıcı, next-intl kullanan HERHANGİ bir Next.js projesiyle çalışır. Sadece işaret edin