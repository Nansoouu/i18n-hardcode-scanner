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

## Особливості

- **Мовно-незалежне виявлення** — знаходить текст, зрозумілий людині, БУДЬ-ЯКОЮ мовою (французька, англійська, в'єтнамська, арабська, CJK, кирилиця…)
- **Французький режим** — налаштований для французьких проєктів, менше хибних спрацьовувань
- **Звіт у форматі Markdown** — ідеально для перевірки командою або артефактів CI
- **Безпечне автоматичне виправлення** — додає `import { useTranslations }`, оголошує `const t = useTranslations(...)`, замінює текст JSX, перевіряє синтаксис
- **Конвеєр перекладу** — вставляє ключі в `fr.json`, потім перекладає на всі 20 локалей через DeepSeek
- **Без етапу збірки** — один файл Python, нуль залежностей (stdlib + опціональний `httpx`)

---

## Швидкий старт

```bash
# Клонувати та запустити
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Сканувати ваш проєкт (пробний запуск, без змін)
python3 i18n_hardcode_scanner.py --project /шлях/до/вашого/фронтенду --universal --dry-run
```

---

## Використання

### Режими сканування

```bash
# Французький режим (точніший, менше результатів)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Усі мови (вичерпний, знаходить усе)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Звіт

```bash
# Генерує scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh з кандидатами на виправлення для кожного файлу
```

### Вставка та переклад

```bash
# Вставити знайдені ключі в fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Перекласти на всі 20 локалей через DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Повний конвеєр: вставка + переклад
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Безпечне виправлення

```bash
# Пробний запуск (показує відмінності, нічого не записує)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Застосувати (додає імпорти, t(), замінює текст JSX, перевіряє синтаксис)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Автоматично замінюються лише текстові вузли JSX (`>text<`). Масиви даних і рядки атрибутів позначаються для ручної перевірки.

---

## Як це працює

Сканер **не** використовує мовні словники. Натомість він шукає **технічні шаблони**, які відрізняють текст інтерфейсу від коду:

### Що він знаходить

| Шаблон | Приклад | Виявляє |
|---------|---------|---------|
| Латинські символи з діакритикою | `é`, `ñ`, `ü` | Французька, іспанська, німецька, в'єтнамська… |
| Нелатинські письменності | 你好, Привет, العربية | CJK, кирилиця, арабська… |
| Багатослівні фрази | `"Завантаження файлу..."` | Будь-яка мова з пробілами |
| Пунктуація речень | `"Готово!"`, `"Продовжити?"` | Закінчується на `.`, `!`, `?`, `:` |
| Слова з великої літери | `"Панель керування"`, `"Параметри"` | Власні назви, заголовки розділів |
| Емодзі в тексті | `"✅ Скопійовано"` | Змішаний емодзі + текст |

### Що він пропускає

| Шаблон | Приклад | Причина |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | Ідентифікатори JS |
| CSS / Tailwind класи | `py-3 px-4`, `text-gray-500` | Стилізація, не текст інтерфейсу |
| URL та шляхи до файлів | `https://...`, `./components/` | Імпорти, ресурси |
| Інструкції коду | `const t =`, `return null` | Код JS |
| Константи ВЕЛИКИМИ_ЛІТЕРАМИ | `API_URL`, `MAX_RETRIES` | Конфігурація |
| Чисті числа / hex | `#fff`, `42` | Технічні значення |

### Конвеєр виявлення для кожного файлу

```
Рядок за рядком → 
  ① Чи це текстовий вузол JSX (>text<)? 
     → Перевірити, чи виглядає як текст для людини → Позначити як JSX
  ② Чи є рядок у лапках ("..." або '...')? 
     → Це ідентифікатор JS? → Пропустити
     → Це технічний? → Пропустити
     → Це текст для людини? → Позначити як STRING
```

---

## Узгодження назв ключів

Сканер автоматично генерує ключі в стилі camelCase з французького/англійського тексту:

| Оригінальний текст | Згенерований ключ |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Колізії** отримують суфікс `_N` (`title_2`, `title_3`). Ключі слід перевіряти після генерації.

---

## Гарантії безпеки

Кожне автоматичне виправлення проходить такі перевірки:

1. **Додано імпорт** — `import { useTranslations } from "next-intl"`, якщо відсутній
2. **Додано оголошення** — `const t = useTranslations("Namespace")` після імпортів
3. **Збалансовані дужки** — `{}[]()` перевіряє, чи не зламано JSX
4. **Виявлено t() всередині рядків** — `placeholder="{t("key")}"` відображалося б як буквальний текст
5. **Атомарний запис** — файл записується лише якщо всі перевірки пройдено

---

## Потрібна допомога спільноти

Цей інструмент стає кращим із більшою кількістю шаблонів виявлення мов. Ось кілька способів допомогти:

### 1. Додати виявлення для вашої мови

Режим `--universal` знаходить усі письменності, але специфічні шаблони підвищують точність. Додайте:

- **Набори символів з діакритикою** — в'єтнамська (ăâđêôơư), польська (łężźć), румунська (ăâîșț) тощо.
- **Нелатинські стоп-слова** — поширені арабські, хінді, тайські, грецькі слова, які є текстом інтерфейсу, а не кодом
- **Виявлення CJK** — діапазони китайських/японських/корейських символів (вже включено, але налаштування підмов допомагає)

### 2. Адаптери фреймворків

- Підтримка синтаксису `react-i18next` / `i18next` (наразі лише next-intl)
- Виявлення шаблонів `formatMessage()`, `intl.formatMessage()`, `$t()`
- Додати підтримку Vue.js / Svelte / Angular

### 3. Покращення назв ключів

- Краще визначення простору імен зі структури каталогів
- Багатомовні пропозиції ключів (не лише з французької)
- Інтеграція з існуючими системами керування перекладами

### 4. Інтеграції CI/CD

- GitHub Action для запуску сканування на PR
- Відмова CI, якщо додано новий жорстко закодований текст
- Автоматичний коментар на PR з результатами сканування

### 5. Плагіни IDE

- Розширення VS Code для підсвічування жорстко закодованого тексту
- Запропоноване швидке виправлення для обгортання у виклик `t()`
- Оглядач файлів локалей

---

## Створено для вашого проєкту

Цей сканер створено для проєкту **[Subvox](https://github.com/Nansoouu/subvox)** — відкритої платформи відеосубтитрів, яка підтримує 150+ мов субтитрів і 20 мов інтерфейсу.

Сканер працює з БУДЬ-ЯКИМ проєктом Next.js, який використовує next-intl. Просто вкажіть `