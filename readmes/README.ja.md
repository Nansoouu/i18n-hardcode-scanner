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

## 機能

- **言語に依存しない検出** — あらゆる言語（フランス語、英語、ベトナム語、アラビア語、CJK、キリル文字など）の人間が読めるテキストを検出します
- **フランス語特化モード** — フランス語プロジェクト向けに調整済み、誤検出が少ない
- **共有可能なMarkdownレポート** — チームレビューやCIアーティファクトに最適
- **安全な自動パッチ** — `import { useTranslations }` を追加、`const t = useTranslations(...)` を宣言、JSXテキストを置換、構文を検証
- **翻訳パイプライン** — キーを `fr.json` に注入し、DeepSeek経由ですべての20ロケールに翻訳
- **ビルド不要** — 単一のPythonファイル、依存関係ゼロ（stdlib + オプションの `httpx`）

---

## クイックスタート

```bash
# クローンして実行
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# プロジェクトをスキャン（ドライラン、変更なし）
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## 使用方法

### スキャンモード

```bash
# フランス語特化（より正確、結果が少ない）
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# 全言語（網羅的、すべてをキャッチ）
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### レポート

```bash
# scripts/i18n-reports/hardcode-scan-{timestamp}.md を生成
# + ファイルごとのパッチ候補を含む scripts/i18n-replacements.sh を生成
```

### 注入と翻訳

```bash
# 検出したキーを fr.json に注入
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# DeepSeek経由ですべての20ロケールに翻訳
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# フルパイプライン：注入 + 翻訳
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### 安全なパッチ適用

```bash
# ドライラン（差分を表示、書き込みなし）
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# 適用（インポート、t()、JSXテキスト置換、構文検証を追加）
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

JSXテキストノード（`>text<`）のみが自動置換されます。データ配列と属性文字列は手動レビュー用にフラグが立てられます。

---

## 仕組み

スキャナーは**言語固有の辞書を使用しません**。代わりに、UIテキストとコードを区別する**技術的なパターン**を探します：

### キャッチするもの

| パターン | 例 | 検出対象 |
|---------|---------|---------|
| アクセント付きラテン文字 | `é`、`ñ`、`ü` | フランス語、スペイン語、ドイツ語、ベトナム語… |
| 非ラテン文字 | 你好、Привет、العربية | CJK、キリル文字、アラビア語… |
| 複数単語のフレーズ | `"Uploading file..."` | スペースのある任意の言語 |
| 文の句読点 | `"Done!"`、`"Continue?"` | `.`、`!`、`?`、`:` で終わる |
| タイトルケースの単語 | `"Dashboard"`、`"Paramètres"` | 固有名詞、セクションタイトル |
| テキスト内の絵文字 | `"✅ Copié"` | 絵文字 + テキストの混合 |

### スキップするもの

| パターン | 例 | 理由 |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`、`error_count` | JS識別子 |
| CSS / Tailwindクラス | `py-3 px-4`、`text-gray-500` | スタイリング、UIテキストではない |
| URLとファイルパス | `https://...`、`./components/` | インポート、リソース |
| コード文 | `const t =`、`return null` | JSコード |
| ALL_CAPS定数 | `API_URL`、`MAX_RETRIES` | 設定 |
| 純粋な数字 / 16進数 | `#fff`、`42` | 技術的な値 |

### ファイルごとの検出パイプライン

```
行ごとに →
  ① JSXテキストノード（>text<）か？
     → 人間が読めるかチェック → JSXとしてフラグ
  ② 引用符で囲まれた文字列（"..." または '...'）か？
     → JS識別子か？ → スキップ
     → 技術的なものか？ → スキップ
     → 人間が読めるか？ → STRINGとしてフラグ
```

---

## キー命名規則

スキャナーはフランス語/英語のテキストからcamelCaseキーを自動生成します：

| 元のテキスト | 生成されたキー |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**衝突**には `_N` サフィックスが付きます（`title_2`、`title_3`）。キーは生成後にレビューする必要があります。

---

## 安全性の保証

すべての自動パッチは以下のチェックを通過します：

1. **インポート追加** — `import { useTranslations } from "next-intl"` が不足している場合に追加
2. **宣言追加** — インポート後に `const t = useTranslations("Namespace")` を追加
3. **括弧のバランス** — `{}[]()` でJSXが壊れていないことを検証
4. **t() が文字列内にある場合を検出** — `placeholder="{t("key")}"` はリテラルテキストとしてレンダリングされる
5. **書き込みはアトミック** — すべてのチェックに合格した場合のみファイルが書き込まれる

---

## コミュニティ貢献歓迎

このツールは、より多くの言語検出パターンによって改善されます。以下は貢献方法の例です：

### 1. 言語の検出を追加

`--universal` モードはすべての文字をキャッチしますが、特定のパターンが精度を向上させます。以下を追加：

- **アクセント付き文字セット** — ベトナム語（ăâđêôơư）、ポーランド語（łężźć）、ルーマニア語（ăâîșț）など
- **非ラテン語のストップワード** — コードではなくUIテキストである一般的なアラビア語、ヒンディー語、タイ語、ギリシャ語の単語
- **CJK検出** — 中国語/日本語/韓国語の文字範囲（すでに含まれていますが、サブ言語の調整が役立ちます）

### 2. フレームワークアダプター

- `react-i18next` / `i18next` 構文のサポート（現在はnext-intlのみ）
- `formatMessage()`、`intl.formatMessage()`、`$t()` パターンの検出
- Vue.js / Svelte / Angularのサポート追加

### 3. キー命名の改善

- ディレクトリ構造からのより良い名前空間推測
- 多言語キーの提案（フランス語だけでなく）
- 既存の翻訳管理システムとの統合

### 4. CI/CD統合

- PRでスキャンを実行するGitHub Action
- 新しいハードコードされたテキストが導入された場合にCIを失敗させる
- スキャン結果でPRに自動コメント

### 5. IDEプラグイン

- インラインでハードコードされたテキストを強調表示するVS Code拡張機能
- `t()` 呼び出しでラップするクイックフィックスを提案
- ロケールファイルエクスプローラー

---

## プロジェクト用にビルド

このスキャナーは **[Subvox](https://github.com/Nansoouu/subvox)** プロジェクト用に構築されました — 150以上の字幕言語と20のUI言語をサポートするオープンソースの動画字幕プラットフォームです。

このスキャナーは、next-intlを使用する任意のNext.jsプロジェクトで動作します。`--project` を指定するだけです。