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

## 功能特性

- **语言无关检测** — 可识别任何语言中的人类可读文本（法语、英语、越南语、阿拉伯语、中日韩文、西里尔文……）
- **法语专用模式** — 针对法语项目优化，误报率更低
- **可分享的 Markdown 报告** — 适合团队审查或 CI 产物
- **安全自动补丁** — 添加 `import { useTranslations }`，声明 `const t = useTranslations(...)`，替换 JSX 文本，验证语法
- **翻译流水线** — 将键注入 `fr.json`，然后通过 DeepSeek 翻译至全部 20 个语言环境
- **无需构建步骤** — 单个 Python 文件，零依赖（标准库 + 可选 `httpx`）

---

## 快速开始

```bash
# 克隆并运行
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# 扫描项目（试运行，不修改文件）
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## 使用方法

### 扫描模式

```bash
# 法语专用（更精确，结果更少）
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# 所有语言（全面扫描，捕获所有内容）
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### 报告

```bash
# 生成 scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh 包含每个文件的补丁候选
```

### 注入与翻译

```bash
# 将发现的键注入 fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# 通过 DeepSeek 翻译至全部 20 个语言环境
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# 完整流水线：注入 + 翻译
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### 安全补丁

```bash
# 试运行（显示差异，不写入任何内容）
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# 应用（添加导入、t()、替换 JSX 文本、验证语法）
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

仅自动替换 JSX 文本节点（`>text<`）。数据数组和属性字符串会标记为需要手动审查。

---

## 工作原理

扫描器**不**使用语言特定词典。而是寻找区分 UI 文本与代码的**技术模式**：

### 捕获的内容

| 模式 | 示例 | 检测对象 |
|---------|---------|---------|
| 带重音拉丁字符 | `é`、`ñ`、`ü` | 法语、西班牙语、德语、越南语…… |
| 非拉丁文字 | 你好、Привет、العربية | 中日韩文、西里尔文、阿拉伯文…… |
| 多词短语 | `"Uploading file..."` | 任何带空格的语言 |
| 句子标点 | `"Done!"`、`"Continue?"` | 以 `.`、`!`、`?`、`:` 结尾 |
| 标题大小写单词 | `"Dashboard"`、`"Paramètres"` | 专有名词、章节标题 |
| 文本中的表情符号 | `"✅ Copié"` | 混合表情符号 + 文本 |

### 跳过的内容

| 模式 | 示例 | 原因 |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`、`error_count` | JS 标识符 |
| CSS / Tailwind 类 | `py-3 px-4`、`text-gray-500` | 样式，非 UI 文本 |
| URL 和文件路径 | `https://...`、`./components/` | 导入、资源 |
| 代码语句 | `const t =`、`return null` | JS 代码 |
| 全大写常量 | `API_URL`、`MAX_RETRIES` | 配置 |
| 纯数字 / 十六进制 | `#fff`、`42` | 技术值 |

### 每个文件的检测流水线

```
逐行扫描 → 
  ① 是否为 JSX 文本节点 (>text<)? 
     → 检查是否看起来像人类可读文本 → 标记为 JSX
  ② 是否有引号字符串 ("..." 或 '...')? 
     → 是否为 JS 标识符? → 跳过
     → 是否为技术内容? → 跳过
     → 是否为人类可读文本? → 标记为 STRING
```

---

## 键命名约定

扫描器根据法语/英语文本自动生成 camelCase 键：

| 原始文本 | 生成的键 |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**冲突**会添加 `_N` 后缀（`title_2`、`title_3`）。生成后应审查键名。

---

## 安全保障

每个自动补丁都会经过以下检查：

1. **添加导入** — 如果缺失则添加 `import { useTranslations } from "next-intl"`
2. **添加声明** — 在导入后添加 `const t = useTranslations("Namespace")`
3. **花括号平衡** — `{}[]()` 验证 JSX 未损坏
4. **检测字符串内的 t()** — `placeholder="{t("key")}"` 会渲染为字面文本
5. **写入是原子操作** — 仅在所有检查通过后才写入文件

---

## 欢迎社区贡献

这个工具会随着更多语言检测模式的加入而变得更好。以下是一些帮助方式：

### 1. 为您的语言添加检测

`--universal` 模式可捕获所有文字，但特定模式可提高准确性。添加：

- **带重音字符集** — 越南语（ăâđêôơư）、波兰语（łężźć）、罗马尼亚语（ăâîșț）等
- **非拉丁停用词** — 常见的阿拉伯语、印地语、泰语、希腊语中属于 UI 文本而非代码的词汇
- **中日韩检测** — 中文/日文/韩文字符范围（已包含，但子语言调优有帮助）

### 2. 框架适配器

- 支持 `react-i18next` / `i18next` 语法（目前仅支持 next-intl）
- 检测 `formatMessage()`、`intl.formatMessage()`、`$t()` 模式
- 添加 Vue.js / Svelte / Angular 支持

### 3. 键命名改进

- 根据目录结构更好地推断命名空间
- 多语言键建议（不仅限于法语）
- 与现有翻译管理系统集成

### 4. CI/CD 集成

- GitHub Action 在 PR 上运行扫描
- 如果引入新的硬编码文本则 CI 失败
- 在 PR 上自动评论扫描结果

### 5. IDE 插件

- VS Code 扩展，内联高亮硬编码文本
- 建议快速修复，包裹在 `t()` 调用中
- 语言环境文件浏览器

---

## 为您的项目构建

此扫描器专为 **[Subvox](https://github.com/Nansoouu/subvox)** 项目构建——一个支持 150+ 字幕语言和 20 种 UI 语言的开源视频字幕平台。

该扫描器适用于任何使用 next-intl 的 Next.js 项目。只需指向