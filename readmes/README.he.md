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

## תכונות

- **זיהוי ללא תלות בשפה** — מוצא טקסט קריא בכל שפה (צרפתית, אנגלית, וייטנאמית, ערבית, CJK, קירילית…)
- **מצב ייעודי לצרפתית** — מותאם לפרויקטים בצרפתית, פחות תוצאות שגויות
- **דוח Markdown לשיתוף** — מושלם לסקירת צוות או לארטיפקטים של CI
- **תיקון אוטומטי בטוח** — מוסיף `import { useTranslations }`, מצהיר `const t = useTranslations(...)`, מחליף טקסט JSX, מוודא תחביר
- **צינור תרגום** — מזריק מפתחות לקובץ `fr.json`, ואז מתרגם לכל 20 הלוקלים דרך DeepSeek
- **ללא שלב בנייה** — קובץ Python יחיד, ללא תלויות (stdlib + `httpx` אופציונלי)

---

## התחלה מהירה

```bash
# שכפול והרצה
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# סריקת הפרויקט שלך (ריצת יבש, ללא שינויים)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## שימוש

### מצבי סריקה

```bash
# ייעודי לצרפתית (מדויק יותר, פחות תוצאות)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# כל השפות (מקיף, תופס הכל)
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
# ריצת יבש (מציג הבדלים, לא כותב דבר)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# יישום (מוסיף יבוא, t(), מחליף טקסט JSX, מוודא תחביר)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

רק צמתי טקסט JSX (`>text<`) מוחלפים אוטומטית. מערכי נתונים ומחרוזות מאפיינים מסומנים לבדיקה ידנית.

---

## איך זה עובד

הסורק **לא** משתמש במילונים ספציפיים לשפה. במקום זאת, הוא מחפש **תבניות טכניות** שמבדילות טקסט ממשק מקוד:

### מה הוא תופס

| תבנית | דוגמה | מזהה |
|---------|---------|---------|
| תווים לטיניים עם סימנים דיאקריטיים | `é`, `ñ`, `ü` | צרפתית, ספרדית, גרמנית, וייטנאמית… |
| כתבים לא-לטיניים | 你好, Привет, العربية | CJK, קירילית, ערבית… |
| ביטויים מרובי מילים | `"מעלה קובץ..."` | כל שפה עם רווחים |
| פיסוק משפטי | `"בוצע!"`, `"להמשיך?"` | מסתיים ב-`.`, `!`, `?`, `:` |
| מילים באותיות רישיות | `"לוח בקרה"`, `"Paramètres"` | שמות עצם, כותרות מדורים |
| אמוג'י בטקסט | `"✅ הועתק"` | שילוב אמוג'י + טקסט |

### מה הוא מדלג

| תבנית | דוגמה | סיבה |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | מזהי JS |
| מחלקות CSS / Tailwind | `py-3 px-4`, `text-gray-500` | עיצוב, לא טקסט ממשק |
| כתובות URL ונתיבי קבצים | `https://...`, `./components/` | יבואים, משאבים |
| הצהרות קוד | `const t =`, `return null` | קוד JS |
| קבועים באותיות גדולות | `API_URL`, `MAX_RETRIES` | תצורה |
| מספרים טהורים / הקסדצימלי | `#fff`, `42` | ערכים טכניים |

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
2. **הצהרה נוספה** — `const t = useTranslations("Namespace")` אחרי היבוא
3. **סוגריים מאוזנים** — `{}[]()` מוודא שאין JSX שבור
4. **t() בתוך מחרוזות מזוהה** — `placeholder="{t("key")}"` יוצג כטקסט מילולי
5. **כתיבה אטומית** — הקובץ נכתב רק אם כל הבדיקות עוברות

---

## תרומות קהילה מתבקשות

הכלי הזה משתפר עם עוד תבניות זיהוי שפה. הנה כמה דרכים לעזור:

### 1. הוספת זיהוי לשפה שלך

מצב `--universal` תופס את כל הכתבים, אבל תבניות ספציפיות משפרות דיוק. הוסף:

- **ערכות תווים עם סימנים דיאקריטיים** — וייטנאמית (ăâđêôơư), פולנית (łężźć), רומנית (ăâîșț) וכו'
- **מילות עצירה לא-לטיניות** — מילים נפוצות בערבית, הינדית, תאית, יוונית שהן טקסט ממשק, לא קוד
- **זיהוי CJK** — טווחי תווים סיניים/יפניים/קוריאניים (כבר כלול, אבל כוונון תת-שפתי עוזר)

### 2. מתאמי מסגרות עבודה

- תמיכה בתחביר `react-i18next` / `i18next` (כרגע רק next-intl)
- זיהוי תבניות `formatMessage()`, `intl.formatMessage()`, `$t()`
- הוספת תמיכה ב-Vue.js / Svelte / Angular

### 3. שיפורי שמות מפתחות

- הסקת מרחב שמות טובה יותר ממבנה התיקיות
- הצעות מפתחות מרובות שפות (לא רק מצרפתית)
- אינטגרציה עם מערכות ניהול תרגום קיימות

### 4. אינטגרציות CI/CD

- GitHub Action להרצת סריקה על PRs
- כשלון CI אם מוכנס טקסט מקודד חדש
- תגובה אוטומטית על PRs עם תוצאות סריקה

### 5. תוספי IDE

- הרחבה ל-VS Code להדגשת טקסט מקודד בשורה
- הצעת תיקון מהיר לעטיפה בקריאת `t()`
- דפדפן קבצי לוקליזציה

---

## בנייה לפרויקט שלך

הסורק הזה נבנה עבור פרויקט **[Subvox](https://github.com/Nansoouu/subvox)** — פלטפורמת כתוביות וידאו בקוד פתוח התומכת ב-150+ שפות כתוביות ו-20 שפות ממשק.

הסורק עובד עם כל פרויקט Next.js המשתמש ב-next-intl. פשוט הפנה את