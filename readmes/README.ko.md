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

## 기능

- **언어 무관 감지** — 모든 언어(프랑스어, 영어, 베트남어, 아랍어, CJK, 키릴 문자 등)에서 사람이 읽을 수 있는 텍스트를 찾습니다.
- **프랑스어 특화 모드** — 프랑스어 프로젝트에 최적화되어 있으며, 오탐지가 적습니다.
- **공유 가능한 마크다운 보고서** — 팀 검토 또는 CI 아티팩트에 적합합니다.
- **안전한 자동 패치** — `import { useTranslations }` 추가, `const t = useTranslations(...)` 선언, JSX 텍스트 교체, 구문 검증을 수행합니다.
- **번역 파이프라인** — 키를 `fr.json`에 주입한 후 DeepSeek을 통해 20개 로케일로 번역합니다.
- **빌드 단계 불필요** — 단일 Python 파일, 제로 의존성(stdlib + 선택적 `httpx`)

---

## 빠른 시작

```bash
# 클론 및 실행
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# 프로젝트 스캔 (드라이 런, 변경 없음)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## 사용법

### 스캔 모드

```bash
# 프랑스어 특화 (더 정확함, 결과 수 적음)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# 모든 언어 (포괄적, 모든 항목 감지)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### 보고서

```bash
# scripts/i18n-reports/hardcode-scan-{timestamp}.md 생성
# + 파일별 패치 후보가 포함된 scripts/i18n-replacements.sh 생성
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
# 드라이 런 (차이점 표시, 쓰지 않음)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# 적용 (import, t(), JSX 텍스트 교체, 구문 검증 추가)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

JSX 텍스트 노드(`>text<`)만 자동으로 교체됩니다. 데이터 배열과 속성 문자열은 수동 검토를 위해 플래그가 지정됩니다.

---

## 작동 방식

스캐너는 언어별 사전을 사용하지 **않습니다**. 대신 UI 텍스트와 코드를 구분하는 **기술적 패턴**을 찾습니다:

### 감지하는 항목

| 패턴 | 예시 | 감지 |
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

### 파일별 감지 파이프라인

```
라인별로 →
  ① JSX 텍스트 노드(>text<)인가?
     → 사람이 읽을 수 있는지 확인 → JSX로 플래그 지정
  ② 따옴표로 묶인 문자열("..." 또는 '...')이 있는가?
     → JS 식별자인가? → 건너뜀
     → 기술적인가? → 건너뜀
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

1. **임포트 추가** — `import { useTranslations } from "next-intl"` (없는 경우)
2. **선언 추가** — 임포트 후 `const t = useTranslations("Namespace")` 추가
3. **중괄호 균형 확인** — `{}[]()`로 JSX 손상 여부 검증
4. **문자열 내 t() 감지** — `placeholder="{t("key")}"`는 리터럴 텍스트로 렌더링됨
5. **원자적 쓰기** — 모든 검사 통과 시에만 파일 쓰기

---

## 커뮤니티 기여 환영

이 도구는 더 많은 언어 감지 패턴이 추가될수록 더 좋아집니다. 도움을 주실 수 있는 방법은 다음과 같습니다:

### 1. 사용자 언어 감지 추가

`--universal` 모드는 모든 문자를 감지하지만, 특정 패턴이 정확도를 향상시킵니다. 추가할 항목:

- **악센트 문자 세트** — 베트남어(ăâđêôơư), 폴란드어(łężźć), 루마니아어(ăâîșț) 등
- **비라틴 중지 단어** — 코드가 아닌 UI 텍스트인 일반적인 아랍어, 힌디어, 태국어, 그리스어 단어
- **CJK 감지** — 중국어/일본어/한국어 문자 범위(이미 포함되어 있지만, 하위 언어 튜닝이 도움이 됨)

### 2. 프레임워크 어댑터

- `react-i18next` / `i18next` 구문 지원(현재는 next-intl만 지원)
- `formatMessage()`, `intl.formatMessage()`, `$t()` 패턴 감지
- Vue.js / Svelte / Angular 지원 추가

### 3. 키 명명 개선

- 디렉토리 구조에서 더 나은 네임스페이스 추론
- 다국어 키 제안(프랑스어뿐만 아니라)
- 기존 번역 관리 시스템과의 통합

### 4. CI/CD 통합

- PR에서 스캔을 실행하는 GitHub Action
- 새로운 하드코딩 텍스트가 도입되면 CI 실패
- 스캔 결과로 PR에 자동 댓글

### 5. IDE 플러그인

- 하드코딩된 텍스트를 인라인으로 강조하는 VS Code 확장
- `t()` 호출로 래핑하는 빠른 수정 제안
- 로케일 파일 탐색기

---

## 프로젝트에 맞게 빌드

이 스캐너는 **[Subvox](https://github.com/Nansoouu/subvox)** 프로젝트를 위해 제작되었습니다 — 150개 이상의 자막 언어와 20개의 UI 언어를 지원하는 오픈소스 비디오 자막 플랫폼입니다.

이 스캐너는 next-intl을 사용하는 모든 Next.js 프로젝트에서 작동합니다.