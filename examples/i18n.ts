/**
 * i18n.ts — Configuration next-intl (sans routing URL)
 * Approche client-side uniquement : locale dans localStorage
 *
 * Copiez ce fichier dans votre projet : app/i18n.ts
 * Then adapt locales to your needs.
 */

export const locales = [
  "fr", "en", "es", "de", "it", "pt",
  "ar", "ru", "zh", "ja", "ko", "tr",
  "nl", "pl", "uk", "hi", "fa", "he",
  "vi", "id",
] as const;

export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "fr";

export const localeNames: Record<Locale, string> = {
  fr: "Français",    en: "English",    es: "Español",
  de: "Deutsch",     it: "Italiano",   pt: "Português",
  ar: "العربية",      ru: "Русский",   zh: "中文",
  ja: "日本語",       ko: "한국어",      tr: "Türkçe",
  nl: "Nederlands",  pl: "Polski",     uk: "Українська",
  hi: "हिन्दी",       fa: "فارسی",      he: "עברית",
  vi: "Tiếng Việt",  id: "Bahasa Indonesia",
};

export const localeFlags: Record<Locale, string> = {
  fr: "🇫🇷", en: "🇬🇧", es: "🇪🇸", de: "🇩🇪", it: "🇮🇹",
  pt: "🇵🇹", ar: "🇸🇦", ru: "🇷🇺", zh: "🇨🇳", ja: "🇯🇵",
  ko: "🇰🇷", tr: "🇹🇷", nl: "🇳🇱", pl: "🇵🇱", uk: "🇺🇦",
  hi: "🇮🇳", fa: "🇮🇷", he: "🇮🇱", vi: "🇻🇳", id: "🇮🇩",
};

/** Returns the locale stored in localStorage (client-side) */
export function getStoredLocale(): Locale {
  if (typeof window === "undefined") return defaultLocale;
  const stored = localStorage.getItem("locale") as Locale | null;
  if (stored && (locales as readonly string[]).includes(stored)) return stored;
  const browserLang = navigator.language.split("-")[0] as Locale;
  return (locales as readonly string[]).includes(browserLang) ? browserLang : defaultLocale;
}

/** Saves locale in localStorage + cookie (for server-side SEO) */
export function setStoredLocale(locale: Locale): void {
  if (typeof window !== "undefined") {
    localStorage.setItem("locale", locale);
    document.cookie = `NEXT_LOCALE=${locale}; path=/; max-age=31536000; SameSite=Lax`;
  }
}
