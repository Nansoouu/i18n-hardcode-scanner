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

## 기능

- **언어에 구애받지 않는 탐지** — 모든 언어(프랑스어, 영어, 베트남어, 아랍어, CJK, 키릴 문자 등)에서 사람이 읽을 수 있는 텍스트를 찾습니다.
- **프랑스어 특화 모드** — 프랑스어 프로젝트에 맞게 조정되어 거짓 양성(false positive)이 적습니다.
- **공유 가능한 마크다운 보고서** — 팀 검토 또는 CI 아티팩트에 적합합니다.
- **안전한 자동 패치** — `import { useTranslations }`를 추가하고, `const t = useTranslations(...)`를 선언하며, JSX 텍스트를 교체하고, 구문을 검증합니다.
- **번역 파이프라인** — 키를 `fr.json`에 주입한 후 DeepSeek을 통해 20개 로케일로 번역합니다.
- **빌드 단계 불필요** — 단일 Python 파일, 종속성 없음(표준 라이브러리 + 선택적 `httpx`)

---

## 프로젝트 구조

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # 스캐너 (단일 파일, 자체 포함)
├── scripts/
│   ├── sync-i18n.py            # DeepSeek 배치 번역 스크립트
│   └── no-emoji-i18n.sh        # 이모지 없는 로케일 파일을 위한 사전 커밋 훅
├── readmes/                    # 번역된 README
├── pyproject.toml              # Python 패키징 (선택 사항)
├── LICENSE                     # MIT
└── README.md                   # 이 파일
```

## 빠른 시작

```bash
# 클론 및 실행 (드라이 런 — API 키 불필요)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## API 키 — DeepSeek (선택 사항)

번역 파이프라인(`--auto`, `--translate`, `--update-stale`)은 DeepSeek을 사용하여 키를 20개 언어로 번역합니다. 이러한 기능에만 API 키가 필요합니다.

```bash
# 1. 키 받기: https://platform.deepseek.com/api_keys
# 2. 환경 변수로 제공:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# 또는 ~/.hermes/auth.json 생성 (자동 감지):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **드라이 런, 주입, 안전 패치, CI, 오래된 항목 확인** — 이러한 기능에는 API 키가 필요하지 않습니다.

---

---

## 사용법

### 스캔 모드

```bash
# 프랑스어 특화 (더 정확하고 결과 수 적음)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# 모든 언어 (철저하게 모든 것을 포착)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### 보고서

```bash
# scripts/i18n-reports/hardcode-scan-{timestamp}.md 생성
# + 파일별 패치 후보가 포함된 scripts/i18n-replacements.sh
```

### 주입 및 번역

```bash
# 발견된 키를 fr.json에 주입
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# DeepSeek을 통해 20개 로케일로 번역
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# 전체 파이프라인: 주입 + 번역
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### 안전한 패치

```bash
# 드라이 런 (차이점 표시, 아무것도 쓰지 않음)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# 적용 (import, t() 추가, JSX 텍스트 교체, 구문 검증)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

JSX 텍스트 노드(`>text<`)만 자동으로 교체됩니다. 데이터 배열과 속성 문자열은 수동 검토를 위해 표시됩니다.

---

## 작동 방식

스캐너는 언어별 사전을 사용하지 **않습니다**. 대신 UI 텍스트와 코드를 구분하는 **기술적 패턴**을 찾습니다:

### 포착하는 항목

| 패턴 | 예시 | 탐지 |
|---------|---------|---------|
| 악센트가 있는 라틴 문자 | `é`, `ñ`, `ü` | 프랑스어, 스페인어, 독일어, 베트남어… |
| 비라틴 문자 | 你好, Привет, العربية | CJK, 키릴 문자, 아랍어… |
| 여러 단어 구문 | `"Uploading file..."` | 공백이 있는 모든 언어 |
| 문장 부호 | `"Done!"`, `"Continue?"` | `.`, `!`, `?`, `:`로 끝남 |
| 대문자로 시작하는 단어 | `"Dashboard"`, `"Paramètres"` | 고유 명사, 섹션 제목 |
| 텍스트 내 이모지 | `"✅ Copié"` | 이모지 + 텍스트 혼합 |

### 건너뛰는 항목

| 패턴 | 예시 | 이유 |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS 식별자 |
| CSS / Tailwind 클래스 | `py-3 px-4`, `text-gray-500` | 스타일링, UI 텍스트 아님 |
| URL 및 파일 경로 | `https://...`, `./components/` | 임포트, 리소스 |
| 코드 문장 | `const t =`, `return null` | JS 코드 |
| ALL_CAPS 상수 | `API_URL`, `MAX_RETRIES` | 설정 |
| 순수 숫자 / 16진수 | `#fff`, `42` | 기술적 값 |

### 파일별 탐지 파이프라인

```
라인별로 →
  ① 이것이 JSX 텍스트 노드(>text<)인가?
     → 사람이 읽을 수 있는지 확인 → JSX로 플래그 지정
  ② 따옴표로 묶인 문자열("..." 또는 '...')이 있는가?
     → JS 식별자인가? → 건너뛰기
     → 기술적인가? → 건너뛰기
     → 사람이 읽을 수 있는가? → STRING으로 플래그 지정
```

---

## 키 명명 규칙

스캐너는 프랑스어/영어 텍스트에서 자동으로 camelCase 키를 생성합니다:

| 원본 텍스트 | 생성된 키 |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**충돌** 시 `_N` 접미사가 추가됩니다(`title_2`, `title_3`). 키는 생성 후 검토해야 합니다.

---

## 안전성 보장

모든 자동 패치는 다음 검사를 거칩니다:

1. **Import 추가** — 누락된 경우 `import { useTranslations } from "next-intl"` 추가
2. **선언 추가** — import 뒤에 `const t = useTranslations("Namespace")` 추가
3. **중괄호 균형 확인** — `{}[]()`로 깨진 JSX가 없는지 검증
4. **문자열 내 t() 감지** — `placeholder="{t("key")}"`는 리터럴 텍스트로 렌더링됨
5. **원자적 쓰기** — 모든 검사가 통과된 경우에만 파일 쓰기

---

## 커뮤니티 기여 환영

이 도구는 **오픈 소스이며 커뮤니티 주도**입니다. 포크하고, 개선하고, 공유하세요.
새로운 언어 패턴, 프레임워크 어댑터 또는 버그 수정 등 모든 기여는 웹을 더 접근성 있게 만드는 데 도움이 됩니다.

특히 i18n 도구에서 현재 과소 대표되는 언어를 사용하는 개발자의 PR을 환영합니다.

### 1. 사용자 언어에 대한 탐지 추가

`--universal` 모드는 모든 문자를 포착하지만, 특정 패턴은