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

## Особливості

- **Мовно-незалежне виявлення** — знаходить текст, зрозумілий людині, БУДЬ-ЯКОЮ мовою (французька, англійська, в'єтнамська, арабська, CJK, кирилиця…)
- **Французький режим** — налаштований для французьких проєктів, менше хибних спрацьовувань
- **Звіт у форматі Markdown** — ідеально для командної перевірки або артефактів CI
- **Безпечне автоматичне виправлення** — додає `import { useTranslations }`, оголошує `const t = useTranslations(...)`, замінює JSX текст, перевіряє синтаксис
- **Конвеєр перекладу** — вставляє ключі в `fr.json`, потім перекладає на всі 20 локалей через DeepSeek
- **Без етапу збірки** — один файл Python, нуль залежностей (stdlib + опціональний `httpx`)

---

## Структура проєкту

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Сканер (один файл, самодостатній)
├── scripts/
│   ├── sync-i18n.py            # Сценарій пакетного перекладу DeepSeek
│   └── no-emoji-i18n.sh        # Pre-commit hook для файлів локалі без емодзі
├── readmes/                    # Перекладені README
├── pyproject.toml              # Пакування Python (опціонально)
├── LICENSE                     # MIT
└── README.md                   # Цей файл
```

## Швидкий старт

```bash
# Клонувати та запустити (пробний запуск — ключ API не потрібен)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /шлях/до/вашого/фронтенду --universal --dry-run
```

---

## Ключ API — DeepSeek (опціонально)

Конвеєр перекладу (`--auto`, `--translate`, `--update-stale`) використовує DeepSeek для перекладу ключів на 20 мов. Ключ API потрібен **лише** для цих функцій.

```bash
# 1. Отримайте ключ: https://platform.deepseek.com/api_keys
# 2. Надайте його через змінну середовища:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Або створіть ~/.hermes/auth.json (автоматично виявляється):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Пробний запуск, вставка, безпечне виправлення, CI, перевірка застарілих** — жодна з цих функцій не потребує ключа API.

---

---

## Використання

### Режими сканування

```bash
# Французький режим (точніший, менше результатів)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Всі мови (вичерпний, знаходить усе)
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

# Застосувати (додає імпорти, t(), замінює JSX текст, перевіряє синтаксис)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Автоматично замінюються лише вузли JSX тексту (`>text<`). Масиви даних та рядки атрибутів позначаються для ручної перевірки.

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
| Константи ALL_CAPS | `API_URL`, `MAX_RETRIES` | Конфігурація |
| Чисті числа / hex | `#fff`, `42` | Технічні значення |

### Конвеєр виявлення для кожного файлу

```
Рядок за рядком → 
  ① Чи це вузол JSX тексту (>text<)? 
     → Перевірити, чи виглядає як текст для людини → Позначити як JSX
  ② Чи є рядок у лапках ("..." або '...')? 
     → Чи це ідентифікатор JS? → Пропустити
     → Чи це технічний? → Пропустити
     → Чи це текст для людини? → Позначити як STRING
```

---

## Узгодження імен ключів

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
4. **Виявлено t() всередині рядків** — `placeholder="{t("key")}"` відображатиметься як буквальний текст
5. **Запис атомарний** — файл записується лише якщо всі перевірки пройдено

---

## Запрошуються внески спільноти

Цей інструмент є **відкритим і керованим спільнотою**. Форкніть його, покращуйте, діліться ним.
Кожен внесок — чи то новий мовний шаблон, адаптер фреймворку або виправлення помилки — допомагає зробити веб більш доступним.

Ми особливо вітаємо PR від розробників, які розмовляють мовами, що наразі недостатньо представлені в інструментах i18n.

### 1. Додайте виявлення для вашої мови

Режим `--universal` знаходить усі письменності, але конкретні шаблони...