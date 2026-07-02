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

## الميزات

- **اكتشاف مستقل عن اللغة** — يجد النصوص القابلة للقراءة البشرية في أي لغة (الفرنسية، الإنجليزية، الفيتنامية، العربية، الصينية/اليابانية/الكورية، السيريلية...)
- **وضع خاص بالفرنسية** — مُحسَّن للمشاريع الفرنسية، نتائج إيجابية خاطئة أقل
- **تقرير ماركداون قابل للمشاركة** — مثالي لمراجعة الفريق أو أرتيفاكتات CI
- **التصحيح الآمن التلقائي** — يضيف `import { useTranslations }`، ويصرح بـ `const t = useTranslations(...)`، ويستبدل نصوص JSX، ويتحقق من الصياغة
- **خط أنابيب الترجمة** — يحقن المفاتيح في `fr.json`، ثم يترجم إلى جميع الإعدادات المحلية العشرين عبر DeepSeek
- **بدون خطوة بناء** — ملف Python واحد، بدون تبعيات (stdlib + `httpx` اختياري)

---

## البداية السريعة

```bash
# استنساخ وتشغيل
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# فحص مشروعك (تشغيل تجريبي، بدون تغييرات)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## الاستخدام

### أوضاع الفحص

```bash
# خاص بالفرنسية (أكثر دقة، نتائج أقل)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# جميع اللغات (شامل، يكتشف كل شيء)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### التقرير

```bash
# ينشئ scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh مع مرشحات التصحيح لكل ملف
```

### الحقن والترجمة

```bash
# حقن المفاتيح المكتشفة في fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# الترجمة إلى جميع الإعدادات المحلية العشرين عبر DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# خط الأنابيب الكامل: حقن + ترجمة
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### التصحيح الآمن

```bash
# تشغيل تجريبي (يعرض الفروقات، لا يكتب شيئًا)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# تطبيق (يضيف الاستيرادات، t()، يستبدل نصوص JSX، يتحقق من الصياغة)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

فقط عُقد نصوص JSX (`>text<`) يتم استبدالها تلقائيًا. مصفوفات البيانات وسلاسل السمات يتم وضع علامة عليها للمراجعة اليدوية.

---

## كيف يعمل

الماسح **لا** يستخدم قواميس خاصة باللغة. بدلاً من ذلك، يبحث عن **أنماط تقنية** تميز نص واجهة المستخدم عن الكود:

### ما يكتشفه

| النمط | مثال | يكتشف |
|---------|---------|---------|
| أحرف لاتينية مُشكَّلة | `é`, `ñ`, `ü` | الفرنسية، الإسبانية، الألمانية، الفيتنامية... |
| نصوص غير لاتينية | 你好, Привет, العربية | الصينية/اليابانية/الكورية، السيريلية، العربية... |
| عبارات متعددة الكلمات | `"Uploading file..."` | أي لغة بها مسافات |
| علامات ترقيم الجمل | `"Done!"`, `"Continue?"` | تنتهي بـ `.`, `!`, `?`, `:` |
| كلمات بحالة عنوان | `"Dashboard"`, `"Paramètres"` | أسماء العلم، عناوين الأقسام |
| رموز تعبيرية في النص | `"✅ Copié"` | رموز تعبيرية + نص مختلط |

### ما يتخطاه

| النمط | مثال | السبب |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | معرفات JavaScript |
| فئات CSS / Tailwind | `py-3 px-4`, `text-gray-500` | تنسيق، وليس نص واجهة مستخدم |
| عناوين URL ومسارات الملفات | `https://...`, `./components/` | استيرادات، موارد |
| عبارات الكود | `const t =`, `return null` | كود JavaScript |
| ثوابت ALL_CAPS | `API_URL`, `MAX_RETRIES` | إعدادات |
| أرقام / سداسي عشري خالص | `#fff`, `42` | قيم تقنية |

