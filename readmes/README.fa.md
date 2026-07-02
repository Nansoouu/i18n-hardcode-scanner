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

## ویژگی‌ها

- **تشخیص مستقل از زبان** — متن‌های قابل خواندن توسط انسان را در هر زبانی پیدا می‌کند (فرانسوی، انگلیسی، ویتنامی، عربی، CJK، سیریلیک و...)
- **حالت مخصوص فرانسوی** — تنظیم شده برای پروژه‌های فرانسوی، با نتایج مثبت کاذب کمتر
- **گزارش مارک‌داون قابل اشتراک‌گذاری** — مناسب برای بازبینی تیمی یا مصنوعات CI
- **وصله خودکار ایمن** — `import { useTranslations }` را اضافه می‌کند، `const t = useTranslations(...)` را اعلام می‌کند، متن JSX را جایگزین می‌کند، نحو را تأیید می‌کند
- **خط لوله ترجمه** — کلیدها را به `fr.json` تزریق می‌کند، سپس از طریق DeepSeek به تمام ۲۰ زبان ترجمه می‌کند
- **بدون مرحله ساخت** — یک فایل پایتونی واحد، بدون وابستگی (stdlib + `httpx` اختیاری)

---

## شروع سریع

```bash
# کلون و اجرا
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# اسکن پروژه (اجرای آزمایشی، بدون تغییر)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## نحوه استفاده

### حالت‌های اسکن

```bash
# مخصوص فرانسوی (دقیق‌تر، نتایج کمتر)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# همه زبان‌ها (جامع، همه چیز را می‌گیرد)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### گزارش

```bash
# فایل scripts/i18n-reports/hardcode-scan-{timestamp}.md را تولید می‌کند
# + فایل scripts/i18n-replacements.sh با کاندیداهای وصله به ازای هر فایل
```

### تزریق و ترجمه

```bash
# تزریق کلیدهای کشف شده به fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# ترجمه به تمام ۲۰ زبان از طریق DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# خط لوله کامل: تزریق + ترجمه
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### وصله ایمن

```bash
# اجرای آزمایشی (تفاوت‌ها را نشان می‌دهد، چیزی نمی‌نویسد)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# اعمال (importها، t()، جایگزینی متن JSX، تأیید نحو را اضافه می‌کند)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

فقط گره‌های متنی JSX (`>text<`) به طور خودکار جایگزین می‌شوند. آرایه‌های داده و رشته‌های ویژگی برای بازبینی دستی علامت‌گذاری می‌شوند.

---

## نحوه کار

اسکنر از **دیکشنری‌های مخصوص زبان** استفاده نمی‌کند. در عوض، به دنبال **الگوهای فنی** می‌گردد که متن رابط کاربری را از کد متمایز می‌کند:

### چه چیزی را می‌گیرد

| الگو | مثال | تشخیص می‌دهد |
|---------|---------|---------|
| کاراکترهای لاتین با اکسنت | `é`, `ñ`, `ü` | فرانسوی، اسپانیایی، آلمانی، ویتنامی... |
| اسکریپت‌های غیر لاتین | 你好, Привет, العربية | CJK، سیریلیک، عربی... |
| عبارات چند کلمه‌ای | `"Uploading file..."` | هر زبانی با فاصله |
| نشانه‌گذاری جمله | `"Done!"`, `"Continue?"` | پایان با `.`, `!`, `?`, `:` |
| کلمات با حرف اول بزرگ | `"Dashboard"`, `"Paramètres"` | اسم‌های خاص، عنوان‌های بخش |
| ایموجی در متن | `"✅ Copié"` | ترکیب ایموجی + متن |

### چه چیزی را رد می‌کند

| الگو | مثال | دلیل |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | شناسه‌های JS |
| کلاس‌های CSS / Tailwind | `py-3 px-4`, `text-gray-500` | استایل‌دهی، نه متن رابط کاربری |
| URLها و مسیرهای فایل | `https://...`, `./components/` | importها، منابع |
| عبارات کد | `const t =`, `return null` | کد JS |
| ثابت‌های ALL_CAPS | `API_URL`, `MAX_RETRIES` | پیکربندی |
| اعداد خالص / هگز | `#fff`, `42` | مقادیر فنی |

