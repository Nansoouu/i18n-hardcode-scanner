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

## विशेषताएं

- **भाषा-अज्ञेय पहचान** — किसी भी भाषा (फ्रेंच, अंग्रेजी, वियतनामी, अरबी, CJK, सिरिलिक…) में मानव-पठनीय टेक्स्ट ढूंढता है
- **फ्रेंच-विशिष्ट मोड** — फ्रेंच प्रोजेक्ट्स के लिए ट्यून किया गया, कम गलत सकारात्मक परिणाम
- **साझा करने योग्य मार्कडाउन रिपोर्ट** — टीम समीक्षा या CI आर्टिफैक्ट्स के लिए एकदम सही
- **सुरक्षित ऑटो-पैचिंग** — `import { useTranslations }` जोड़ता है, `const t = useTranslations(...)` घोषित करता है, JSX टेक्स्ट बदलता है, सिंटैक्स सत्यापित करता है
- **अनुवाद पाइपलाइन** — `fr.json` में कुंजियाँ इंजेक्ट करता है, फिर DeepSeek के माध्यम से सभी 20 लोकेल में अनुवाद करता है
- **कोई बिल्ड स्टेप नहीं** — एकल Python फ़ाइल, शून्य निर्भरताएँ (stdlib + वैकल्पिक `httpx`)

---

## त्वरित आरंभ

```bash
# क्लोन करें और चलाएं
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner

# अपने प्रोजेक्ट को स्कैन करें (ड्राई-रन, कोई बदलाव नहीं)
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## उपयोग

### स्कैन मोड

```bash
# फ्रेंच-विशिष्ट (अधिक सटीक, कम परिणाम)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# सभी भाषाएँ (विस्तृत, सब कुछ पकड़ता है)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### रिपोर्ट

```bash
# scripts/i18n-reports/hardcode-scan-{timestamp}.md जनरेट करता है
# + प्रति-फ़ाइल पैच उम्मीदवारों के साथ scripts/i18n-replacements.sh
```

### इंजेक्ट और अनुवाद करें

```bash
# खोजी गई कुंजियों को fr.json में इंजेक्ट करें
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# DeepSeek के माध्यम से सभी 20 लोकेल में अनुवाद करें
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# पूर्ण पाइपलाइन: इंजेक्ट + अनुवाद
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### सुरक्षित पैचिंग

```bash
# ड्राई-रन (अंतर दिखाता है, कुछ नहीं लिखता)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# लागू करें (imports, t(), JSX टेक्स्ट बदलता है, सिंटैक्स सत्यापित करता है)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

केवल JSX टेक्स्ट नोड्स (`>text<`) स्वचालित रूप से बदले जाते हैं। डेटा ऐरे और विशेषता स्ट्रिंग्स मैन्युअल समीक्षा के लिए चिह्नित की जाती हैं।

---

## यह कैसे काम करता है

स्कैनर **भाषा-विशिष्ट शब्दकोशों** का उपयोग नहीं करता है। इसके बजाय, यह **तकनीकी पैटर्न** ढूंढता है जो UI टेक्स्ट को कोड से अलग करते हैं:

### यह क्या पकड़ता है

| पैटर्न | उदाहरण | पहचानता है |
|---------|---------|---------|
| उच्चारित लैटिन वर्ण | `é`, `ñ`, `ü` | फ्रेंच, स्पेनिश, जर्मन, वियतनामी… |
| गैर-लैटिन लिपियाँ | 你好, Привет, العربية | CJK, सिरिलिक, अरबी… |
| बहु-शब्द वाक्यांश | `"Uploading file..."` | रिक्त स्थान वाली कोई भी भाषा |
| वाक्य विराम चिह्न | `"Done!"`, `"Continue?"` | `.`, `!`, `?`, `:` से समाप्त होता है |
| शीर्षक-केस शब्द | `"Dashboard"`, `"Paramètres"` | उचित संज्ञाएँ, अनुभाग शीर्षक |
| टेक्स्ट में इमोजी | `"✅ Copié"` | मिश्रित इमोजी + टेक्स्ट |

### यह क्या छोड़ता है

| पैटर्न | उदाहरण | कारण |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS पहचानकर्ता |
| CSS / Tailwind क्लासेस | `py-3 px-4`, `text-gray-500` | स्टाइलिंग, UI टेक्स्ट नहीं |
| URL और फ़ाइल पथ | `https://...`, `./components/` | इम्पोर्ट, संसाधन |
| कोड स्टेटमेंट | `const t =`, `return null` | JS कोड |
| ALL_CAPS स्थिरांक | `API_URL`, `MAX_RETRIES` | कॉन्फ़िगरेशन |
| शुद्ध संख्याएँ / हेक्स | `#fff`, `42` | तकनीकी मान |

