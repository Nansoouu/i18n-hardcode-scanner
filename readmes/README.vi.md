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

## Tính năng

- **Phát hiện không phụ thuộc ngôn ngữ** — tìm văn bản có thể đọc được bằng con người trong BẤT KỲ ngôn ngữ nào (Pháp, Anh, Việt, Ả Rập, CJK, Cyrillic…)
- **Chế độ dành riêng cho tiếng Pháp** — được tinh chỉnh cho các dự án tiếng Pháp, ít cảnh báo sai hơn
- **Báo cáo markdown có thể chia sẻ** — hoàn hảo cho đánh giá nhóm hoặc tạo tạo phẩm CI
- **Tự động vá an toàn** — thêm `import { useTranslations }`, khai báo `const t = useTranslations(...)`, thay thế văn bản JSX, xác minh cú pháp
- **Quy trình dịch thuật** — chèn khóa vào `fr.json`, sau đó dịch sang tất cả 20 ngôn ngữ qua DeepSeek
- **Không cần bước xây dựng** — tệp Python đơn lẻ, không phụ thuộc (stdlib + `httpx` tùy chọn)

---

## Cấu trúc dự án

```
i18n-hardcode-scanner/
├── i18n_hardcode_scanner.py    # Trình quét (tệp đơn, khép kín)
├── scripts/
│   ├── sync-i18n.py            # Tập lệnh dịch hàng loạt DeepSeek
│   └── no-emoji-i18n.sh        # Móc pre-commit cho tệp ngôn ngữ không có biểu tượng cảm xúc
├── readmes/                    # README đã dịch
├── pyproject.toml              # Đóng gói Python (tùy chọn)
├── LICENSE                     # MIT
└── README.md                   # Tệp này
```

## Bắt đầu nhanh

```bash
# Sao chép và chạy (chạy thử — không cần khóa API)
git clone https://github.com/Nansoouu/i18n-hardcode-scanner.git
cd i18n-hardcode-scanner
python3 i18n_hardcode_scanner.py --project /path/to/your/frontend --universal --dry-run
```

---

## Khóa API — DeepSeek (tùy chọn)

Quy trình dịch thuật (`--auto`, `--translate`, `--update-stale`) sử dụng DeepSeek để dịch các khóa sang 20 ngôn ngữ. Bạn chỉ cần khóa API **cho các tính năng này**.

```bash
# 1. Lấy khóa: https://platform.deepseek.com/api_keys
# 2. Cung cấp qua biến môi trường:
export DEEPSEEK_API_KEY="sk-..."
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Hoặc tạo ~/.hermes/auth.json (tự động phát hiện):
# {"credential_pool": {"deepseek": [{"access_token": "sk-..."}]}}
```

> 💡 **Chạy thử, chèn, vá an toàn, ci, kiểm tra lỗi thời** — không tính năng nào cần khóa API.

---

---

## Cách sử dụng

### Chế độ quét

```bash
# Dành riêng cho tiếng Pháp (chính xác hơn, ít kết quả hơn)
python3 i18n_hardcode_scanner.py --project ./my-app --dry-run

# Tất cả ngôn ngữ (toàn diện, bắt mọi thứ)
python3 i18n_hardcode_scanner.py --project ./my-app --universal --dry-run
```

### Báo cáo

```bash
# Tạo scripts/i18n-reports/hardcode-scan-{timestamp}.md
# + scripts/i18n-replacements.sh với các bản vá theo tệp
```

### Chèn & dịch

```bash
# Chèn các khóa đã phát hiện vào fr.json
python3 i18n_hardcode_scanner.py --project ./my-app --inject

# Dịch sang tất cả 20 ngôn ngữ qua DeepSeek
python3 i18n_hardcode_scanner.py --project ./my-app --translate

# Quy trình đầy đủ: chèn + dịch
python3 i18n_hardcode_scanner.py --project ./my-app --auto
```

### Vá an toàn

```bash
# Chạy thử (hiển thị khác biệt, không ghi gì)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe --dry-run

# Áp dụng (thêm import, t(), thay thế văn bản JSX, xác minh cú pháp)
python3 i18n_hardcode_scanner.py --project ./my-app --patch-safe
```

Chỉ các nút văn bản JSX (`>text<`) mới được tự động thay thế. Mảng dữ liệu và chuỗi thuộc tính được đánh dấu để xem xét thủ công.