### خط لوله تشخیص به ازای هر فایل

```
خط به خط → 
  ① آیا این یک گره متنی JSX است (>text<)? 
     → بررسی کنید که آیا قابل خواندن توسط انسان به نظر می‌رسد → علامت‌گذاری به عنوان JSX
  ② آیا یک رشته نقل قول شده ("..." یا '...') وجود دارد؟ 
     → آیا یک شناسه JS است؟ → رد کردن
     → آیا فنی است؟ → رد کردن
     → آیا قابل خواندن توسط انسان است؟ → علامت‌گذاری به عنوان STRING
```

---

## قراردادهای نام‌گذاری کلید

اسکنر به طور خودکار کلیدهای camelCase را از متن فرانسوی/انگلیسی تولید می‌کند:

| متن اصلی | کلید تولید شده |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**برخوردها** پسوند `_N` دریافت می‌کنند (`title_2`, `title_3`). کلیدها باید پس از تولید بازبینی شوند.

---

## تضمین‌های ایمنی

هر وصله خودکار این بررسی‌ها را پشت سر می‌گذارد:

1. **import اضافه شده** — `import { useTranslations } from "next-intl"` در صورت عدم وجود
2. **اعلان اضافه شده** — `const t = useTranslations("Namespace")` بعد از importها
3. **تعادل براکت‌ها** — `{}[]()` تأیید می‌کند که JSX شکسته نشده است
4. **تشخیص t() درون رشته‌ها** — `placeholder="{t("key")}"` به عنوان متن تحت‌اللفظی نمایش داده می‌شود
5. **نوشتن اتمی است** — فایل فقط در صورت قبولی در تمام بررسی‌ها نوشته می‌شود

---

## مشارکت جامعه مورد استقبال است

این ابزار با الگوهای تشخیص زبان بیشتر بهتر می‌شود. در اینجا چند راه برای کمک وجود دارد:

### 1. تشخیص زبان خود را اضافه کنید

حالت `--universal` تمام اسکریپت‌ها را می‌گیرد، اما الگوهای خاص دقت را بهبود می‌بخشند. اضافه کنید:

- **مجموعه کاراکترهای اکسنت‌دار** — ویتنامی (ăâđêôơư)، لهستانی (łężźć)، رومانیایی (ăâîșț) و غیره.
- **کلمات توقف غیر لاتین** — کلمات رایج عربی، هندی، تایلندی، یونانی که متن رابط کاربری هستند، نه کد
- **تشخیص CJK** — محدوده کاراکترهای چینی/ژاپنی/کره‌ای (از قبل گنجانده شده، اما تنظیم زیرزبانی کمک می‌کند)

### 2. آداپتورهای فریم‌ورک

- پشتیبانی از نحو `react-i18next` / `i18next` (در حال حاضر فقط next-intl)
- تشخیص الگوهای `formatMessage()`، `intl.formatMessage()`، `$t()`
- اضافه کردن پشتیبانی Vue.js / Svelte / Angular

### 3. بهبودهای نام‌گذاری کلید

- استنتاج بهتر فضای نام از ساختار دایرکتوری
- پیشنهادات کلید چند زبانه (نه فقط از فرانسوی)
- ادغام با سیستم‌های مدیریت ترجمه موجود

### 4. ادغام‌های CI/CD

- اکشن گیت‌هاب برای اجرای اسکن در PRها
- شکست CI در صورت معرفی متن سخت‌کد شده جدید
- نظر خودکار در PRها با نتایج اسکن

### 5. پلاگین‌های IDE

- افزونه VS Code برای برجسته‌سازی متن سخت‌کد شده درون خطی
- رفع سریع پیشنهادی برای بسته‌بندی در فراخوانی `t()`
- مرورگر فایل محلی

---

## برای پروژه خود بسازید

این اسکنر برای پروژه **[Subvox](https://github.com/Nansoouu/subvox)** ساخته شده است — یک پلتفرم زیرنویس ویدیویی متن‌باز که از ۱۵۰+ زبان زیرنویس و ۲۰ زبان رابط کاربری پشتیبانی می‌کند.

اسکنر با هر پروژه Next.js که از next-intl استفاده می‌کند کار می‌کند. فقط به