#!/usr/bin/env python3
"""
Comprehensive Distractor Fixer for Trivia Topics.
Fixes all dummy/placeholder/mismatched distractors across:
1. cinema_greatest_movies (en & he)
2. space_exploration (en & he)
3. true_crime_famous_heists (en & he)
4. famous_inventions_discoveries (en & he)
"""
import yaml

def fix_cinema():
    # -------------------------------------------------------------------------
    # CINEMA FIXES
    # -------------------------------------------------------------------------
    for lang, fpath in [('en', 'topics/cinema_greatest_movies_en.yaml'), ('he', 'topics/cinema_greatest_movies_he.yaml')]:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        for cat in data['categories']:
            if cat['id'] == 'important_facts':
                for q in cat.get('trivia', []):
                    q_text = q.get('question', '')
                    
                    # Q0: The Jazz Singer (1927)
                    if '1927' in q_text and ('talkie' in q_text.lower() or 'המדבר' in q_text):
                        if lang == 'en':
                            q['options'] = ['The Jazz Singer', 'Metropolis', 'Sunrise: A Song of Two Humans', 'Wings']
                        else:
                            q['options'] = ["זמר הג'אז (The Jazz Singer)", 'מטרופוליס (Metropolis)', 'זריחה (Sunrise)', 'כנפיים (Wings)']
                        q['correct'] = 0
                    
                    # Q1: 3 films tied with 11 Oscars
                    elif '11' in q_text and ('oscars' in q_text.lower() or 'פסלונים' in q_text or 'אוסקר' in q_text):
                        if lang == 'en':
                            q['options'] = [
                                'Ben-Hur, Titanic, and The Lord of the Rings: The Return of the King',
                                'Gone with the Wind, The Godfather, and Forrest Gump',
                                'Star Wars, Raiders of the Lost Ark, and Gladiator',
                                'The Silence of the Lambs, Casablanca, and Chicago'
                            ]
                        else:
                            q['options'] = [
                                'בן חור, טיטניק ושר הטבעות: שיבת המלך',
                                'חלף עם הרוח, הסנדק ופורסט גאמפ',
                                'מלחמת הכוכבים, שודדי התיבה האבודה וגלדיאטור',
                                'שתיקת הכבשים, קזבלנקה ושיקגו'
                            ]
                        q['correct'] = 0
                    
                    # Q3: Dolly zoom in Vertigo
                    elif 'Vertigo' in q_text or 'ורטיגו' in q_text:
                        if lang == 'en':
                            q['options'] = ['The Dolly Zoom (Vertigo Effect)', 'Steadicam tracking shot', 'Dutch Angle tilt', 'Double Exposure layering']
                        else:
                            q['options'] = ['דולי זום (Dolly Zoom / אפקט ורטיגו)', 'שוט מעקב רציף (Steadicam)', 'זווית הולנדית עקומה (Dutch Angle)', 'חשיפה כפולה (Double Exposure)']
                        q['correct'] = 0
                    
                    # Q5: Parasite 2020
                    elif 'Parasite' in q_text or 'פרזיטים' in q_text or 'דרום קוריאני' in q_text or 'South Korean' in q_text:
                        if lang == 'en':
                            q['options'] = ['Parasite', 'Roma', "Pan's Labyrinth", 'The Lives of Others']
                        else:
                            q['options'] = ['פרזיטים (Parasite)', 'רומא (Roma)', "המבוך של פאן (Pan's Labyrinth)", 'חיים של אחרים (The Lives of Others)']
                        q['correct'] = 0
                    
                    # Q7: 1939 greatest year
                    elif 'Gone with the Wind' in q_text or 'חלף עם הרוח' in q_text:
                        q['options'] = ['1939', '1927', '1968', '1994']
                        q['correct'] = 0
                    
                    # Q9: Marlon Brando cue cards
                    elif 'Marlon Brando' in q_text or 'מרלון ברנדו' in q_text:
                        if lang == 'en':
                            q['options'] = ['Cue cards taped to walls and actors', 'A hidden in-ear wireless receiver', 'Pure unscripted dialogue improvisation', 'Pre-recording audio to lip-sync']
                        else:
                            q['options'] = ['כרטיסיות טקסט (Cue Cards) שהודבקו על קירות ושחקנים', 'אוזנייה אלחוטית נסתרת באוזנו', 'אלתור מוחלט של הדיאלוג מול המצלמה', 'הקלטה מראש ודיבוב חוזר']
                        q['correct'] = 0
                    
                    # Q11: Bullet Time
                    elif 'Bullet Time' in q_text or 'מטריקס' in q_text or 'The Matrix' in q_text:
                        if lang == 'en':
                            q['options'] = ['Bullet Time', 'Motion Capture sensor suits', 'Chroma Key green screen', 'Front Projection mattes']
                        else:
                            q['options'] = ['זמן קליע (Bullet Time)', 'לכידת תנועה בחליפות חיישנים (Motion Capture)', 'מסך ירוק דיגיטלי (Chroma Key)', 'הקרנה קדמית של מודלים (Front Projection)']
                        q['correct'] = 0
                    
                    # Q13: Statuette depicting
                    elif 'statuette' in q_text.lower() or 'פסלון' in q_text:
                        if lang == 'en':
                            q['options'] = [
                                'A knight holding a crusader sword standing on a film reel',
                                'A winged Greek goddess holding a flaming torch',
                                'A cinematic muse holding a vintage hand-crank camera',
                                'A golden eagle spreading its wings across a globe'
                            ]
                        else:
                            q['options'] = [
                                'אביר האוחז בחרב צלבנים ועומד על גליל פילם',
                                'אלה יוונית מכונפת המחזיקה לפיד בוער',
                                'מוזה קולנועית האוחזת במצלמת ראינוע עתיקה',
                                'נשר מוזהב הפורש כנפיו מעל גלובוס העולם'
                            ]
                        q['correct'] = 0
                    
                    # Q15: PG-13 year (1984)
                    elif 'PG-13' in q_text:
                        q['options'] = ['1984', '1968', '1975', '1990']
                        q['correct'] = 0
        
        with open(fpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Fixed distractors in {fpath}")

def fix_true_crime():
    # -------------------------------------------------------------------------
    # TRUE CRIME FIXES (unsolved_mysteries_cryptic_crimes)
    # -------------------------------------------------------------------------
    for lang, fpath in [('en', 'topics/true_crime_famous_heists_en.yaml'), ('he', 'topics/true_crime_famous_heists_he.yaml')]:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        for cat in data['categories']:
            if cat['id'] == 'unsolved_mysteries_cryptic_crimes':
                for q in cat.get('trivia', []):
                    q_text = q.get('question', '')
                    
                    # Q1: 1888 Jack the Ripper
                    if '1888' in str(q.get('options')) or 'Jack the Ripper' in q_text or 'ג\'ק המרטש' in q_text:
                        q['options'] = ['1888', '1865', '1901', '1924']
                        q['correct'] = 0
                    
                    # Q3: Elizabeth Short / Black Dahlia
                    elif 'Elizabeth Short' in str(q.get('options')) or 'Black Dahlia' in q_text or 'הדליה השחורה' in q_text:
                        if lang == 'en':
                            q['options'] = ['Elizabeth Short', 'Marilyn Delano', 'Jean Spangler', 'Virginia Hill']
                        else:
                            q['options'] = ['אליזבת שורט (Elizabeth Short)', 'מרילין דלאנו', "ג'ין ספנגלר", 'וירג\'יניה היל']
                        q['correct'] = 0
                    
                    # Q5: 2020 Zodiac cipher cracked
                    elif 'Zodiac' in q_text or 'זודיאק' in q_text:
                        q['options'] = ['2020', '1995', '2008', '2014']
                        q['correct'] = 0
                    
                    # Q7: Tamam Shud
                    elif 'Tamam Shud' in str(q.get('options')) or 'Somerton' in q_text or 'סומרטון' in q_text:
                        if lang == 'en':
                            q['options'] = ['Tamam Shud', 'Carpe Diem', 'Memento Mori', 'Tabula Rasa']
                        else:
                            q['options'] = ['תמאם שוד (Tamam Shud)', 'קרפה דיאם (Carpe Diem)', 'ממנטו מורי (Memento Mori)', 'טאבולה ראסה (Tabula Rasa)']
                        q['correct'] = 0
                    
                    # Q9: The Canonical Five
                    elif 'Canonical Five' in str(q.get('options')) or 'קנוניות' in str(q.get('options')):
                        if lang == 'en':
                            q['options'] = ['The Canonical Five', 'The Whitechapel Syndicate', 'The Autumn Victims', 'The East End Circle']
                        else:
                            q['options'] = ['חמש הקנוניות (The Canonical Five)', 'סינדיקט וייטצ\'אפל', 'קורבנות הסתיו האדום', 'מעגל האיסט אנד']
                        q['correct'] = 0
                    
                    # Q11: Industrial alcohol Mary Celeste
                    elif 'Mary Celeste' in q_text or 'מרי סלסט' in q_text:
                        if lang == 'en':
                            q['options'] = ['Denatured raw industrial alcohol', 'Refined olive oil barrels', 'Gunpowder and munitions', 'Whale blubber oil']
                        else:
                            q['options'] = ['אלכוהול גולמי תעשייתי', 'חביות שמן זית מזוכך', 'אבק שריפה ותחמושת', 'שומן לווייתנים מזוקק']
                        q['correct'] = 0
                    
                    # Q13: Teamsters union Jimmy Hoffa
                    elif 'Jimmy Hoffa' in q_text or 'הופה' in q_text:
                        if lang == 'en':
                            q['options'] = ['The International Brotherhood of Teamsters', 'United Steelworkers Union', 'AFL-CIO Maritime Division', 'United Auto Workers (UAW)']
                        else:
                            q['options'] = ['איגוד הטימסטרס (Teamsters)', 'איגוד עובדי הפלדה (United Steelworkers)', 'איגוד עובדי הרכב (UAW)', 'פדרציית פועלי הנמלים']
                        q['correct'] = 0
                    
                    # Q15: $200,000 DB Cooper ransom
                    elif '200,000' in str(q.get('options')) or 'Cooper' in q_text or 'קופר' in q_text:
                        if lang == 'en':
                            q['options'] = ['$200,000 in negotiable $20 bills', '$1,000,000 in unmarked gold coins', '$500,000 in bearer bonds', '$50,000 in cash']
                        else:
                            q['options'] = ['200,000 דולר בשטרות של 20 דולר', '1,000,000 דולר במטבעות זהב', '500,000 דולר באיגרות חוב', '50,000 דולר במזומן']
                        q['correct'] = 0

        with open(fpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Fixed distractors in {fpath}")

def fix_space():
    # -------------------------------------------------------------------------
    # SPACE EXPLORATION FIXES (black_holes_cosmic_mysteries)
    # -------------------------------------------------------------------------
    for lang, fpath in [('en', 'topics/space_exploration_en.yaml'), ('he', 'topics/space_exploration_he.yaml')]:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        for cat in data['categories']:
            if cat['id'] == 'black_holes_cosmic_mysteries':
                for q in cat.get('trivia', []):
                    q_text = q.get('question', '')
                    
                    # Q5: 2019 first black hole image
                    if '2019' in str(q.get('options')) or 'Event Horizon Telescope' in q_text or 'אופק האירועים' in q_text or 'צילום' in q_text:
                        q['options'] = ['2019', '2005', '2012', '2023']
                        q['correct'] = 0
                    
                    # Q11: Kepler space telescope / James Webb / etc.
                    elif 'Kepler' in str(q.get('options')) or 'קפלר' in str(q.get('options')):
                        if lang == 'en':
                            q['options'] = ['Kepler Space Telescope', 'Hubble Space Telescope', 'James Webb Space Telescope', 'Spitzer Space Telescope']
                        else:
                            q['options'] = ['טלסקופ החלל קפלר (Kepler)', 'טלסקופ החלל האבל (Hubble)', 'טלסקופ החלל ג\'יימס וב (JWST)', 'טלסקופ החלל שפיצר (Spitzer)']
                        q['correct'] = 0
                    
                    # Q15: Hawking Radiation
                    elif 'Hawking' in str(q.get('options')) or 'הוקינג' in str(q.get('options')):
                        if lang == 'en':
                            q['options'] = ['Hawking Radiation', 'Cosmic Microwave Background (CMB)', 'Cherenkov Radiation', 'Synchrotron Emission']
                        else:
                            q['options'] = ['קרינת הוקינג (Hawking Radiation)', 'קרינת הרקע הקוסמית (CMB)', 'קרינת צ\'רנקוב (Cherenkov)', 'קרינת סינכרוטרון']
                        q['correct'] = 0

        with open(fpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Fixed distractors in {fpath}")

def fix_inventions():
    # -------------------------------------------------------------------------
    # FAMOUS INVENTIONS FIXES
    # -------------------------------------------------------------------------
    for lang, fpath in [('en', 'topics/famous_inventions_discoveries_en.yaml'), ('he', 'topics/famous_inventions_discoveries_he.yaml')]:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        for cat in data['categories']:
            if cat['id'] == 'everyday_objects':
                for q in cat.get('trivia', []):
                    q_text = q.get('question', '')
                    # Q9: Year 1879 / light bulb patent
                    if '1879' in str(q.get('options')) or 'נורה' in q_text or 'light bulb' in q_text.lower():
                        q['options'] = ['1879', '1850', '1903', '1925']
                        q['correct'] = 0

        with open(fpath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=120)
        print(f"Fixed distractors in {fpath}")

if __name__ == "__main__":
    fix_cinema()
    fix_true_crime()
    fix_space()
    fix_inventions()
