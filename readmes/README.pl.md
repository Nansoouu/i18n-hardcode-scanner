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

## Funkcje

- **Wykrywanie niezależne od języka** — znajduje czytelny tekst w DOWOLNYM języku (francuski, angielski, wietnamski, arabski, CJK, cyrylica…)
- **Tryb specyficzny dla francuskiego** — dostrojony do projektów francuskich, mniej fałszywych trafień
- **Raport w formacie Markdown do udostępniania** — idealny do przeglądu zespołowego lub artefaktów CI
- **Bezpieczne automatyczne łatanie** — dodaje `import { useTranslations }`, deklaruje `const t = useTranslations(...)`, zastępuje tekst JSX, weryfikuje składnię
- **Potok tłumaczeniowy** — wstrzykuje klucze do `fr.json`, a następnie tłumaczy na wszystkie 20 lokalizacji przez DeepSeek
- **Brak kroku budowania** — pojedynczy plik Pythona, zero zależności (stdlib + opcjonalny `httpx`)

---

## Szybki start

```bash
# Sklonuj i uruchom
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Skanuj swój projekt (symulacja, bez zmian)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## Użycie

### Tryby skanowania

```bash
# Specyficzny dla francuskiego (bardziej precyzyjny, mniej wyników)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Wszystkie języki (wyczerpujący, wykrywa wszystko)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Raport

```bash
# Generuje scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh z kandydatami do łatania dla poszczególnych plików
```

### Wstrzykiwanie i tłumaczenie

```bash
# Wstrzyknij odkryte klucze do fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Tłumacz na wszystkie 20 lokalizacji przez DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Pełny potok: wstrzyknij + tłumacz
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Bezpieczne łatanie

```bash
# Symulacja (pokazuje różnice, nic nie zapisuje)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Zastosuj (dodaje importy, t(), zastępuje tekst JSX, weryfikuje składnię)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Tylko węzły tekstowe JSX (`>text<`) są automatycznie zastępowane. Tablice danych i ciągi znaków w atrybutach są oznaczane do ręcznego przeglądu.

---

## Jak to działa

Skaner **nie** używa słowników specyficznych dla języka. Zamiast tego szuka **wzorców technicznych**, które odróżniają tekst interfejsu od kodu:

### Co wykrywa

| Wzorzec | Przykład | Wykrywa |
|---------|----------|---------|
| Akcentowane znaki łacińskie | `é`, `ñ`, `ü` | Francuski, hiszpański, niemiecki, wietnamski… |
| Skrypty niełacińskie | 你好, Привет, العربية | CJK, cyrylica, arabski… |
| Wyrażenia wielowyrazowe | `"Przesyłanie pliku..."` | Dowolny język ze spacjami |
| Interpunkcja zdaniowa | `"Gotowe!"`, `"Kontynuować?"` | Kończy się na `.`, `!`, `?`, `:` |
| Wyrazy z dużej litery | `"Panel"`, `"Paramètres"` | Nazwy własne, tytuły sekcji |
| Emoji w tekście | `"✅ Skopiowano"` | Mieszane emoji + tekst |

### Co pomija

| Wzorzec | Przykład | Powód |
|---------|----------|-------|
| camelCase / snake_case | `activeUsers`, `error_count` | Identyfikatory JS |
| Klasy CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Stylowanie, nie tekst UI |
| Adresy URL i ścieżki plików | `https://...`, `./components/` | Importy, zasoby |
| Instrukcje kodu | `const t =`, `return null` | Kod JS |
| Stałe ALL_CAPS | `API_URL`, `MAX_RETRIES` | Konfiguracja |
| Czyste liczby / hex | `#fff`, `42` | Wartości techniczne |

### Potok wykrywania na plik

```
Linia po linii → 
  ① Czy to węzeł tekstowy JSX (>text<)? 
     → Sprawdź, czy wygląda na czytelny → Oznacz jako JSX
  ② Czy jest cytowany ciąg znaków ("..." lub '...')? 
     → Czy to identyfikator JS? → Pomiń
     → Czy to techniczne? → Pomiń
     → Czy to czytelne? → Oznacz jako STRING
```

---

## Konwencje nazewnictwa kluczy

Skaner automatycznie generuje klucze w camelCase z tekstu francuskiego/angielskiego:

| Oryginalny tekst | Wygenerowany klucz |
|------------------|--------------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Kolizje** otrzymują sufiks `_N` (`title_2`, `title_3`). Klucze należy przejrzeć po wygenerowaniu.

---

## Gwarancje bezpieczeństwa

Każde automatyczne łatanie przechodzi przez następujące kontrole:

1. **Dodanie importu** — `import { useTranslations } from "next-intl"` jeśli brakuje
2. **Dodanie deklaracji** — `const t = useTranslations("Namespace")` po importach
3. **Zbalansowanie nawiasów** — `{}[]()` weryfikuje brak uszkodzonego JSX
4. **Wykrycie t() wewnątrz ciągów znaków** — `placeholder="{t("key")}"` byłoby renderowane jako dosłowny tekst
5. **Zapis jest atomowy** — plik jest zapisywany tylko wtedy, gdy wszystkie kontrole przejdą

---

## Poszukiwane wkłady społeczności

To narzędzie staje się lepsze z większą liczbą wzorców wykrywania języków. Oto kilka sposobów na pomoc:

### 1. Dodaj wykrywanie dla swojego języka

Tryb `--universal` wykrywa wszystkie skrypty, ale specyficzne wzorce poprawiają dokładność. Dodaj:

- **Zestawy akcentowanych znaków** — wietnamski (ăâđêôơư), polski (łężźć), rumuński (ăâîșț) itp.
- **Niełacińskie słowa stop** — popularne arabskie, hindi, tajskie, greckie słowa będące tekstem UI, a nie kodem
- **Wykrywanie CJK** — zakresy znaków chińskich/japońskich/koreańskich (już zawarte, ale dostrojenie podjęzykowe pomaga)

### 2. Adaptery frameworków

- Obsługa składni `react-i18next` / `i18next` (obecnie tylko next-intl)
- Wykrywanie wzorców `formatMessage()`, `intl.formatMessage()`, `$t()`
- Dodanie obsługi Vue.js / Svelte / Angular

### 3. Ulepszenia nazewnictwa kluczy

- Lepsze wnioskowanie przestrzeni nazw na podstawie struktury katalogów
- Sugestie kluczy wielojęzycznych (nie tylko z francuskiego)
- Integracja z istniejącymi systemami zarządzania tłumaczeniami

### 4. Integracje CI/CD

- Akcja GitHub do uruchamiania skanowania na PR
- Niepowodzenie CI w przypadku wprowadzenia nowego zakodowanego tekstu
- Automatyczne komentowanie PR z wynikami skanowania

### 5. Wtyczki IDE

- Rozszerzenie VS Code do podświetlania zakodowanego tekstu w linii
- Sugerowana szybka naprawa do zawinięcia w wywołanie `t()`
- Przeglądarka plików lokalizacji

---

## Zbuduj dla swojego projektu

Ten skaner został zbudowany dla projektu **[Subvox](https://github.com/Nansoouu/subvox)** — otwartoźródłowej platformy napisów wideo obsługującej 150+ języków napisów i 20 języków interfejsu.

Skaner działa z DOWOLNYM projektem Next.js używającym next-intl. Wystarczy wskazać `