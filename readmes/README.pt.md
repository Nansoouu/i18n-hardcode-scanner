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

## Funcionalidades

- **Detecção independente de idioma** — encontra texto legível em QUALQUER idioma (francês, inglês, vietnamita, árabe, CJK, cirílico…)
- **Modo específico para francês** — ajustado para projetos franceses, menos falsos positivos
- **Relatório markdown compartilhável** — perfeito para revisão em equipe ou artefatos de CI
- **Correção automática segura** — adiciona `import { useTranslations }`, declara `const t = useTranslations(...)`, substitui texto JSX, verifica sintaxe
- **Pipeline de tradução** — injeta chaves em `fr.json`, depois traduz para todos os 20 locais via DeepSeek
- **Sem etapa de build** — arquivo Python único, zero dependências (stdlib + `httpx` opcional)

---

## Início Rápido

```bash
# Clone e execute
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# Escaneie seu projeto (simulação, sem alterações)
python3 i18n_hardcode_scanner.py --project /caminho/para/seu/frontend --universal --dry-run
```

---

## Uso

### Modos de escaneamento

```bash
# Específico para francês (mais preciso, menos resultados)
python3 i18n_hardcode_scanner.py --project ./meu-app --dry-run

# Todos os idiomas (exaustivo, captura tudo)
python3 i18n_hardcode_scanner.py --project ./meu-app --universal --dry-run
```

### Relatório

```bash
# Gera scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh com candidatos a patch por arquivo
```

### Injetar e traduzir

```bash
# Injeta chaves descobertas em fr.json
python3 i18n_hardcode_scanner.py --project ./meu-app --inject

# Traduz para todos os 20 locais via DeepSeek
python3 i18n_hardcode_scanner.py --project ./meu-app --translate

# Pipeline completo: injetar + traduzir
python3 i18n_hardcode_scanner.py --project ./meu-app --auto
```

### Correção segura

```bash
# Simulação (mostra diferenças, não escreve nada)
python3 i18n_hardcode_scanner.py --project ./meu-app --patch-safe --dry-run

# Aplicar (adiciona imports, t(), substitui texto JSX, verifica sintaxe)
python3 i18n_hardcode_scanner.py --project ./meu-app --patch-safe
```

Apenas nós de texto JSX (`>texto<`) são substituídos automaticamente. Arrays de dados e strings de atributos são sinalizados para revisão manual.

---

## Como funciona

O scanner **não** usa dicionários específicos de idioma. Em vez disso, ele procura **padrões técnicos** que distinguem texto de UI de código:

### O que ele captura

| Padrão | Exemplo | Detecta |
|---------|---------|---------|
| Caracteres latinos acentuados | `é`, `ñ`, `ü` | Francês, Espanhol, Alemão, Vietnamita… |
| Scripts não latinos | 你好, Привет, العربية | CJK, Cirílico, Árabe… |
| Frases com várias palavras | `"Enviando arquivo..."` | Qualquer idioma com espaços |
| Pontuação de frase | `"Pronto!"`, `"Continuar?"` | Termina com `.`, `!`, `?`, `:` |
| Palavras em título | `"Painel"`, `"Configurações"` | Substantivos próprios, títulos de seção |
| Emoji em texto | `"✅ Copiado"` | Emoji + texto misturados |

### O que ele ignora

| Padrão | Exemplo | Motivo |
|---------|---------|--------|
| camelCase / snake_case | `usuariosAtivos`, `contagem_erros` | Identificadores JS |
| Classes CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Estilização, não texto de UI |
| URLs e caminhos de arquivo | `https://...`, `./componentes/` | Imports, recursos |
| Declarações de código | `const t =`, `return null` | Código JS |
| Constantes em MAIÚSCULAS | `API_URL`, `MAX_TENTATIVAS` | Configuração |
| Números puros / hex | `#fff`, `42` | Valores técnicos |

### Pipeline de detecção por arquivo

```
Linha por linha → 
  ① É um nó de texto JSX (>texto<? 
     → Verificar se parece legível → Sinalizar como JSX
  ② Há uma string entre aspas ("..." ou '...')? 
     → É um identificador JS? → Pular
     → É técnico? → Pular
     → É legível? → Sinalizar como STRING
```

---

## Convenções de nomenclatura de chaves

O scanner gera automaticamente chaves em camelCase a partir do texto em francês/inglês:

| Texto original | Chave gerada |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Colisões** recebem um sufixo `_N` (`titulo_2`, `titulo_3`). As chaves devem ser revisadas após a geração.

---

## Garantias de segurança

Cada correção automática passa por estas verificações:

1. **Import adicionado** — `import { useTranslations } from "next-intl"` se ausente
2. **Declaração adicionada** — `const t = useTranslations("Namespace")` após imports
3. **Chaves balanceadas** — `{}[]()` verifica se não há JSX quebrado
4. **t() dentro de strings detectado** — `placeholder="{t("chave")}"` seria renderizado como texto literal
5. **Escrita é atômica** — arquivo só é escrito se todas as verificações passarem

---

## Contribuições da comunidade são bem-vindas

Esta ferramenta melhora com mais padrões de detecção de idioma. Aqui estão algumas formas de ajudar:

### 1. Adicionar detecção para seu idioma

O modo `--universal` captura todos os scripts, mas padrões específicos melhoram a precisão. Adicione:

- **Conjuntos de caracteres acentuados** — Vietnamita (ăâđêôơư), Polonês (łężźć), Romeno (ăâîșț), etc.
- **Stopwords não latinas** — Palavras comuns em Árabe, Hindi, Tailandês, Grego que são texto de UI, não código
- **Detecção CJK** — Intervalos de caracteres Chinês/Japonês/Coreano (já incluídos, mas ajuste por sub-idioma ajuda)

### 2. Adaptadores de framework

- Suporte à sintaxe `react-i18next` / `i18next` (atualmente apenas next-intl)
- Detectar padrões `formatMessage()`, `intl.formatMessage()`, `$t()`
- Adicionar suporte a Vue.js / Svelte / Angular

### 3. Melhorias na nomenclatura de chaves

- Melhor inferência de namespace a partir da estrutura de diretórios
- Sugestões de chaves em vários idiomas (não apenas do francês)
- Integração com sistemas existentes de gerenciamento de tradução

### 4. Integrações CI/CD

- GitHub Action para executar escaneamento em PRs
- Falhar CI se novo texto hardcoded for introduzido
- Comentário automático em PRs com resultados do escaneamento

### 5. Plugins para IDE

- Extensão VS Code para destacar texto hardcoded inline
- Correção rápida sugerida para envolver em chamada `t()`
- Explorador de arquivos de localidade

---

## Construído para seu projeto

Este scanner foi construído para o projeto **[Subvox](https://github.com/Nansoouu/subvox)** — uma plataforma de legendas de vídeo open-source que suporta 150+ idiomas de legenda e 20 idiomas de UI.

O scanner funciona com QUALQUER projeto Next.js que use next-intl. Basta apontar