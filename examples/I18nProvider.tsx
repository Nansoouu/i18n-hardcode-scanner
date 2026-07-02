"use client";
/**
 * I18nProvider.tsx — Client-side internationalization provider
 *
 * Copiez dans : app/components/I18nProvider.tsx
 *
 * How it works:
 * 1. Reads locale from localStorage
 * 2. Dynamically loads JSON messages via dynamic import()
 * 3. Wraps the app with NextIntlClientProvider
 * 4. Expose useI18n() hook to change locale from anywhere
 *
 * Benefit: no "fr" flash on first render (useState lazy initializer)
 */
import { createContext, useContext, useEffect, useState, useCallback, ReactNode } from "react";
import { NextIntlClientProvider } from "next-intl";
import {
  locales,
  defaultLocale,
  type Locale,
  localeNames,
  localeFlags,
  getStoredLocale,
  setStoredLocale,
} from "@/i18n";
import frMessages from "@/messages/fr.json";

// ── Context ──────────────────────────────────────────────────
interface I18nContextValue {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  localeNames: typeof localeNames;
  localeFlags: typeof localeFlags;
  locales: typeof locales;
}

const I18nContext = createContext<I18nContextValue>({
  locale: defaultLocale,
  setLocale: () => {},
  localeNames,
  localeFlags,
  locales,
});

export function useI18n() {
  return useContext(I18nContext);
}

// ── Dynamic message loader ────────────────────────────
async function loadMessages(locale: Locale): Promise<Record<string, unknown>> {
  try {
    const mod = await import(`@/messages/${locale}.json`);
    return mod.default ?? mod;
  } catch {
    try {
      const mod = await import("@/messages/fr.json");
      return mod.default ?? mod;
    } catch {
      return {};
    }
  }
}

// ── Main provider ────────────────────────────────────────
export default function I18nProvider({ children }: { children: ReactNode }) {
  // Lazy initializer → no "fr" flash
  const [locale, setLocaleState] = useState<Locale>(() => {
    if (typeof window !== "undefined") {
      const stored = localStorage.getItem("locale") as Locale | null;
      if (stored && (locales as readonly string[]).includes(stored)) return stored;
    }
    return defaultLocale;
  });
  const [messages, setMessages] = useState<Record<string, unknown>>(
    frMessages as unknown as Record<string, unknown>
  );

  // Initialization: localStorage > browser > default
  useEffect(() => {
    const stored = localStorage.getItem("locale") as Locale | null;
    if (stored && (locales as readonly string[]).includes(stored)) {
      if (stored !== locale) setLocaleState(stored);
      if (stored !== defaultLocale) loadMessages(stored).then(setMessages);
      return;
    }
    const browserLang = navigator.language.split("-")[0] as Locale;
    const detected = (locales as readonly string[]).includes(browserLang)
      ? browserLang
      : defaultLocale;
    if (detected !== locale) {
      setLocaleState(detected);
      if (detected !== defaultLocale) loadMessages(detected).then(setMessages);
    }
  }, []);

  // Change locale
  const setLocale = useCallback((newLocale: Locale) => {
    setStoredLocale(newLocale);
    setLocaleState(newLocale);
    loadMessages(newLocale).then(setMessages);
  }, []);

  return (
    <I18nContext.Provider value={{ locale, setLocale, localeNames, localeFlags, locales }}>
      <NextIntlClientProvider
        locale={locale}
        messages={messages}
        timeZone="Europe/Paris"
      >
        {children}
      </NextIntlClientProvider>
    </I18nContext.Provider>
  );
}
