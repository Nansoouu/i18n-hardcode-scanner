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

## Возможности

- **Языконезависимое обнаружение** — находит читаемый человеком текст на ЛЮБОМ языке (французский, английский, вьетнамский, арабский, CJK, кириллица…)
- **Французский режим** — настроен для французских проектов, меньше ложных срабатываний
- **Отчет в формате Markdown** — идеально для командного ревью или артефактов CI
- **Безопасное автоматическое исправление** — добавляет `import { useTranslations }`, объявляет `const t = useTranslations(...)`, заменяет JSX-текст, проверяет синтаксис
- **Конвейер перевода** — вставляет ключи в `fr.json`, затем переводит на все 20 локалей через DeepSeek
- **Без сборки** — один Python-файл, нулевые зависимости (stdlib + опциональный `httpx`)

---

## Быстрый старт

```bash
# Клонируйте и запустите
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Сканируйте проект (пробный запуск, без изменений)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## Использование

### Режимы сканирования

```bash
# Французский режим (более точный, меньше результатов)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Все языки (исчерпывающий, находит всё)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Отчет

```bash
# Создает scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh с кандидатами на исправление по файлам
```

### Вставка и перевод

```bash
# Вставьте найденные ключи в fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Переведите на все 20 локалей через DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Полный конвейер: вставка + перевод
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Безопасное исправление

```bash
# Пробный запуск (показывает различия, ничего не записывает)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Применить (добавляет импорты, t(), заменяет JSX-текст, проверяет синтаксис)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Автоматически заменяются только JSX-текстовые узлы (`>text<`). Массивы данных и строки атрибутов помечаются для ручного ревью.

---

## Как это работает

Сканер **не** использует языковые словари. Вместо этого он ищет **технические шаблоны**, отличающие UI-текст от кода:

### Что он находит

| Шаблон | Пример | Обнаруживает |
|---------|---------|---------|
| Латинские символы с диакритикой | `é`, `ñ`, `ü` | Французский, испанский, немецкий, вьетнамский… |
| Нелатинские письменности | 你好, Привет, العربية | CJK, кириллица, арабский… |
| Многословные фразы | `"Uploading file..."` | Любой язык с пробелами |
| Пунктуация предложений | `"Done!"`, `"Continue?"` | Заканчивается на `.`, `!`, `?`, `:` |
| Слова с заглавной буквы | `"Dashboard"`, `"Paramètres"` | Имена собственные, заголовки разделов |
| Эмодзи в тексте | `"✅ Copié"` | Смешанные эмодзи + текст |

### Что он пропускает

| Шаблон | Пример | Причина |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS-идентификаторы |
| CSS / Tailwind классы | `py-3 px-4`, `text-gray-500` | Стилизация, не UI-текст |
| URL и пути к файлам | `https://...`, `./components/` | Импорты, ресурсы |
| Операторы кода | `const t =`, `return null` | JS-код |
| Константы в ВЕРХНЕМ_РЕГИСТРЕ | `API_URL`, `MAX_RETRIES` | Конфигурация |
| Чистые числа / hex | `#fff`, `42` | Технические значения |

### Конвейер обнаружения для каждого файла

```
Строка за строкой → 
  ① Это JSX-текстовый узел (>text<)? 
     → Проверить, выглядит ли как читаемый текст → Пометить как JSX
  ② Есть ли строка в кавычках ("..." или '...')? 
     → Это JS-идентификатор? → Пропустить
     → Это технический текст? → Пропустить
     → Это читаемый текст? → Пометить как STRING
```

---

## Соглашения об именовании ключей

Сканер автоматически генерирует ключи в camelCase из французского/английского текста:

| Исходный текст | Сгенерированный ключ |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Коллизии** получают суффикс `_N` (`title_2`, `title_3`). Ключи следует проверять после генерации.

---

## Гарантии безопасности

Каждое автоматическое исправление проходит следующие проверки:

1. **Добавлен импорт** — `import { useTranslations } from "next-intl"`, если отсутствует
2. **Добавлено объявление** — `const t = useTranslations("Namespace")` после импортов
3. **Скобки сбалансированы** — `{}[]()` проверяет отсутствие сломанного JSX
4. **t() внутри строк обнаружена** — `placeholder="{t("key")}"` отображался бы как буквальный текст
5. **Запись атомарна** — файл записывается только если все проверки пройдены

---

## Требуются вклады сообщества

Этот инструмент становится лучше с добавлением новых шаблонов обнаружения языков. Вот несколько способов помочь:

### 1. Добавьте обнаружение для вашего языка

Режим `--universal` находит все письменности, но специфические шаблоны повышают точность. Добавьте:

- **Наборы символов с диакритикой** — вьетнамский (ăâđêôơư), польский (łężźć), румынский (ăâîșț) и т.д.
- **Нелатинские стоп-слова** — распространенные арабские, хинди, тайские, греческие слова, являющиеся UI-текстом, а не кодом
- **Обнаружение CJK** — диапазоны китайских/японских/корейских символов (уже включены, но настройка под язык помогает)

### 2. Адаптеры фреймворков

- Поддержка синтаксиса `react-i18next` / `i18next` (сейчас только next-intl)
- Обнаружение шаблонов `formatMessage()`, `intl.formatMessage()`, `$t()`
- Поддержка Vue.js / Svelte / Angular

### 3. Улучшение именования ключей

- Лучшее определение пространства имен из структуры каталогов
- Предложения ключей на нескольких языках (не только с французского)
- Интеграция с существующими системами управления переводами

### 4. Интеграции CI/CD

- GitHub Action для запуска сканирования на PR
- Ошибка CI при добавлении нового жестко закодированного текста
- Автоматические комментарии на PR с результатами сканирования

### 5. Плагины для IDE

- Расширение VS Code для подсветки жестко закодированного текста
- Предлагаемое быстрое исправление для оборачивания в вызов `t()`
- Обозреватель файлов локалей

---

## Создано для вашего проекта

Этот сканер был создан для проекта **[Subvox](https://github.com/Nansoouu/subvox)** — платформы субтитров с открытым исходным кодом, поддерживающей 150+ языков субтитров и 20 языков интерфейса.

Сканер работает с ЛЮБЫМ проектом Next.js, использующим next-intl. Просто укажите `