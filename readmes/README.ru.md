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

## Возможности

- **Языконезависимое обнаружение** — находит читаемый человеком текст на ЛЮБОМ языке (французский, английский, вьетнамский, арабский, CJK, кириллица…)
- **Французский режим** — настроен для французских проектов, меньше ложных срабатываний
- **Отчет в формате Markdown** — идеально для командного ревью или артефактов CI
- **Безопасное автопатчинг** — добавляет `import { useTranslations }`, объявляет `const t = useTranslations(...)`, заменяет JSX-текст, проверяет синтаксис
- **Конвейер перевода** — вставляет ключи в `fr.json`, затем переводит на все 20 локалей через DeepSeek
- **Без этапа сборки** — один Python-файл, нулевые зависимости (stdlib + опциональный `httpx`)

---

## Структура проекта

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Сканер (один файл, самодостаточный)
├── scripts/
│   ├── sync-i18n.py            # Скрипт пакетного перевода DeepSeek
│   └── no-emoji-i18n.sh        # Pre-commit hook для файлов локалей без эмодзи
├── readmes/                    # Переведенные README
├── pyproject.toml              # Упаковка Python (опционально)
├── LICENSE                     # MIT
└── README.md                   # Этот файл
```

## Быстрый старт

```bash
# Клонировать и запустить (пробный запуск — API-ключ не нужен)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## API-ключ — DeepSeek (опционально)

Конвейер перевода (`--auto`, `--translate`, `--update-stale`) использует DeepSeek для перевода ключей на 20 языков. API-ключ нужен **только** для этих функций.

```bash
# 1. Получить ключ: https://platform.deepseek.com/api_keys
# 2. Указать через переменную окружения:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Или создать ~/.hermes/auth.json (автоопределение):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Пробный запуск, инжекция, безопасное патчинг, CI, проверка устаревших** — ни одна из этих функций не требует API-ключа.

---

---

## Использование

### Режимы сканирования

```bash
# Французский режим (более точный, меньше результатов)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Все языки (исчерпывающий, ловит всё)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Отчет

```bash
# Генерирует scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh с кандидатами на патчинг по файлам
```

### Инжекция и перевод

```bash
# Вставить найденные ключи в fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Перевести на все 20 локалей через DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Полный конвейер: инжекция + перевод
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Безопасное патчинг

```bash
# Пробный запуск (показывает различия, ничего не записывает)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Применить (добавляет импорты, t(), заменяет JSX-текст, проверяет синтаксис)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Автоматически заменяются только узлы JSX-текста (`>text<`). Массивы данных и строки атрибутов помечаются для ручного ревью.

---

## Как это работает

Сканер **не** использует языковые словари. Вместо этого он ищет **технические шаблоны**, которые отличают UI-текст от кода:

### Что он ловит

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
| camelCase / snake_case | `activeUsers`, `error_count` | Идентификаторы JS |
| CSS / Tailwind классы | `py-3 px-4`, `text-gray-500` | Стилизация, не UI-текст |
| URL и пути к файлам | `https://...`, `./components/` | Импорты, ресурсы |
| Операторы кода | `const t =`, `return null` | JS-код |
| Константы в ALL_CAPS | `API_URL`, `MAX_RETRIES` | Конфигурация |
| Чистые числа / hex | `#fff`, `42` | Технические значения |

### Конвейер обнаружения для каждого файла

```
Строка за строкой → 
  ① Это узел JSX-текста (>text<)? 
     → Проверить, выглядит ли как читаемый человеком → Пометить как JSX
  ② Есть ли строка в кавычках ("..." или '...')? 
     → Это JS-идентификатор? → Пропустить
     → Это техническое? → Пропустить
     → Это читаемый человеком текст? → Пометить как STRING
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

Каждое автопатчинг проходит следующие проверки:

1. **Добавлен импорт** — `import { useTranslations } from "next-intl"` если отсутствует
2. **Добавлено объявление** — `const t = useTranslations("Namespace")` после импортов
3. **Скобки сбалансированы** — `{}[]()` проверяет отсутствие сломанного JSX
4. **Обнаружен t() внутри строк** — `placeholder="{t("key")}"` будет отображаться как буквальный текст
5. **Запись атомарна** — файл записывается только если все проверки пройдены

---

## Требуются вклады сообщества

Этот инструмент **с открытым исходным кодом и управляется сообществом**. Форкните его, улучшайте, делитесь им.
Каждый вклад — будь то новый языковой шаблон, адаптер фреймворка или исправление ошибки — помогает сделать веб более доступным.

Мы особенно приветствуем PR от разработчиков, говорящих на языках, которые в настоящее время недостаточно представлены в инструментарии i18n.

### 1. Добавьте обнаружение для вашего языка

Режим `--universal` ловит все письменности, но конкретные шаблоны...