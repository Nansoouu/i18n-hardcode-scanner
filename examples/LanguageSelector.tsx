"use client";
/**
 * LanguageSelector.tsx — Navbar language selector
 *
 * Copiez dans : app/components/ui/LanguageSelector.tsx
 *
 * Shows a button with flag + language code in the navbar.
 * On click, opens a dropdown with all available languages.
 * Uses the useI18n() hook to switch language instantly.
 */
import { useEffect, useRef, useState } from "react";
import { useTranslations } from "next-intl";
import { useI18n } from "@/components/I18nProvider";

const DEFAULT_FLAG = "🌐";

export default function LanguageSelector() {
  const t = useTranslations("common");
  const { locale, setLocale, localeFlags, localeNames, locales } = useI18n();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Fermer le dropdown si click dehors
  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    if (open) document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [open]);

  const currentFlag = localeFlags[locale as keyof typeof localeFlags] ?? DEFAULT_FLAG;

  return (
    <div ref={ref} className="relative">
      <button
        onClick={() => setOpen(v => !v)}
        className="flex items-center gap-1.5 text-xs text-gray-400 hover:text-white
                   transition-colors px-2.5 py-1.5 rounded-lg hover:bg-gray-800
                   border border-transparent hover:border-gray-700"
        title={t("changeLanguage")}
      >
        <span className="text-base leading-none">{currentFlag}</span>
        <span className="hidden sm:block font-medium">{locale.toUpperCase()}</span>
        <svg
          className={`w-3 h-3 transition-transform ${open ? "rotate-180" : ""}`}
          fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {open && (
        <div className="absolute right-0 top-full mt-1.5 w-52 bg-gray-900 border
                        border-gray-700 rounded-xl shadow-2xl shadow-black/50
                        overflow-hidden z-50">
          <div className="max-h-72 overflow-y-auto py-1 scrollbar-thin">
            {(locales as unknown as string[]).map(loc => {
              const flag = localeFlags[loc as keyof typeof localeFlags] ?? DEFAULT_FLAG;
              const name = localeNames[loc as keyof typeof localeNames] ?? loc;
              const isActive = loc === locale;
              return (
                <button
                  key={loc}
                  onClick={() => { setLocale(loc as typeof locale); setOpen(false); }}
                  className={`
                    w-full flex items-center gap-3 px-3 py-2 text-left text-xs
                    transition-colors
                    ${isActive
                      ? "bg-[#10704B]/20 text-emerald-400 font-semibold"
                      : "text-gray-300 hover:bg-gray-800 hover:text-white"
                    }
                  `}
                >
                  <span className="text-base w-5 text-center leading-none">{flag}</span>
                  <span className="flex-1">{name}</span>
                  {isActive && (
                    <svg className="w-3 h-3 text-blue-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
