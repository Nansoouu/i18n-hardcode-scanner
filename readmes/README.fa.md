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

## ویژگی‌ها

- **تشخیص مستقل از زبان** — متن‌های قابل خواندن توسط انسان را در هر زبانی پیدا می‌کند (فرانسوی، انگلیسی، ویتنامی، عربی، CJK، سیریلیک و...)
- **حالت مخصوص فرانسوی** — تنظیم شده برای پروژه‌های فرانسوی، با خطاهای مثبت کاذب کمتر
- **گزارش قابل اشتراک‌گذاری Markdown** — مناسب برای بازبینی تیمی یا مصنوعات CI
- **وصله خودکار ایمن** — `import { useTranslations }` را اضافه می‌کند، `const t = useTranslations(...)` را اعلام می‌کند، متن JSX را جایگزین می‌کند، نحو را تأیید می‌کند
- **خط لوله ترجمه** — کلیدها را به `fr.json` تزریق می‌کند، سپس از طریق DeepSeek به تمام ۲۰ زبان ترجمه می‌کند
- **بدون مرحله ساخت** — یک فایل پایتون واحد، بدون وابستگی (stdlib + `httpx` اختیاری)

---

## ساختار پروژه

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # اسکنر (یک فایل، خودکفا)
├── scripts/
│   ├── sync-i18n.py            # اسکریپت ترجمه دسته‌ای DeepSeek
│   └── no-emoji-i18n.sh        # هوک پیش از commit برای فایل‌های محلی بدون ایموجی
├── readmes/                    # فایل‌های README ترجمه شده
├── pyproject.toml              # بسته‌بندی پایتون (اختیاری)
├── LICENSE                     # MIT
└── README.md                   # این فایل
```

## شروع سریع

```bash
# کلون و اجرا (اجرای آزمایشی — بدون نیاز به کلید API)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## کلید API — DeepSeek (اختیاری)

خط لوله ترجمه (`--auto`، `--translate`، `--update-stale`) از DeepSeek برای ترجمه کلیدها به ۲۰ زبان استفاده می‌کند. شما فقط برای این ویژگی‌ها به کلید API نیاز دارید.

```bash
# 1. دریافت کلید: https://platform.deepseek.com/api_keys
# 2. ارائه آن از طریق متغیر محیطی:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# یا ایجاد ~/.hermes/auth.json (تشخیص خودکار):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **اجرای آزمایشی، تزریق، وصله ایمن، CI، بررسی قدیمی بودن** — هیچ‌کدام به کلید API نیاز ندارند.

---

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
# تولید scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh با کاندیداهای وصله به ازای هر فایل
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
# اجرای آزمایشی (نمایش تفاوت‌ها، چیزی نمی‌نویسد)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# اعمال (اضافه کردن importها، t()، جایگزینی متن JSX، تأیید نحو)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

فقط گره‌های متنی JSX (`>text<`) به طور خودکار جایگزین می‌شوند. آرایه‌های داده و رشته‌های ویژگی برای بازبینی دستی علامت‌گذاری می‌شوند.

---

## نحوه کار

اسکنر از **دیکشنری‌های مخصوص زبان** استفاده نمی‌کند. در عوض، به دنبال **الگوهای فنی** می‌گردد که متن رابط کاربری را از کد متمایز می‌کند:

### چه مواردی را می‌گیرد

| الگو | مثال | تشخیص |
|---------|---------|---------|
| کاراکترهای لاتین با اکسنت | `é`، `ñ`، `ü` | فرانسوی، اسپانیایی، آلمانی، ویتنامی... |
| اسکریپت‌های غیر لاتین | 你好, Привет, العربية | CJK، سیریلیک، عربی... |
| عبارات چند کلمه‌ای | `"Uploading file..."` | هر زبانی با فاصله |
| نشانه‌گذاری جمله | `"Done!"`، `"Continue?"` | پایان با `.`، `!`، `?`، `:` |
| کلمات با حرف اول بزرگ | `"Dashboard"`، `"Paramètres"` | اسم‌های خاص، عنوان‌های بخش |
| ایموجی در متن | `"✅ Copié"` | ترکیب ایموجی + متن |

### چه مواردی را رد می‌کند

| الگو | مثال | دلیل |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`، `error_count` | شناسه‌های JS |
| کلاس‌های CSS / Tailwind | `py-3 px-4`، `text-gray-500` | استایل‌دهی، نه متن رابط کاربری |
| URLها و مسیرهای فایل | `https://...`، `./components/` | importها، منابع |
| عبارات کد | `const t =`، `return null` | کد JS |
| ثابت‌های ALL_CAPS | `API_URL`، `MAX_RETRIES` | پیکربندی |
| اعداد خالص / هگز | `#fff`، `42` | مقادیر فنی |

### خط لوله تشخیص به ازای هر فایل

```
خط به خط → 
  ① آیا این یک گره متنی JSX است (>text<)؟ 
     → بررسی کنید که آیا قابل خواندن توسط انسان به نظر می‌رسد → علامت‌گذاری به عنوان JSX
  ② آیا یک رشته نقل قول شده ("..." یا '...') وجود دارد؟ 
     → آیا یک شناسه JS است؟ → رد کردن
     → آیا فنی است؟ → رد کردن
     → آیا قابل خواندن توسط انسان است؟ → علامت‌گذاری به عنوان STRING
```

---

## قراردادهای نام‌گذاری کلیدها

اسکنر به طور خودکار کلیدهای camelCase را از متن فرانسوی/انگلیسی تولید می‌کند:

| متن اصلی | کلید تولید شده |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**برخوردها** پسوند `_N` دریافت می‌کنند (`title_2`، `title_3`). کلیدها باید پس از تولید بازبینی شوند.

---

## تضمین‌های ایمنی

هر وصله خودکار این بررسی‌ها را پشت سر می‌گذارد:

1. **اضافه شدن import** — `import { useTranslations } from "next-intl"` در صورت عدم وجود
2. **اضافه شدن اعلام** — `const t = useTranslations("Namespace")` بعد از importها
3. **تعادل براکت‌ها** — `{}[]()` عدم شکستگی JSX را تأیید می‌کند
4. **تشخیص t() درون رشته‌ها** — `placeholder="{t("key")}"` به صورت متن تحت‌اللفظی نمایش داده می‌شود
5. **نوشتن اتمی** — فایل فقط در صورت قبولی در تمام بررسی‌ها نوشته می‌شود

---

## مشارکت جامعه مورد استقبال است

این ابزار **متن‌باز و مبتنی بر جامعه** است. آن را فورک کنید، بهبود دهید، به اشتراک بگذارید.
هر مشارکتی — چه یک الگوی زبانی جدید، یک آداپتور فریم‌ورک، یا یک رفع باگ — به دسترسی‌پذیرتر شدن وب کمک می‌کند.

ما به ویژه از PRهای توسعه‌دهندگانی که به زبان‌هایی صحبت می‌کنند که در حال حاضر در ابزارهای i18n کمتر نمایندگی دارند، استقبال می‌کنیم.

### 1. اضافه کردن تشخیص برای زبان خود

حالت `--universal` تمام اسکریپت‌ها را می‌گیرد، اما الگوهای خاص