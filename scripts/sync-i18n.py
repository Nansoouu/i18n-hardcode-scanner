#!/usr/bin/env python3
"""Sync all i18n JSON files with fr.json — translate missing keys via DeepSeek.
Usage: python3 scripts/sync-i18n.py
"""
import json, os, sys, time, httpx

MESSAGES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app", "messages")

auth = json.load(open(os.path.expanduser("~/.hermes/auth.json")))
cp = auth.get("credential_pool", {})
ds = cp.get("deepseek", [])
KEY = ds[0].get("access_token") if ds else os.environ.get("DEEPSEEK_API_KEY")
if not KEY:
    print("ERROR: No DeepSeek key found")
    sys.exit(1)

LANGS = {
    "ar": "Arabic", "de": "German", "es": "Spanish", "fa": "Persian",
    "he": "Hebrew", "hi": "Hindi", "id": "Indonesian", "it": "Italian",
    "ja": "Japanese", "ko": "Korean", "nl": "Dutch", "pl": "Polish",
    "pt": "Portuguese", "ru": "Russian", "tr": "Turkish", "uk": "Ukrainian",
    "vi": "Vietnamese", "zh": "Chinese (Simplified)",
}

def flatten(d, p=""):
    r = {}
    for k, v in d.items():
        path = f"{p}.{k}" if p else k
        if isinstance(v, dict): r.update(flatten(v, path))
        else: r[path] = v
    return r

def unflatten(d):
    r = {}
    for path, value in d.items():
        parts = path.split(".")
        cur = r
        for part in parts[:-1]:
            cur = cur.setdefault(part, {})
        cur[parts[-1]] = value
    return r

def translate_batch(texts, lang_name):
    items = "\n".join([f'  "{k}": "{v}"' for _, k, v in texts])
    prompt = f"""Translate these French JSON values to {lang_name}. Keep keys unchanged.
{{{items}}}
Return ONLY valid JSON, no markdown."""
    for attempt in range(3):
        try:
            r = httpx.post("https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
                json={"model": "deepseek-chat", "messages": [
                    {"role": "system", "content": f"Translator FR→{lang_name}. Return ONLY valid JSON."},
                    {"role": "user", "content": prompt}
                ], "temperature": 0.1, "max_tokens": 3000}, timeout=60)
            content = r.json()["choices"][0]["message"]["content"].strip()
            if "```" in content:
                content = content.split("```")[1] if content.count("```") > 1 else content.replace("```json", "").replace("```", "")
            return json.loads(content)
        except Exception as e:
            print(f"    Retry {attempt+1}: {e}")
            time.sleep(2)
    return {k: v for _, k, v in texts}  # fallback

# Load FR as reference
with open(os.path.join(MESSAGES, "fr.json")) as f:
    fr_flat = flatten(json.load(f))

for code, name in sorted(LANGS.items()):
    fp = os.path.join(MESSAGES, f"{code}.json")
    with open(fp) as f:
        flat = flatten(json.load(f))

    missing = {k: v for k, v in fr_flat.items() if k not in flat}
    if not missing:
        print(f"  ✓ {code} ({name}) — OK ({len(flat)} keys)")
        continue

    # English: just copy FR as placeholders
    if code == "en":
        flat.update(missing)
        with open(fp, "w") as f:
            json.dump(unflatten(flat), f, indent=2, ensure_ascii=False)
        print(f"  → en — {len(missing)} keys added (copied from FR)")
        continue

    print(f"  → {code} ({name}) — {len(missing)} missing, translating...")

    # Group by namespace for batch translation
    by_ns = {}
    for path, value in missing.items():
        ns = path.split(".")[0]
        by_ns.setdefault(ns, []).append((path, path.split(".", 1)[1] if "." in path else path, value))

    for ns, texts in by_ns.items():
        # Split batches larger than 20 keys to avoid DeepSeek timeouts
        batch_size = 20
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            print(f"    {ns}[{i//batch_size+1}] ({len(batch)} keys)...", end=" ", flush=True)
            translated = translate_batch(batch, name)
            for (path, _, _), t_val in zip(batch, translated.values()):
                flat[path] = t_val
            print("✓")
            time.sleep(0.3)

    with open(fp, "w") as f:
        json.dump(unflatten(flat), f, indent=2, ensure_ascii=False)
    print(f"  ✓ {code} done")

print("\n✅ All done")
