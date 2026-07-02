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

## विशेषताएं

- **भाषा-अज्ञेय पहचान** — किसी भी भाषा (फ्रेंच, अंग्रेजी, वियतनामी, अरबी, CJK, सिरिलिक…) में मानव-पठनीय टेक्स्ट ढूंढता है
- **फ्रेंच-विशिष्ट मोड** — फ्रेंच प्रोजेक्ट्स के लिए ट्यून किया गया, कम गलत सकारात्मक परिणाम
- **साझा करने योग्य मार्कडाउन रिपोर्ट** — टीम समीक्षा या CI आर्टिफैक्ट्स के लिए एकदम सही
- **सुरक्षित ऑटो-पैचिंग** — `import { useTranslations }` जोड़ता है, `const t = useTranslations(...)` घोषित करता है, JSX टेक्स्ट बदलता है, सिंटैक्स सत्यापित करता है
- **अनुवाद पाइपलाइन** — `fr.json` में कुंजियाँ इंजेक्ट करता है, फिर DeepSeek के माध्यम से सभी 20 लोकेल में अनुवाद करता है
- **कोई बिल्ड स्टेप नहीं** — एकल Python फ़ाइल, शून्य निर्भरताएँ (stdlib + वैकल्पिक `httpx`)

---

## प्रोजेक्ट संरचना

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # स्कैनर (एकल फ़ाइल, स्व-निहित)
├── scripts/
│   ├── sync-i18n.py            # DeepSeek बैच अनुवाद स्क्रिप्ट
│   └── no-emoji-i18n.sh        # इमोजी-मुक्त लोकेल फ़ाइलों के लिए प्री-कमिट हुक
├── readmes/                    # अनुवादित READMEs
├── pyproject.toml              # Python पैकेजिंग (वैकल्पिक)
├── LICENSE                     # MIT
└── README.md                   # यह फ़ाइल
```

## त्वरित आरंभ

```bash
# क्लोन करें और चलाएं (ड्राई-रन — कोई API कुंजी आवश्यक नहीं)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## API कुंजी — DeepSeek (वैकल्पिक)

अनुवाद पाइपलाइन (`--auto`, `--translate`, `--update-stale`) कुंजियों को 20 भाषाओं में अनुवाद करने के लिए DeepSeek का उपयोग करती है। आपको इन सुविधाओं के लिए **केवल** एक API कुंजी की आवश्यकता है।

```bash
# 1. कुंजी प्राप्त करें: https://platform.deepseek.com/api_keys
# 2. इसे पर्यावरण चर के माध्यम से प्रदान करें:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# या ~/.hermes/auth.json बनाएं (स्वचालित रूप से पहचाना जाता है):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **ड्राई-रन, इंजेक्ट, पैच-सेफ, सीआई, चेक-स्टेल** — इनमें से किसी को भी API कुंजी की आवश्यकता नहीं है।

---

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

केवल JSX टेक्स्ट नोड्स (`>text<`) स्वचालित रूप से बदले जाते हैं। डेटा ऐरे और विशेषता स्ट्रिंग्स को मैन्युअल समीक्षा के लिए चिह्नित किया जाता है।

---

## यह कैसे काम करता है

स्कैनर भाषा-विशिष्ट शब्दकोशों का **उपयोग नहीं** करता है। इसके बजाय, यह **तकनीकी पैटर्न** देखता है जो UI टेक्स्ट को कोड से अलग करते हैं:

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
|---------|---------|---------|
| camelCase / snake_case | `activeUsers`, `error_count` | JS पहचानकर्ता |
| CSS / Tailwind क्लासेस | `py-3 px-4`, `text-gray-500` | स्टाइलिंग, UI टेक्स्ट नहीं |
| URL और फ़ाइल पथ | `https://...`, `./components/` | इम्पोर्ट, संसाधन |
| कोड स्टेटमेंट | `const t =`, `return null` | JS कोड |
| ALL_CAPS कॉन्स्टेंट | `API_URL`, `MAX_RETRIES` | कॉन्फ़िगरेशन |
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
4. **स्ट्रिंग के अंदर t() का पता लगाया गया** — `placeholder="{t("key")}"` शाब्दिक टेक्स्ट के रूप में प्रस्तुत होगा
5. **लेखन परमाणु है** — फ़ाइल तभी लिखी जाती है जब सभी जाँचें पास हो जाती हैं

---

## सामुदायिक योगदान स्वागत है

यह टूल **ओपन सोर्स और सामुदायिक-संचालित** है। इसे फोर्क करें, इसे बेहतर बनाएं, इसे साझा करें।
हर योगदान — चाहे वह एक नया भाषा पैटर्न हो, एक फ्रेमवर्क एडॉप्टर हो, या एक बग फिक्स हो — वेब को अधिक सुलभ बनाने में मदद करता है।

हम विशेष रूप से उन डेवलपर्स से PR का स्वागत करते हैं जो वर्तमान में i18n टूलिंग में कम प्रतिनिधित्व वाली भाषाएँ बोलते हैं।

### 1. अपनी भाषा के लिए पहचान जोड़ें

`--universal` मोड सभी लिपियों को पकड़ता है, लेकिन विशिष्ट पैट