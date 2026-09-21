#!/usr/bin/env python3
"""
Generates the Modern Hollywood Masterpieces (1990s–Present) topic
in both English (hollywood_modern_classics_en.yaml) and Hebrew (hollywood_modern_classics_he.yaml).
Follows:
- 100% 4-option multiple choice with dynamic client-side shuffle support (correct: 0).
- High distractor quality (domain-aligned options).
- Every question has an 'explanation' field.
- Hebrew gershayim / valid quotes.
- Detailed movie cards with IMDb scores, directors, release years, cast, storyline, filming locations, and trivia.
"""
import os
import yaml

TARGET_EN = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/hollywood_modern_classics_en.yaml"
TARGET_HE = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/hollywood_modern_classics_he.yaml"

def format_trivia_list(raw_questions):
    res = []
    for item in raw_questions:
        q_text = item.get("q") or item.get("question")
        res.append({
            "type": "multiple_choice",
            "question": q_text,
            "options": item["options"],
            "correct": item.get("correct", 0),
            "explanation": item.get("explanation", "")
        })
    return res

def create_datasets():
    # -------------------------------------------------------------------------
    # ENGLISH DATASET
    # -------------------------------------------------------------------------
    en_data = {
        "id": "hollywood_modern_classics_en",
        "title": "Modern Hollywood Masterpieces (1990s–Present)",
        "description": "An electrifying journey through modern cinema from the 1990s to today! Test your knowledge on landmark adult classics, Tarantino & Fincher thrillers, Christopher Nolan mind-benders, modern sci-fi epics, iconic directors, and legendary behind-the-scenes lore.",
        "lang": "en",
        "audience": "adult",
        "categories": [
            # =================================================================
            # CATEGORY 1: 90s Groundbreakers & Cult Revolutions (1990–1999)
            # =================================================================
            {
                "id": "groundbreakers_90s",
                "title": "90s Groundbreakers & Cult Revolutions (1990–1999)",
                "description": "The decade that transformed independent cinema, auteur storytelling, and visual effects forever.",
                "cards": [
                    {
                        "title": "The Shawshank Redemption (1994)",
                        "points": [
                            "IMDb Rating: 9.3/10 (Highest-rated film of all time on IMDb) | Directed by Frank Darabont.",
                            "Cast & Characters: Tim Robbins as Andy Dufresne (a wrongly convicted banker) and Morgan Freeman as Ellis Boyd 'Red' Redding (the prison contraband fixer).",
                            "Storyline & Themes: Over nearly two decades inside Maine's Shawshank State Penitentiary, Andy maintains quiet dignity, fosters hope, and secretly executes a brilliant geological escape plan.",
                            "Filming Location: Filmed primarily at the historic Ohio State Reformatory in Mansfield, Ohio.",
                            "Trivia & Legacy: While a commercial disappointment at the box office due to stiff competition from 'Forrest Gump' and 'Pulp Fiction', it became a colossal home-video sensation and cultural masterpiece."
                        ]
                    },
                    {
                        "title": "Pulp Fiction (1994)",
                        "points": [
                            "IMDb Rating: 8.9/10 | Directed and written by Quentin Tarantino | Won the Palme d'Or at Cannes and Best Original Screenplay Oscar.",
                            "Cast & Characters: John Travolta (Vincent Vega), Samuel L. Jackson (Jules Winnfield), Uma Thurman (Mia Wallace), and Bruce Willis (Butch Coolidge).",
                            "Storyline & Themes: Intertwined, non-linear Los Angeles crime stories exploring redemption, loyalty, and chance with rapid-fire pop culture dialogue and eclectic surf rock/funk tracks.",
                            "Filming Location: Shot entirely across Los Angeles and Hawthorne, California (including the famous Hawthorne Grill).",
                            "Trivia: The glowing contents of Marsellus Wallace's mysterious briefcase (combination 666) were never revealed, sparking endless fan theories."
                        ]
                    },
                    {
                        "title": "The Matrix (1999)",
                        "points": [
                            "IMDb Rating: 8.7/10 | Written and directed by The Wachowskis (Lana & Lilly Wachowski).",
                            "Cast & Characters: Keanu Reeves as Thomas Anderson / Neo, Laurence Fishburne as Morpheus, Carrie-Anne Moss as Trinity, and Hugo Weaving as Agent Smith.",
                            "Storyline & Themes: A dystopian cyber-thriller where humanity is unknowingly trapped inside a simulated reality created by sentient machines to harvest bio-electric power.",
                            "Filming Location: Shot on sound stages and downtown streets in Sydney, Australia to maximize budget efficiency.",
                            "Revolutionary Tech: Pioneered 'Bullet Time' cinematography using circular camera rigs with 120+ still cameras firing in microsecond sequences."
                        ]
                    },
                    {
                        "title": "Fight Club (1999)",
                        "points": [
                            "IMDb Rating: 8.8/10 | Directed by David Fincher | Adapted from Chuck Palahniuk's novel.",
                            "Cast & Characters: Edward Norton as the unnamed depressed Narrator, Brad Pitt as charismatic soapmaker Tyler Durden, and Helena Bonham Carter as Marla Singer.",
                            "Storyline & Themes: A searing critique of late-20th-century consumerism, corporate alienation, and toxic masculinity escalating into an anarchist financial collapse.",
                            "Filming Location: Shot across dozens of industrial and urban alley locations in downtown Los Angeles.",
                            "Visual Detail: Fincher hid a Starbucks coffee cup in almost every single scene of the movie to symbolize ubiquitous corporate saturation."
                        ]
                    },
                    {
                        "title": "Goodfellas (1990)",
                        "points": [
                            "IMDb Rating: 8.7/10 | Directed by Martin Scorsese | Based on Nicholas Pileggi's non-fiction book 'Wiseguy'.",
                            "Cast & Characters: Ray Liotta as Henry Hill, Robert De Niro as Jimmy Conway, and Joe Pesci as the volatile Tommy DeVito (winning Best Supporting Actor).",
                            "Storyline & Themes: The three-decade rise and fall of Lucchese crime family associate Henry Hill, tracing the seductive allure and brutal paranoia of mob life.",
                            "Cinematic Landmark: Features the legendary 3-minute continuous Steadicam tracking shot entering the Copacabana nightclub through the kitchen service entrance.",
                            "Trivia: Pesci's iconic 'Funny how? Like I'm a clown, I amuse you?' interrogation scene was improvised based on a real-life incident Pesci experienced while working as a young waiter."
                        ]
                    },
                    {
                        "title": "The Silence of the Lambs (1991)",
                        "points": [
                            "IMDb Rating: 8.6/10 | Directed by Jonathan Demme | Based on Thomas Harris's novel.",
                            "Cast & Characters: Jodie Foster as FBI trainee Clarice Starling and Anthony Hopkins as the brilliant, cannibalistic psychiatrist Dr. Hannibal Lecter.",
                            "Storyline & Themes: Clarice must probe Lecter's terrifying psychological intellect from behind glass to catch active serial killer Buffalo Bill.",
                            "Filming Location: Shot predominantly around Pittsburgh, Pennsylvania and the Western Penitentiary.",
                            "Historic Triumph: One of only three films in Oscar history to sweep the 'Big Five' Academy Awards (Best Picture, Director, Actor, Actress, and Adapted Screenplay), with Hopkins on screen for just 16 minutes."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "What is the primary filming location that served as Shawshank State Penitentiary in 'The Shawshank Redemption'?",
                        "options": ["Ohio State Reformatory in Mansfield", "Alcatraz Federal Penitentiary in San Francisco", "Eastern State Penitentiary in Philadelphia", "Sing Sing Correctional Facility in New York"],
                        "correct": 0,
                        "explanation": "'The Shawshank Redemption' was filmed at the historic Ohio State Reformatory in Mansfield, Ohio, which is now a major historic museum and tourist destination."
                    },
                    {
                        "q": "In 'Pulp Fiction', what is the lock combination on Marsellus Wallace's mysterious glowing briefcase?",
                        "options": ["666", "777", "123", "999"],
                        "correct": 0,
                        "explanation": "The briefcase combination is 666, which fueled many popular fan theories that the glowing contents represented Marsellus Wallace's soul."
                    },
                    {
                        "q": "Which groundbreaking visual effects camera technique was invented and popularized by 'The Matrix' in 1999?",
                        "options": ["Bullet Time", "Deepfake Motion Capture", "StageCraft LED Volume", "Dolly Zoom (Vertigo Effect)"],
                        "correct": 0,
                        "explanation": "Bullet Time used a circular array of high-speed still cameras triggered in micro-second intervals to allow the camera to rotate around a frozen or slow-motion subject."
                    },
                    {
                        "q": "In David Fincher's 'Fight Club', what everyday commercial object did the director hide in almost every single scene?",
                        "options": ["A Starbucks coffee cup", "A Coca-Cola bottle", "A Nike sneaker", "A yellow Post-it note"],
                        "correct": 0,
                        "explanation": "David Fincher placed a Starbucks coffee cup in virtually every scene to underscore the film's satire on ubiquitous corporate consumerism."
                    },
                    {
                        "q": "Which iconic nightclub entrance is featured in Martin Scorsese's famous uncut 3-minute Steadicam shot in 'Goodfellas'?",
                        "options": ["The Copacabana", "Studio 54", "The Cotton Club", "The Tropicana"],
                        "correct": 0,
                        "explanation": "The legendary continuous tracking shot follows Henry Hill and Karen entering the Copacabana nightclub through the back kitchen."
                    },
                    {
                        "q": "Anthony Hopkins won the Best Actor Oscar for 'The Silence of the Lambs' despite appearing on screen for approximately how much total time?",
                        "options": ["About 16 minutes", "About 42 minutes", "About 65 minutes", "About 85 minutes"],
                        "correct": 0,
                        "explanation": "Hopkins is on screen for approximately 16 minutes (less than 15% of the runtime), delivering one of the most hypnotic and efficient Oscar-winning performances in film history."
                    },
                    {
                        "q": "Which actor played the volatile mobster Tommy DeVito in 'Goodfellas' and won the Best Supporting Actor Oscar?",
                        "options": ["Joe Pesci", "Robert De Niro", "Ray Liotta", "Paul Sorvino"],
                        "correct": 0,
                        "explanation": "Joe Pesci won the Academy Award for Best Supporting Actor for his electrifying performance as Tommy DeVito."
                    },
                    {
                        "q": "Where was the dystopian city exterior and street action of 'The Matrix' primarily filmed?",
                        "options": ["Sydney, Australia", "Toronto, Canada", "Chicago, USA", "London, UK"],
                        "correct": 0,
                        "explanation": "The Wachowskis chose Sydney, Australia to shoot 'The Matrix' because of favorable exchange rates and state-of-the-art Fox Studios sound stages."
                    },
                    {
                        "q": "What precious stone or geological tool does Andy Dufresne use over 19 years to dig his escape tunnel in 'The Shawshank Redemption'?",
                        "options": ["A small rock hammer", "A rusted railroad spike", "A steel dental scraper", "A brass pocket knife"],
                        "correct": 0,
                        "explanation": "Andy purchases a small rock hammer through Red under the pretense of carving chess pieces out of soapstone and rocks."
                    },
                    {
                        "q": "Which prestigous film festival awarded Quentin Tarantino's 'Pulp Fiction' its top prize, the Palme d'Or, in 1994?",
                        "options": ["Cannes Film Festival", "Venice Film Festival", "Berlin International Film Festival", "Sundance Film Festival"],
                        "correct": 0,
                        "explanation": "'Pulp Fiction' took the world by storm when it won the prestigious Palme d'Or at the 1994 Cannes Film Festival."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 2: 2000s Modern Epics & Prestige Cinema (2000–2009)
            # =================================================================
            {
                "id": "modern_epics_2000s",
                "title": "2000s Modern Epics & Prestige Cinema (2000–2009)",
                "description": "The golden age of gritty realism, visionary epics, and genre-defining masterpieces.",
                "cards": [
                    {
                        "title": "The Dark Knight (2008)",
                        "points": [
                            "IMDb Rating: 9.0/10 | Directed by Christopher Nolan | Co-written with Jonathan Nolan.",
                            "Cast & Characters: Christian Bale as Bruce Wayne / Batman, Heath Ledger as The Joker, Aaron Eckhart as Harvey Dent / Two-Face, and Gary Oldman as Jim Gordon.",
                            "Storyline & Themes: A gripping crime thriller disguised as a superhero epic, probing escalating chaos, political surveillance, moral compromise, and vigilantism.",
                            "Filming Locations: Chicago, Illinois (serving as Gotham City), London, and Hong Kong.",
                            "Landmark Feat: The first major Hollywood feature to film select action sequences using full 70mm IMAX cameras; Heath Ledger posthumously won the Best Supporting Actor Oscar."
                        ]
                    },
                    {
                        "title": "The Lord of the Rings: The Return of the King (2003)",
                        "points": [
                            "IMDb Rating: 9.0/10 | Directed by Peter Jackson | Adapted from J.R.R. Tolkien's fantasy epic.",
                            "Cast & Characters: Elijah Wood (Frodo), Viggo Mortensen (Aragorn), Ian McKellen (Gandalf), and Andy Serkis (Gollum / Sméagol).",
                            "Storyline & Themes: The climatic battle for Middle-earth at Minas Tirith while Frodo and Sam journey into the heart of Mount Doom to destroy the One Ring.",
                            "Filming Location: Spectacular natural landscapes across the North and South Islands of New Zealand.",
                            "Historic Clean Sweep: Won all 11 Academy Awards for which it was nominated, tying 'Ben-Hur' and 'Titanic' for the most Oscar wins in history."
                        ]
                    },
                    {
                        "title": "Gladiator (2000)",
                        "points": [
                            "IMDb Rating: 8.5/10 | Directed by Ridley Scott | Winner of 5 Oscars including Best Picture.",
                            "Cast & Characters: Russell Crowe as General Maximus Decimus Meridius and Joaquin Phoenix as the corrupt Emperor Commodus.",
                            "Storyline & Themes: A betrayed Roman general is stripped of rank, sold into slavery, and rises through the Colosseum gladiator arena to seek vengeance for his murdered family.",
                            "Filming Locations: Bourne Wood in Surrey, England (opening battle), Ouarzazate, Morocco, and Fort Ricasoli, Malta (Colosseum set).",
                            "Trivia: Russell Crowe performed many of his own stunts and sustained multiple injuries, including foot numbness and broken bones, during the intense sword fights."
                        ]
                    },
                    {
                        "title": "No Country for Old Men (2007)",
                        "points": [
                            "IMDb Rating: 8.2/10 | Written and directed by Joel and Ethan Coen | Adapted from Cormac McCarthy's novel.",
                            "Cast & Characters: Javier Bardem as relentless hitman Anton Chigurh, Josh Brolin as Llewelyn Moss, and Tommy Lee Jones as Sheriff Ed Tom Bell.",
                            "Storyline & Themes: A hunter stumbles upon a desert drug deal gone wrong and $2 million in cash, sparking a ruthless manhunt exploring chance, fate, and aging in a violent world.",
                            "Filming Locations: Marfa, Texas and Las Vegas / Santa Fe, New Mexico.",
                            "Acoustic Design: Features almost zero non-diegetic musical score, creating an eerie, pulse-pounding reliance on wind, footsteps, and Foley sounds."
                        ]
                    },
                    {
                        "title": "The Departed (2006)",
                        "points": [
                            "IMDb Rating: 8.5/10 | Directed by Martin Scorsese | Remake of Hong Kong thriller 'Infernal Affairs' | Won 4 Oscars including Scorsese's first Best Director win.",
                            "Cast & Characters: Leonardo DiCaprio (undercover cop Billy Costigan), Matt Damon (mob mole Colin Sullivan), and Jack Nicholson (crime boss Frank Costello).",
                            "Storyline & Themes: Set in South Boston, the Massachusetts State Police and the Irish Mob simultaneously discover an enemy mole in their ranks, sparking a paranoid race to uncover each other.",
                            "Visual Motifs: Scorsese placed subtle 'X' patterns in the background framing before almost every major character's impending death.",
                            "Filming Location: Filmed primarily in Boston, Massachusetts and New York City sound stages."
                        ]
                    },
                    {
                        "title": "Inglourious Basterds (2009)",
                        "points": [
                            "IMDb Rating: 8.4/10 | Written and directed by Quentin Tarantino.",
                            "Cast & Characters: Christoph Waltz as ruthless SS Colonel Hans Landa ('The Jew Hunter'), Brad Pitt as Lt. Aldo Raine, and Mélanie Laurent as Shosanna Dreyfus.",
                            "Storyline & Themes: Alternate-history WWII drama culminating in a daring cinema assassination plot against top Nazi leadership in Paris.",
                            "Linguistic Feat: Spoken across English, German, French, and Italian; Christoph Waltz gave an astonishing multilingual performance that launched him to global superstardom.",
                            "Filming Locations: Filmed at Studio Babelsberg outside Berlin and on location in Saxony, Germany."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "Which actor won a posthumous Academy Award for Best Supporting Actor for portraying The Joker in 'The Dark Knight' (2008)?",
                        "options": ["Heath Ledger", "Joaquin Phoenix", "Jack Nicholson", "Jared Leto"],
                        "correct": 0,
                        "explanation": "Heath Ledger's electrifying performance as The Joker earned him a posthumous Oscar, recognized as one of the greatest acting feats in cinema history."
                    },
                    {
                        "q": "How many Academy Awards did 'The Lord of the Rings: The Return of the King' win in 2004, achieving a 100% clean sweep?",
                        "options": ["11 Oscars", "9 Oscars", "13 Oscars", "7 Oscars"],
                        "correct": 0,
                        "explanation": "'The Return of the King' was nominated for 11 Oscars and won all 11, including Best Picture and Best Director for Peter Jackson."
                    },
                    {
                        "q": "What unusual weapon does the psychopathic hitman Anton Chigurh wield to kill victims and breach door locks in 'No Country for Old Men'?",
                        "options": ["A captive bolt stunner with compressed air tank", "A silenced crossbow", "A custom titanium wire garrote", "A high-caliber sniper rifle"],
                        "correct": 0,
                        "explanation": "Anton Chigurh carries a pneumatic captive bolt pistol connected to an air tank, typically used to humanely stun cattle in slaughterhouses."
                    },
                    {
                        "q": "What subtle visual symbol did Martin Scorsese embed in frame backgrounds throughout 'The Departed' to foreshadow impending character deaths?",
                        "options": ["The letter 'X'", "A broken clock", "A red rose", "A spilling cup of coffee"],
                        "correct": 0,
                        "explanation": "Scorsese paid homage to Howard Hawks' 1932 classic 'Scarface' by framing subtle 'X' tape marks, architectural crosses, and window beams behind characters about to die."
                    },
                    {
                        "q": "Which breakout actor played SS Colonel Hans Landa in 'Inglourious Basterds', winning both Cannes Best Actor and the Academy Award?",
                        "options": ["Christoph Waltz", "Daniel Brühl", "Michael Fassbender", "Til Schweiger"],
                        "correct": 0,
                        "explanation": "Austrian actor Christoph Waltz won international acclaim and his first Oscar for his masterfully multilingual and chilling performance as Hans Landa."
                    },
                    {
                        "q": "In Ridley Scott's 'Gladiator', what was General Maximus Decimus Meridius's original homeland in the Roman Empire?",
                        "options": ["Hispania (Spain)", "Gaul (France)", "Germania (Germany)", "Britannia (Britain)"],
                        "correct": 0,
                        "explanation": "Maximus is known in the gladiatorial arenas as 'The Spaniard' because his beloved family villa and fertile farm were located in Trujillo, Hispania (modern-day Spain)."
                    },
                    {
                        "q": "What is unique about the sound design and soundtrack of the Coen Brothers' Oscar-winning film 'No Country for Old Men'?",
                        "options": ["It features virtually no musical score", "It uses exclusively a cappella choral vocals", "It consists solely of 1950s rock-and-roll hits", "It was recorded in reverse audio playback"],
                        "correct": 0,
                        "explanation": "The film contains almost no musical score throughout its two-hour runtime, relying entirely on natural environmental sounds and ambient silence."
                    },
                    {
                        "q": "Which major real-world US metropolis served as the primary filming location for Gotham City in 'The Dark Knight'?",
                        "options": ["Chicago", "New York City", "Philadelphia", "Pittsburgh"],
                        "correct": 0,
                        "explanation": "Christopher Nolan filmed Gotham's iconic sweeping architecture, Lower Wacker Drive truck chase, and downtown explosions across Chicago, Illinois."
                    },
                    {
                        "q": "Which Asian action thriller served as the direct source material and inspiration for Martin Scorsese's 'The Departed'?",
                        "options": ["Infernal Affairs (Hong Kong)", "Oldboy (South Korea)", "A Bittersweet Life (South Korea)", "Hard Boiled (Hong Kong)"],
                        "correct": 0,
                        "explanation": "'The Departed' is an American adaptation of Andrew Lau and Alan Mak's critically acclaimed 2002 Hong Kong crime thriller 'Infernal Affairs'."
                    },
                    {
                        "q": "Which country provided the vast natural landscapes and mountain backdrops for Peter Jackson's 'Lord of the Rings' trilogy?",
                        "options": ["New Zealand", "Scotland", "Norway", "Iceland"],
                        "correct": 0,
                        "explanation": "Peter Jackson shot the entire 'Lord of the Rings' trilogy simultaneously across the breathtaking national parks and peaks of his native New Zealand."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 3: 2010s Mind-Benders & Auteur Masterpieces (2010–2019)
            # =================================================================
            {
                "id": "mindbenders_2010s",
                "title": "2010s Mind-Benders & Auteur Masterpieces (2010–2019)",
                "description": "Complex narrative puzzles, jaw-dropping practical action, and intense psychological dramas.",
                "cards": [
                    {
                        "title": "Inception (2010)",
                        "points": [
                            "IMDb Rating: 8.8/10 | Written and directed by Christopher Nolan | Won 4 Academy Awards.",
                            "Cast & Characters: Leonardo DiCaprio (Dom Cobb), Joseph Gordon-Levitt (Arthur), Elliot Page (Ariadne), Tom Hardy (Eames), and Marion Cotillard (Mal).",
                            "Storyline & Themes: An extractor who infiltrates targets' subconscious minds during REM sleep is tasked with planting an idea ('inception') deep inside a corporate heir's mind across four nested dream layers.",
                            "Technical Wonder: Nolan constructed a full-scale 360-degree rotating hotel hallway gimbal rig in a repurposed airship hangar in Cardington, UK, for Arthur's zero-gravity fight.",
                            "The Ending Debate: The final shot cuts to black as Cobb's spinning pewter totem wobbles, leaving viewers to decide whether he is truly awake with his children."
                        ]
                    },
                    {
                        "title": "Interstellar (2014)",
                        "points": [
                            "IMDb Rating: 8.7/10 | Directed by Christopher Nolan | Original score by Hans Zimmer.",
                            "Cast & Characters: Matthew McConaughey as Cooper, Anne Hathaway as Dr. Brand, Jessica Chastain as adult Murph, and Michael Caine as Professor Brand.",
                            "Storyline & Themes: As Earth's biosphere collapses from blight, astronauts venture through a wormhole near Saturn to find habitable worlds, navigating extreme gravitational time dilation and higher dimensions.",
                            "Scientific Realism: Nobel laureate physicist Kip Thorne consulted on the physics and gravitational lensing algorithms, producing the first scientifically accurate visual model of a supermassive black hole ('Gargantua').",
                            "Filming Locations: Svínafellsjökull glacier in Iceland (representing Mann's and Miller's ice and water planets) and vast cornfields in Alberta, Canada."
                        ]
                    },
                    {
                        "title": "The Wolf of Wall Street (2013)",
                        "points": [
                            "IMDb Rating: 8.2/10 | Directed by Martin Scorsese | Adapted from Jordan Belfort's memoir.",
                            "Cast & Characters: Leonardo DiCaprio as Jordan Belfort, Jonah Hill as Donnie Azoff, and Margot Robbie in her breakout role as Naomi Lapaglia.",
                            "Storyline & Themes: A fast-paced, hedonistic dark comedy exploring boiler room pump-and-dump securities fraud, unbridled Wall Street greed, and chaotic excess.",
                            "Cinematic Technique: DiCaprio frequently breaks the fourth wall to address the audience directly about trading schemes, accompanied by rapid montage cuts.",
                            "Trivia: Holds the record for one of the highest uses of profanity in mainstream cinema history (over 500 F-bombs)."
                        ]
                    },
                    {
                        "title": "Whiplash (2014)",
                        "points": [
                            "IMDb Rating: 8.5/10 | Written and directed by Damien Chazelle | Won 3 Academy Awards.",
                            "Cast & Characters: Miles Teller as ambitious jazz drummer Andrew Neiman and J.K. Simmons as the tyrannical, abusive conductor Terence Fletcher.",
                            "Storyline & Themes: Set at the prestigious Shaffer Conservatory in New York, the film examines whether ruthless psychological torment is necessary to forge artistic greatness.",
                            "Filming Pace: Shot in just 19 days in Los Angeles on a modest $3.3 million budget after Chazelle proved the concept with an award-winning Sundance short.",
                            "Physical Performance: Miles Teller, who has played drums since age 15, performed almost all of his drumming scenes, resulting in real blistering and blood on his hands."
                        ]
                    },
                    {
                        "title": "Mad Max: Fury Road (2015)",
                        "points": [
                            "IMDb Rating: 8.1/10 | Directed and co-written by George Miller | Winner of 6 Academy Awards.",
                            "Cast & Characters: Tom Hardy as Max Rockatansky, Charlize Theron as Imperator Furiosa, and Nicholas Hoult as War Boy Nux.",
                            "Storyline & Themes: A relentless high-octane desert chase across a post-apocalyptic wasteland where Furiosa rebels against warlord Immortan Joe to rescue his enslaved wives.",
                            "Stunt Mastery: Over 80% of the film's visual stunts and explosive vehicle collisions were performed practically in the Namibian desert with real stunt drivers and pole-cats.",
                            "Production Saga: Filming moved from Broken Hill, Australia to Swakopmund, Namibia after unexpected seasonal rainfall turned the Australian red desert into lush wildflower fields."
                        ]
                    },
                    {
                        "title": "Parasite (2019)",
                        "points": [
                            "IMDb Rating: 8.5/10 | Directed by Bong Joon-ho | Co-written with Han Jin-won.",
                            "Cast & Characters: Song Kang-ho (Kim Ki-taek), Choi Woo-shik (Ki-woo), Park So-dam (Ki-jung), and Cho Yeo-jeong (Mrs. Park).",
                            "Storyline & Themes: A destitute family schemes to infiltrate a wealthy household as unrelated qualified professionals, unraveling dark class inequalities, systemic symbiosis, and subterranean secrets.",
                            "Historic Triumph: First non-English language film in the 92-year history of the Academy Awards to win Best Picture, alongside Best Director, Best Original Screenplay, and Best International Feature.",
                            "Architecture: The luxurious modern Park family mansion was not a real home, but an elaborate multi-tiered architectural set constructed on an outdoor lot in Jeonju."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "What practical mechanical device did Christopher Nolan build to film Joseph Gordon-Levitt's zero-gravity fight scene in 'Inception'?",
                        "options": ["A full-scale 360-degree rotating hotel hallway gimbal", "A submerged underwater soundstage tank", "A Boeing 727 parabolic 'vomit comet' flight", "A motorized vertical wire-harness crane"],
                        "correct": 0,
                        "explanation": "Nolan and special effects supervisor Chris Corbould constructed a massive 100-foot-long rotating cylindrical steel gimbal that turned 360 degrees inside a hangar."
                    },
                    {
                        "q": "Which theoretical astrophysicist and Nobel laureate advised Christopher Nolan on the black hole physics in 'Interstellar'?",
                        "options": ["Kip Thorne", "Stephen Hawking", "Neil deGrasse Tyson", "Roger Penrose"],
                        "correct": 0,
                        "explanation": "Caltech physicist Kip Thorne provided the exact Einstein field equations used by visual effects house Double Negative to render the black hole Gargantua."
                    },
                    {
                        "q": "Which actor won the Best Supporting Actor Oscar for his terrifying portrayal of ruthless music instructor Terence Fletcher in 'Whiplash' (2014)?",
                        "options": ["J.K. Simmons", "Edward Norton", "Mark Ruffalo", "Ethan Hawke"],
                        "correct": 0,
                        "explanation": "J.K. Simmons swept the entire awards season, winning the Oscar, BAFTA, and Golden Globe for his fierce performance."
                    },
                    {
                        "q": "Why was the production of 'Mad Max: Fury Road' relocated from Australia to the Namib Desert in Namibia?",
                        "options": ["Unprecedented rainfall turned the Australian desert green with flowers", "Australian road transport unions blocked the heavy war rigs", "Severe heatwaves damaged the digital camera sensors", "Filming permits were revoked by the Australian government"],
                        "correct": 0,
                        "explanation": "Historic rainfall in Broken Hill, Australia caused the red desert to bloom with green vegetation and wildflowers, ruining the barren post-apocalyptic aesthetic."
                    },
                    {
                        "q": "What historic milestone did Bong Joon-ho's 'Parasite' achieve at the 92nd Academy Awards in 2020?",
                        "options": ["First non-English film to win Best Picture", "First film to win all 4 acting categories", "First movie filmed entirely on an iPhone to win an Oscar", "First animated movie to be nominated for Best Picture"],
                        "correct": 0,
                        "explanation": "'Parasite' made Oscar history as the very first foreign-language film to win the coveted Best Picture Academy Award."
                    },
                    {
                        "q": "In 'Inception', what personal object (totem) does Dom Cobb use to verify whether he is in the waking world or a dream?",
                        "options": ["A weighted brass spinning top", "A loaded silver die", "A hollow chess bishop", "A poker chip with an engraved skull"],
                        "correct": 0,
                        "explanation": "Cobb uses a small pewter spinning top that originally belonged to his late wife Mal; in the dream world, the top spins indefinitely without falling."
                    },
                    {
                        "q": "On Miller's ocean planet in 'Interstellar', one hour on the planet's surface corresponds to how many Earth years due to extreme gravitational time dilation?",
                        "options": ["7 years on Earth", "1 year on Earth", "25 years on Earth", "50 years on Earth"],
                        "correct": 0,
                        "explanation": "Because Miller's planet orbits very close to the supermassive black hole Gargantua, one hour spent on its surface equals seven years of elapsed Earth time."
                    },
                    {
                        "q": "Which actress had her major breakout Hollywood performance opposite Leonardo DiCaprio in 'The Wolf of Wall Street' (2013)?",
                        "options": ["Margot Robbie", "Emma Stone", "Florence Pugh", "Ana de Armas"],
                        "correct": 0,
                        "explanation": "Australian actress Margot Robbie catapulted to international stardom with her charismatic performance as Naomi Lapaglia."
                    },
                    {
                        "q": "What song does Fletcher instruct Andrew to play to set the grueling tempo in 'Whiplash'?",
                        "options": ["'Caravan' and 'Whiplash'", "'Take Five' and 'Blue Rondo'", "'Sing, Sing, Sing' and 'Moanin''", "'Giant Steps' and 'So What'"],
                        "correct": 0,
                        "explanation": "Hank Levy's intricate 'Whiplash' (in 7/4 time signature) and Juan Tizol / Duke Ellington's 'Caravan' form the core musical trials of the film."
                    },
                    {
                        "q": "Who played Imperator Furiosa in George Miller's 2015 action masterpiece 'Mad Max: Fury Road'?",
                        "options": ["Charlize Theron", "Emily Blunt", "Sigourney Weaver", "Scarlett Johansson"],
                        "correct": 0,
                        "explanation": "Charlize Theron delivered an iconic, career-defining performance as the one-armed warrior Imperator Furiosa."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 4: 2020s Modern Epics, Sci-Fi & New Visions (2020–Present)
            # =================================================================
            {
                "id": "modern_visions_2020s",
                "title": "2020s Modern Epics, Sci-Fi & New Visions (2020–Present)",
                "description": "Technological leaps, 70mm IMAX cinema, and multi-genre triumphs of the current era.",
                "cards": [
                    {
                        "title": "Oppenheimer (2023)",
                        "points": [
                            "IMDb Rating: 8.9/10 | Written and directed by Christopher Nolan | Winner of 7 Academy Awards including Best Picture and Best Director.",
                            "Cast & Characters: Cillian Murphy as J. Robert Oppenheimer, Robert Downey Jr. as Lewis Strauss, and Emily Blunt as Katherine 'Kitty' Oppenheimer.",
                            "Storyline & Themes: The biographical epic of theoretical physicist J. Robert Oppenheimer leading the Manhattan Project to develop the atomic bomb, followed by postwar political betrayal and moral reckoning.",
                            "Cinematic Innovation: Nolan convinced Kodak to manufacture the world's first large-format 65mm black-and-white film stock to shoot Strauss's objective perspective scenes in 70mm IMAX.",
                            "Practical Explosion: The Trinity atomic test was staged practically without computer-generated imagery (CGI), utilizing magnesium, gasoline, black powder, and aluminum shavings."
                        ]
                    },
                    {
                        "title": "Dune: Part Two (2024)",
                        "points": [
                            "IMDb Rating: 8.6/10 | Directed and co-written by Denis Villeneuve | Adapted from Frank Herbert's seminal sci-fi novel.",
                            "Cast & Characters: Timothée Chalamet (Paul Atreides), Zendaya (Chani), Austin Butler (Feyd-Rautha Harkonnen), and Rebecca Ferguson (Lady Jessica).",
                            "Storyline & Themes: Paul unites with the Fremen to wage holy war against the Harkonnens and the Padishah Emperor on the desert planet Arrakis, wrestling with grim prophetic tyranny.",
                            "Cinematography & Sound: Greig Fraser shot the monochrome Giedi Prime gladiatorial sequences using infrared cameras; Hans Zimmer composed an otherworldly sonic score.",
                            "Filming Locations: Filmed across the desert dunes of Wadi Rum in Jordan, Abu Dhabi's Liwa Oasis, Budapest sound stages, and the Brion Tomb in San Vito d'Altivole, Italy."
                        ]
                    },
                    {
                        "title": "Everything Everywhere All at Once (2022)",
                        "points": [
                            "IMDb Rating: 7.8/10 | Written and directed by Daniel Kwan and Daniel Scheinert ('The Daniels') | Winner of 7 Academy Awards including Best Picture.",
                            "Cast & Characters: Michelle Yeoh (Evelyn Wang), Ke Huy Quan (Waymond Wang), Stephanie Hsu (Joy Wang / Jobu Tupaki), and Jamie Lee Curtis (Deirdre).",
                            "Storyline & Themes: An overwhelmed Chinese-American laundromat owner audit subject discovers she must connect with parallel universe versions of herself to save the multiverse from cosmic existential dread.",
                            "Historic Indie Feat: Produced on a modest $14–25 million budget with a tiny 5-person visual effects team of self-taught artists, becoming A24's highest-grossing film ever.",
                            "Emotional Comeback: Ke Huy Quan won Best Supporting Actor in a triumphant Hollywood return after nearly 30 years away from major acting roles."
                        ]
                    },
                    {
                        "title": "Blade Runner 2049 (2017)",
                        "points": [
                            "IMDb Rating: 8.0/10 | Directed by Denis Villeneuve | Produced by Ridley Scott | Won 2 Oscars.",
                            "Cast & Characters: Ryan Gosling as K (a Nexus-9 replicant blade runner), Harrison Ford reprising Rick Deckard, and Ana de Armas as Joi.",
                            "Storyline & Themes: A replicant detective unearths a long-buried secret that threatens to overturn the foundations of human-synthetic society, exploring memory, soul, and artificial yearning.",
                            "Visual Mastery: Legendary cinematographer Roger Deakins won his first Academy Award for the film's spellbinding orange-hued dust storm palettes and high-contrast lighting.",
                            "Filming Location: Constructed across sprawling soundstages at Korda Studios and Origo Studios in Budapest, Hungary."
                        ]
                    },
                    {
                        "title": "John Wick: Chapter 4 (2023)",
                        "points": [
                            "IMDb Rating: 7.7/10 | Directed by Chad Stahelski | Starring Keanu Reeves, Donnie Yen, and Bill Skarsgård.",
                            "Storyline & Themes: The legendary hitman battles the High Table across the globe to earn his freedom, featuring jaw-dropping 'gun-fu' stunt choreography.",
                            "Landmark Action Scene: Features a breathtaking continuous top-down overhead tracking shot inside an abandoned Paris apartment using 'Dragon's Breath' incendiary shotgun rounds.",
                            "Filming Locations: Filmed across real iconic locations in Paris (Eiffel Tower, Arc de Triomphe, Sacré-Cœur 222 steps), Berlin, and Osaka."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "What special custom film stock did Kodak manufacture specifically for Christopher Nolan's 'Oppenheimer' (2023)?",
                        "options": ["Large-format 65mm black-and-white IMAX film", "Infrared 35mm night-vision film", "High-speed 120-frame-per-second 70mm color film", "Dual-emulsion 3D stereoscopic 65mm film"],
                        "correct": 0,
                        "explanation": "Kodak created the first-ever 65mm black-and-white film emulsion specifically so Nolan and cinematographer Hoyte van Hoytema could film Strauss's scenes in full IMAX resolution."
                    },
                    {
                        "q": "How did cinematographer Greig Fraser achieve the eerie, desaturated monochrome look for the Giedi Prime arena scenes in 'Dune: Part Two'?",
                        "options": ["Shooting with modified digital cameras capturing only infrared light", "Using vintage 1920s orthochromatic black-and-white film", "Applying post-production green-screen color replacement", "Spraying the entire stadium with black chalk and polarized filters"],
                        "correct": 0,
                        "explanation": "Fraser used ARRI digital cameras modified to capture near-infrared spectrum light, making skin look translucent and clothing starkly surreal."
                    },
                    {
                        "q": "Which actor made an emotional return to Hollywood after nearly 30 years and won an Oscar for 'Everything Everywhere All at Once'?",
                        "options": ["Ke Huy Quan", "Steven Yeun", "BD Wong", "Hiroyuki Sanada"],
                        "correct": 0,
                        "explanation": "Ke Huy Quan (who starred as Short Round in 'Indiana Jones' as a child) won the Academy Award for Best Supporting Actor for his role as Waymond Wang."
                    },
                    {
                        "q": "Which legendary cinematographer won his first long-awaited Academy Award for Denis Villeneuve's 'Blade Runner 2049'?",
                        "options": ["Roger Deakins", "Emmanuel Lubezki", "Hoyte van Hoytema", "Robert Richardson"],
                        "correct": 0,
                        "explanation": "After 13 previous nominations without a win, Roger Deakins won the Best Cinematography Oscar for his visual masterpiece in 'Blade Runner 2049'."
                    },
                    {
                        "q": "In 'John Wick: Chapter 4', what famous Paris landmark staircase features John Wick battling hitmen up its 222 steps?",
                        "options": ["The steps leading to Sacré-Cœur Basilica in Montmartre", "The Eiffel Tower base stairs", "The steps of the Palais Garnier Opera House", "The Grand Palais entry stairs"],
                        "correct": 0,
                        "explanation": "John Wick fights his way up (and tumbles all the way back down) the famous 222-step Rue Foyatier staircase leading up to Sacré-Cœur in Montmartre."
                    },
                    {
                        "q": "Which actor portrayed the antagonistic US Atomic Energy Commission chairman Lewis Strauss in 'Oppenheimer', winning the Best Supporting Actor Oscar?",
                        "options": ["Robert Downey Jr.", "Matt Damon", "Kenneth Branagh", "Josh Hartnett"],
                        "correct": 0,
                        "explanation": "Robert Downey Jr. won his first Academy Award for his brilliant performance as Lewis Strauss in 'Oppenheimer'."
                    },
                    {
                        "q": "Which famous real-world desert valley in Jordan served as the primary filming location for the desert planet Arrakis in 'Dune'?",
                        "options": ["Wadi Rum", "Death Valley", "Atacama Desert", "Sahara Dunes of Merzouga"],
                        "correct": 0,
                        "explanation": "Denis Villeneuve filmed the sweeping desert landscapes and sandstone cliffs of Arrakis in Wadi Rum, Jordan (the 'Valley of the Moon')."
                    },
                    {
                        "q": "What video game camera perspective inspired the continuous Parisian apartment shootout with incendiary shotgun shells in 'John Wick: Chapter 4'?",
                        "options": ["A top-down bird's-eye view (like 'Hong Kong Massacre')", "A first-person shooter perspective (like 'Doom')", "A side-scrolling platformer view (like 'Street Fighter')", "An over-the-shoulder third-person camera (like 'Resident Evil')"],
                        "correct": 0,
                        "explanation": "Director Chad Stahelski utilized a top-down crane rig tracking above rooms in a continuous shot, inspired by top-down shooter games like 'The Hong Kong Massacre'."
                    },
                    {
                        "q": "How many Academy Awards did 'Everything Everywhere All at Once' win at the 95th Oscars, including Best Picture and 3 acting wins?",
                        "options": ["7 Oscars", "4 Oscars", "10 Oscars", "12 Oscars"],
                        "correct": 0,
                        "explanation": "The film swept 7 major Oscars: Best Picture, Best Director, Best Actress (Michelle Yeoh), Best Supporting Actor (Ke Huy Quan), Best Supporting Actress (Jamie Lee Curtis), Best Original Screenplay, and Best Film Editing."
                    },
                    {
                        "q": "Who directed both 'Blade Runner 2049' and 'Dune: Part One & Part Two'?",
                        "options": ["Denis Villeneuve", "Christopher Nolan", "Ridley Scott", "George Miller"],
                        "correct": 0,
                        "explanation": "French-Canadian visionary director Denis Villeneuve directed both landmark sci-fi epics."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 5: Master Directors, Legendary Plot Twists & Unscripted Moments
            # =================================================================
            {
                "id": "directors_twists_lore",
                "title": "Master Directors, Legendary Twists & Behind-The-Scenes Lore",
                "description": "The unscripted accidents, signature auteur styles, and shock endings that redefined cinema history.",
                "cards": [
                    {
                        "title": "Christopher Nolan & Quentin Tarantino: Auteur Signatures",
                        "points": [
                            "Christopher Nolan: Passionate defender of celluloid 70mm film stock, practical in-camera effects (crashing real Boeing 747s, building full-scale rotating sets), and non-linear temporal narrative structures.",
                            "Quentin Tarantino: Famous for rapid-fire pop-culture dialogue, chapter-based story structures, encyclopedic film homages, needle-drop soundtracks, and alternate-history climaxes.",
                            "David Fincher: Renowned for extreme digital perfectionism, often demanding 50 to 100+ takes per scene to strip actors of artificial performance habits.",
                            "Martin Scorsese: Signature use of kinetic moving camera tracking shots, freeze frames, voiceover narration, and deep collaborative partnerships with Robert De Niro and Leonardo DiCaprio."
                        ]
                    },
                    {
                        "title": "Legendary Unscripted & Improvised Movie Moments",
                        "points": [
                            "Django Unchained (2012): Leonardo DiCaprio accidentally slammed his hand into a glass goblet, cutting his palm open. He stayed fully in character, bleeding profusely across the table throughout his monologue.",
                            "The Dark Knight (2008): Heath Ledger's Joker sarcastically clapping in his GCPD jail cell when Gordon is promoted to Commissioner was entirely improvised on the spot.",
                            "The Wolf of Wall Street (2013): Matthew McConaughey's rhythmic chest-thumping and humming was his personal pre-scene warm-up ritual; DiCaprio suggested putting it directly into the scene.",
                            "The Lord of the Rings: The Two Towers (2002): When Aragorn kicks an Uruk-hai helmet in despair, Viggo Mortensen broke two toes and let out an agonized scream that Jackson kept in the final cut."
                        ]
                    },
                    {
                        "title": "The Greatest Modern Plot Twists",
                        "points": [
                            "The Sixth Sense (1999): Child psychologist Malcolm Crowe (Bruce Willis) realizes at the climax that he has been a ghost the entire time.",
                            "The Prestige (2006): Magician Alfred Borden (Christian Bale) reveals he is actually a set of identical twins living one shared life, while Robert Angier (Hugh Jackman) cloned and drowned himself nightly using Tesla's machine.",
                            "Shutter Island (2010): US Marshal Teddy Daniels (Leonardo DiCaprio) discovers he is actually Andrew Laeddis, a traumatized patient at the psychiatric hospital participating in a radical role-playing therapy experiment.",
                            "Memento (2000): Leonard Shelby (Guy Pearce) discovers he has been intentionally manipulating his own anterograde amnesia to create an endless quest for vengeance against people who did not murder his wife."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "In 'Django Unchained' (2012), what genuine real-life injury occurred during Calvin Candie's intense dining room monologue?",
                        "options": ["Leonardo DiCaprio cut his hand on a shattered glass and kept acting while bleeding", "Jamie Foxx dislocated his shoulder during a quick-draw scene", "Christoph Waltz fractured his ankle falling off a horse", "Samuel L. Jackson burned his hand on a hot cast-iron poker"],
                        "correct": 0,
                        "explanation": "Leonardo DiCaprio accidentally slammed his hand into a crystal glass goblet, slicing his palm. Rather than stopping, he incorporated the bleeding hand into his menacing monologue."
                    },
                    {
                        "q": "What real-life warm-up ritual of Matthew McConaughey was incorporated into his famous diner scene in 'The Wolf of Wall Street'?",
                        "options": ["Rhythmically thumping his chest and humming a cadence", "Doing rapid pushups while reciting stock ticker symbols", "Snapping his fingers in a syncopated jazz rhythm", "Drinking a double espresso while staring unblinkingly at the mirror"],
                        "correct": 0,
                        "explanation": "McConaughey regularly thumps his chest and hums to relax his vocal cords before takes. Leonardo DiCaprio noticed it and urged Martin Scorsese to shoot it as part of the scene."
                    },
                    {
                        "q": "In 'The Prestige' (2006), how does illusionist Alfred Borden (Christian Bale) achieve his impossible 'Transported Man' teleportation trick?",
                        "options": ["He is actually a pair of identical twin brothers living one single identity", "He uses a quantum duplication machine built by Nikola Tesla", "He hires a lookalike alcoholic double named Gerald Root", "He relies on trapdoors and synchronized mirror optics"],
                        "correct": 0,
                        "explanation": "Alfred and Fallon are identical twin brothers who live one shared life (sacrificing their individual identities) to perform the ultimate illusion."
                    },
                    {
                        "q": "What is the climactic revelation about US Marshal Teddy Daniels in Martin Scorsese's 'Shutter Island' (2010)?",
                        "options": ["He is actually a patient at the asylum (Andrew Laeddis) living a role-play delusion", "He was secretly hired by the FBI to assassinate the head psychiatrist", "He is a German spy attempting to steal mind-control formulas", "He hallucinated the entire island while trapped in a Boston blizzard"],
                        "correct": 0,
                        "explanation": "Teddy Daniels is revealed to be Andrew Laeddis, the hospital's most dangerous patient, and the investigation was an elaborate role-playing therapy orchestrated by his doctors."
                    },
                    {
                        "q": "What injury did Viggo Mortensen suffer when he kicked a heavy steel helmet in 'The Lord of the Rings: The Two Towers'?",
                        "options": ["He broke two toes", "He sprained his ankle", "He fractured his kneecap", "He tore his Achilles tendon"],
                        "correct": 0,
                        "explanation": "Mortensen kicked the heavy helmet with genuine fury on the fifth take, breaking two of his toes; his agonizing scream was kept in the film because of its raw emotional power."
                    },
                    {
                        "q": "Which director is famous for demanding dozens or even hundreds of takes for simple scenes to achieve exact digital precision?",
                        "options": ["David Fincher", "Quentin Tarantino", "Steven Spielberg", "Clint Eastwood"],
                        "correct": 0,
                        "explanation": "David Fincher is famous for his exhaustive 50-to-100+ take methodology (e.g., in 'The Social Network' and 'Zodiac') to strip actors of rehearsed mannerisms."
                    },
                    {
                        "q": "In Christopher Nolan's breakthrough non-linear film 'Memento' (2000), what condition affects the protagonist Leonard Shelby?",
                        "options": ["Anterograde amnesia (inability to form new short-term memories)", "Dissociative fugue identity disorder", "Retrograde amnesia (loss of all childhood memories)", "Prosopagnosia (inability to recognize human faces)"],
                        "correct": 0,
                        "explanation": "Leonard suffers from anterograde amnesia following head trauma, relying on Polaroid photos, handwritten notes, and tattoos to track his investigation."
                    },
                    {
                        "q": "In 'The Dark Knight', Heath Ledger improvised which famous chilling reaction while sitting locked in a jail cell?",
                        "options": ["Slowly and sarcastically clapping for Commissioner Gordon's promotion", "Licking his lips while whispering a nursery rhyme", "Banging his head against the iron bars in rhythm", "Balancing a playing card on the tip of his shoe"],
                        "correct": 0,
                        "explanation": "When the police officers begin applauding Jim Gordon's promotion, Ledger unscriptedly began slowly clapping along with an unsettling smirk."
                    },
                    {
                        "q": "What famous plot twist stunned audiences in M. Night Shyamalan's 1999 breakout hit 'The Sixth Sense'?",
                        "options": ["Dr. Malcolm Crowe had been dead the entire time", "The young boy Cole was actually hallucinating all the ghosts", "Cole's mother was the one poisoning the town's children", "The ghosts were physical beings from an alternate dimension"],
                        "correct": 0,
                        "explanation": "Child psychologist Malcolm Crowe (Bruce Willis) realizes in the final moments that he was killed in the opening scene and only exists as a ghost that Cole can see."
                    },
                    {
                        "q": "Which iconic actor has starred as the lead in collaborative films with both Martin Scorsese ('The Wolf of Wall Street', 'The Departed') and Quentin Tarantino ('Django Unchained', 'Once Upon a Time in Hollywood')?",
                        "options": ["Leonardo DiCaprio", "Brad Pitt", "Robert De Niro", "Christian Bale"],
                        "correct": 0,
                        "explanation": "Leonardo DiCaprio has played iconic, critically acclaimed leading roles for both Scorsese and Tarantino."
                    }
                ]
            }
        ]
    }

    # -------------------------------------------------------------------------
    # HEBREW DATASET
    # -------------------------------------------------------------------------
    he_data = {
        "id": "hollywood_modern_classics_he",
        "title": "יצירות המופת של הוליווד המודרנית (משנות ה-90 ועד היום)",
        "description": "מסע קולנועי מחשמל בשוברי הקופות וביצירות המופת הגדולות של הוליווד משנות ה-90 ועד היום! בחנו את הידע שלכם בסרטי פולחן למבוגרים, מותחנים של טרנטינו ופינצ'ר, חידות פילוסופיות של כריסטופר נולאן, אפוסים של מדע בדיוני, במאים אגדיים וסודות ממאחורי הקלעים.",
        "lang": "he",
        "audience": "adult",
        "categories": [
            # =================================================================
            # CATEGORY 1: 90s Groundbreakers & Cult Revolutions (1990–1999)
            # =================================================================
            {
                "id": "groundbreakers_90s",
                "title": "מהפכת שנות ה-90 וסרטי פולחן (1990–1999)",
                "description": "העשור ששינה לעד את הקולנוע העצמאי, שוברי הקופות והאפקטים החזותיים.",
                "cards": [
                    {
                        "title": "חומות של תקווה (The Shawshank Redemption, 1994)",
                        "points": [
                            "ציון IMDb: 9.3/10 (מדורג במקום הראשון בכל הזמנים ב-IMDb) | בימוי: פרנק דרבונט.",
                            "שחקנים ודמויות: טים רובינס בתור אנדי דופריין (בנקאי שהורשע לשווא) ומורגן פרימן בתור אליס בויד 'רד' רדינג (ספק ההברחות של הכלא).",
                            "עלילה ותמות: במשך שני עשורים בכלא שושנק במיין, אנדי שומר על כבוד עצמי, מעורר תקווה באסירים ומוציא לפועל תוכנית בריחה גיאולוגית גאונית.",
                            "אתר צילום: צולם בעיקר בבית הסוהר ההיסטורי של מדינת אוהיו במנספילד.",
                            "טריוויה ומורשת: למרות אכזבה בקופות בעת יציאתו עקב תחרות מול 'פורסט גאמפ' ו'ספרות זולה', הפך ללהיט ענק בהשכרות וידאו וליצירת מופת תרבותית."
                        ]
                    },
                    {
                        "title": "ספרות זולה (Pulp Fiction, 1994)",
                        "points": [
                            "ציון IMDb: 8.9/10 | בימוי ותסריט: קוונטין טרנטינו | זכה בפרס 'דקל הזהב' בקאן ובאוסקר לתסריט המקורי הטוב ביותר.",
                            "שחקנים ודמויות: ג'ון טרבולטה (וינסנט וגה), סמואל ל. ג'קסון (ג'ולס וינפילד), אומה תורמן (מיה וואלאס) וברוס ויליס (בוץ' קולידג').",
                            "עלילה ותמות: סיפורי פשע לא-ליניאריים שזורים בלוס אנג'לס, העוסקים בגאולה, נאמנות ומקריות, בליווי דיאלוגים מושחזים ופסקול סרף-רוק ופאנק מלהיב.",
                            "אתר צילום: צולם כולו ברחבי לוס אנג'לס וקליפורניה (כולל מסעדת Hawthorne Grill המפורסמת).",
                            "טריוויה: תכולתה הזוהרת של המזוודה המסתורית של מרסלוס וואלאס (צירוף המנעול: 666) מעולם לא נחשפה בסרט, ועוררה אינספור תיאוריות מעריצים."
                        ]
                    },
                    {
                        "title": "המטריקס (The Matrix, 1999)",
                        "points": [
                            "ציון IMDb: 8.7/10 | תסריט ובימוי: האחיות וצ'אוסקי (לאנה ולילי וצ'אוסקי).",
                            "שחקנים ודמויות: קיאנו ריבס (ניאו / תומאס אנדרסון), לורנס פישבורן (מורפיוס), קארי-אן מוס (טריניטי) והוגו וויבינג (הסוכן סמית').",
                            "עלילה ותמות: מותחן סייבר-פאנק דיסטופי שבו האנושות כלואה במציאות מדומה שנוצרה על ידי מכונות תבוניות כדי לשאוב את האנרגיה הביו-חשמלית של בני האדם.",
                            "אתר צילום: צולם באולפנים וברחובות סידני, אוסטרליה, לצורך ניצול מרבי של תקציב ההפקה.",
                            "טכנולוגיה מהפכנית: פיתח והנחיל את אפקט ה-'Bullet Time' באמצעות מערך מעגלי של מעל 120 מצלמות סטילס שצילמו במרווחי מיקרו-שניות."
                        ]
                    },
                    {
                        "title": "מועדון קרב (Fight Club, 1999)",
                        "points": [
                            "ציון IMDb: 8.8/10 | בימוי: דייוויד פינצ'ר | עיבוד לספרו של צ'אק פלאניוק.",
                            "שחקנים ודמויות: אדוארד נורטון בתור המספר המדוכא, בראד פיט בתור יצרן הסבון הכריזמטי טיילר דרדן, והלנה בונהם קרטר בתור מרלה סינגר.",
                            "עלילה ותמות: ביקורת חריפה על תרבות הצריכה, הניכור התאגידי וגבריות רעילה, המתדרדרת לתנועת מחתרת אנרכיסטית להשמדת מערכת האשראי.",
                            "אתר צילום: צולם בעשרות סמטאות ואתרים תעשייתיים בלוס אנג'לס.",
                            "פרט ויזואלי מבריק: פינצ'ר החביא כוס קפה של סטארבקס כמעט בכל סצנה בודדת בסרט כסמל להשתלטות התאגידית על חיי היומיום."
                        ]
                    },
                    {
                        "title": "החבר'ה הטובים (Goodfellas, 1990)",
                        "points": [
                            "ציון IMDb: 8.7/10 | בימוי: מרטין סקורסזה | מבוסס על הספר 'Wiseguy' מאת ניקולס פילאג'י.",
                            "שחקנים ודמויות: ריי ליוטה (הנרי היל), רוברט דה נירו (ג'ימי קונוויי) וג'ו פשי (טומי דה-ויטו חם המזג, שזכה באוסקר לשחקן משנה).",
                            "עלילה ותמות: עלייתו ונפילתו לאורך שלושה עשורים של שותף משפחת המאפיה לוקזה, הנרי היל, תוך הצגת הפיתוי הנוצץ והפרנויה האכזרית של עולם הפשע.",
                            "שוט קולנועי מיתולוגי: שוט רציף מפורסם בן 3 דקות במצלמת סטדיקאם (Steadicam) העוקב אחר כניסתם של הנרי וקארן למועדון הלילה קופקבנה דרך המטבח האחורי.",
                            "טריוויה: סצנת החקירה המאיימת 'Funny how? Like I'm a clown?' של ג'ו פשי הייתה אלתור המבוסס על מקרה אמיתי שפשי חווה כמלצר צעיר."
                        ]
                    },
                    {
                        "title": "שתיקת הכבשים (The Silence of the Lambs, 1991)",
                        "points": [
                            "ציון IMDb: 8.6/10 | בימוי: ג'ונתן דמי | מבוסס על ספרו של תומאס האריס.",
                            "שחקנים ודמויות: ג'ודי פוסטר בתור חניכת ה-FBI קלריס סטרלינג, ואנתוני הופקינס בתור הפסיכיאטר הקניבל המבריק ד״ר חניבעל לקטר.",
                            "עלילה ותמות: קלריס נאלצת לחקור את מוחו המצמרר של לקטר הכלוא מאחורי זכוכית כדי לפענח את זהותו של הרוצח הסדרתי הפעיל 'באפלו ביל'.",
                            "אתר צילום: צולם בעיקר בפיטסבורג, פנסילבניה ובבית הסוהר המערבי של המדינה.",
                            "הישג היסטורי: אחד משלושה סרטים בלבד בתולדות האוסקר שגרפו את 'חמשת הגדולים' (סרט, במאי, שחקן, שחקנית ותסריט מעובד), כאשר הופקינס מופיע על המסך כ-16 דקות בלבד."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "מהו אתר הצילום המרכזי ששימש ככלא שושנק בסרט 'חומות של תקווה' (1994)?",
                        "options": ["בית הסוהר ההיסטורי של מדינת אוהיו במנספילד", "כלא אלקטרז הפדרלי בסן פרנסיסקו", "בית הסוהר המזרחי בפילדלפיה", "מתקן הכליאה סינג סינג בניו יורק"],
                        "correct": 0,
                        "explanation": "'חומות של תקווה' צולם בבית הסוהר ההיסטורי במנספילד שבמדינת אוהיו, המשמש כיום כמוזיאון ואתר תיירות פופולרי."
                    },
                    {
                        "q": "בסרט 'ספרות זולה', מהו צירוף המנעול של המזווה המסתורית והזוהרת של מרסלוס וואלאס?",
                        "options": ["666", "777", "123", "999"],
                        "correct": 0,
                        "explanation": "צירוף המנעול של המזוודה הוא 666, דבר שהזין תיאוריות מעריצים רבות לפיהן המזוודה מכילה את נשמתו של מרסלוס וואלאס."
                    },
                    {
                        "q": "איזו טכניקת צילום חזותית מהפכנית הומצאה והתפרסמה בעולם בזכות הסרט 'המטריקס' (1999)?",
                        "options": ["זמן קליע (Bullet Time)", "לכידת תנועה דיגיטלית (Deepfake Mocap)", "צילום בנפח מסכי לד (StageCraft LED)", "אפקט דולי-זום (Dolly Zoom)"],
                        "correct": 0,
                        "explanation": "טכניקת 'זמן קליע' (Bullet Time) התבססה על מערך מצלמות סטילס מעגלי שאפשר למצלמה להסתובב סביב אובייקט בהילוך סופר-איטי או קפוא."
                    },
                    {
                        "q": "בסרטו של דייוויד פינצ'ר 'מועדון קרב', איזה פריט מסחרי יומיומי החביא הבמאי כמעט בכל סצנה בסרט?",
                        "options": ["כוס קפה של סטארבקס", "בקבוק זכוכית של קוקה-קולה", "נעל ספורט של נייקי", "פתקית ממו צהובה (Post-it)"],
                        "correct": 0,
                        "explanation": "דייוויד פינצ'ר שתל כוס קפה של סטארבקס כמעט בכל סצנה כדי להדגיש את הסאטירה על השתלטות תרבות הצריכה על החברה."
                    },
                    {
                        "q": "לאיזה מועדון לילה מפורסם נכנסים הנרי וקארן בשוט הרציף המפורסם בן ה-3 דקות בסרט 'החבר'ה הטובים'?",
                        "options": ["הקופקבנה (The Copacabana)", "סטודיו 54 (Studio 54)", "מועדון הכותנה (The Cotton Club)", "טרופיקנה (The Tropicana)"],
                        "correct": 0,
                        "explanation": "השוט המפורסם והבלתי-חתוך במצלמת סטדיקאם מציג את כניסתם דרך המטבח האחורי ישירות למועדון הקופקבנה היוקרתי."
                    },
                    {
                        "q": "אנתוני הופקינס זכה באוסקר לשחקן הטוב ביותר על תפקידו ב'שתיקת הכבשים' למרות שהופיע על המסך במשך כמה זמן בסך הכל?",
                        "options": ["כ-16 דקות בלבד", "כ-42 דקות", "כ-65 דקות", "כ-85 דקות"],
                        "correct": 0,
                        "explanation": "הופקינס מופיע בסרט כ-16 דקות בלבד (פחות מ-15% מזמן הריצה הכולל), בהופעה מהפנטת שנחרטה בהיסטוריה הקולנועית."
                    },
                    {
                        "q": "איזה שחקן גילם את הגנגסטר חם המזג טומי דה-ויטו ב'החבר'ה הטובים' וזכה באוסקר לשחקן המשנה?",
                        "options": ["ג'ו פשי", "רוברט דה נירו", "ריי ליוטה", "פול סורבינו"],
                        "correct": 0,
                        "explanation": "ג'ו פשי זכה באוסקר לשחקן המשנה על הופעתו המחשמלת והבלתי-נשכחת כטומי דה-ויטו."
                    },
                    {
                        "q": "היכן צולמו מרבית סצנות הרחוב והאולפן של הסרט 'המטריקס' בשנת 1999?",
                        "options": ["סידני, אוסטרליה", "טורונטו, קנדה", "שיקגו, ארה״ב", "לונדון, בריטניה"],
                        "correct": 0,
                        "explanation": "האחיות וצ'אוסקי בחרו לצלם את הסרט באולפני פוקס וברחובות סידני באוסטרליה כדי לחסוך בעלויות ההפקה."
                    },
                    {
                        "q": "באמצעות איזה כלי גיאולוגי חופר אנדי דופריין את מנהרת המילוט שלו במשך כמעט 20 שנה ב'חומות של תקווה'?",
                        "options": ["פטיש סלעים קטן", "יתד רכבת חלודה", "מגרד שיניים מפלדה", "אולר כיס מפליז"],
                        "correct": 0,
                        "explanation": "אנדי רוכש מ'רד' פטיש סלעים קטן במסווה של גילוף כלי שחמט מאבן, ומשתמש בו בסתר לחפירת מנהרת המילוט."
                    },
                    {
                        "q": "איזה פסטיבל קולנוע יוקרתי העניק לסרטו של קוונטין טרנטינו 'ספרות זולה' את פרס 'דקל הזהב' בשנת 1994?",
                        "options": ["פסטיבל קאן", "פסטיבל ונציה", "פסטיבל ברלין", "פסטיבל סאנדנס"],
                        "correct": 0,
                        "explanation": "'ספרות זולה' זכה להצלחה עולמית מסחררת לאחר שזכה בפרס 'דקל הזהב' (Palme d'Or) בפסטיבל קאן בשנת 1994."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 2: 2000s Modern Epics & Prestige Cinema (2000–2009)
            # =================================================================
            {
                "id": "modern_epics_2000s",
                "title": "שוברי קופות ויצירות מופת של שנות ה-2000 (2000–2009)",
                "description": "תור הזהב של הריאליזם המחוספס, האפוסים ההיסטוריים ויצירות המופת ששברו את גבולות הז'אנר.",
                "cards": [
                    {
                        "title": "האביר האפל (The Dark Knight, 2008)",
                        "points": [
                            "ציון IMDb: 9.0/10 | בימוי: כריסטופר נולאן | תסריט: כריסטופר וג'ונתן נולאן.",
                            "שחקנים ודמויות: כריסטיאן בייל בתור ברוס ויין / באטמן, הית' לדג'ר בתור הג'וקר, אהרון אקהרט בתור הארווי דנט / דו-פרצוף, וגרי אולדמן בתור ג'ים גורדון.",
                            "עלילה ותמות: מותחן פשע פסיכולוגי אפל במסווה של סרט גיבורי-על, הבוחן אנרכיה, מעקבים המוניים, פשרות מוסריות והסלמה של אלימות.",
                            "אתרי צילום: שיקגו (ששימשה כעיר גות'אם), לונדון והונג קונג.",
                            "הישג קולנועי: הסרט ההוליוודי הגדול הראשון שצילם סצנות אקשן מרכזיות במצלמות IMAX 70mm מקוריות; הית' לדג'ר זכה באוסקר לאחר מותו על תפקיד הג'וקר."
                        ]
                    },
                    {
                        "title": "שר הטבעות: שיבת המלך (The Return of the King, 2003)",
                        "points": [
                            "ציון IMDb: 9.0/10 | בימוי: פיטר ג'קסון | עיבוד לספרי הפנטזיה המיתולוגיים של ג'.ר.ר. טולקין.",
                            "שחקנים ודמויות: אלייז'ה ווד (פרודו), ויגו מורטנסן (אראגורן), איאן מקלן (גנדלף) ואנדי סירקיס (גולום / סמיאגול).",
                            "עלילה ותמות: הקרב המכריע על הארץ התיכונה במינאס טירית, לצד מסעם הגורלי של פרודו וסאם אל לב הר הגזירה להשמדת הטבעת האחת.",
                            "אתר צילום: נופיה הפראיים והמרהיבים של ניו זילנד.",
                            "סוויפ היסטורי באוסקר: זכה בכל 11 פרסי האוסקר להם היה מועמד (100% הצלחה), והשווה את שיא הזכיות של 'בן חור' ו'טיטאניק'."
                        ]
                    },
                    {
                        "title": "גלדיאטור (Gladiator, 2000)",
                        "points": [
                            "ציון IMDb: 8.5/10 | בימוי: רידלי סקוט | זוכה 5 פרסי אוסקר כולל הסרט הטוב ביותר.",
                            "שחקנים ודמויות: ראסל קרואו בתור הגנרל מקסימוס דסימוס מרידיוס וחואקין פיניקס בתור הקיסר המושחת קומודוס.",
                            "עלילה ותמות: גנרל רומי נבגד מופשט מתוארו, נמכר לעבדות כגלדיאטור, ומפלס את דרכו בזירה אל הקולוסיאום ברומא כדי לנקום את רצח משפחתו.",
                            "אתרי צילום: יער בורן ווד באנגליה (קרב הפתיחה), ווארזאזאת במרוקו, ומבצר ריקאסולי במלטה (שחזור הקולוסיאום).",
                            "טריוויה: ראסל קרואו ביצע בעצמו רבות מסצנות הפעלולים וספג פציעות רבות, כולל שברים ואיבוד תחושה ברגליים מקרבות החרבות."
                        ]
                    },
                    {
                        "title": "ארץ קשוחה (No Country for Old Men, 2007)",
                        "points": [
                            "ציון IMDb: 8.2/10 | תסריט ובימוי: האחים ג'ואל ואיתן כהן | עיבוד לספרו של קורמאק מקארתי.",
                            "שחקנים ודמויות: חאווייר ברדם בתור המתנקש האכזרי אנטון שיגור, ג'וש ברולין בתור לואלין מוס, וטומי לי ג'ונס בתור השריף אד טום בל.",
                            "עלילה ותמות: צייד נתקל בזירת עסקת סמים שהשתבשה בלב המדבר ולוקח תיק עם 2 מיליון דולר, מה שמצית מצוד חסר רחמים העוסק בגורל ואלימות שרירותית.",
                            "אתרי צילום: מרפה בטקסס ואזור לאס וגאס / סנטה פה בניו מקסיקו.",
                            "עיצוב קול: כולל כמעט אפס מוזיקת רקע (פסקול מולחן), ומייצר מתח מצמרר המתבסס על רחשי רוח, צעדים ואפקטי סאונד טבעיים."
                        ]
                    },
                    {
                        "title": "השתולים (The Departed, 2006)",
                        "points": [
                            "ציון IMDb: 8.5/10 | בימוי: מרטין סקורסזה | עיבוד מחודש למותחן מהונג קונג 'האינפרנל אפיירס' | זכה ב-4 פרסי אוסקר כולל אוסקר ראשון לסקורסזה כבמאי.",
                            "שחקנים ודמויות: לאונרדו דיקפריו (השוטר הסמוי בילי קוסטיגן), מאט דיימון (חפרפרת המאפיה במשטרה קולין סאליבן) וג'ק ניקולסון (ראש המאפיה פרנק קוסטלו).",
                            "עלילה ותמות: בבוסטון, משטרת המדינה והמאפיה האירית מגלות בו-זמנית שיש חפרפרת בשורותיהן, ומתחיל מרוץ פרנואידי לחשיפת הזהויות.",
                            "מוטיב חזותי: סקורסזה שתל סימני 'X' נסתרים ברקע לפני מותו של כמעט כל גיבור בסרט כמחווה לסרט 'פני צלקת' מ-1932.",
                            "אתרי צילום: צולם בעיקר בבוסטון, מסצ'וסטס ובאולפנים בניו יורק."
                        ]
                    },
                    {
                        "title": "ממזרים חסרי כבוד (Inglourious Basterds, 2009)",
                        "points": [
                            "ציון IMDb: 8.4/10 | תסריט ובימוי: קוונטין טרנטינו.",
                            "שחקנים ודמויות: כריסטוף ואלץ בתור קולונל האס-אס הנס לנדה ('צייד היהודים'), בראד פיט בתור לוטננט אלדו ריין, ומלאני לורן בתור שושנה דרייפוס.",
                            "עלילה ותמות: דרמת מלחמת עולם שנייה בהיסטוריה חלופית המגיעה לשיאה במבצע התנקשות נועז בצמרת השלטון הנאצי בתוך בית קולנוע בפריז.",
                            "הישג לשוני: מתנהל בארבע שפות (אנגלית, גרמנית, צרפתית ואיטלקית); כריסטוף ואלץ הדהים את העולם במשחקו הרב-לשוני וזכה באוסקר.",
                            "אתרי צילום: צולם באולפני בבלסברג מחוץ לברלין ובחבל סקסוניה בגרמניה."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "איזה שחקן זכה בפרס אוסקר לשחקן המשנה לאחר מותו על גילום דמותו של הג'וקר ב'האביר האפל' (2008)?",
                        "options": ["הית' לדג'ר", "חואקין פיניקס", "ג'ק ניקולסון", "ג'ארד לטו"],
                        "correct": 0,
                        "explanation": "הופעתו המהפנטת והטוטאלית של הית' לדג'ר כג'וקר זיכתה אותו בפרס אוסקר לאחר מותו, ונחשבת לאחת מפסגות המשחק בקולנוע."
                    },
                    {
                        "q": "כמה פרסי אוסקר גרף הסרט 'שר הטבעות: שיבת המלך' בשנת 2004, כשהוא מנצח בכל הקטגוריות להן היה מועמד?",
                        "options": ["11 פרסי אוסקר", "9 פרסי אוסקר", "13 פרסי אוסקר", "7 פרסי אוסקר"],
                        "correct": 0,
                        "explanation": "'שיבת המלך' היה מועמד ל-11 פרסי אוסקר וזכה בכולם (11 מתוך 11), כולל הסרט הטוב ביותר והבמאי לפיטר ג'קסון."
                    },
                    {
                        "q": "באיזה נשק ייחודי משתמש המתנקש הפסיכופת אנטון שיגור כדי לחסל קורבנות ולפרוץ מנעולים בסרט 'ארץ קשוחה'?",
                        "options": ["אקדח הלם פנאומטי עם מכל אוויר דחוס לבקר", "קשת מושתקת עם חיצים מורעלים", "חבל תיל טיטניום מיוחד לחניקה", "רובה צלפים בעל קליבר כבד"],
                        "correct": 0,
                        "explanation": "אנטון שיגור משתמש באקדח הלם מופעל אוויר דחוס (Captive Bolt Pistol), המשמש בבתי מטבחיים להממת בקר."
                    },
                    {
                        "q": "איזה סימן חזותי סמוי שתל מרטין סקורסזה ברקע הסצנות בסרט 'השתולים' כדי לרמוז על מותן הקרב של הדמויות?",
                        "options": ["האות 'X'", "שעון קיר שבור", "ורד אדום נבול", "כוס קפה נשפכת"],
                        "correct": 0,
                        "explanation": "סקורסזה שתל סימוני X ברקע המשקופים, החלונות והקירות מאחורי דמויות רגע לפני מותן, כמחווה לסרט 'פני צלקת' משנת 1932."
                    },
                    {
                        "q": "איזה שחקן אוסטרי גילם את קולונל האס-אס הנס לנדה ב'ממזרים חסרי כבוד' וזכה באוסקר ובפרס פסטיבל קאן?",
                        "options": ["כריסטוף ואלץ", "דניאל בריהל", "מייקל פסבנדר", "טיל שווייגר"],
                        "correct": 0,
                        "explanation": "כריסטוף ואלץ כבש את הקולנוע העולמי וזכה באוסקר הראשון שלו על תפקידו הבלתי-נשכח כהנס לנדה."
                    },
                    {
                        "q": "בסרט 'גלדיאטור' של רידלי סקוט, מה היה מחוז הולדתו של הגנרל מקסימוס באימפריה הרומית?",
                        "options": ["היספניה (ספרד)", "גאליה (צרפת)", "גרמאניה (גרמניה)", "בריטניה"],
                        "correct": 0,
                        "explanation": "מקסימוס מכונה בזירות הגלדיאטורים 'הספרדי' (The Spaniard) מכיוון שאחוזתו ומשפחתו שכנו בהיספניה (ספרד המודרנית)."
                    },
                    {
                        "q": "מה מאפיין באופן יוצא דופן את עיצוב הפסקול של הסרט זוכה האוסקר 'ארץ קשוחה' של האחים כהן?",
                        "options": ["הסרט כמעט ואינו מכיל מוזיקת רקע מולחנת", "הפסקול מורכב כולו משירת מקהלה א-קפלה", "נעשה שימוש בלעדי בלהיטי רוק משנות ה-50", "הפסקול הוקלט כולו בהשמעה לאחור"],
                        "correct": 0,
                        "explanation": "הסרט מתאפיין בהיעדר כמעט מוחלט של מוזיקה מולחנת, מה שמייצר מתח עז המבוסס על צלילי סביבה טבעיים."
                    },
                    {
                        "q": "איזו עיר אמריקאית מרכזית שימשה כאתר הצילומים העיקרי לעיר גות'אם בסרט 'האביר האפל' (2008)?",
                        "options": ["שיקגו", "ניו יורק", "פילדלפיה", "פיטסבורג"],
                        "correct": 0,
                        "explanation": "כריסטופר נולאן צילם את מרבית הסצנות האייקוניות של גות'אם ברחבי גורדי השחקים והכבישים התחתיים של שיקגו, אילינוי."
                    },
                    {
                        "q": "איזה מותחן פעולה אסייתי שימש כבסיס וכהשראה ישירה לסרטו של מרטין סקורסזה 'השתולים'?",
                        "options": ["האינפרנל אפיירס (Infernal Affairs, הונג קונג)", "שבעה צעדים / אולדבוי (Oldboy, דרום קוריאה)", "חיים מתוקים (A Bittersweet Life, דרום קוריאה)", "התנגשות חזיתית (Hard Boiled, הונג קונג)"],
                        "correct": 0,
                        "explanation": "'השתולים' הוא עיבוד אמריקאי למותחן המופת ההונג-קונגי משנת 2002 'Infernal Affairs' (האינפרנל אפיירס)."
                    },
                    {
                        "q": "איזו מדינה העניקה את נופי הפרא המרהיבים לצילומי טרילוגיית 'שר הטבעות' של פיטר ג'קסון?",
                        "options": ["ניו זילנד", "סקוטלנד", "נורווגיה", "איסלנד"],
                        "correct": 0,
                        "explanation": "פיטר ג'קסון צילם את כל שלושת סרטי 'שר הטבעות' ברחבי הפארקים הלאומיים וההרים של מולדתו ניו זילנד."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 3: 2010s Mind-Benders & Auteur Masterpieces (2010–2019)
            # =================================================================
            {
                "id": "mindbenders_2010s",
                "title": "פאזלים מנטליים ויצירות מופת של העשור (2010–2019)",
                "description": "מותחנים פסיכולוגיים מורכבים, אקשן מעשי מסמר שיער ודרמות אישיות בעוצמה גבוהה.",
                "cards": [
                    {
                        "title": "התחלה (Inception, 2010)",
                        "points": [
                            "ציון IMDb: 8.8/10 | תסריט ובימוי: כריסטופר נולאן | זוכה 4 פרסי אוסקר.",
                            "שחקנים ודמויות: לאונרדו דיקפריו (דום קוב), ג'וזף גורדון-לוויט (ארתור), אליוט פייג' (אריאדנה), טום הארדי (אימס) ומריון קוטיאר (מאל).",
                            "עלילה ותמות: גנב מחשבות החודר לתת-המודע של מטרות במהלך שנת חלום נשכר לשתול רעיון ('אינספשן') במוחו של יורש תאגיד ענק על פני ארבע שכבות חלום מקבילות.",
                            "פלא הנדסי: נולאן בנה מתקן מסתובב 360 מעלות באורך עשרות מטרים בתוך האנגר ספינות אוויר בקרדינגטון לצילום קרב חוסר-המשקל במסדרון המלון.",
                            "סיום פתוח: השוט האחרון נחתך לשחור כשהסביבון של קוב מתנדנד מעט, ומותיר את הצופים בוויכוח האם הוא אכן התעורר למציאות עם ילדיו."
                        ]
                    },
                    {
                        "title": "בין כוכבים (Interstellar, 2014)",
                        "points": [
                            "ציון IMDb: 8.7/10 | בימוי: כריסטופר נולאן | פסקול מקורי בלתי-נשכח מאת הנס זימר.",
                            "שחקנים ודמויות: מת'יו מקונוהיי בתור קופר, אן האת'וויי בתור ד״ר ברנד, ג'סיקה צ'סטיין בתור מרף הבוגרת ומייקל קיין בתור פרופסור ברנד.",
                            "עלילה ותמות: כשהביוספרה של כדור הארץ קורסת, אסטרונאוטים יוצאים דרך חור תולעת סמוך לשבתאי לחפש עולמות חלופיים, תוך התמודדות עם עיוותי זמן כבידתיים וממדים גבוהים.",
                            "דיוק מדעי: הפיזיקאי חתן פרס נובל קיפ תורן שימש כיועץ מדעי, ויצר את המודל הממוחשב הראשון המדויק פיזיקלית של חור שחור סופר-מאסיבי ('גרגנטואה').",
                            "אתרי צילום: קרחון סווינאפלסיוקול באיסלנד (עולמות המים והקרח) ושדות תירס ענקיים באלברטה, קנדה."
                        ]
                    },
                    {
                        "title": "הזאב מוול סטריט (The Wolf of Wall Street, 2013)",
                        "points": [
                            "ציון IMDb: 8.2/10 | בימוי: מרטין סקורסזה | מבוסס על ספרו האוטוביוגרפי של ג'ורדן בלפורט.",
                            "שחקנים ודמויות: לאונרדו דיקפריו בתור ג'ורדן בלפורט, ג'ונה היל בתור דוני אזוף, ומרגו רובי בתפקיד הפריצה הגדול שלה כנעמי לאפליה.",
                            "עלילה ותמות: קומדיית פשע פרועה החושפת את הונאות המניות, תאוות הבצע חסרת המעצורים וחיי הנהנתנות הפרועים בוול סטריט של שנות ה-90.",
                            "טכניקה קולנועית: דיקפריו שובר שוב ושוב את 'הקיר הרביעי' ופונה ישירות אל הצופים להסברת מנגנוני המסחר.",
                            "טריוויה: מחזיק בשיא השימוש בקללות בסרט קולנוע מרכזי (מעל 500 פעמים המילה F-word)."
                        ]
                    },
                    {
                        "title": "וויפלאש (Whiplash, 2014)",
                        "points": [
                            "ציון IMDb: 8.5/10 | תסריט ובימוי: דמיאן שאזל | זוכה 3 פרסי אוסקר.",
                            "שחקנים ודמויות: מיילס טלר בתור מתופף הג'אז השאפתן אנדרו ניימן, וג'יי. קיי. סימונס בתור המנצח הרודן והמתעלל טרנס פלצ'ר.",
                            "עלילה ותמות: בקונסרבטוריון שייפר היוקרתי בניו יורק, הסרט בוחן האם התעללות פסיכולוגית קיצונית נחוצה כדי להוליד גאונות אמנותית.",
                            "הפקה מזורזת: צולם ב-19 ימים בלבד בלוס אנג'לס בתקציב צנוע של 3.3 מיליון דולר בלבד.",
                            "ביצוע פיזי: מיילס טלר, המתופף מגיל 15, ניגן בעצמו ברבות מהסצנות וסבל מיבלות ומדימום ממשי של כפות ידיו ממהירות התיפוף."
                        ]
                    },
                    {
                        "title": "מקס הזועם: כביש הזעם (Mad Max: Fury Road, 2015)",
                        "points": [
                            "ציון IMDb: 8.1/10 | בימוי וכתיבה: ג'ורג' מילר | זוכה 6 פרסי אוסקר.",
                            "שחקנים ודמויות: טום הארדי בתור מקס רוקטנסקי, שרליז ת'רון בתור אימפרטור פיוריוסה, וניקולס הולט בתור נאקס.",
                            "עלילה ותמות: מרדף מדברי עוצר נשימה בעולם פוסט-אפוקליפטי שבו פיוריוסה מורדת בעריץ אימורטן ג'ו כדי להציל את נשותיו המשועבדות.",
                            "פעלולים מעשיים: מעל 80% מהפעלולים וההתנגשויות בסרט בוצעו באופן מעשי בשטח במדבריות נמיביה ללא CGI.",
                            "שינוי אתר צילום: ההפקה נאלצה לעבור מאוסטרליה לנמיביה לאחר שגשמים נדירים גרמו למדבר האוסטרלי לפרוח בשטיחי פרחים ירוקים."
                        ]
                    },
                    {
                        "title": "פרזיטים (Parasite, 2019)",
                        "points": [
                            "ציון IMDb: 8.5/10 | בימוי: בונג ג'ון-הו | תסריט משותף עם האן ג'ין-וון.",
                            "שחקנים ודמויות: סונג קאנג-הו (קים קי-טק), צ'וי וו-שיק (קי-וו), פארק סו-דאם (קי-ג'ונג) וצ'ו יו-ג'ונג (גברת פארק).",
                            "עלילה ותמות: משפחה חסרת אמצעים חודרת בערמומיות לבית משפחה עשירה במסווה של אנשי מקצוע בלתי תלויים, ומגלה סודות תת-קרקעיים המציפים את פערי המעמדות.",
                            "הישג היסטורי באוסקר: הסרט הראשון בשפה שאינה אנגלית ב-92 שנות האוסקר שזכה בפרס הסרט הטוב ביותר, לצד פרסי הבמאי, התסריט והסרט הבינלאומי.",
                            "אדריכלות: אחוזת הפאר של משפחת פארק לא הייתה בית קיים, אלא תפאורה רב-מפלסית מורכבת שנבנתה בשטח פתוח בעיר ג'ונג'ו."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "איזה מתקן מכני ענק בנה כריסטופר נולאן לצורך צילום סצנת קרב חוסר-המשקל של ג'וזף גורדון-לוויט ב'התחלה' (Inception)?",
                        "options": ["מסדרון מלון מסתובב 360 מעלות שנבנה בתוך האנגר ספינות אוויר", "מכל מים תת-קרקעי ענק לצילום בצלילה חופשית", "מטוס בואינג ייעודי בטיסה פרבולית המדמה אפס כבידה", "מנוף רתמות דיגיטלי ממונע"],
                        "correct": 0,
                        "explanation": "נולאן וצוות האפקטים בנו מסדרון פלדה עגול באורך כ-30 מטרים שהסתובב סביב צירו בהאנגר בקרדינגטון."
                    },
                    {
                        "q": "איזה פיזיקאי תיאורטי חתן פרס נובל שימש כיועץ המדעי הראשי של כריסטופר נולאן בסרט 'בין כוכבים'?",
                        "options": ["קיפ תורן", "סטיבן הוקינג", "ניל דה-גראס טייסון", "רוג'ר פנרוז"],
                        "correct": 0,
                        "explanation": "הפיזיקאי קיפ תורן מ-Caltech סיפק את משוואות תורת היחסות הכללית ששימשו לעיבוד החזותי של החור השחור 'גרגנטואה'."
                    },
                    {
                        "q": "איזה שחקן זכה באוסקר לשחקן המשנה על גילום מורה המוזיקה הרודן טרנס פלצ'ר בסרט 'וויפלאש' (2014)?",
                        "options": ["ג'יי. קיי. סימונס", "אדוארד נורטון", "מארק ראפלו", "אית'ן הוק"],
                        "correct": 0,
                        "explanation": "ג'יי. קיי. סימונס גרף את כל הפרסים המרכזיים של עונת הפרסים כולל האוסקר וגלובוס הזהב על הופעתו המצמררת."
                    },
                    {
                        "q": "מדוע הועברו צילומי הסרט 'מקס הזועם: כביש הזעם' מאוסטרליה למדבריות נמיביה?",
                        "options": ["גשמים חריגים גרמו למדבר האוסטרלי לפרוח בשטיחי פרחים ירוקים", "איגודי התחבורה באוסטרליה חסמו את שיירות כלי הרכב הכבדים", "גלי חום קיצוניים פגעו בחיישני המצלמות הדיגיטליות", "אישורי הצילום בוטלו על ידי הרשויות המקומיות"],
                        "correct": 0,
                        "explanation": "גשמים כבדים וחסרי תקדים הפכו את המדבר האדום של ברוקן היל לשדה ירוק ופורח, מה שחייב את העברת ההפקה לנמיביה."
                    },
                    {
                        "q": "איזה הישג חסר תקדים רשם סרטו של בונג ג'ון-הו 'פרזיטים' בטקס האוסקר ה-92 בשנת 2020?",
                        "options": ["הסרט הראשון בשפה שאינה אנגלית שזכה בפרס הסרט הטוב ביותר", "הסרט הראשון שזכה בכל ארבע קטגוריות המשחק", "הסרט הראשון שצולם כולו בסמארטפון וזכה באוסקר", "סרט האנימציה הראשון שהיה מועמד לפרס הסרט הטוב ביותר"],
                        "correct": 0,
                        "explanation": "'פרזיטים' עשה היסטוריה עולמית כאשר הפך לסרט הזר הראשון אי פעם שזכה בפרס הסרט הטוב ביותר באוסקר."
                    },
                    {
                        "q": "בסרט 'התחלה', באיזה חפץ אישי (טוטם) משתמש דום קוב כדי לוודא האם הוא נמצא במציאות או בתוך חלום?",
                        "options": ["סביבון מתכת קטן", "קוביית משחק עמוסה", "רץ שחמט חלול", "ז'יטון פוקר עם גילוף של גולגולת"],
                        "correct": 0,
                        "explanation": "קוב משתמש בסביבון קטן שהיה שייך לאשתו מאל; בתוך חלום הסביבון מסתובב לנצח ואינו נופל לעולם."
                    },
                    {
                        "q": "בכוכב המים של מילר בסרט 'בין כוכבים', שעה אחת על פני הכוכב שוות ערך לכמה שנים בכדור הארץ?",
                        "options": ["7 שנים בכדור הארץ", "שנה אחת בכדור הארץ", "25 שנים בכדור הארץ", "50 שנים בכדור הארץ"],
                        "correct": 0,
                        "explanation": "עקב הקרבה לחור השחור הסופר-מאסיבי גרגנטואה והכבידה העצומה שלו, שעה אחת על פני הכוכב שווה לשבע שנות ארץ."
                    },
                    {
                        "q": "איזו שחקנית רשמה את תפקיד הפריצה ההוליוודי הענק שלה מול לאונרדו דיקפריו ב'הזאב מוול סטריט' (2013)?",
                        "options": ["מרגו רובי", "אמה סטון", "פלורנס פיו", "אנה דה ארמס"],
                        "correct": 0,
                        "explanation": "השחקנית האוסטרלית מרגו רובי פרצה לצמרת הקולנוע העולמי בתפקידה המחשמל כנעמי לאפליה."
                    },
                    {
                        "q": "איזה שיר ג'אז מורכב במשקל 7/4 דורש פלצ'ר מאנדרו לנגן עד זוב דם בסרט 'וויפלאש'?",
                        "options": ["'וויפלאש' (Whiplash) של האנק לוי", "'קרוואן' (Caravan)", "'Take Five'", "'Giant Steps'"],
                        "correct": 0,
                        "explanation": "הקטע 'וויפלאש' של האנק לוי (במקצב 7/4 הייחודי) הוא יצירת המפתח שעליה מתאמן אנדרו בייסורים."
                    },
                    {
                        "q": "מי גילמה את הלוחמת קטועת הזרוע אימפרטור פיוריוסה בסרטו של ג'ורג' מילר 'מקס הזועם: כביש הזעם'?",
                        "options": ["שרליז ת'רון", "אמילי בלאנט", "סיגורני ויבר", "סקרלט ג'והנסון"],
                        "correct": 0,
                        "explanation": "שרליז ת'רון הציגה הופעה מיתולוגית ובלתי-נשכחת כאימפרטור פיוריוסה."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 4: 2020s Modern Epics, Sci-Fi & New Visions (2020–Present)
            # =================================================================
            {
                "id": "modern_visions_2020s",
                "title": "עידן המופת החדש, מדע בדיוני וחזונות מודרניים (2020 ועד היום)",
                "description": "הזינוקים הטכנולוגיים של קולנוע 70 מ״מ IMAX, אפוסים פילוסופיים והצלחות רב-ז'אנריות.",
                "cards": [
                    {
                        "title": "אופנהיימר (Oppenheimer, 2023)",
                        "points": [
                            "ציון IMDb: 8.9/10 | תסריט ובימוי: כריסטופר נולאן | זוכה 7 פרסי אוסקר כולל הסרט הטוב ביותר והבמאי.",
                            "שחקנים ודמויות: קיליאן מרפי בתור ג'יי. רוברט אופנהיימר, רוברט דאוני ג'וניור בתור לואיס שטראוס, ואמילי בלאנט בתור קיטי אופנהיימר.",
                            "עלילה ותמות: האפוס הביוגרפי על הפיזיקאי התיאורטי שהוביל את פרויקט מנהטן לפיתוח פצצת האטום, ועל רדיפתו הפוליטית והייסורים המוסריים בעקבותיה.",
                            "חידוש קולנועי: נולאן שכנע את חברת קודאק לייצר לראשונה בהיסטוריה סרט צילום שחור-לבן בפורמט ענק 65 מ״מ כדי לצלם את סצנות השימוע של שטראוס ב-IMAX.",
                            "פיצוץ מעשי: ניסוי טריניטי שוחזר ללא שימוש ב-CGI ממוחשב, באמצעות שילוב חומרי בעירה, אלומיניום, אבק שריפה ובנזין."
                        ]
                    },
                    {
                        "title": "חולית: חלק 2 (Dune: Part Two, 2024)",
                        "points": [
                            "ציון IMDb: 8.6/10 | בימוי וכתיבה: דני וילנב | עיבוד לספרו המכונן של פרנק הרברט.",
                            "שחקנים ודמויות: טימותי שאלאמה (פול אטריידיס), זנדאיה (צ'אני), אוסטין באטלר (פייד-ראותה הארקונן) ורבקה פרגוסון (ליידי ג'סיקה).",
                            "עלילה ותמות: פול מתאחד עם שבטי הדררים למלחמת חורמה בבית הארקונן ובקיסר על כוכב המדבר אראקיס, תוך התמודדות עם סכנות המשיחיות והטוטליטריזם.",
                            "צילום וקול: גריג פרייז'ר צילם את זירת הקרב המונוכרומטית של ג'יידי פריים במצלמות אינפרא-אדום מיוחדות; הנס זימר הלחין פסקול עתידני ועוצמתי.",
                            "אתרי צילום: צולם במדבר ואדי רם בירדן, בנווה המדבר ליווה באבו דאבי, באולפנים בבודפשט ובאתר הקבר בריון באיטליה."
                        ]
                    },
                    {
                        "title": "הכול בכל מקום בבת אחת (Everything Everywhere All at Once, 2022)",
                        "points": [
                            "ציון IMDb: 7.8/10 | תסריט ובימוי: הצמד דניאלס (דניאל קוואן ודניאל שיינרט) | זוכה 7 פרסי אוסקר כולל הסרט הטוב ביותר.",
                            "שחקנים ודמויות: מישל יאו (אוולין וואנג), קי הוי קוואן (וויימונד וואנג), סטפני הסו (ג'וי וואנג / ג'ובו טופאקי) וג'יימי לי קרטיס (דירדרה).",
                            "עלילה ותמות: בעלת מכבסה ממוצא סיני הנמצאת תחת ביקורת מס מגלה שעליה להתחבר לגרסאותיה ביקומים מקבילים כדי להציל את המולטיוורס מניהיליזם קוסמי בעזרת טוב לב וחמלה.",
                            "הישג אינדי ענק: הופק בתקציב עצמאי של כ-14–25 מיליון דולר בלבד עם צוות אפקטים ביתי של 5 אנשים, והפך לסרט הרווחי ביותר בתולדות חברת A24.",
                            "קאמבק מרגש: קי הוי קוואן זכה באוסקר לשחקן משנה לאחר היעדרות של כמעט שלושה עשורים מתפקידי משחק בהוליווד."
                        ]
                    },
                    {
                        "title": "בלייד ראנר 2049 (Blade Runner 2049, 2017)",
                        "points": [
                            "ציון IMDb: 8.0/10 | בימוי: דני וילנב | הפקה: רידלי סקוט | זוכה 2 פרסי אוסקר.",
                            "שחקנים ודמויות: ראיין גוסלינג בתור K (בלייד ראנר רפליקנט), האריסון פורד השב לתפקידו כריק דקארד, ואנה דה ארמס בתור ג'וי.",
                            "עלילה ותמות: בלש משטרתי חושף סוד עמוק המאיים למוטט את יסודות החברה וההפרדה בין אדם למכונה, תוך עיסוק בזיכרון, נשמה וכמיהה לקשר אמיתי.",
                            "מאסטרפיס חזותי: הצלם האגדי רוג'ר דיקינס זכה באוסקר הראשון שלו על עיצוב התאורה וסופות האבק הכתומות המהפנטות.",
                            "אתר צילום: נבנה על פני במות ענק באולפני קורדה ואוריגו בבודפשט, הונגריה."
                        ]
                    },
                    {
                        "title": "ג'ון וויק 4 (John Wick: Chapter 4, 2023)",
                        "points": [
                            "ציון IMDb: 7.7/10 | בימוי: צ'אד סטהלסקי | בכיכובם של קיאנו ריבס, דוני ין וביל סקארסגארד.",
                            "עלילה ותמות: המתנקש האגדי נלחם נגד 'השולחן הגבוה' ברחבי העולם כדי להשיג את חירותו, בכוריאוגרפיית קרבות ואקשן עוצרת נשימה ('Gun-Fu').",
                            "סצנת אקשן מיתולוגית: כולל שוט עילי רציף ומרהיב מלמעלה (Top-Down) מתוך דירה בפריז שבה יורה וויק כדורי רובה-ציד בוערים ('Dragon's Breath').",
                            "אתרי צילום: צולם באייקונים מפורסמים בפריז (הלובר, שער הניצחון, 222 המדרגות של בזיליקת הלב הקדוש), ברלין ואוסקה."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "איזה סרט צילום ייחודי פותח על ידי חברת קודאק במיוחד עבור הסרט 'אופנהיימר' של כריסטופר נולאן?",
                        "options": ["סרט צילום שחור-לבן בפורמט ענק 65 מ״מ ל-IMAX", "סרט אינפרא-אדום לצילומי לילה בפורמט 35 מ״מ", "סרט צבעוני 70 מ״מ בקצב של 120 פריימים לשנייה", "סרט סטריאוסקופי תלת-ממדי כפול"],
                        "correct": 0,
                        "explanation": "קודאק פיתחה לראשונה בהיסטוריה סרט שחור-לבן בפורמט 65 מ״מ כדי לאפשר לנולאן ולצלם הויטה ואן הויטמה לצלם את נקודת המבט של שטראוס ב-IMAX מלא."
                    },
                    {
                        "q": "כיצד השיג הצלם גריג פרייז'ר את המראה המונוכרומטי המצמרר של זירת הקרב של הארקונן ב'חולית: חלק 2'?",
                        "options": ["צילום במצלמות דיגיטליות שהוסבו לקליטת אור אינפרא-אדום בלבד", "שימוש בסרטי צילום אורתוכרומטיים משנות ה-20", "החלפת צבע דיגיטלית בפוסט-פרודקשן", "ריסוס האצטדיון כולו בגיר שחור ופילטרים מקטבים"],
                        "correct": 0,
                        "explanation": "פרייז'ר השתמש במצלמות דיגיטליות שהותאמו לקליטת ספקטרום אינפרא-אדום בלבד, מה שהעניק לעור השחקנים מראה שקוף ולבגדים ניגודיות חריגה."
                    },
                    {
                        "q": "איזה שחקן חזר להוליווד לאחר היעדרות של כמעט 30 שנה וזכה באוסקר על 'הכול בכל מקום בבת אחת'?",
                        "options": ["קי הוי קוואן", "סטיבן יאן", "בי.די וונג", "הירויוקי סנאדה"],
                        "correct": 0,
                        "explanation": "קי הוי קוואן (שכיכב כילד ב'אינדיאנה ג'ונס ומקדש הארור') זכה באוסקר לשחקן המשנה על גילום וויימונד וואנג."
                    },
                    {
                        "q": "איזה צלם קולנוע אגדי זכה באוסקר הראשון שלו על יצירת המופת הוויזואלית 'בלייד ראנר 2049' של דני וילנב?",
                        "options": ["רוג'ר דיקינס", "עמנואל לובצקי", "הויטה ואן הויטמה", "רוברט ריצ'רדסון"],
                        "correct": 0,
                        "explanation": "לאחר 13 מועמדויות לאורך הקריירה ללא זכייה, רוג'ר דיקינס זכה באוסקר לצילום הטוב ביותר על עבודתו ב'בלייד ראנר 2049'."
                    },
                    {
                        "q": "איזה גרם מדרגות מפורסם בפריז משמש כזירת קרב שבה ג'ון וויק נלחם במעלה 222 מדרגות ב'ג'ון וויק 4'?",
                        "options": ["המדרגות המובילות לבזיליקת הלב הקדוש (סקרה קר) במונמארטר", "מדרגות בסיס מגדל אייפל", "מדרגות בית האופרה גרנייה", "מדרגות הכניסה של הגראן פאלה"],
                        "correct": 0,
                        "explanation": "ג'ון וויק מפלס את דרכו (ומתגלגל כל הדרך למטה בחזרה) בגרם המדרגות המפורסם ברחוב פואטייה במונמארטר המוביל לבזיליקת הסקרה קר."
                    },
                    {
                        "q": "איזה שחקן גילם את לואיס שטראוס, יושב ראש הוועדה לאנרגיה אטומית, בסרט 'אופנהיימר' וזכה באוסקר לשחקן המשנה?",
                        "options": ["רוברט דאוני ג'וניור", "מאט דיימון", "קנת בראנה", "ג'וש הארטנט"],
                        "correct": 0,
                        "explanation": "רוברט דאוני ג'וניור זכה בפרס האוסקר הראשון בקריירה שלו על הופעתו המבריקה והמאופקת כיו״ר הוועדה לואיס שטראוס."
                    },
                    {
                        "q": "איזה עמק מדברי מפורסם בירדן שימש כאתר הצילומים המרכזי של כוכב הלכת אראקיס בסרטי 'חולית'?",
                        "options": ["ואדי רם", "עמק המוות", "מדבר אטקמה", "דיונות סהרה במרזוגה"],
                        "correct": 0,
                        "explanation": "דני וילנב צילם את הנופים המדבריים ומצוקי אבן החול של אראקיס בואדי רם בירדן ('בקעת הירח')."
                    },
                    {
                        "q": "איזו נקודת מבט חזותית בהשראת משחקי וידאו שימשה בסצנת הירי הרציפה בדירה הפריזאית ב'ג'ון וויק 4'?",
                        "options": ["מבט-על מלמעלה (Top-down bird's-eye view)", "מבט מגוף ראשון (First-person shooter)", "מבט צדדי של משחק פלטפורמה (Side-scroller)", "מבט מגוף שלישי מעבר לכתף"],
                        "correct": 0,
                        "explanation": "הבמאי צ'אד סטהלסקי השתמש במצלמת מנוף שצילמה מעל תקרות החדרים בשוט רציף מלמעלה, בהשראת משחקי ירי כמו 'The Hong Kong Massacre'."
                    },
                    {
                        "q": "כמה פרסי אוסקר גרף הסרט 'הכול בכל מקום בבת אחת' בטקס האוסקר ה-95, כולל הסרט הטוב ביותר ו-3 פרסי משחק?",
                        "options": ["7 פרסי אוסקר", "4 פרסי אוסקר", "10 פרסי אוסקר", "12 פרסי אוסקר"],
                        "correct": 0,
                        "explanation": "הסרט גרף 7 פרסי אוסקר מרכזיים: הסרט הטוב ביותר, בימוי, שחקנית ראשית (מישל יאו), שחקן משנה (קי הוי קוואן), שחקנית משנה (ג'יימי לי קרטיס), תסריט מקורי ועריכה."
                    },
                    {
                        "q": "איזה במאי ביים הן את 'בלייד ראנר 2049' והן את שני חלקי 'חולית' (Dune Part 1 & 2)?",
                        "options": ["דני וילנב", "כריסטופר נולאן", "רידלי סקוט", "ג'ורג' מילר"],
                        "correct": 0,
                        "explanation": "הבמאי הקנדי דני וילנב חתום על שתיים מיצירות המדע הבדיוני הוויזואליות והמוערכות ביותר של המאה ה-21."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 5: Master Directors, Legendary Twists & Behind-The-Scenes Lore
            # =================================================================
            {
                "id": "directors_twists_lore",
                "title": "במאים אגדיים, טוויסטים מטורפים וסודות מאחורי הקלעים",
                "description": "האלתורים המפורסמים, סגנונות הבימוי הייחודיים והסופים המפתיעים ששינו את תולדות הקולנוע.",
                "cards": [
                    {
                        "title": "כריסטופר נולאן וקוונטין טרנטינו: חותמת הבמאים הגדולים",
                        "points": [
                            "כריסטופר נולאן: תומך נלהב בפילם 70 מ״מ, שימוש באפקטים מעשיים בלבד ללא מחשב (התרסקות מטוס בואינג אמיתי, בניית סטים מסתובבים ענקיים) ומבנים נרטיביים מורכבים ולא ליניאריים.",
                            "קוונטין טרנטינו: ידוע בדיאלוגים מושחזים ומהירים מתרבות הפופ, חלוקה לפרקים, מחוות אנציקלופדיות לקלאסיקות, פסקולים אקלקטיים וסופי היסטוריה אלטרנטיבית נועזים.",
                            "דייוויד פינצ'ר: פרפקציוניזם דיגיטלי קיצוני, הדורש לעיתים קרובות 50 עד מעל 100 טייקים לכל שוט בודד כדי לפרק את מניירות המשחק המלאכותיות של השחקנים.",
                            "מרטין סקורסזה: תנועות מצלמה קינטיות מהירות, הקפאות פריים (Freeze Frames), קריינות קולית ושותפויות עבודה ארוכות שנים עם רוברט דה נירו ולאונרדו דיקפריו."
                        ]
                    },
                    {
                        "title": "אלתורים ופציעות אמיתיות שנכנסו לקולנוע",
                        "points": [
                            "ג'אנגו ללא מעצורים (Django Unchained, 2012): לאונרדו דיקפריו הטיח בטעות את ידו בכוס זכוכית שרוסקה וחתכה את כף ידו. הוא נשאר בדמות והמשיך במונולוג המאיים כשידו שותתת דם על השולחן.",
                            "האביר האפל (The Dark Knight, 2008): מחיאות הכפיים הסרקסטיות והאיטיות של הית' לדג'ר (הג'וקר) בתא המעצר בעת קידומו של ג'ים גורדון היו אלתור מוחלט על הסט.",
                            "הזאב מוול סטריט (The Wolf of Wall Street, 2013): התיפוף הקצבי על החזה והזמזום של מת'יו מקונוהיי היה טקס החימום האישי שלו לפני צילום; דיקפריו הציע לסקורסזה להכניס זאת ישירות לסצנה.",
                            "שר הטבעות: שני הצריחים (2002): כאשר אראגורן בועט בקסדת אורוק-האי מזעם, ויגו מורטנסן שבר שתי בהונות ברגלו; זעקת הכאב האמיתית שלו נשמרה בגרסה הסופית של הסרט."
                        ]
                    },
                    {
                        "title": "הטוויסטים העלילתיים הגדולים של הקולנוע המודרני",
                        "points": [
                            "החוש השישי (The Sixth Sense, 1999): פסיכולוג הילדים מלקולם קרואו (ברוס ויליס) מגלה בסיום הסרט שהוא עצמו היה רוח רפאים לאורך כל העלילה.",
                            "יוקרה (The Prestige, 2006): הקוסם אלפרד בורדן (כריסטיאן בייל) חושף כי הוא למעשה זוג תאומים זהים החיים זהות אחת משותפת, בעוד שרוברט אנג'ייר (יו ג'קמן) שכפל והטביע את עצמו בכל לילה.",
                            "שאטר איילנד (Shutter Island, 2010): המרשל טדי דניאלס (לאונרדו דיקפריו) מגלה כי הוא בעצם אנדרו לאדיס – מטופל פסיכיאטרי מסוכן הלוקח חלק בטיפול מורכב של משחק תפקידים.",
                            "ממנטו (Memento, 2000): לאונרד שלבי (גאי פירס) מגלה שהוא מנצל במודע את איבוד הזיכרון לטווח קצר שלו כדי לייצר מסע נקמה נצחי כנגד אנשים שלא רצחו את אשתו."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "בסרט 'ג'אנגו ללא מעצורים' (2012), איזו פציעה אמיתית התרחשה במהלך המונולוג הזועם של לאונרדו דיקפריו?",
                        "options": ["דיקפריו חתך את כף ידו בכוס זכוכית שבורה והמשיך לשחק כשידו מדממת", "ג'יימי פוקס פרק את כתפו במהלך שליפת אקדח מהירה", "כריסטוף ואלץ סדק את קרסולו בנפילה מסוס", "סמואל ל. ג'קסון נכווה בידו ממוט ברזל לוהט"],
                        "correct": 0,
                        "explanation": "דיקפריו ניפץ כוס קריסטל על השולחן בלהט הרגע וחתך את כף ידו, אך המשיך את המונולוג המהפנט בלי לעצור את הטייק."
                    },
                    {
                        "q": "איזה טקס חימום אישי של מת'יו מקונוהיי שולב בסצנת המסעדה המפורסמת ב'הזאב מוול סטריט'?",
                        "options": ["תיפוף קצבי באגרוף על החזה וזמזום מונוטוני", "ביצוע שכיבות סמיכה מהירות תוך ציטוט מניות", "הקשת אצבעות במקצב ג'אז מהיר", "שתיית אספרסו כפול תוך בהייה בלתי-ממצמצת במראה"],
                        "correct": 0,
                        "explanation": "מקונוהיי נוהג לתופף על חזהו כדי להרפות את מיתרי הקול לפני צילומים; דיקפריו הבחין בכך ושכנע את סקורסזה לכלול זאת בסצנה."
                    },
                    {
                        "q": "בסרט 'יוקרה' (The Prestige, 2006), כיצד מבצע הקוסם אלפרד בורדן (כריסטיאן בייל) את קסם הטלפורטציה המושלם שלו?",
                        "options": ["הוא למעשה זוג אחים תאומים זהים החולקים חיים שלמים בזהות אחת", "הוא משתמש במכונת שכפול קוונטית שנבנתה על ידי ניקולה טסלה", "הוא מעסיק כפיל אלכוהוליסט זהה בשם ג'ראלד רוט", "הוא נעזר בדלתות מלכודת תת-קרקעיות ומערך מראות מסונכרן"],
                        "correct": 0,
                        "explanation": "אלפרד ופאלון הם אחים תאומים זהים שהקריבו את חייהם האישיים וחלקו זהות אחת כדי להוציא לפועל את האשליה המושלמת."
                    },
                    {
                        "q": "מהו הגילוי הדרמטי המרעיש בסיום הסרט 'שאטר איילנד' לגבי המרשל טדי דניאלס (לאונרדו דיקפריו)?",
                        "options": ["הוא בעצמו מטופל בבית החולים הפסיכיאטרי (אנדרו לאדיס) השרוי בהזיה", "הוא נשכר בסתר על ידי ה-FBI להתנקש במנהל המוסד", "הוא סוכן ריגול זר המנסה לגנוב נוסחאות לשליטה מוחית", "הוא חלם את כל האי בעת שהיה לכוד בסופת שלגים בבוסטון"],
                        "correct": 0,
                        "explanation": "טדי דניאלס מתגלה כאנדרו לאדיס, המטופל המסוכן ביותר באי, והחקירה כולה הייתה תרפיית משחק תפקידים מבוקרת שיזמו רופאיו."
                    },
                    {
                        "q": "איזו פציעה ספג ויגו מורטנסן כאשר בעט בקסדת הפלדה בסרט 'שר הטבעות: שני הצריחים'?",
                        "options": ["הוא שבר שתי בהונות ברגלו", "הוא נקע את קרסולו", "הוא סדק את פיקת הברך", "הוא קרע את גיד אכילס"],
                        "correct": 0,
                        "explanation": "מורטנסן בעט בקסדת הפלדה הכבדה בטייק החמישי ושבר שתי בהונות ברגלו; זעקת הכאב האותנטית שלו נותרה בסרט."
                    },
                    {
                        "q": "איזה במאי הוליוודי מפורסם בפרפקציוניזם קיצוני ודרישה לעשרות רבות של טייקים (לעיתים מעל 80) לכל סצנה?",
                        "options": ["דייוויד פינצ'ר", "קוונטין טרנטינו", "סטיבן ספילברג", "קלינט איסטווד"],
                        "correct": 0,
                        "explanation": "דייוויד פינצ'ר ידוע בדרישתו ל-50 עד 100 טייקים לסצנות כדי להביא שחקנים לביצועים טבעיים ונטולי גינונים."
                    },
                    {
                        "q": "בסרטו המהפכני של כריסטופר נולאן 'ממנטו' (2000), מאיזו תופעה רפואית סובל הגיבור לאונרד שלבי?",
                        "options": ["אמנזיה אנטרוגרדית (חוסר יכולת לייצר זיכרונות חדשים לטווח קצר)", "הפרעת זהות דיסוציאטיבית", "אמנזיה רטרוגרדית (מחיקת כל זיכרונות הילדות)", "פרוסופגנוזיה (עיוורון לזיהוי פרצופים)"],
                        "correct": 0,
                        "explanation": "לאונרד סובל מאמנזיה אנטרוגרדית עקב פגיעת ראש, ונאלץ להיעזר בתמונות פולארויד, פתקים וקעקועים כדי לחקור את רצח אשתו."
                    },
                    {
                        "q": "איזו תגובה מצמררת ומפורסמת אלתר הית' לדג'ר (הג'וקר) בעת שישב כלוא בתא המעצר ב'האביר האפל'?",
                        "options": ["מחיאות כפיים איטיות וסרקסטיות בעת קידומו של גורדון למפקח", "ליקוק איטי של שפתיו תוך לחישת שיר ילדים", "חבטת ראשו בסורגי הברזל במקצב קבוע", "איזון קלף ג'וקר על קצה נעלו"],
                        "correct": 0,
                        "explanation": "כאשר השוטרים החלו למחוא כפיים לרגל קידומו של ג'ים גורדון, לדג'ר החל באלתור מבריק למחוא כפיים באיטיות ובלעג מהפנט."
                    },
                    {
                        "q": "איזה טוויסט מפורסם היכה את הצופים בהלם בסרטו של מ. נייט שאמלאן 'החוש השישי' (1999)?",
                        "options": ["ד״ר מלקולם קרואו (ברוס ויליס) היה מת לאורך כל הסרט", "הילד קול למעשה דמיין את כל רוחות הרפאים", "אמו של קול הייתה זו שהרעילה את ילדי העיירה", "רוחות הרפאים היו יצורים פיזיים מממד מקביל"],
                        "correct": 0,
                        "explanation": "פסיכולוג הילדים מלקולם קרואו מגלה ברגע השיא כי הוא נרצח כבר בתחילת הסרט והוא למעשה רוח רפאים שרק קול מסוגל לראות."
                    },
                    {
                        "q": "איזה שחקן כיכב בתפקידים ראשיים איקוניים הן בסרטיו של מרטין סקורסזה ('הזאב מוול סטריט', 'השתולים') והן בסרטיו של קוונטין טרנטינו ('ג'אנגו ללא מעצורים', 'היו זמנים בהוליווד')?",
                        "options": ["לאונרדו דיקפריו", "בראד פיט", "רוברט דה נירו", "כריסטיאן בייל"],
                        "correct": 0,
                        "explanation": "לאונרדו דיקפריו כיכב בשורה של יצירות מופת מובילות הן אצל מרטין סקורסזה והן אצל קוונטין טרנטינו."
                    }
                ]
            }
        ]
    }

    # Convert questions to trivia for EN and HE
    for cat in en_data["categories"]:
        if "questions" in cat:
            cat["trivia"] = format_trivia_list(cat.pop("questions"))
    for cat in he_data["categories"]:
        if "questions" in cat:
            cat["trivia"] = format_trivia_list(cat.pop("questions"))

    # Write files
    os.makedirs(os.path.dirname(TARGET_EN), exist_ok=True)
    with open(TARGET_EN, 'w', encoding='utf-8') as f:
        yaml.dump(en_data, f, allow_unicode=True, sort_keys=False, width=120)
    print(f"Wrote English modern classics topic to {TARGET_EN}")

    with open(TARGET_HE, 'w', encoding='utf-8') as f:
        yaml.dump(he_data, f, allow_unicode=True, sort_keys=False, width=120)
    print(f"Wrote Hebrew modern classics topic to {TARGET_HE}")

if __name__ == "__main__":
    create_datasets()
