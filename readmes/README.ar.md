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

## الميزات

- **اكتشاف مستقل عن اللغة** — يجد النصوص القابلة للقراءة البشرية في أي لغة (الفرنسية، الإنجليزية، الفيتنامية، العربية، اللغات الآسيوية، السيريلية...)
- **وضع خاص بالفرنسية** — مُحسَّن للمشاريع الفرنسية، نتائج إيجابية خاطئة أقل
- **تقرير ماركداون قابل للمشاركة** — مثالي لمراجعة الفريق أو نتائج CI
- **تصحيح تلقائي آمن** — يضيف `import { useTranslations }`، يُصرِّح بـ `const t = useTranslations(...)`، يستبدل نصوص JSX، يتحقق من الصياغة
- **خط أنابيب الترجمة** — يُدخل المفاتيح في `fr.json`، ثم يُترجم إلى جميع الإعدادات المحلية العشرين عبر DeepSeek
- **لا حاجة لخطوة بناء** — ملف Python واحد، بدون تبعيات (stdlib + `httpx` اختياري)

---

## هيكل المشروع

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # الماسح الضوئي (ملف واحد، مكتفي ذاتيًا)
├── scripts/
│   ├── sync-i18n.py            # نص برمجي للترجمة الجماعية عبر DeepSeek
│   └── no-emoji-i18n.sh        # خطاف ما قبل الالتزام لملفات الإعدادات المحلية الخالية من الرموز التعبيرية
├── readmes/                    # ملفات README المترجمة
├── pyproject.toml              # تغليف Python (اختياري)
├── LICENSE                     # MIT
└── README.md                   # هذا الملف
```

## بداية سريعة

```bash
# استنساخ وتشغيل (تشغيل تجريبي — لا حاجة لمفتاح API)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## مفتاح API — DeepSeek (اختياري)

يستخدم خط أنابيب الترجمة (`--auto`، `--translate`، `--update-stale`) DeepSeek لترجمة المفاتيح إلى 20 لغة. أنت بحاجة إلى مفتاح API **فقط** لهذه الميزات.

```bash
# 1. احصل على مفتاح: https://platform.deepseek.com/api_keys
# 2. قدمه عبر متغير بيئي:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# أو أنشئ ~/.hermes/auth.json (يتم اكتشافه تلقائيًا):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **التشغيل التجريبي، الحقن، التصحيح الآمن، CI، التحقق من القديم** — لا يحتاج أي منها إلى مفتاح API.

---

---

## الاستخدام

### أوضاع المسح

```bash
# خاص بالفرنسية (أكثر دقة، نتائج أقل)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# جميع اللغات (شامل، يلتقط كل شيء)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### التقرير

```bash
# يُنشئ scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh مع بدائل التصحيح لكل ملف
```

### الحقن والترجمة

```bash
# حقن المفاتيح المكتشفة في fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# الترجمة إلى جميع الإعدادات المحلية العشرين عبر DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# خط أنابيب كامل: حقن + ترجمة
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### التصحيح الآمن

```bash
# تشغيل تجريبي (يظهر الفروقات، لا يكتب شيئًا)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# تطبيق (يضيف الاستيرادات، t()، يستبدل نصوص JSX، يتحقق من الصياغة)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

فقط عُقد نصوص JSX (`>text<`) يتم استبدالها تلقائيًا. يتم وضع علامة على مصفوفات البيانات وسلاسل السمات للمراجعة اليدوية.

---

## كيف يعمل

لا يستخدم الماسح الضوئي **قواميس خاصة باللغة**. بدلاً من ذلك، يبحث عن **أنماط تقنية** تميز نص واجهة المستخدم عن الكود:

### ما يلتقطه

| النمط | مثال | يكتشف |
|---------|---------|---------|
| أحرف لاتينية مُشكَّلة | `é`، `ñ`، `ü` | الفرنسية، الإسبانية، الألمانية، الفيتنامية... |
| نصوص غير لاتينية | 你好, Привет, العربية | اللغات الآسيوية، السيريلية، العربية... |
| عبارات متعددة الكلمات | `"Uploading file..."` | أي لغة بها مسافات |
| علامات ترقيم الجمل | `"Done!"`، `"Continue?"` | تنتهي بـ `.`، `!`، `?`، `:` |
| كلمات بحرف أول كبير | `"Dashboard"`، `"Paramètres"` | أسماء العلم، عناوين الأقسام |
| رموز تعبيرية في النص | `"✅ Copié"` | مزيج من الرموز التعبيرية والنص |

### ما يتجاوزه

| النمط | مثال | السبب |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`، `error_count` | معرفات JavaScript |
| فئات CSS / Tailwind | `py-3 px-4`، `text-gray-500` | تنسيق، وليس نص واجهة مستخدم |
| عناوين URL ومسارات الملفات | `https://...`، `./components/` | استيرادات، موارد |
| عبارات الكود | `const t =`، `return null` | كود JavaScript |
| ثوابت ALL_CAPS | `API_URL`، `MAX_RETRIES` | إعدادات |
| أرقام / سداسي عشري خالص | `#fff`، `42` | قيم تقنية |

### خط أنابيب الكشف لكل ملف

```
سطرًا بسطر → 
  ① هل هذا عقدة نص JSX (>text<)؟ 
     → تحقق مما إذا كان يبدو قابلاً للقراءة البشرية → ضع علامة كـ JSX
  ② هل هناك سلسلة مقتبسة ("..." أو '...')؟ 
     → هل هي معرف JS؟ → تخطى
     → هل هي تقنية؟ → تخطى
     → هل هي قابلة للقراءة البشرية؟ → ضع علامة كـ STRING
```

---

## اصطلاحات تسمية المفاتيح

يُولِّد الماسح الضوئي تلقائيًا مفاتيح camelCase من النص الفرنسي/الإنجليزي:

| النص الأصلي | المفتاح المُولَّد |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**التصادمات** تحصل على لاحقة `_N` (`title_2`، `title_3`). يجب مراجعة المفاتيح بعد التوليد.

---

## ضمانات السلامة

كل تصحيح تلقائي يمر عبر هذه الفحوصات:

1. **إضافة الاستيراد** — `import { useTranslations } from "next-intl"` إذا كان مفقودًا
2. **إضافة التصريح** — `const t = useTranslations("Namespace")` بعد الاستيرادات
3. **توازن الأقواس** — `{}[]()` يتحقق من عدم وجود JSX مكسور
4. **اكتشاف t() داخل السلاسل** — `placeholder="{t("key")}"` سيتم عرضه كنص حرفي
5. **الكتابة ذرية** — يتم كتابة الملف فقط إذا نجحت جميع الفحوصات

---

## المساهمات المجتمعية مطلوبة

هذه الأداة **مفتوحة المصدر ومُدارة من قبل المجتمع**. انسخها، حسّنها، شاركها.
كل مساهمة — سواء كانت نمط لغة جديد، أو إطار عمل مكيف، أو إصلاح خطأ — تساعد في جعل الويب أكثر سهولة في الوصول.

نرحب بشكل خاص بطلبات السحب من المطورين الذين يتحدثون لغات غير ممثلة بشكل كافٍ في أدوات التدويل.

### 1. أضف اكتشافًا للغتك

وضع `--universal` يلتقط جميع النصوص، ولكن الأنماط المحددة