### خط أنابيب الكشف لكل ملف

```
سطرًا بسطر → 
  ① هل هذه عقدة نص JSX (>text<)? 
     → تحقق مما إذا كانت تبدو قابلة للقراءة البشرية → ضع علامة كـ JSX
  ② هل هناك سلسلة مقتبسة ("..." أو '...')? 
     → هل هي معرف JavaScript؟ → تخطى
     → هل هي تقنية؟ → تخطى
     → هل هي قابلة للقراءة البشرية؟ → ضع علامة كـ STRING
```

---

## اصطلاحات تسمية المفاتيح

الماسح يولد تلقائيًا مفاتيح camelCase من النص الفرنسي/الإنجليزي:

| النص الأصلي | المفتاح المُنشأ |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**التصادمات** تحصل على لاحقة `_N` (`title_2`, `title_3`). يجب مراجعة المفاتيح بعد الإنشاء.

---

## ضمانات السلامة

كل تصحيح تلقائي يمر عبر هذه الفحوصات:

1. **تمت إضافة الاستيراد** — `import { useTranslations } from "next-intl"` إذا كان مفقودًا
2. **تمت إضافة التصريح** — `const t = useTranslations("Namespace")` بعد الاستيرادات
3. **الأقواس متوازنة** — `{}[]()` يتحقق من عدم كسر JSX
4. **اكتشاف t() داخل السلاسل** — `placeholder="{t("key")}"` سيتم عرضه كنص حرفي
5. **الكتابة ذرية** — يتم كتابة الملف فقط إذا نجحت جميع الفحوصات

---

## مساهمات المجتمع مطلوبة

هذه الأداة تتحسن مع المزيد من أنماط اكتشاف اللغة. إليك بعض الطرق للمساعدة:

### 1. إضافة اكتشاف للغتك

الوضع `--universal` يكتشف جميع النصوص، لكن الأنماط المحددة تحسن الدقة. أضف:

- **مجموعات الأحرف المُشكَّلة** — الفيتنامية (ăâđêôơư)، البولندية (łężźć)، الرومانية (ăâîșț)، إلخ.
- **كلمات توقف غير لاتينية** — كلمات عربية، هندية، تايلاندية، يونانية شائعة هي نصوص واجهة مستخدم، وليست كودًا
- **اكتشاف الصينية/اليابانية/الكورية** — نطاقات الأحرف الصينية/اليابانية/الكورية (مضمنة بالفعل، لكن الضبط الفرعي للغة يساعد)

### 2. محولات الأطر

- دعم صياغة `react-i18next` / `i18next` (حاليًا next-intl فقط)
- اكتشاف أنماط `formatMessage()`، `intl.formatMessage()`، `$t()`
- إضافة دعم Vue.js / Svelte / Angular

### 3. تحسينات تسمية المفاتيح

- استنتاج أفضل للفضاء الاسمي من هيكل الدليل
- اقتراحات مفاتيح متعددة اللغات (ليس فقط من الفرنسية)
- التكامل مع أنظمة إدارة الترجمة الحالية

### 4. تكاملات CI/CD

- إجراء GitHub لتشغيل الفحص على طلبات السحب
- فشل CI إذا تم إدخال نص مشفر جديد
- تعليق تلقائي على طلبات السحب بنتائج الفحص

### 5. إضافات IDE

- إضافة VS Code لتسليط الضوء على النص المشفر مباشرة
- إصلاح سريع مقترح للتغليف في استدعاء `t()`
- مستعرض ملفات الإعدادات المحلية

---

## بناء لمشروعك

تم بناء هذا الماسح لمشروع **[Subvox](https://github.com/Nansoouu/subvox)** — منصة ترجمة فيديو مفتوحة المصدر تدعم 150+ لغة ترجمة و 20 لغة واجهة مستخدم.

الماسح يعمل مع أي مشروع Next.js يستخدم next-intl. فقط أشر