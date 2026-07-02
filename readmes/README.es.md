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

## Características

- **Detección independiente del idioma** — encuentra texto legible en CUALQUIER idioma (francés, inglés, vietnamita, árabe, CJK, cirílico…)
- **Modo específico para francés** — ajustado para proyectos franceses, menos falsos positivos
- **Informe markdown compartible** — perfecto para revisión en equipo o artefactos de CI
- **Parcheo automático seguro** — añade `import { useTranslations }`, declara `const t = useTranslations(...)`, reemplaza texto JSX, verifica sintaxis
- **Pipeline de traducción** — inyecta claves en `fr.json`, luego traduce a los 20 locales vía DeepSeek
- **Sin paso de compilación** — archivo Python único, cero dependencias (stdlib + `httpx` opcional)

---

## Inicio rápido

```bash
# Clonar y ejecutar
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Escanear tu proyecto (simulación, sin cambios)
python3 i18n_hardcode_scanner.py --project /ruta/a/tu/frontend --universal --dry-run
```

---

## Uso

### Modos de escaneo

```bash
# Específico para francés (más preciso, menos resultados)
python3 i18n_hardcode_scanner.py --project ./mi-app --dry-run

# Todos los idiomas (exhaustivo, captura todo)
python3 i18n_hardcode_scanner.py --project ./mi-app --universal --dry-run
```

### Informe

```bash
# Genera scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh con candidatos de parche por archivo
```

### Inyectar y traducir

```bash
# Inyectar claves descubiertas en fr.json
python3 i18n_hardcode_scanner.py --project ./mi-app --inject

# Traducir a los 20 locales vía DeepSeek
python3 i18n_hardcode_scanner.py --project ./mi-app --translate

# Pipeline completo: inyectar + traducir
python3 i18n_hardcode_scanner.py --project ./mi-app --auto
```

### Parcheo seguro

```bash
# Simulación (muestra diferencias, no escribe nada)
python3 i18n_hardcode_scanner.py --project ./mi-app --patch-safe --dry-run

# Aplicar (añade imports, t(), reemplaza texto JSX, verifica sintaxis)
python3 i18n_hardcode_scanner.py --project ./mi-app --patch-safe
```

Solo los nodos de texto JSX (`>texto<`) se reemplazan automáticamente. Los arrays de datos y cadenas de atributos se marcan para revisión manual.

---

## Cómo funciona

El escáner **no** utiliza diccionarios específicos de idioma. En su lugar, busca **patrones técnicos** que distinguen el texto de UI del código:

### Lo que captura

| Patrón | Ejemplo | Detecta |
|--------|---------|---------|
| Caracteres latinos acentuados | `é`, `ñ`, `ü` | Francés, español, alemán, vietnamita… |
| Escrituras no latinas | 你好, Привет, العربية | CJK, cirílico, árabe… |
| Frases de varias palabras | `"Subiendo archivo..."` | Cualquier idioma con espacios |
| Puntuación de oraciones | `"¡Hecho!"`, `"¿Continuar?"` | Termina con `.`, `!`, `?`, `:` |
| Palabras en mayúscula inicial | `"Panel"`, `"Paramètres"` | Nombres propios, títulos de sección |
| Emoji en texto | `"✅ Copiado"` | Emoji + texto mixto |

### Lo que omite

| Patrón | Ejemplo | Razón |
|--------|---------|-------|
| camelCase / snake_case | `activeUsers`, `error_count` | Identificadores JS |
| Clases CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Estilo, no texto de UI |
| URLs y rutas de archivo | `https://...`, `./componentes/` | Importaciones, recursos |
| Sentencias de código | `const t =`, `return null` | Código JS |
| Constantes en MAYÚSCULAS | `API_URL`, `MAX_RETRIES` | Configuración |
| Números puros / hex | `#fff`, `42` | Valores técnicos |

### Pipeline de detección por archivo

```
Línea por línea → 
  ① ¿Es un nodo de texto JSX (>texto<)? 
     → Verificar si parece legible → Marcar como JSX
  ② ¿Hay una cadena entre comillas ("..." o '...')? 
     → ¿Es un identificador JS? → Omitir
     → ¿Es técnico? → Omitir
     → ¿Es legible? → Marcar como STRING
```

---

## Convenciones de nomenclatura de claves

El escáner genera automáticamente claves en camelCase a partir del texto en francés/inglés:

| Texto original | Clave generada |
|---------------|----------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Colisiones** reciben un sufijo `_N` (`title_2`, `title_3`). Las claves deben revisarse después de la generación.

---

## Garantías de seguridad

Cada parche automático pasa por estas verificaciones:

1. **Importación añadida** — `import { useTranslations } from "next-intl"` si falta
2. **Declaración añadida** — `const t = useTranslations("Namespace")` después de las importaciones
3. **Llaves equilibradas** — `{}[]()` verifica que no haya JSX roto
4. **t() dentro de cadenas detectado** — `placeholder="{t("clave")}"` se renderizaría como texto literal
5. **Escritura atómica** — el archivo solo se escribe si todas las verificaciones pasan

---

## Contribuciones de la comunidad deseadas

Esta herramienta mejora con más patrones de detección de idiomas. Aquí hay algunas formas de ayudar:

### 1. Añadir detección para tu idioma

El modo `--universal` captura todas las escrituras, pero los patrones específicos mejoran la precisión. Añade:

- **Conjuntos de caracteres acentuados** — Vietnamita (ăâđêôơư), Polaco (łężźć), Rumano (ăâîșț), etc.
- **Palabras vacías no latinas** — Palabras comunes en árabe, hindi, tailandés, griego que son texto de UI, no código
- **Detección CJK** — Rangos de caracteres chino/japonés/coreano (ya incluidos, pero el ajuste por sub-idioma ayuda)

### 2. Adaptadores de frameworks

- Soporte para sintaxis `react-i18next` / `i18next` (actualmente solo next-intl)
- Detectar patrones `formatMessage()`, `intl.formatMessage()`, `$t()`
- Añadir soporte para Vue.js / Svelte / Angular

### 3. Mejoras en la nomenclatura de claves

- Mejor inferencia de espacios de nombres desde la estructura de directorios
- Sugerencias de claves multilingües (no solo desde francés)
- Integración con sistemas de gestión de traducciones existentes

### 4. Integraciones CI/CD

- Acción de GitHub para ejecutar escaneo en PRs
- Fallar CI si se introduce nuevo texto hardcodeado
- Comentario automático en PRs con resultados del escaneo

### 5. Plugins para IDE

- Extensión de VS Code para resaltar texto hardcodeado en línea
- Solución rápida sugerida para envolver en llamada `t()`
- Explorador de archivos de locale

---

## Construido para tu proyecto

Este escáner fue construido para el proyecto **[Subvox](https://github.com/Nansoouu/subvox)** — una plataforma de subtítulos de video de código abierto que soporta 150+ idiomas de subtítulos y 20 idiomas de UI.

El escáner funciona con CUALQUIER proyecto Next.js que use next-intl. Solo apunta