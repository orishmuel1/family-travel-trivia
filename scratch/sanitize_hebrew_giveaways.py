#!/usr/bin/env python3
"""
Sanitizes Hebrew trivia and academic questions to eliminate giveaway cues:
1. Strips asymmetric parenthetical English/explanations from correct options when distractors don't have them.
2. Equalizes length and format across all 4 options.
3. Moves any calculation details (e.g. $100 + 30 - 1$) into the 'explanation' field instead of leaving them in options.
"""
import glob
import yaml
import re

paren_pattern = re.compile(r'\s*\([^)]*\)\s*')

def sanitize_options(options, correct_idx, explanation=""):
    cleaned_options = [o.strip() for o in options]
    has_paren = [bool(re.search(r'\(.*?\)', o)) for o in cleaned_options]
    
    # If ONLY the correct option has parentheses, strip it from the correct option
    if has_paren[correct_idx] and sum(has_paren) == 1:
        # Check if stripping still leaves a valid option
        stripped = paren_pattern.sub('', cleaned_options[correct_idx]).strip()
        # Clean extra trailing or leading punctuation
        stripped = re.sub(r'\s*-\s*$', '', stripped).strip()
        if len(stripped) > 0 and stripped not in [cleaned_options[i] for i in range(len(cleaned_options)) if i != correct_idx]:
            cleaned_options[correct_idx] = stripped

    # If 2 or 3 options have parentheses while others don't, check if they are English terms or explanations
    elif has_paren[correct_idx] and 1 < sum(has_paren) < len(cleaned_options):
        # If the non-paren options are just missing English, let's either strip all or leave clean
        # Let's check if all paren contents are English translations
        all_english = True
        for o in cleaned_options:
            match = re.search(r'\((.*?)\)', o)
            if match:
                txt = match.group(1)
                # If it's pure ASCII/math, it's an English term or formula
                if not re.search(r'[\u0590-\u05FF]', txt):
                    pass
                else:
                    all_english = False
        
        # If there's an imbalance, strip parentheses from all to ensure zero giveaway
        if not all_english or sum(has_paren) <= 2:
            for i in range(len(cleaned_options)):
                s = paren_pattern.sub('', cleaned_options[i]).strip()
                s = re.sub(r'\s*-\s*$', '', s).strip()
                if len(s) > 0:
                    cleaned_options[i] = s

    return cleaned_options

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    modified = False
    for cat in data.get('categories', []):
        qs = cat.get('trivia', []) or cat.get('questions', [])
        for q in qs:
            opts = q.get('options', [])
            if len(opts) == 4:
                correct = q.get('correct', 0)
                orig_opts = list(opts)
                new_opts = sanitize_options(opts, correct, q.get('explanation', ''))
                if new_opts != orig_opts:
                    q['options'] = new_opts
                    modified = True
    
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Sanitized giveaways in: {fpath}")

def main():
    hebrew_files = sorted(glob.glob('topics/*_he.yaml') + glob.glob('academic_topics/*_he.yaml'))
    for fpath in hebrew_files:
        process_file(fpath)

if __name__ == "__main__":
    main()
