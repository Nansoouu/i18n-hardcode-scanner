"use client";
/**
 * LanguagePicker.tsx — Advanced multi-language selector
 *
 * Copiez dans : app/components/ui/LanguagePicker.tsx
 *
 * Features:
 * - Real-time search (name, native, code)
 * - Region filtering (Europe, Asia, Middle East...)
 * - Auto-detect region from timezone
 * - Multi-select with configurable limit
 * - Responsive design (3-4 column grid)
 * - Fixed-position dropdown to avoid overflow
 */
import { useState, useMemo, useRef, useEffect } from "react";
import { useTranslations } from "next-intl";
import type { LangOption } from "@/lib/languages";
import { LANGUAGES, getUserRegion } from "@/lib/languages";

interface LanguagePickerProps {
  selected: string[];
  onToggle: (code: string) => void;
  max?: number;
}

export default function LanguagePicker({ selected, onToggle, max = 20 }: LanguagePickerProps) {
  const [search, setSearch] = useState("");
  const [region, setRegion] = useState<string>("auto");
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);
  const t = useTranslations("HomePage");

  // Detect user region on first render
  useEffect(() => {
    if (region === "auto") setRegion(getUserRegion());
  }, []);

  // Close on outside click
  useEffect(() => {
    if (!open) return;
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, [open]);

  // Filtered languages
  const filtered = useMemo(() => {
    let list = LANGUAGES;
    if (region !== "all") list = list.filter(l => l.region === region);
    if (search.trim()) {
      const q = search.toLowerCase();
      list = list.filter(l =>
        l.name.toLowerCase().includes(q) ||
        l.native.toLowerCase().includes(q) ||
        l.code.toLowerCase().includes(q)
      );
    }
    return list;
  }, [search, region]);

  const REGIONS = [
    { id: "americas", label: "🌎 Amériques" },
    { id: "europe", label: "🌍 Europe" },
    { id: "middle-east", label: "🌏 Moyen-Orient" },
    { id: "africa", label: "🌍 Afrique" },
    { id: "asia", label: "🌏 Asie" },
    { id: "oceania", label: "🌏 Océanie" },
  ];

  return (
    <div ref={ref} className="relative">
      {/* Selected language tags */}
      <div className="flex flex-wrap gap-1.5 mb-2">
        {selected.map(code => {
          const lang = LANGUAGES.find(l => l.code === code);
          if (!lang) return null;
          return (
            <span key={code} onClick={() => onToggle(code)}
              className="inline-flex items-center gap-1 px-2 py-1 rounded-lg
                         bg-blue-500/15 border border-blue-500/30 text-blue-300
                         text-xs cursor-pointer hover:bg-blue-500/25 transition-colors"
            >
              {lang.flag} {lang.code.toUpperCase()}
              <span className="text-blue-400/60 ml-0.5">×</span>
            </span>
          );
        })}
        {selected.length < max && (
          <button onClick={() => setOpen(!open)}
            className="inline-flex items-center gap-1 px-2 py-1 rounded-lg
                       border border-dashed border-gray-700 text-gray-500 text-xs
                       hover:border-gray-500 hover:text-gray-300 transition-colors"
          >
            + {t("addLang")}
          </button>
        )}
      </div>

      {/* Dropdown */}
      {open && (
        <div className="fixed z-[100] inset-x-4 top-1/2 -translate-y-1/2 mx-auto
                        max-w-lg bg-gray-900 border border-gray-800 rounded-2xl
                        shadow-2xl shadow-black/70 overflow-hidden">
          {/* Barre de recherche */}
          <div className="p-3 border-b border-gray-800">
            <div className="relative">
              <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 text-sm">🔍</span>
              <input type="text" value={search} onChange={e => setSearch(e.target.value)}
                placeholder={t("searchLang")} autoFocus
                className="w-full bg-gray-800 text-white text-sm rounded-xl pl-9 pr-3 py-2
                           border border-gray-700 focus:border-blue-500 focus:ring-1
                           focus:ring-blue-500/30 outline-none transition-colors
                           placeholder:text-gray-600"
              />
            </div>
          </div>

          {/* Region tabs */}
          <div className="flex gap-1 px-3 pt-2 pb-1 overflow-x-auto scrollbar-hide border-b border-gray-800">
            <button onClick={() => setRegion("auto")}
              className={`shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-medium transition-colors ${
                region === "auto" || region === getUserRegion()
                  ? "bg-blue-500/20 text-blue-300 border border-blue-500/30"
                  : "text-gray-500 hover:text-gray-300 border border-transparent"
              }`}
            >
              {t("autoDetect")}
            </button>
            <button onClick={() => setRegion("all")}
              className={`shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-medium transition-colors ${
                region === "all"
                  ? "bg-blue-500/20 text-blue-300 border border-blue-500/30"
                  : "text-gray-500 hover:text-gray-300 border border-transparent"
              }`}
            >
              🌐 {t("all")}
            </button>
            {REGIONS.map(r => (
              <button key={r.id} onClick={() => setRegion(r.id)}
                className={`shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-medium transition-colors ${
                  region === r.id
                    ? "bg-blue-500/20 text-blue-300 border border-blue-500/30"
                    : "text-gray-500 hover:text-gray-300 border border-transparent"
                }`}
              >
                {r.label}
              </button>
            ))}
          </div>

          {/* Language grid */}
          <div className="max-h-32 overflow-y-auto p-1.5">
            {filtered.length === 0 ? (
              <div className="text-center py-6 text-gray-600 text-sm">{t("noResults")}</div>
            ) : (
              <div className="grid grid-cols-3 sm:grid-cols-4 gap-1">
                {filtered.slice(0, 14).map(lang => {
                  const isSelected = selected.includes(lang.code);
                  const isDisabled = !isSelected && selected.length >= max;
                  return (
                    <button key={lang.code} onClick={() => !isDisabled && onToggle(lang.code)}
                      disabled={isDisabled}
                      className={`flex items-center gap-1.5 px-2 py-1.5 rounded-lg text-left transition-all ${
                        isSelected
                          ? "bg-blue-500/20 border border-blue-500/30"
                          : isDisabled
                            ? "opacity-30 cursor-not-allowed border border-transparent"
                            : "hover:bg-gray-800/50 border border-transparent"
                      }`}
                    >
                      <span className="text-base leading-none shrink-0">{lang.flag}</span>
                      <div className="min-w-0">
                        <div className={`text-[10px] font-medium truncate ${isSelected ? "text-blue-200" : "text-gray-300"}`}>
                          {lang.name}
                        </div>
                      </div>
                      {isSelected && <span className="ml-auto text-blue-400 text-[9px]">✓</span>}
                    </button>
                  );
                })}
                {filtered.length > 14 && (
                  <div className="col-span-full text-center pt-1">
                    <span className="text-[10px] text-gray-600">
                      +{filtered.length - 14} more languages — refine your search
                    </span>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Footer */}
          <div className="px-3 py-2.5 border-t border-gray-800 flex items-center justify-between bg-gray-900/80">
            <span className="text-[10px] text-gray-500">
              {t("langSelected", { count: selected.length })} · {t("langs")}
            </span>
            <button onClick={() => setOpen(false)}
              className="px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold transition-colors shadow-sm shadow-blue-500/20"
            >
              {t("done")} ✓
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