### प्रति फ़ाइल पहचान पाइपलाइन

```
पंक्ति दर पंक्ति → 
  ① क्या यह JSX टेक्स्ट नोड है (>text<)? 
     → जाँचें कि क्या यह मानव-पठनीय दिखता है → JSX के रूप में चिह्नित करें
  ② क्या कोई उद्धृत स्ट्रिंग है ("..." या '...')? 
     → क्या यह JS पहचानकर्ता है? → छोड़ें
     → क्या यह तकनीकी है? → छोड़ें
     → क्या यह मानव-पठनीय है? → STRING के रूप में चिह्नित करें
```

---

## कुंजी नामकरण परंपराएँ

स्कैनर फ्रेंच/अंग्रेजी टेक्स्ट से स्वचालित रूप से camelCase कुंजियाँ उत्पन्न करता है:

| मूल टेक्स्ट | उत्पन्न कुंजी |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**टकराव** को `_N` प्रत्यय मिलता है (`title_2`, `title_3`)। उत्पन्न होने के बाद कुंजियों की समीक्षा की जानी चाहिए।

---

## सुरक्षा गारंटी

प्रत्येक ऑटो-पैच इन जाँचों से गुज़रता है:

1. **इम्पोर्ट जोड़ा गया** — यदि गायब है तो `import { useTranslations } from "next-intl"`
2. **घोषणा जोड़ी गई** — इम्पोर्ट के बाद `const t = useTranslations("Namespace")`
3. **ब्रैकेट संतुलित** — `{}[]()` सत्यापित करता है कि कोई टूटा हुआ JSX नहीं है
4. **स्ट्रिंग्स के अंदर t() का पता लगाया** — `placeholder="{t("key")}"` शाब्दिक टेक्स्ट के रूप में प्रस्तुत होगा
5. **लेखन परमाणु है** — फ़ाइल तभी लिखी जाती है जब सभी जाँचें पास हो जाएँ

---

## सामुदायिक योगदान वांछित

यह टूल अधिक भाषा पहचान पैटर्न के साथ बेहतर होता है। यहाँ मदद करने के कुछ तरीके हैं:

### 1. अपनी भाषा के लिए पहचान जोड़ें

`--universal` मोड सभी लिपियों को पकड़ता है, लेकिन विशिष्ट पैटर्न सटीकता में सुधार करते हैं। जोड़ें:

- **उच्चारित वर्ण सेट** — वियतनामी (ăâđêôơư), पोलिश (łężźć), रोमानियाई (ăâîșț), आदि।
- **गैर-लैटिन स्टॉपवर्ड्स** — सामान्य अरबी, हिंदी, थाई, ग्रीक शब्द जो UI टेक्स्ट हैं, कोड नहीं
- **CJK पहचान** — चीनी/जापानी/कोरियाई वर्ण श्रेणियाँ (पहले से शामिल, लेकिन उप-भाषा ट्यूनिंग मदद करती है)

### 2. फ्रेमवर्क एडाप्टर

- `react-i18next` / `i18next` सिंटैक्स के लिए समर्थन (वर्तमान में केवल next-intl)
- `formatMessage()`, `intl.formatMessage()`, `$t()` पैटर्न का पता लगाएं
- Vue.js / Svelte / Angular समर्थन जोड़ें

### 3. कुंजी नामकरण में सुधार

- निर्देशिका संरचना से बेहतर नेमस्पेस अनुमान
- बहु-भाषा कुंजी सुझाव (केवल फ्रेंच से नहीं)
- मौजूदा अनुवाद प्रबंधन प्रणालियों के साथ एकीकरण

### 4. CI/CD एकीकरण

- PR पर स्कैन चलाने के लिए GitHub Action
- यदि नया हार्डकोडेड टेक्स्ट पेश किया जाता है तो CI विफल करें
- स्कैन परिणामों के साथ PR पर ऑटो-टिप्पणी

### 5. IDE प्लगइन्स

- इनलाइन हार्डकोडेड टेक्स्ट को हाइलाइट करने के लिए VS Code एक्सटेंशन
- `t()` कॉल में लपेटने के लिए सुझाया गया त्वरित-सुधार
- लोकेल फ़ाइल एक्सप्लोरर

---

## अपने प्रोजेक्ट के लिए बनाएं

यह स्कैनर **[Subvox](https://github.com/Nansoouu/subvox)** प्रोजेक्ट के लिए बनाया गया था — एक ओपन-सोर्स वीडियो सबटाइटल प्लेटफ़ॉर्म जो 150+ सबटाइटल भाषाओं और 20 UI भाषाओं का समर्थन करता है।

स्कैनर next-intl का उपयोग करने वाले किसी भी Next.js प्रोजेक्ट के साथ काम करता है। बस पॉइंट करें