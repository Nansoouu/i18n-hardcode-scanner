# i18n Integration Examples

This directory contains ready-to-use components for adding multi-language support
to your Next.js project. Copy them into your project and adapt as needed.

## Architecture

```
app/
├── i18n.ts                          # Locale config + localStorage helpers
├── components/
│   ├── I18nProvider.tsx              # Context provider (wrap your layout)
│   └── ui/
│       ├── LanguageSelector.tsx       # Navbar dropdown (20 locales)
│       └── LanguagePicker.tsx         # Advanced multi-select (150+ langs)
└── lib/
    └── languages.ts                  # 150+ language definitions (from Subvox)
```

## Files

| File | Purpose | Required |
|------|---------|----------|
| `i18n.ts` | Locale list, names, flags, localStorage get/set | ✅ Yes |
| `I18nProvider.tsx` | Context provider, dynamic message loading | ✅ Yes |
| `LanguageSelector.tsx` | Navbar dropdown selector | Optional |
| `LanguagePicker.tsx` | Advanced multi-language picker | Optional |

## Quick start

```bash
# 1. Copy the config
cp examples/i18n.ts app/i18n.ts

# 2. Copy the provider
cp examples/I18nProvider.tsx app/components/I18nProvider.tsx

# 3. Wrap your layout
```

```tsx
// app/layout.tsx
import I18nProvider from "@/components/I18nProvider";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>
        <I18nProvider>
          {children}
        </I18nProvider>
      </body>
    </html>
  );
}
```

```bash
# 4. (Optional) Add the selector to your navbar
cp examples/LanguageSelector.tsx app/components/ui/LanguageSelector.tsx
cp examples/LanguagePicker.tsx app/components/ui/LanguagePicker.tsx
```

```tsx
// In your navbar component
import LanguageSelector from "@/components/ui/LanguageSelector";

export default function Navbar() {
  return (
    <nav>
      {/* ... */}
      <LanguageSelector />
    </nav>
  );
}
```

## Required dependencies

```bash
npm install next-intl
```

Your `messages/` directory should contain one JSON file per locale
(e.g., `messages/fr.json`, `messages/en.json`, etc.).

## How it works

1. **`i18n.ts`** defines your 20 locales with names, flags, and localStorage helpers
2. **`I18nProvider.tsx`** creates a React context, reads locale from localStorage,
   dynamically imports the correct JSON messages, and wraps children with
   `NextIntlClientProvider` from `next-intl`
3. **`LanguageSelector`** — a simple button + dropdown for the navbar
4. **`LanguagePicker`** — a full-featured modal with search, region filters,
   and multi-select for 150+ languages

The locale is persisted in **localStorage** (not in the URL), so there's no
URL prefix like `/fr/...`. This keeps your routes clean and avoids SEO
complexity.

## Credits

These components are extracted from **[Subvox](https://github.com/Nansoouu/subvox)** —
the open-source video subtitle platform. They power the 20-language UI
and 150+ language translation system in production.
