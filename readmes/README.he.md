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

## תכונות

- **זיהוי ללא תלות בשפה** — מוצא טקסט קריא בכל שפה (צרפתית, אנגלית, וייטנאמית, ערבית, CJK, קירילית…)
- **מצב ייעודי לצרפתית** — מותאם לפרויקטים בצרפתית, פחות תוצאות חיוביות שגויות
- **דוח Markdown לשיתוף** — מושלם לבדיקת צוות או לארטיפקטים של CI
- **תיקון אוטומטי בטוח** — מוסיף `import { useTranslations }`, מצהיר על `const t = useTranslations(...)`, מחליף טקסט JSX, מוודא תחביר
- **צינור תרגום** — מזריק מפתחות לקובץ `fr.json`, ואז מתרגם לכל 20 הלוקלים דרך DeepSeek
- **ללא שלב בנייה** — קובץ Python יחיד, אפס תלויות (stdlib + `httpx` אופציונלי)

---

## מבנה הפרויקט

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # הסורק (קובץ יחיד, עצמאי)
├── scripts/
│   ├── sync-i18n.py            # סקריפט תרגום אצווה של DeepSeek
│   └── no-emoji-i18n.sh        # הוק pre-commit לקבצי לוקל ללא אמוג'י
├── readmes/                    # קבצי README מתורגמים
├── pyproject.toml              # אריזת Python (אופציונלי)
├── LICENSE                     # MIT
└── README.md                   # הקובץ הזה
```

## התחלה מהירה

```bash
# שכפול והרצה (ריצת בדיקה — אין צורך במפתח API)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## מפתח API — DeepSeek (אופציונלי)

צינור התרגום (`--auto`, `--translate`, `--update-stale`) משתמש ב-DeepSeek כדי לתרגם מפתחות ל-20 שפות. אתה צריך מפתח API **רק** עבור תכונות אלה.

```bash
# 1. קבל מפתח: https://platform.deepseek.com/api_keys
# 2. ספק אותו דרך משתנה סביבה:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# או צור ~/.hermes/auth.json (זיהוי אוטומטי):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **ריצת בדיקה, הזרקה, תיקון בטוח, CI, בדיקת מיושנים** — אף אחת מאלה לא דורשת מפתח API.

---

---

## שימוש

### מצבי סריקה

```bash
# ייעודי לצרפתית (מדויק יותר, פחות תוצאות)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# כל השפות (ממצה, תופס הכל)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### דוח

```bash
# יוצר scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh עם הצעות תיקון לפי קובץ
```

### הזרקה ותרגום

```bash
# הזרקת מפתחות שהתגלו לתוך fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# תרגום לכל 20 הלוקלים דרך DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# צינור מלא: הזרקה + תרגום
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### תיקון בטוח

```bash
# ריצת בדיקה (מציג הבדלים, לא כותב דבר)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# יישום (מוסיף יבוא, t(), מחליף טקסט JSX, מוודא תחביר)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

רק צמתי טקסט JSX (`>text<`) מוחלפים אוטומטית. מערכי נתונים ומחרוזות מאפיינים מסומנים לבדיקה ידנית.

---

## איך זה עובד

הסורק **לא** משתמש במילונים ספציפיים לשפה. במקום זאת, הוא מחפש **דפוסים טכניים** שמבדילים טקסט ממשק מקוד:

### מה הוא תופס

| דפוס | דוגמה | מזהה |
|---------|---------|---------|
| תווים לטיניים עם סימנים דיאקריטיים | `é`, `ñ`, `ü` | צרפתית, ספרדית, גרמנית, וייטנאמית… |
| כתבים שאינם לטיניים | 你好, Привет, العربية | CJK, קירילית, ערבית… |
| ביטויים מרובי מילים | `"מעלה קובץ..."` | כל שפה עם רווחים |
| פיסוק משפטים | `"בוצע!"`, `"להמשיך?"` | מסתיים ב-`.`, `!`, `?`, `:` |
| מילים באותיות רישיות | `"לוח בקרה"`, `"Paramètres"` | שמות עצם, כותרות מדורים |
| אמוג'י בטקסט | `"✅ הועתק"` | אמוג'י + טקסט מעורב |

### מה הוא מדלג

| דפוס | דוגמה | סיבה |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | מזהי JS |
| מחלקות CSS / Tailwind | `py-3 px-4`, `text-gray-500` | עיצוב, לא טקסט ממשק |
| כתובות URL ונתיבי קבצים | `https://...`, `./components/` | יבוא, משאבים |
| הצהרות קוד | `const t =`, `return null` | קוד JS |
| קבועים ב-ALL_CAPS | `API_URL`, `MAX_RETRIES` | תצורה |
| מספרים טהורים / הקסה | `#fff`, `42` | ערכים טכניים |

### צינור זיהוי לפי קובץ

```
שורה אחר שורה → 
  ① האם זה צומת טקסט JSX (>text<)? 
     → בדוק אם זה נראה קריא → סמן כ-JSX
  ② האם יש מחרוזת מצוטטת ("..." או '...')? 
     → האם זה מזהה JS? → דלג
     → האם זה טכני? → דלג
     → האם זה קריא? → סמן כ-STRING
```

---

## מוסכמות שמות מפתחות

הסורק יוצר אוטומטית מפתחות ב-camelCase מהטקסט הצרפתי/אנגלי:

| טקסט מקורי | מפתח שנוצר |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**התנגשויות** מקבלות סיומת `_N` (`title_2`, `title_3`). יש לבדוק מפתחות לאחר יצירה.

---

## ערבויות בטיחות

כל תיקון אוטומטי עובר את הבדיקות הבאות:

1. **יבוא נוסף** — `import { useTranslations } from "next-intl"` אם חסר
2. **הצהרה נוספה** — `const t = useTranslations("Namespace")` אחרי יבוא
3. **סוגריים מאוזנים** — `{}[]()` מוודא שאין JSX שבור
4. **זיהוי t() בתוך מחרוזות** — `placeholder="{t("key")}"` יוצג כטקסט מילולי
5. **כתיבה אטומית** — קובץ נכתב רק אם כל הבדיקות עוברות

---

## תרומות קהילה מתבקשות

כלי זה הוא **קוד פתוח ומונחה קהילה**. תפצלו אותו, שפרו אותו, שתפו אותו.
כל תרומה — בין אם דפוס שפה חדש, מתאם מסגרת עבודה, או תיקון באג — עוזרת להפוך את הרשת לנגישה יותר.

אנו במיוחד מברכים על PRs ממפתחים הדוברים שפות שמיוצגות כיום בחסר בכלי i18n.

### 1. הוסף זיהוי לשפה שלך

מצב `--universal` תופס את כל הכתבים, אבל דפוסים ספציפיים