---

## Cách hoạt động

Trình quét **không** sử dụng từ điển ngôn ngữ cụ thể. Thay vào đó, nó tìm kiếm **các mẫu kỹ thuật** phân biệt văn bản UI với mã:

### Những gì nó bắt được

| Mẫu | Ví dụ | Phát hiện |
|---------|---------|---------|
| Ký tự Latin có dấu | `é`, `ñ`, `ü` | Tiếng Pháp, Tây Ban Nha, Đức, Việt… |
| Chữ viết không phải Latin | 你好, Привет, العربية | CJK, Cyrillic, Ả Rập… |
| Cụm từ nhiều từ | `"Uploading file..."` | Bất kỳ ngôn ngữ nào có dấu cách |
| Dấu câu câu | `"Done!"`, `"Continue?"` | Kết thúc bằng `.`, `!`, `?`, `:` |
| Từ viết hoa đầu | `"Dashboard"`, `"Paramètres"` | Danh từ riêng, tiêu đề phần |
| Biểu tượng cảm xúc trong văn bản | `"✅ Copié"` | Biểu tượng cảm xúc + văn bản hỗn hợp |

### Những gì nó bỏ qua

| Mẫu | Ví dụ | Lý do |
|---------|---------|--------|
| camelCase / snake_case | `activeUsers`, `error_count` | Định danh JS |
| Lớp CSS / Tailwind | `py-3 px-4`, `text-gray-500` | Định dạng, không phải văn bản UI |
| URL và đường dẫn tệp | `https://...`, `./components/` | Import, tài nguyên |
| Câu lệnh mã | `const t =`, `return null` | Mã JS |
| Hằng số ALL_CAPS | `API_URL`, `MAX_RETRIES` | Cấu hình |
| Số thuần / hex | `#fff`, `42` | Giá trị kỹ thuật |

### Quy trình phát hiện theo tệp

```
Từng dòng → 
  ① Đây có phải là nút văn bản JSX (>text<)? 
     → Kiểm tra xem nó có trông giống văn bản có thể đọc được không → Đánh dấu là JSX
  ② Có chuỗi được trích dẫn ("..." hoặc '...')? 
     → Nó có phải là định danh JS không? → Bỏ qua
     → Nó có phải là kỹ thuật không? → Bỏ qua
     → Nó có thể đọc được không? → Đánh dấu là STRING
```

---

## Quy ước đặt tên khóa

Trình quét tự động tạo khóa camelCase từ văn bản tiếng Pháp/Anh:

| Văn bản gốc | Khóa được tạo |
|--------------|---------------|
| `"Paiement annulé"` | `paiementAnnule` |
| `"✅ Copié"` | `copie` |
| `"Wallet non connecté"` | `walletNonConnecte` |
| `"Hello world"` | `helloWorld` |

**Xung đột** nhận được hậu tố `_N` (`title_2`, `title_3`). Các khóa nên được xem xét sau khi tạo.

---

## Đảm bảo an toàn

Mọi bản vá tự động đều trải qua các kiểm tra sau:

1. **Thêm import** — `import { useTranslations } from "next-intl"` nếu thiếu
2. **Thêm khai báo** — `const t = useTranslations("Namespace")` sau các import
3. **Dấu ngoặc cân bằng** — `{}[]()` xác minh không có JSX bị hỏng
4. **Phát hiện t() bên trong chuỗi** — `placeholder="{t("key")}"` sẽ hiển thị dưới dạng văn bản chữ
5. **Ghi là nguyên tử** — tệp chỉ được ghi nếu tất cả các kiểm tra đều đạt

---

## Đóng góp từ cộng đồng được hoan nghênh

Công cụ này là **mã nguồn mở và do cộng đồng điều hành**. Fork nó, cải thiện nó, chia sẻ nó.
Mọi đóng góp — dù là một mẫu ngôn ngữ mới, một bộ chuyển đổi framework, hay một sửa lỗi — đều giúp web trở nên dễ tiếp cận hơn.

Chúng tôi đặc biệt hoan nghênh các PR từ các nhà phát triển nói các ngôn ngữ hiện đang ít được đại diện trong các công cụ i18n.

### 1. Thêm phát hiện cho ngôn ngữ của bạn

Chế độ `--universal` bắt tất cả các chữ viết, nhưng các mẫu cụ thể