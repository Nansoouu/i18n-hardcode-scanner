#!/usr/bin/env python3
"""Translate README.md to all 20 languages via DeepSeek."""
import json, os, sys, time, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, "README.md")
READMES_DIR = os.path.join(ROOT, "readmes")

os.makedirs(READMES_DIR, exist_ok=True)

# Read source README
with open(README_PATH) as f:
    source_text = f.read()

# Extract the banner (everything before ---\n\n)
banner_end = source_text.find("\n\n---\n\n")
banner = source_text[:banner_end] if banner_end > 0 else ""

# Get the body (everything after the first ---)
body_start = source_text.find("\n\n---\n\n", banner_end + 5) if banner_end > 0 else source_text.find("\n\n---\n\n")
if body_start > 0:
    body = source_text[body_start + 5:]
else:
    body = source_text

# Get DeepSeek key
auth_path = os.path.expanduser("~/.hermes/auth.json")
try:
    with open(auth_path) as f:
        auth = json.load(f)
    key = auth["credential_pool"]["deepseek"][0]["access_token"]
except Exception:
    key = os.environ.get("DEEPSEEK_API_KEY")
if not key:
    print("ERROR: No DeepSeek key")
    sys.exit(1)

LOCALES = {
    "ar": "Arabic", "de": "German", "es": "Spanish", "fa": "Persian",
    "fr": "French", "he": "Hebrew", "hi": "Hindi", "id": "Indonesian",
    "it": "Italian", "ja": "Japanese", "ko": "Korean", "nl": "Dutch",
    "pl": "Polish", "pt": "Portuguese", "ru": "Russian", "tr": "Turkish",
    "uk": "Ukrainian", "vi": "Vietnamese", "zh": "Chinese",
}

ALL_LANGS = sorted(LOCALES.items())

def translate_markdown(text, lang_name):
    prompt = f"""Translate this English technical documentation to {lang_name}.

RULES:
1. Keep ALL markdown syntax intact (headings, lists, tables, code blocks)
2. Keep ALL HTML tags and attributes unchanged
3. Keep ALL URLs, image paths, and shields.io badges unchanged
4. Keep all code examples in ``` blocks in English
5. Keep the Solana wallet address unchanged
6. Keep the Subvox project link unchanged
7. Do NOT add or remove any content
8. Translate only visible text content and UI labels

TEXT TO TRANSLATE:
{text[:6000]}

Return ONLY the translated markdown, no explanations."""

    for attempt in range(3):
        try:
            import httpx
            r = httpx.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.15,
                    "max_tokens": 8000,
                },
                timeout=180,
            )
            result = r.json()["choices"][0]["message"]["content"].strip()
            # Remove wrapping markdown code blocks if present
            if result.startswith("```"):
                result = result.split("```", 2)[1] if "```" in result[3:] else result
                if result.startswith("markdown"):
                    result = result[8:].strip()
            return result
        except Exception as e:
            print(f"  Retry {attempt+1}: {e}")
            time.sleep(3)
    return text  # fallback

for code, name in ALL_LANGS:
    fname = f"README.{code}.md" if code != "en" else "README.md"
    fpath = os.path.join(READMES_DIR, fname) if code != "en" else ROOT + "/README.md"

    if os.path.exists(fpath) and code != "en":
        # Skip if already exists (update manually later)
        print(f"  ⏭️  {code} ({name}) — already exists")
        continue

    print(f"  → {code} ({name})...", end=" ", flush=True)

    if code == "en":
        # Just copy
        print("✓ (source)")
        continue

    translated = translate_markdown(body, name)
    time.sleep(0.5)

    # Build the full README: banner + translated body
    full = banner + "\n\n---\n\n" + translated

    with open(fpath, "w") as f:
        f.write(full)
    print("✓")

print("\n✅ All READMEs generated")
