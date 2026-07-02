#!/bin/bash
# Pre-commit hook: reject emoji characters in translation JSON files
# Install: ln -sf ../../scripts/no-emoji-i18n.sh .git/hooks/pre-commit

STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep 'messages/.*\.json' || true)
if [ -z "$STAGED" ]; then
  exit 0
fi

python3 -c "
import sys, json, re

# Unicode ranges for emoji characters (no external dependency)
# NOTE: do NOT use '\\U000024C2-\\U0001F251' — it overlaps with CJK ideographs
EMOJI_PAT = re.compile(
    '[\\U0001F600-\\U0001F64F'   # Emoticons
    '\\U0001F300-\\U0001F5FF'   # Misc Symbols and Pictographs
    '\\U0001F680-\\U0001F6FF'   # Transport and Map
    '\\U0001F1E0-\\U0001F1FF'   # Flags
    '\\U00002702-\\U000027B0'   # Dingbats
    '\\U0001F900-\\U0001F9FF'   # Supplemental Symbols
    '\\U0001FA00-\\U0001FA6F'   # Chess Symbols
    '\\U0001FA70-\\U0001FAFF'   # Symbols Extended-A
    '\\U00002600-\\U000026FF'   # Misc symbols
    '\\U0000FE00-\\U0000FE0F'   # Variation selectors
    '\\U0000200D'              # Zero-width joiner
    ']'
)

def has_emoji(text):
    return bool(EMOJI_PAT.search(text))

errors = []
for fpath in '''$STAGED'''.strip().split('\\n'):
    if not fpath:
        continue
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    if has_emoji(content):
        data = json.loads(content)
        def find_emojis(obj, prefix=''):
            for k, v in obj.items():
                key = f'{prefix}.{k}' if prefix else k
                if isinstance(v, str) and has_emoji(v):
                    errors.append(f'  {fpath}:{key}: {v[:60]}')
                elif isinstance(v, dict):
                    find_emojis(v, key)
        find_emojis(data)

if errors:
    print('ERROR: Emojis found in translation files. Remove them and try again:')
    for e in errors:
        print(e)
    sys.exit(1)
"
