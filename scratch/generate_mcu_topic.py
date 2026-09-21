#!/usr/bin/env python3
"""
Generates the Marvel Cinematic Universe (MCU) & Superhero Sagas topic
in both English (mcu_superhero_cinema_en.yaml) and Hebrew (mcu_superhero_cinema_he.yaml).
Follows:
- 100% 4-option multiple choice with dynamic client-side shuffle support (correct: 0).
- High distractor quality (domain-aligned options).
- Every question has an 'explanation' field.
- Hebrew gershayim / valid quotes.
- Detailed movie cards with IMDb scores, directors, release years, cast, storyline, filming locations, and trivia.
"""
import os
import yaml

TARGET_EN = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/mcu_superhero_cinema_en.yaml"
TARGET_HE = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/mcu_superhero_cinema_he.yaml"

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

def create_mcu_datasets():
    # -------------------------------------------------------------------------
    # ENGLISH DATASET
    # -------------------------------------------------------------------------
    en_data = {
        "id": "mcu_superhero_cinema_en",
        "title": "The Marvel Cinematic Universe & Superhero Sagas",
        "description": "Step into the most ambitious interconnected cinematic universe in film history! From the origins of Iron Man and the battle for the Infinity Stones to the Multiverse Saga and Deadpool, test your knowledge on iconic MCU movies, Marvel lore, and behind-the-scenes secrets.",
        "lang": "en",
        "audience": "adult",
        "categories": [
            # =================================================================
            # CATEGORY 1: Phase 1: The Origins & Avengers Assemble (2008–2012)
            # =================================================================
            {
                "id": "phase1_origins",
                "title": "Phase 1: The Origins & Avengers Assemble (2008–2012)",
                "description": "How Kevin Feige, Robert Downey Jr., and Joss Whedon laid the foundation for the superhero cinematic era.",
                "cards": [
                    {
                        "title": "Iron Man (2008)",
                        "points": [
                            "IMDb Rating: 7.9/10 | Directed by Jon Favreau | Starring Robert Downey Jr., Gwyneth Paltrow (Pepper Potts), and Jeff Bridges (Obadiah Stane / Iron Monger).",
                            "Storyline & Themes: Billionaire weapons industrialist Tony Stark is captured in Afghanistan, builds an improvised powered exoskeleton (Mark I) powered by an Arc Reactor, and vows to protect the world.",
                            "Filming & Production: Shot primarily in California (Edwards Air Force Base, Lone Pine, and sound stages). Jon Favreau allowed extensive dialogue improvisation because the script was continuously refined during shooting.",
                            "Cinematic Milestone: The film's post-credits scene featuring Samuel L. Jackson as Nick Fury ('You've become part of a bigger universe, you just don't know it yet') birthed the modern cinematic universe concept."
                        ]
                    },
                    {
                        "title": "Captain America: The First Avenger (2011)",
                        "points": [
                            "IMDb Rating: 6.9/10 | Directed by Joe Johnston | Starring Chris Evans as Steve Rogers and Hugo Weaving as Johann Schmidt / Red Skull.",
                            "Storyline & Themes: During WWII, sickly volunteer Steve Rogers is injected with Dr. Erskine's Super-Soldier Serum, wielding a vibranium shield against Nazi rogue science division HYDRA.",
                            "Infinity Stone Debut: Introduced the glowing blue Tesseract, later revealed to house the Space Stone.",
                            "Visual Effects: Lola VFX used digital body-shrinking techniques (composite plates and body doubles) to create 'Skinny Steve' Rogers before his serum transformation."
                        ]
                    },
                    {
                        "title": "Thor (2011)",
                        "points": [
                            "IMDb Rating: 7.0/10 | Directed by Shakespearean veteran Kenneth Branagh.",
                            "Cast & Characters: Chris Hemsworth as the arrogant God of Thunder, Tom Hiddleston in his breakout role as Loki, and Anthony Hopkins as King Odin.",
                            "Storyline & Themes: Stripped of his powers and divine hammer Mjolnir, Thor is banished to Earth (New Mexico) to learn humility and true worthiness.",
                            "Casting Trivia: Tom Hiddleston originally auditioned for the role of Thor, bulking up with 20 pounds of muscle, before Branagh cast him as the deceptive trickster Loki."
                        ]
                    },
                    {
                        "title": "The Avengers (2012)",
                        "points": [
                            "IMDb Rating: 8.0/10 | Written and directed by Joss Whedon | First film in history to generate a $200M+ opening weekend in North America.",
                            "Storyline & Themes: Earth's Mightiest Heroes (Iron Man, Captain America, Thor, Hulk, Black Widow, and Hawkeye) unite to stop Loki and the alien Chitauri army during the Battle of New York.",
                            "Iconic Scene: The continuous 360-degree circling hero shot of the assembled team in the middle of Grand Central / Park Avenue.",
                            "End Credits: Featured the legendary silent 'Shawarma' eating scene, filmed just days after the world premiere at the El Capitan Theatre."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "What iconic line does Tony Stark announce to the press at the end of 'Iron Man' (2008), completely breaking comic book secret-identity convention?",
                        "options": ["'I am Iron Man.'", "'The truth is, I work with Iron Man.'", "'Peace in our time.'", "'Avengers, assemble.'"],
                        "correct": 0,
                        "explanation": "Robert Downey Jr.'s line 'I am Iron Man' was partially improvised and cemented Tony Stark's bold, public persona in the MCU."
                    },
                    {
                        "q": "Which rare, vibration-absorbing fictional metal was used by Howard Stark to forge Captain America's circular shield?",
                        "options": ["Vibranium", "Adamantium", "Uru", "Promethium"],
                        "correct": 0,
                        "explanation": "Howard Stark created Steve Rogers' iconic shield using the world's rarest metal, Vibranium, mined from the isolated nation of Wakanda."
                    },
                    {
                        "q": "Which actor originally auditioned and screen-tested for the role of Thor before being cast as Loki?",
                        "options": ["Tom Hiddleston", "Benedict Cumberbatch", "Sebastian Stan", "Paul Bettany"],
                        "correct": 0,
                        "explanation": "Tom Hiddleston originally gained 20 lbs of muscle to audition for Thor before director Kenneth Branagh realized he was the perfect Loki."
                    },
                    {
                        "q": "What fast-food meal do the exhausted Avengers silently eat together in the famous post-credits scene of 'The Avengers' (2012)?",
                        "options": ["Shawarma", "Cheeseburgers", "New York pizza slices", "Chinese takeout noodles"],
                        "correct": 0,
                        "explanation": "Following Tony Stark's battle line asking if anyone had tried shawarma, the team is shown quietly chewing shawarma at a wrecked restaurant."
                    },
                    {
                        "q": "Which mysterious cosmic entity makes his first brief MCU appearance in the mid-credits scene of 'The Avengers' (2012)?",
                        "options": ["Thanos (The Mad Titan)", "Galactus", "Kang the Conqueror", "The Collector"],
                        "correct": 0,
                        "explanation": "Thanos turns to the camera with a sinister grin when his servant The Other warns that challenging Earth's heroes would be 'to court death'."
                    },
                    {
                        "q": "What is the name of the AI digital assistant Tony Stark created that resides in his helmet and mansion in early MCU films (voiced by Paul Bettany)?",
                        "options": ["J.A.R.V.I.S.", "F.R.I.D.A.Y.", "E.D.I.T.H.", "K.A.R.E.N."],
                        "correct": 0,
                        "explanation": "J.A.R.V.I.S. (Just A Rather Very Intelligent System) was Tony's primary AI before Paul Bettany physically transitioned into Vision."
                    },
                    {
                        "q": "In 'Captain America: The First Avenger', what ancient artifact houses the Space Stone that Red Skull uses to power HYDRA weapons?",
                        "options": ["The Tesseract", "The Aether", "The Orb", "The Eye of Agamotto"],
                        "correct": 0,
                        "explanation": "Johann Schmidt (Red Skull) steals the blue glowing Tesseract from a church crypt in Tønsberg, Norway."
                    },
                    {
                        "q": "Who directed the critically acclaimed 2011 Shakespearean fantasy epic 'Thor'?",
                        "options": ["Kenneth Branagh", "Joss Whedon", "Jon Favreau", "Taika Waititi"],
                        "correct": 0,
                        "explanation": "Acclaimed Shakespearean actor and director Kenneth Branagh brought regal, theatrical weight to the kingdom of Asgard."
                    },
                    {
                        "q": "Which weapon does Odin whisper an enchantment onto: 'Whosoever holds this hammer, if he be worthy, shall possess the power of Thor'?",
                        "options": ["Mjolnir", "Stormbreaker", "Gungnir", "The Hofund Sword"],
                        "correct": 0,
                        "explanation": "Odin enchants Thor's hammer Mjolnir (forged in the heart of a dying star) before casting it down to Earth."
                    },
                    {
                        "q": "Which SHIELD director approaches Tony Stark in the historic post-credits scene of 'Iron Man' to talk about 'The Avengers Initiative'?",
                        "options": ["Nick Fury", "Phil Coulson", "Alexander Pierce", "Maria Hill"],
                        "correct": 0,
                        "explanation": "Samuel L. Jackson made a surprise cameo as Nick Fury, initiating the overarching MCU storyline."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 2: Phase 2 & 3: The Infinity Saga & Cosmic Horizons (2014–2018)
            # =================================================================
            {
                "id": "phase2_3_infinity",
                "title": "Phase 2 & 3: The Infinity Saga & Cosmic Horizons (2014–2018)",
                "description": "The golden expansion of the MCU, introducing political thrillers, space outlaws, and internal civil wars.",
                "cards": [
                    {
                        "title": "Captain America: The Winter Soldier (2014)",
                        "points": [
                            "IMDb Rating: 7.8/10 | Directed by Anthony & Joe Russo (The Russo Brothers).",
                            "Cast & Characters: Chris Evans, Scarlett Johansson (Black Widow), Anthony Mackie (Sam Wilson / Falcon), and Sebastian Stan as Bucky Barnes / The Winter Soldier.",
                            "Storyline & Themes: A 1970s-style political conspiracy thriller revealing that SHIELD has been secretly infiltrated by HYDRA sleeper cells since WWII.",
                            "Action Landmark: Features the famous claustrophobic 10-on-1 glass elevator fight sequence ('Before we get started, does anyone want to get out?').",
                            "Influence: Propelled the Russo Brothers to helm 'Civil War', 'Infinity War', and 'Endgame'."
                        ]
                    },
                    {
                        "title": "Guardians of the Galaxy (2014)",
                        "points": [
                            "IMDb Rating: 8.0/10 | Written and directed by James Gunn.",
                            "Cast & Characters: Chris Pratt (Peter Quill / Star-Lord), Zoe Saldaña (Gamora), Dave Bautista (Drax), Bradley Cooper (Rocket), and Vin Diesel (Groot).",
                            "Storyline & Themes: A ragtag band of galactic criminals unite to prevent Ronan the Accuser from using the purple Power Stone to destroy planet Xandar.",
                            "Musical Sensation: The vintage 1970s soundtrack cassette tape ('Awesome Mix Vol. 1') topped the US Billboard 200 chart with zero new original songs."
                        ]
                    },
                    {
                        "title": "Captain America: Civil War (2016)",
                        "points": [
                            "IMDb Rating: 7.8/10 | Directed by the Russo Brothers | Adapting Mark Millar's comic event.",
                            "Storyline & Themes: The Avengers split into opposing factions over the UN Sokovia Accords (government oversight) and Bucky's past: Team Iron Man vs. Team Captain America.",
                            "Major MCU Debuts: Introduced Tom Holland as Peter Parker / Spider-Man and Chadwick Boseman as T'Challa / Black Panther.",
                            "Set Piece: The iconic 17-minute Leipzig/Halle Airport clash shot with digital IMAX cameras."
                        ]
                    },
                    {
                        "title": "Thor: Ragnarok (2017)",
                        "points": [
                            "IMDb Rating: 7.9/10 | Directed by New Zealand visionary Taika Waititi.",
                            "Cast & Characters: Chris Hemsworth, Mark Ruffalo (Hulk), Cate Blanchett (Hela, Goddess of Death), Jeff Goldblum (Grandmaster), and Tessa Thompson (Valkyrie).",
                            "Storyline & Re-invention: Reinvented Thor with vibrant 80s synth colors and improvisational humor as he fights Hulk in a gladiatorial arena on Sakaar and battles Hela to save Asgard.",
                            "Key Theme: Asgard is not a place; it is a people."
                        ]
                    },
                    {
                        "title": "Black Panther (2018)",
                        "points": [
                            "IMDb Rating: 7.3/10 | Directed by Ryan Coogler | Starring Chadwick Boseman, Michael B. Jordan (Erik Killmonger), Lupita Nyong'o, and Letitia Wright.",
                            "Cultural Phenomenon: First superhero film in history nominated for the Academy Award for Best Picture; won 3 Oscars (Costume Design, Production Design, Original Score).",
                            "Storyline & Themes: T'Challa ascends the throne of the technologically advanced, hidden African nation of Wakanda, challenged by Killmonger's global revolutionary ideology."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "In 'Captain America: The Winter Soldier', what historic intelligence agency is revealed to have been secretly infiltrated and controlled by HYDRA?",
                        "options": ["S.H.I.E.L.D.", "The C.I.A.", "M.I.6", "The Department of Damage Control"],
                        "correct": 0,
                        "explanation": "Captain America uncovers that HYDRA has grown secretly inside S.H.I.E.L.D. like a parasite since the end of World War II."
                    },
                    {
                        "q": "What is the name of the vintage 1970s cassette mixtape given to Peter Quill by his mother in 'Guardians of the Galaxy'?",
                        "options": ["Awesome Mix Vol. 1", "Cosmic Hits Vol. 1", "Star-Lord Grooves", "Earth Classics '88"],
                        "correct": 0,
                        "explanation": "'Awesome Mix Vol. 1' is Peter Quill's most cherished possession, packed with classic 1970s tracks like 'Hooked on a Feeling'."
                    },
                    {
                        "q": "Which two major superhero characters made their official Marvel Cinematic Universe debut in 'Captain America: Civil War' (2016)?",
                        "options": ["Spider-Man and Black Panther", "Doctor Strange and Ant-Man", "Deadpool and Wolverine", "Captain Marvel and Falcon"],
                        "correct": 0,
                        "explanation": "Tom Holland's Peter Parker / Spider-Man and Chadwick Boseman's T'Challa / Black Panther both debuted in 'Civil War'."
                    },
                    {
                        "q": "Who directed the vibrant, comedic reinvention of the God of Thunder in 'Thor: Ragnarok' (2017)?",
                        "options": ["Taika Waititi", "James Gunn", "Jon Watts", "Shane Black"],
                        "correct": 0,
                        "explanation": "Taika Waititi revitalized the Thor franchise with vibrant color, humor, and Led Zeppelin's 'Immigrant Song'."
                    },
                    {
                        "q": "What historic Oscar milestone did Ryan Coogler's 'Black Panther' (2018) achieve at the 91st Academy Awards?",
                        "options": ["First superhero film nominated for Best Picture", "First film to win Best Visual Effects and Best Animated Feature", "First film to sweep all four acting Oscars", "First Marvel movie to win Best Director"],
                        "correct": 0,
                        "explanation": "'Black Panther' made history as the first comic book / superhero movie ever nominated for the Best Picture Oscar."
                    },
                    {
                        "q": "What international legislation causes the ideological divide between Tony Stark and Steve Rogers in 'Captain America: Civil War'?",
                        "options": ["The Sokovia Accords", "The Geneva Superhero Protocol", "The Wakandan Treaty", "The New York Sanctions"],
                        "correct": 0,
                        "explanation": "The Sokovia Accords, drafted by 117 nations following the collateral damage in Sokovia, required Avengers to register with the UN."
                    },
                    {
                        "q": "Which Infinity Stone was encased inside the Orb retrieved by Star-Lord on the planet Morag in 'Guardians of the Galaxy'?",
                        "options": ["The Power Stone (Purple)", "The Soul Stone (Orange)", "The Reality Stone (Red)", "The Mind Stone (Yellow)"],
                        "correct": 0,
                        "explanation": "The Orb contained the purple Power Stone, capable of annihilating entire planetary surfaces upon direct contact."
                    },
                    {
                        "q": "Who played the complex, critically acclaimed antagonist Erik 'Killmonger' Stevens in 'Black Panther' (2018)?",
                        "options": ["Michael B. Jordan", "Daniel Kaluuya", "Winston Duke", "Sterling K. Brown"],
                        "correct": 0,
                        "explanation": "Michael B. Jordan delivered a widely celebrated performance as the vengeful and ideological Killmonger."
                    },
                    {
                        "q": "Which villainess, played by Cate Blanchett, is revealed to be Thor and Loki's banished older sister and the Goddess of Death in 'Thor: Ragnarok'?",
                        "options": ["Hela", "Enchantress", "Morgan le Fay", "Deathbird"],
                        "correct": 0,
                        "explanation": "Cate Blanchett played Hela, Odin's firstborn child who drew immense supernatural power directly from Asgard."
                    },
                    {
                        "q": "What famous martial arts / fight sequence inside a glass elevator takes place in 'Captain America: The Winter Soldier'?",
                        "options": ["Steve Rogers fighting 10 STRIKE agents in a descending elevator", "Black Widow fighting Winter Soldier on an escalator", "Falcon dodging drone missiles in an elevator shaft", "Bucky fighting Tony Stark in a bank elevator"],
                        "correct": 0,
                        "explanation": "Cap calmly delivers the line 'Before we get started, does anyone want to get out?' before fighting Rumlow and the STRIKE strike team in the elevator."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 3: The Climax: Infinity War & Endgame (2018–2019)
            # =================================================================
            {
                "id": "climax_infinity_endgame",
                "title": "The Climax: Infinity War & Endgame (2018–2019)",
                "description": "The epic 2-part conclusion of the 22-film Infinity Saga that shattered global box office records.",
                "cards": [
                    {
                        "title": "Avengers: Infinity War (2018)",
                        "points": [
                            "IMDb Rating: 8.4/10 | Directed by Anthony & Joe Russo | Written by Christopher Markus and Stephen McFeely.",
                            "Storyline & Themes: Thanos embarks on a merciless quest across the cosmos to collect all six Infinity Stones and wipe out 50% of all living beings to achieve universal resource balance.",
                            "Filming Landmark: The first Hollywood studio blockbuster shot entirely using ARRI Alexa IMAX digital cameras.",
                            "The Snap ('The Blip'): Concludes with Thanos snapping his fingers in Wakanda, turning half of the universe (including Spider-Man, Black Panther, and Doctor Strange) into dust."
                        ]
                    },
                    {
                        "title": "Avengers: Endgame (2019)",
                        "points": [
                            "IMDb Rating: 8.4/10 | Directed by the Russo Brothers | Runtime: 181 minutes.",
                            "Storyline & Themes: Five years after the devastating snap, the surviving Avengers execute a complex 'Time Heist' through the Quantum Realm to retrieve the Infinity Stones from past MCU timelines.",
                            "Iconic Payoffs: Captain America proves worthy to lift Mjolnir; the 'Portals' assembly scene uniting every MCU hero; Tony Stark's ultimate sacrifice ('And I... am... Iron Man').",
                            "Box Office King: Briefly surpassed 'Avatar' as the highest-grossing film of all time, generating $2.798 billion worldwide."
                        ]
                    },
                    {
                        "title": "The Six Infinity Stones Explained",
                        "points": [
                            "Space Stone (Blue): Teleportation across space (originally housed in the Tesseract).",
                            "Mind Stone (Yellow): Consciousness and psychic power (in Loki's Scepter, then Vision's forehead).",
                            "Reality Stone (Red): Alters matter and physical reality (originally manifested as the liquid Aether).",
                            "Power Stone (Purple): Pure destructive planetary energy (contained inside the Morag Orb).",
                            "Time Stone (Green): Temporal manipulation and forward/backward time travel (the Eye of Agamotto).",
                            "Soul Stone (Orange): Control over life and death; requires the ultimate sacrifice of a loved one on the cliff of Vormir."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "How many possible future outcomes did Doctor Strange view using the Time Stone on Titan in 'Avengers: Infinity War' to find the 1 winning scenario?",
                        "options": ["14,000,605 futures", "1,000,000 futures", "500,000 futures", "140,000,000 futures"],
                        "correct": 0,
                        "explanation": "Doctor Strange looked forward in time to view 14,000,605 alternate futures, stating there was only one scenario where the Avengers won."
                    },
                    {
                        "q": "Which Avenger makes the ultimate sacrifice on the planet Vormir to allow Hawkeye to claim the Soul Stone in 'Avengers: Endgame'?",
                        "options": ["Natasha Romanoff (Black Widow)", "Nebula", "Gamora", "Wanda Maximoff"],
                        "correct": 0,
                        "explanation": "Natasha Romanoff sacrifices herself by jumping off the cliff on Vormir so Clint Barton (Hawkeye) can retrieve the Soul Stone."
                    },
                    {
                        "q": "Which iconic weapon does Captain America summon and wield against Thanos during the climax of 'Avengers: Endgame'?",
                        "options": ["Mjolnir (Thor's hammer)", "Stormbreaker", "The Infinity Gauntlet", "The Dragonfang Sword"],
                        "correct": 0,
                        "explanation": "Steve Rogers proves his worthiness by summoning Mjolnir, prompting Thor to joyfully exclaim 'I knew it!'."
                    },
                    {
                        "q": "What final six words does Tony Stark say right before snapping his fingers to disintegrate Thanos and his army in 'Avengers: Endgame'?",
                        "options": ["'And I... am... Iron Man.'", "'I am inevitable.'", "'Avengers... assemble!'", "'We are the Avengers.'"],
                        "correct": 0,
                        "explanation": "After Thanos proclaims 'I am inevitable', Tony reveals the Infinity Stones on his nano-gauntlet and replies, 'And I... am... Iron Man.'"
                    },
                    {
                        "q": "Where does Thanos retreat to live peacefully as a farmer after wiping out half the universe in 'Avengers: Infinity War'?",
                        "options": ["The Garden (Planet 0259-S)", "Knowhere", "Titan", "Nidavellir"],
                        "correct": 0,
                        "explanation": "Thanos retires to a lush, peaceful planet known simply as 'The Garden' to hang up his armor as a scarecrow."
                    },
                    {
                        "q": "What mechanism allows the Avengers to travel back in time to 2012, 2013, and 2014 in 'Avengers: Endgame'?",
                        "options": ["The Quantum Realm navigated with Pym Particles", "Doctor Strange's sling rings", "The Bifrost Bridge", "A modified Tesseract engine"],
                        "correct": 0,
                        "explanation": "Using Scott Lang's knowledge and Pym Particles, Tony Stark engineers a 'Time Space GPS' to navigate the Quantum Realm."
                    },
                    {
                        "q": "What sweet phrase does Tony Stark's young daughter Morgan say to him, which became the emotional motto of 'Endgame'?",
                        "options": ["'I love you 3,000.'", "'You are my hero.'", "'Love you to the moon and back.'", "'Cheeseburgers first.'"],
                        "correct": 0,
                        "explanation": "'I love you 3,000' came directly from Robert Downey Jr.'s real-life children saying it to him, which the directors added to the script."
                    },
                    {
                        "q": "Who forges Thor's giant axe Stormbreaker in the heart of the dying neutron star on Nidavellir in 'Infinity War'?",
                        "options": ["Eitri the Dwarf King (Peter Dinklage)", "The Grandmaster", "The Collector", "Heimdall"],
                        "correct": 0,
                        "explanation": "Giant dwarf king Eitri (played by Peter Dinklage) operates the cosmic forge on Nidavellir to cast Stormbreaker."
                    },
                    {
                        "q": "Which character utters the long-awaited rallying cry 'Avengers... assemble' into his radio earpiece in 'Avengers: Endgame'?",
                        "options": ["Captain America (Steve Rogers)", "Iron Man (Tony Stark)", "Thor Odinson", "Nick Fury"],
                        "correct": 0,
                        "explanation": "Steve Rogers quietly says 'Avengers... assemble' as the armies charge at Thanos's forces at the ruined Avengers Compound."
                    },
                    {
                        "q": "What is the five-year time period between Thanos's snap in 2018 and the heroes' return in 2023 officially called in the MCU?",
                        "options": ["The Blip (The Decimation)", "The Great Silence", "The Void Period", "The Dark Half"],
                        "correct": 0,
                        "explanation": "In MCU canon (established in 'Spider-Man: Far From Home'), the 5-year disappearance and subsequent sudden return is known as 'The Blip'."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 4: The Multiverse Saga & Modern Hits (2021–Present)
            # =================================================================
            {
                "id": "multiverse_saga_modern",
                "title": "The Multiverse Saga, Spider-Man & Deadpool (2021–Present)",
                "description": "Crossing cinematic dimensions, the Time Variance Authority, and blockbuster multiverse team-ups.",
                "cards": [
                    {
                        "title": "Spider-Man: No Way Home (2021)",
                        "points": [
                            "IMDb Rating: 8.2/10 | Directed by Jon Watts | Starring Tom Holland, Zendaya, and Benedict Cumberbatch.",
                            "Multiverse Reunion: Brought together three generations of cinematic Spider-Men: Tobey Maguire (Sam Raimi era), Andrew Garfield (Marc Webb era), and Tom Holland (MCU).",
                            "Villains Return: Willem Dafoe (Green Goblin), Alfred Molina (Doc Ock), and Jamie Foxx (Electro) reprised their iconic roles via multiverse rifts.",
                            "Emotional Climax: To heal the fractured multiverse, Peter Parker sacrifices his personal identity, having Doctor Strange cast a spell that makes the entire world forget Peter Parker ever existed."
                        ]
                    },
                    {
                        "title": "Deadpool & Wolverine (2024)",
                        "points": [
                            "IMDb Rating: 7.8/10 | Directed by Shawn Levy | Starring Ryan Reynolds (Wade Wilson / Deadpool) and Hugh Jackman (Logan / Wolverine).",
                            "Historic R-Rated Milestone: The first R-rated film in the Marvel Cinematic Universe, earning over $1.3 billion worldwide.",
                            "Plot & Themes: Pulled from his timeline by the Time Variance Authority (TVA), Deadpool recruits a grief-stricken alternate Wolverine to save his universe from annihilation in 'The Void'.",
                            "Cameo Extravaganza: Featured beloved retro Marvel heroes including Wesley Snipes as Blade, Channing Tatum as Gambit, Chris Evans as Johnny Storm, and Jennifer Garner as Elektra."
                        ]
                    },
                    {
                        "title": "Guardians of the Galaxy Vol. 3 (2023)",
                        "points": [
                            "IMDb Rating: 7.9/10 | Written and directed by James Gunn.",
                            "Storyline & Heart: The emotional swan song of the original Guardians lineup, delving into Rocket Raccoon's tragic backstory and genetic creation by the cruel High Evolutionary (Chukwudi Iwuji).",
                            "Visual Feat: Set the Guinness World Record for the most makeup appliances created for a single production (over 22,500 prosthetics across 1,000+ actors)."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "Which three actors appeared together on screen as their respective versions of Peter Parker / Spider-Man in 'Spider-Man: No Way Home' (2021)?",
                        "options": ["Tom Holland, Tobey Maguire, and Andrew Garfield", "Tom Holland, Miles Morales, and Nicolas Cage", "Tobey Maguire, Jake Gyllenhaal, and Andrew Garfield", "Tom Holland, Chris Pine, and Shameik Moore"],
                        "correct": 0,
                        "explanation": "In a historic cinematic event, Holland, Maguire, and Garfield united on screen as Peter 1, Peter 2, and Peter 3."
                    },
                    {
                        "q": "Which actor reprised his iconic role as Green Goblin / Norman Osborn in 'Spider-Man: No Way Home', delivering all of his own physical stunts at age 66?",
                        "options": ["Willem Dafoe", "Alfred Molina", "Thomas Haden Church", "Rhys Ifans"],
                        "correct": 0,
                        "explanation": "Willem Dafoe returned as Norman Osborn / Green Goblin, insisting on performing his own hand-to-hand fight stunts."
                    },
                    {
                        "q": "What official age rating did 'Deadpool & Wolverine' (2024) hold, making it the very first MCU film with that classification?",
                        "options": ["R-Rated (Restricted)", "PG-13", "NC-17", "Unrated"],
                        "correct": 0,
                        "explanation": "'Deadpool & Wolverine' was the first R-rated entry in the Marvel Cinematic Universe, breaking records as the highest-grossing R-rated film in history."
                    },
                    {
                        "q": "Which classic comic book character did Channing Tatum portray in a heavily celebrated live-action cameo in 'Deadpool & Wolverine'?",
                        "options": ["Gambit (Remy LeBeau)", "Cyclops", "Nightcrawler", "Bishop"],
                        "correct": 0,
                        "explanation": "After nearly a decade of canceled solo film development, Channing Tatum finally donned the kinetic-card-throwing trench coat as Gambit."
                    },
                    {
                        "q": "Who is revealed as the sadistic creator and genetic tormentor of Rocket Raccoon in 'Guardians of the Galaxy Vol. 3'?",
                        "options": ["The High Evolutionary", "The Grandmaster", "Ego the Living Planet", "Ronan the Accuser"],
                        "correct": 0,
                        "explanation": "Chukwudi Iwuji played the High Evolutionary, a megalomaniac obsessed with engineering a flawless cybernetic civilization."
                    },
                    {
                        "q": "What does Doctor Strange's final spell in 'Spider-Man: No Way Home' make the world forget to prevent the collapse of reality?",
                        "options": ["The existence and identity of Peter Parker", "The existence of Spider-Man", "The events of the Battle of New York", "The secret of the multiverse"],
                        "correct": 0,
                        "explanation": "Strange's spell wipes all memories of Peter Parker from the entire world, leaving Peter completely anonymous and isolated."
                    },
                    {
                        "q": "Which mysterious organization monitors timelines and prunes rogue branches in the MCU (featured in 'Loki' and 'Deadpool & Wolverine')?",
                        "options": ["The Time Variance Authority (TVA)", "The Nova Corps", "The Ravagers", "The High Council of Elders"],
                        "correct": 0,
                        "explanation": "The TVA (Time Variance Authority) operates outside of space and time to regulate timelines and prevent multiversal war."
                    },
                    {
                        "q": "Which actor unexpectedly appeared in 'Deadpool & Wolverine' playing Johnny Storm (The Human Torch), shocking fans who expected Captain America?",
                        "options": ["Chris Evans", "Michael B. Jordan", "Sebastian Stan", "Anthony Mackie"],
                        "correct": 0,
                        "explanation": "Chris Evans reprised his pre-MCU 2005 role as Johnny Storm from Fox's 'Fantastic Four', shouting 'Flame On!'."
                    },
                    {
                        "q": "What Guinness World Record was officially broken by the production team of 'Guardians of the Galaxy Vol. 3' (2023)?",
                        "options": ["Most prosthetic makeup appliances created for a single movie (over 22,500)", "Most stunt performers set on fire in one scene", "Most digital CGI models used in space battles", "Longest continuous IMAX camera take in cinema"],
                        "correct": 0,
                        "explanation": "Legacy Effects and the makeup department created over 22,500 prosthetics for over 1,000 alien background actors."
                    },
                    {
                        "q": "Who directed the supernatural horror-infused MCU blockbuster 'Doctor Strange in the Multiverse of Madness' (2022)?",
                        "options": ["Sam Raimi", "Scott Derrickson", "James Wan", "Guillermo del Toro"],
                        "correct": 0,
                        "explanation": "Legendary 'Evil Dead' and original 'Spider-Man' trilogy director Sam Raimi directed the multiversal horror thriller."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 5: Marvel Lore, Stan Lee Cameos & Behind-The-Scenes Secrets
            # =================================================================
            {
                "id": "lore_cameos_secrets",
                "title": "Marvel Lore, Stan Lee Cameos & Behind-The-Scenes Secrets",
                "description": "Fascinating easter eggs, comic creator tributes, and casting near-misses of the MCU.",
                "cards": [
                    {
                        "title": "Stan Lee: The Father of Marvel's Cinematic Cameos",
                        "points": [
                            "Legendary Legacy: Marvel comics co-creator Stan Lee (1922–2018) appeared in 22 MCU films from 'Iron Man' (2008) through his final posthumous cameo in 'Avengers: Endgame' (1970s flower child driver).",
                            "Watchers Theory: In 'Guardians of the Galaxy Vol. 2', Stan Lee is shown on an asteroid reporting his human adventures to The Watchers, confirming the fan theory that he plays the same cosmic informant across all Marvel films."
                        ]
                    },
                    {
                        "title": "MCU Casting Near-Misses & Alternate Realities",
                        "points": [
                            "Iron Man: Marvel executives initially resisted Robert Downey Jr. due to his past legal troubles, pushing for Tom Cruise or Nicolas Cage before Jon Favreau fought tirelessly for Downey.",
                            "Black Widow: Emily Blunt was originally cast as Natasha Romanoff in 'Iron Man 2' but had to drop out due to a contractual obligation to film 'Gulliver's Travels', opening the door for Scarlett Johansson.",
                            "Star-Lord: Glenn Howerton (Dennis in 'It's Always Sunny in Philadelphia') was James Gunn's second choice for Peter Quill if Chris Pratt had declined."
                        ]
                    },
                    {
                        "title": "The Post-Credits Scene Tradition",
                        "points": [
                            "Origins: Starting with Nick Fury in 2008, post-credits scenes became mandatory viewing for cinema audiences worldwide.",
                            "Dual Formula: Marvel perfected a standard two-scene structure: the mid-credits scene sets up major future plot arcs, while the end-credits stinger delivers a comedic gag or character easter egg (e.g., Captain America's PSA on patience in 'Spider-Man: Homecoming')."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "In which MCU film did Stan Lee make his final, posthumous on-screen cameo appearance before his passing?",
                        "options": ["Avengers: Endgame (2019)", "Spider-Man: Far From Home (2019)", "Captain Marvel (2019)", "Avengers: Infinity War (2018)"],
                        "correct": 0,
                        "explanation": "Stan Lee's final cameo was in 'Avengers: Endgame', where he appeared digitally de-aged as a 1970s pacifist driving past Camp Lehigh yelling 'Hey man, make love, not war!'."
                    },
                    {
                        "q": "Which actress was originally cast as Black Widow (Natasha Romanoff) in 'Iron Man 2' before dropping out due to a scheduling conflict?",
                        "options": ["Emily Blunt", "Jessica Chastain", "Charlize Theron", "Rachel McAdams"],
                        "correct": 0,
                        "explanation": "Emily Blunt was contracted to film 'Gulliver's Travels' for Fox and was forced to decline the role, allowing Scarlett Johansson to claim it."
                    },
                    {
                        "q": "In 'Guardians of the Galaxy Vol. 2', Stan Lee is depicted sitting in a space suit talking to which ancient cosmic observers?",
                        "options": ["The Watchers", "The Celestials", "The Elders of the Universe", "The Kree Supreme Intelligence"],
                        "correct": 0,
                        "explanation": "Stan Lee is seen chatting with The Watchers, giant cosmic entities tasked with observing all multiversal events without interfering."
                    },
                    {
                        "q": "What comedic PSA topic does Captain America speak about in the very last end-credits gag of 'Spider-Man: Homecoming' (2017)?",
                        "options": ["The virtue of patience (mocking audiences waiting for post-credits scenes)", "The dangers of skipping school lunches", "The importance of dental hygiene", "Why gym class rope climbs build character"],
                        "correct": 0,
                        "explanation": "Cap directly talks to the theater audience about how patience is a valuable trait, but sometimes 'you wonder why you waited so long for something so disappointing'."
                    },
                    {
                        "q": "Which Marvel character's voice was provided by director Taika Waititi via on-set motion capture in 'Thor: Ragnarok'?",
                        "options": ["Korg (the Kronan rock gladiator)", "Miek", "Surtur", "Fenris the Wolf"],
                        "correct": 0,
                        "explanation": "Taika Waititi wore a motion capture suit on set and provided the gentle, soft-spoken Polynesian-accented voice for Korg."
                    },
                    {
                        "q": "Which real-life music artist's song 'Back in Black' is mistakenly called 'Led Zeppelin' by Peter Parker in 'Spider-Man: Far From Home'?",
                        "options": ["AC/DC", "Black Sabbath", "Guns N' Roses", "Aerosmith"],
                        "correct": 0,
                        "explanation": "Happy Hogan plays AC/DC's 'Back in Black' on the Stark jet, and Peter excitedly responds: 'I love Led Zeppelin!'."
                    },
                    {
                        "q": "What is the name of Thor's home kingdom's rainbow teleportation bridge operated by Heimdall?",
                        "options": ["The Bifrost", "The Yggdrasil Beam", "The Valhalla Gate", "The Asgardian Conduit"],
                        "correct": 0,
                        "explanation": "The Bifrost is the rainbow light bridge that instantly transports Asgardians across the Nine Realms."
                    },
                    {
                        "q": "What pet animal is Goose in 'Captain Marvel' (2019), who appears as a normal ginger cat but is actually a dangerous alien?",
                        "options": ["A Flerken", "A Skrull", "A Chitauri hound", "A Kree beast"],
                        "correct": 0,
                        "explanation": "Goose is a Flerken, a highly dangerous alien species capable of swallowing massive objects (and the Tesseract) using dimensional pocket tentacles."
                    },
                    {
                        "q": "What is the name of the iconic Marvel Studios president who has served as the master architect and producer of the entire MCU since 2008?",
                        "options": ["Kevin Feige", "Avi Arad", "Bob Iger", "Louis D'Esposito"],
                        "correct": 0,
                        "explanation": "Kevin Feige has been the visionary president of Marvel Studios, overseeing the unprecedented interconnected cinematic universe."
                    },
                    {
                        "q": "Which iconic weapon did Thanos use his giant double-bladed sword to shatter in 'Avengers: Endgame'?",
                        "options": ["Captain America's vibranium shield", "Iron Man's Mark 85 helmet", "Thor's Stormbreaker handle", "Hawkeye's tactical bow"],
                        "correct": 0,
                        "explanation": "Thanos violently chops into Cap's shield with his double-edged blade, splintering the vibranium into ragged halves."
                    }
                ]
            }
        ]
    }

    # -------------------------------------------------------------------------
    # HEBREW DATASET
    # -------------------------------------------------------------------------
    he_data = {
        "id": "mcu_superhero_cinema_he",
        "title": "היקום הקולנועי של מארוול וסרטי גיבורי-על (The MCU)",
        "description": "היכנסו אל היקום הקולנועי המצליח והמורכב ביותר בתולדות הקולנוע! החל מלידתו של איירון מן ומלחמת אבני האינסוף ועד לסאגת המולטיוורס, ספיידרמן ודדפול – בחנו את הידע שלכם בסרטי מארוול, תיאוריות, דמויות וסודות ממאחורי הקלעים.",
        "lang": "he",
        "audience": "adult",
        "categories": [
            # =================================================================
            # CATEGORY 1: Phase 1: The Origins & Avengers Assemble (2008–2012)
            # =================================================================
            {
                "id": "phase1_origins",
                "title": "שלב 1: מקורות הגיבורים והנוקמים מתאחדים (2008–2012)",
                "description": "כיצד קווין פייגי, רוברט דאוני ג'וניור וג'וס ווידון יצרו את הבסיס ליקום הקולנועי המשותף.",
                "cards": [
                    {
                        "title": "איירון מן (Iron Man, 2008)",
                        "points": [
                            "ציון IMDb: 7.9/10 | בימוי: ג'ון פאברו | בכיכובם של רוברט דאוני ג'וניור, גווינת' פאלטרו (פפר פוטס) וג'ף ברידג'ס (עובדיה סטיין / איירון מונגר).",
                            "עלילה ותמות: התעשיין המיליארדר טוני סטארק נחטף באפגניסטן, בונה חליפת שריון מאולתרת המונעת על ידי כור קשת (Arc Reactor), ומחליט להקדיש את חייו להגנה על האנושות.",
                            "הפקה ואלתורים: צולם בעיקר בקליפורניה. הבמאי ג'ון פאברו איפשר חופש אלתור נרחב לדיאלוגים מכיוון שהתסריט שוכתב בזמן אמת לאורך הצילומים.",
                            "רגע מכונן: סצנת אחרי-הכתוביות הראשונה בהשתתפות סמואל ל. ג'קסון כניק פיורי ('אתה חלק מיקום גדול יותר, אתה פשוט עוד לא יודע את זה') ילדה את רעיון היקום המשותף."
                        ]
                    },
                    {
                        "title": "קפטן אמריקה: הנוקם הראשון (The First Avenger, 2011)",
                        "points": [
                            "ציון IMDb: 6.9/10 | בימוי: ג'ו ג'ונסטון | בכיכובם של כריס אוונס (סטיב רוג'רס) והוגו וויבינג (יוהאן שמידט / הגולגולת האדומה).",
                            "עלילה ותמות: במלחמת העולם השנייה, המתנדב הצנום סטיב רוג'רס מקבל את נסיוב 'חייל-העל' של ד״ר ארסקין, ויוצא להילחם בזרוע המדע הנאצית הסוררת 'הידרה' כשהוא חמוש במגן ויברניום.",
                            "חשיפת אבן אינסוף: הציג לראשונה את קוביית הטסרקט הכחולה והזוהרת, שלימים התגלתה כמכילה את אבן המרחב.",
                            "אפקטים חזותיים: חברת Lola VFX השתמשה בהקטנה דיגיטלית מתקדמת של גופו של כריס אוונס ליצירת דמותו של 'סטיב הרזה' לפני קבלת הנסיוב."
                        ]
                    },
                    {
                        "title": "תור (Thor, 2011)",
                        "points": [
                            "ציון IMDb: 7.0/10 | בימוי: הבמאי והשחקן השייקספירי קנת בראנה.",
                            "שחקנים ודמויות: כריס המסוורת' בתור אל הרעם היהיר, טום הידלסטון בתפקיד הפריצה הגדול שלו כלוקי אל התככים, ואנתוני הופקינס בתור המלך אודין.",
                            "עלילה ותמות: תור מנושל מכוחותיו ומפטישו מיולניר ומוגלה לכדור הארץ (ניו מקסיקו) כדי ללמוד ענווה, בגרות וראויות אמיתית.",
                            "טריוויה על ליהוק: טום הידלסטון נבחן במקור לתפקידו של תור והעלה כ-10 ק״ג מסת שריר, לפני שבראנה הבין שהוא מושלם לתפקיד לוקי."
                        ]
                    },
                    {
                        "title": "הנוקמים (The Avengers, 2012)",
                        "points": [
                            "ציון IMDb: 8.0/10 | תסריט ובימוי: ג'וס ווידון | הסרט הראשון בהיסטוריה שהכניס מעל 200 מיליון דולר בסוף שבוע הפתיחה בצפון אמריקה.",
                            "עלילה ותמות: גיבורי-העל החזקים ביותר בכדור הארץ (איירון מן, קפטן אמריקה, תור, הענק הירוק, האלמנה השחורה והוקאיי) מתאחדים לעצור את לוקי וצבא הצ'יטאורי בקרב על ניו יורק.",
                            "סצנה מיתולוגית: השוט המעגלי המפורסם ב-360 מעלות של כל חברי הצוות העומדים גב אל גב במרכז מנהטן.",
                            "אחרי הכתוביות: סצנת השווארמה הדוממת והמפורסמת, שצולמה ימים ספורים בלבד לאחר הקרנת הבכורה החגיגית בהוליווד."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "איזה משפט מפורסם מכריז טוני סטארק במסיבת העיתונאים בסיום הסרט 'איירון מן' (2008), כשהוא שובר את מוסכמת הזהות הסודית?",
                        "options": ["'אני איירון מן' (I am Iron Man)", "'האמת היא שאני עובד עם איירון מן'", "'שלום בימינו'", "'הנוקמים, התאחדו'"],
                        "correct": 0,
                        "explanation": "המשפט 'I am Iron Man' נאמר בחלקו באלתור של רוברט דאוני ג'וניור, והפך לחותמת המובהקת של טוני סטארק ביקום מארוול."
                    },
                    {
                        "q": "מאיזו מתכת בדיונית ונדירה בנה הווארד סטארק את המגן העגול של קפטן אמריקה?",
                        "options": ["ויברניום (Vibranium)", "אדמנטיום (Adamantium)", "אורו (Uru)", "פרומתיום"],
                        "correct": 0,
                        "explanation": "הווארד סטארק השתמש במתכת הבולמת רעידות וויברציות, ויברניום, שמקורה בממלכת ווקאנדה המבודדת."
                    },
                    {
                        "q": "איזה שחקן נבחן והעלה משקל במקור עבור תפקידו של תור, לפני שלוהק בסופו של דבר לתפקיד לוקי?",
                        "options": ["טום הידלסטון", "בנדיקט קמברבאץ'", "סבסטיאן סטן", "פול בטאני"],
                        "correct": 0,
                        "explanation": "טום הידלסטון התאמן והעלה מסת שריר לקראת מבחן הבד לדמותו של תור, אך הבמאי קנת בראנה זיהה בו את לוקי המושלם."
                    },
                    {
                        "q": "איזה מאכל מהיר אוכלים הנוקמים בדממה מוחלטת בסצנת אחרי-הכתוביות המפורסמת בסרט 'הנוקמים' (2012)?",
                        "options": ["שווארמה", "צ'יזבורגרים", "משולשי פיצה ניו יורקית", "נודלס סיני מוקפץ"],
                        "correct": 0,
                        "explanation": "בהמשך להצעתו של טוני סטארק בסיום הקרב לבדוק מקום שווארמה סמוך, חברי הצוות יושבים מותשים ואוכלים שווארמה בדממה."
                    },
                    {
                        "q": "איזו ישות קוסמית מאיימת מופיעה לראשונה בהצצה חטופה בסצנת אמצע-הכתוביות של 'הנוקמים' (2012)?",
                        "options": ["תאנוס (הטיטאן המטורף)", "גלקטוס", "קאנג הכובש", "האספן (The Collector)"],
                        "correct": 0,
                        "explanation": "תאנוס מסתובב אל המצלמה בחיוך מאיים כאשר עוזרו מזהיר אותו כי עימות מול גיבורי כדור הארץ הוא 'חיזור אחר המוות'."
                    },
                    {
                        "q": "מהו שמה של מערכת הבינה המלאכותית של טוני סטארק המלווה אותו בקסדתו ובמעבדתו (בקולו של פול בטאני)?",
                        "options": ["ג'ארוויס (J.A.R.V.I.S.)", "פריידיי (F.R.I.D.A.Y.)", "אדית' (E.D.I.T.H.)", "קארן (K.A.R.E.N.)"],
                        "correct": 0,
                        "explanation": "ג'ארוויס (J.A.R.V.I.S.) שירת כבינה המלאכותית של טוני סטארק לפני שהוטמע בגופו של ויז'ן."
                    },
                    {
                        "q": "בסרט 'קפטן אמריקה: הנוקם הראשון', באיזה חפץ מיסטי מוטמנת אבן המרחב שבאמצעותה מפתח הגולגולת האדומה נשקי-על?",
                        "options": ["הטסרקט (The Tesseract)", "האת'ר (The Aether)", "האורב (The Orb)", "עין אגאמוטו"],
                        "correct": 0,
                        "explanation": "יוהאן שמידט גונב את קוביית הטסרקט הזוהרת מכנסייה בנורווגיה כדי להניע את נשקי הידרה."
                    },
                    {
                        "q": "מי ביים את הסרט השייקספירי והמלכותי 'תור' שיצא לאקרנים בשנת 2011?",
                        "options": ["קנת בראנה", "ג'וס ווידון", "ג'ון פאברו", "טאיקה וואיטיטי"],
                        "correct": 0,
                        "explanation": "הבמאי והשחקן השייקספירי הבריטי קנת בראנה ביים את הסרט והעניק לממלכת אסגרד נופך תיאטרלי רם-מעלה."
                    },
                    {
                        "q": "על איזה כלי נשק לחש המלך אודין את הכישוף: 'כל האוחז בפטיש זה, אם ראוי הוא, יזכה בכוחו של תור'?",
                        "options": ["מיולניר (Mjolnir)", "סטורמברייקר (Stormbreaker)", "גונגניר (רומח אודין)", "חרב ההופונד של היימדל"],
                        "correct": 0,
                        "explanation": "אודין כישף את פטיש הקרב של תור, מיולניר, שחושל בלבו של כוכב גוסס, לפני שהשליך אותו לכדור הארץ."
                    },
                    {
                        "q": "איזה מנהל סוכנות S.H.I.E.L.D. מופיע בסצנת אחרי-הכתוביות ב'איירון מן' (2008) כדי לדבר עם טוני על 'יוזמת הנוקמים'?",
                        "options": ["ניק פיורי", "פיל קולסון", "אלכסנדר פירס", "מריה היל"],
                        "correct": 0,
                        "explanation": "סמואל ל. ג'קסון בהופעת אורח מפתיעה כניק פיורי הצית את הרעיון של יקום קולנועי משותף."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 2: Phase 2 & 3: The Infinity Saga & Cosmic Horizons (2014–2018)
            # =================================================================
            {
                "id": "phase2_3_infinity",
                "title": "שלב 2 ו-3: סאגת האינסוף והרחבת הקוסמוס (2014–2018)",
                "description": "התרחבות היקום עם מותחני ריגול, הרפתקאות בחלל ומלחמת אזרחים פנימית בין הגיבורים.",
                "cards": [
                    {
                        "title": "קפטן אמריקה: חייל החורף (The Winter Soldier, 2014)",
                        "points": [
                            "ציון IMDb: 7.8/10 | בימוי: האחים אנתוני וג'ו רוסו.",
                            "שחקנים ודמויות: כריס אוונס, סקרלט ג'והנסון (האלמנה השחורה), אנתוני מאקי (סאם וילסון / פלקון) וסבסטיאן סטן כבאקי ברנז / חייל החורף.",
                            "עלילה ותמות: מותחן קונספירציה וריגול בסגנון שנות ה-70 החושף כי ארגון הידרה הסתנן ושלט בחשאי בסוכנות S.H.I.E.L.D. מאז מלחמת העולם השנייה.",
                            "אקשן בלתי-נשכח: קרב המעלית המפורסם שבו קפטן אמריקה נלחם לבדו מול 10 סוכני יחידת STRIKE במעלית זכוכית יורדת.",
                            "השפעה: ההצלחה הביקורתית סללה לאחים רוסו את הדרך לבימוי 'מלחמת האזרחים', 'מלחמת האינסוף' ו'סוף המשחק'."
                        ]
                    },
                    {
                        "title": "שומרי הגלקסיה (Guardians of the Galaxy, 2014)",
                        "points": [
                            "ציון IMDb: 8.0/10 | תסריט ובימוי: ג'יימס גאן.",
                            "שחקנים ודמויות: כריס פראט (פיטר קוויל / סטאר לורד), זואי סלדנה (גאמורה), דייב בטיסטה (דראקס), בראדלי קופר (רוקט) ווין דיזל (גרוט).",
                            "עלילה ותמות: חבורת פושעים גלקטיים מפוקפקים מתאחדים כדי למנוע מרונאן המאשים להשתמש באבן הכוח הסגולה להשמדת כוכב קסאנדר.",
                            "תופעה מוזיקלית: קלטת הלהיטים הנוסטלגית משנות ה-70 ('Awesome Mix Vol. 1') כבשה את המקום הראשון במצעד בילבורד 200 ללא אף שיר מקורי חדש."
                        ]
                    },
                    {
                        "title": "קפטן אמריקה: מלחמת האזרחים (Civil War, 2016)",
                        "points": [
                            "ציון IMDb: 7.8/10 | בימוי: האחים רוסו | עיבוד לקשת הקומיקס המפורסמת של מארק מילר.",
                            "עלילה ותמות: הנוקמים מתפצלים לשני מחנות עקב 'הסכמי סוקוביה' לפיקוח האו״ם על גיבורי-על: צוות איירון מן מול צוות קפטן אמריקה המגן על חברו באקי.",
                            "בכורות ענק ב-MCU: הציג לראשונה את טום הולנד כספיידרמן ואת צ'דוויק בוזמן כפנתר השחור.",
                            "שוט אקשן מרכזי: קרב נמל התעופה בלייפציג בן 17 הדקות שצולם במצלמות IMAX דיגיטליות."
                        ]
                    },
                    {
                        "title": "תור: ראגנארוק (Thor: Ragnarok, 2017)",
                        "points": [
                            "ציון IMDb: 7.9/10 | בימוי: הבמאי הניו זילנדי טאיקה וואיטיטי.",
                            "שחקנים ודמויות: כריס המסוורת', מארק ראפלו (הענק הירוק), קייט בלאנשט (הלה אלת המוות), ג'ף גולדבלום (הגראנדמאסטר) וטסה תומפסון (ואלקירי).",
                            "המצאה מחדש: הפך את מותג תור לקומדיית אקשן צבעונית ומלהיבה בהשראת האייטיז, שבה תור נלחם בענק הירוק בזירה בסאקאר ונאבק בהלה כדי להציל את אנשי אסגרד.",
                            "מסר מרכזי: אסגרד איננה מקום גיאוגרפי – היא האנשים עצמם."
                        ]
                    },
                    {
                        "title": "הפנתר השחור (Black Panther, 2018)",
                        "points": [
                            "ציון IMDb: 7.3/10 | בימוי: ראיין קוגלר | בכיכובם של צ'דוויק בוזמן, מייקל בי. ג'ורדן (אריק קילמונגר), לופיטה ניונגו ולטישה רייט.",
                            "תופעה תרבותית: סרט גיבורי-העל הראשון בהיסטוריה שהיה מועמד לפרס אוסקר לסרט הטוב ביותר; זכה ב-3 פרסי אוסקר (עיצוב תלבושות, עיצוב אמנותי ופסקול מקורי).",
                            "עלילה ותמות: ט'צ'אלה יורש את כס המלכות בממלכת ווקאנדה המתקדמת טכנולוגית, ומתמודד עם חזונו המהפכני והכואב של קילמונגר."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "איזה ארגון ביון וביטחון בינלאומי מתגלה כמי שנשלט בחשאי על ידי 'הידרה' ב'קפטן אמריקה: חייל החורף'?",
                        "options": ["S.H.I.E.L.D.", "ה-C.I.A.", "ה-M.I.6", "מחלקת בקרת הנזקים (Damage Control)"],
                        "correct": 0,
                        "explanation": "קפטן אמריקה מגלה כי ארגון הידרה צמח כטפיל בתוך שורות שילד מאז מלחמת העולם השנייה."
                    },
                    {
                        "q": "מהו שמה של קלטת הלהיטים הנוסטלגית משנות ה-70 שפיטר קוויל שומר מאימו ב'שומרי הגלקסיה'?",
                        "options": ["Awesome Mix Vol. 1", "Cosmic Hits Vol. 1", "Star-Lord Grooves", "Earth Classics '88"],
                        "correct": 0,
                        "explanation": "הקלטת 'Awesome Mix Vol. 1' היא החפץ היקר ביותר לפיטר קוויל וכוללת קלאסיקות פופ ורוק משנות ה-70."
                    },
                    {
                        "q": "אילו שתי דמויות גיבורי-על מרכזיות ערכו את הופעת הבכורה הרשמית שלהן ב-MCU בסרט 'קפטן אמריקה: מלחמת האזרחים' (2016)?",
                        "options": ["ספיידרמן והפנתר השחור", "דוקטור סטריינג' ואנטמן", "דדפול ווולברין", "קפטן מארוול ופלקון"],
                        "correct": 0,
                        "explanation": "טום הולנד (ספיידרמן) וצ'דוויק בוזמן (הפנתר השחור) הצטרפו לראשונה ליקום הקולנועי ב'מלחמת האזרחים'."
                    },
                    {
                        "q": "איזה במאי ביים את השינוי הקומי והסגנוני המבריק של אל הרעם בסרט 'תור: ראגנארוק' (2017)?",
                        "options": ["טאיקה וואיטיטי", "ג'יימס גאן", "ג'ון וואטס", "שיין בלאק"],
                        "correct": 0,
                        "explanation": "טאיקה וואיטיטי העניק למותג צבעוניות, הומור שנון ושימוש אייקוני בשיר 'Immigrant Song' של לד זפלין."
                    },
                    {
                        "q": "איזה הישג חסר תקדים רשם סרטו של ראיין קוגלר 'הפנתר השחור' בטקס פרסי האוסקר ה-91?",
                        "options": ["סרט גיבורי-העל הראשון שהיה מועמד לפרס הסרט הטוב ביותר", "הסרט הראשון שזכה באוסקר לאפקטים ובאוסקר לאנימציה", "סרט מארוול הראשון שזכה באוסקר לבמאי הטוב ביותר", "הסרט הראשון שגרף את כל ארבעת פרסי המשחק"],
                        "correct": 0,
                        "explanation": "'הפנתר השחור' עשה היסטוריה כאשר היה לסרט הקומיקס / גיבורי-העל הראשון אי פעם שהועמד לאוסקר לסרט הטוב ביותר."
                    },
                    {
                        "q": "איזה הסכם בינלאומי בפיקוח האו״ם מייצר את הקרע האידיאולוגי בין טוני סטארק לסטיב רוג'רס ב'מלחמת האזרחים'?",
                        "options": ["הסכמי סוקוביה (The Sokovia Accords)", "אמנת ז'נבה לגיבורי-על", "הסכם ווקאנדה", "הסנקציות של ניו יורק"],
                        "correct": 0,
                        "explanation": "הסכמי סוקוביה נחתמו על ידי 117 מדינות כדי לחייב את הנוקמים לפעול תחת פיקוח הדוק של ועדה בינלאומית."
                    },
                    {
                        "q": "איזו אבן אינסוף הייתה מוטמנת בתוך כדור המתכת (The Orb) שגנב סטאר לורד על כוכב מוראג ב'שומרי הגלקסיה'?",
                        "options": ["אבן הכוח (סגולה)", "אבן הנשמה (כתומה)", "אבן המציאות (אדומה)", "אבן המחשבה (צהובה)"],
                        "correct": 0,
                        "explanation": "האורב הכיל את אבן הכוח הסגולה, המסוגלת למחוק חיים מכוכבי לכת שלמים במגע ישיר עם הקרקע."
                    },
                    {
                        "q": "איזה שחקן גילם את הנבל האידיאולוגי המורכב אריק 'קילמונגר' סטיבנס בסרט 'הפנתר השחור' (2018)?",
                        "options": ["מייקל בי. ג'ורדן", "דניאל קלויה", "וינסטון דיוק", "סטרלינג קיי בראון"],
                        "correct": 0,
                        "explanation": "מייקל בי. ג'ורדן זכה לשבחים מקיר לקיר על הופעתו העוצמתית והכואבת כקילמונגר."
                    },
                    {
                        "q": "איזו נבלית, אותה גילמה קייט בלאנשט, מתגלה כאחותם הבכורה של תור ולוקי וכאלת המוות ב'תור: ראגנארוק'?",
                        "options": ["הלה (Hela)", "אנצ'נטרס (המכשפת)", "מורגן לה פיי", "דת'בירד"],
                        "correct": 0,
                        "explanation": "קייט בלאנשט גילמה את הלה, בכורתו האכזרית של אודין ששאבה את כוחותיה האלוהיים ישירות מאסגרד."
                    },
                    {
                        "q": "איזה קרב מפורסם בתוך מעלית זכוכית מתרחש בסרט 'קפטן אמריקה: חייל החורף'?",
                        "options": ["סטיב רוג'רס נלחם לבדו ב-10 סוכני יחידת STRIKE במעלית יורדת", "האלמנה השחורה נלחמת בחייל החורף על דרגנוע", "פלקון מתחמק מטילים בתוך פיר מעלית", "באקי נלחם בטוני סטארק במעלית בנק"],
                        "correct": 0,
                        "explanation": "קפטן אמריקה אומר בשלווה 'לפני שנתחיל, מישהו רוצה לצאת?' ואז מביס בידיים חשופות את כל הסוכנים במעלית הצפופה."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 3: The Climax: Infinity War & Endgame (2018–2019)
            # =================================================================
            {
                "id": "climax_infinity_endgame",
                "title": "השיא: מלחמת האינסוף וסוף המשחק (2018–2019)",
                "description": "הסיום הדרמטי של סאגת 22 הסרטים ששבר את שיאי ההכנסות בקופות בכל הזמנים.",
                "cards": [
                    {
                        "title": "הנוקמים: מלחמת האינסוף (Infinity War, 2018)",
                        "points": [
                            "ציון IMDb: 8.4/10 | בימוי: האחים אנתוני וג'ו רוסו | תסריט: כריסטופר מרקוס וסטיבן מק'פילי.",
                            "עלילה ותמות: תאנוס יוצא למסע חסר רחמים ברחבי הקוסמוס לאיסוף כל שש אבני האינסוף כדי למחוק 50% מכלל היצורים החיים ולהביא לאיזון משאבים ביקום.",
                            "הישג טכנולוגי: הסרט ההוליוודי הגדול הראשון שצולם כולו מתחילתו ועד סופו במצלמות IMAX דיגיטליות ייעודיות.",
                            "הנקישה המפורסמת ('הבליפ'): מסתיים בנקישת האצבעות של תאנוס בווקאנדה, שהופכת לאפר מחצית מיצורי היקום (כולל ספיידרמן, הפנתר השחור ודוקטור סטריינג')."
                        ]
                    },
                    {
                        "title": "הנוקמים: סוף המשחק (Avengers: Endgame, 2019)",
                        "points": [
                            "ציון IMDb: 8.4/10 | בימוי: האחים רוסו | אורך הסרט: 181 דקות (3 שעות).",
                            "עלילה ותמות: חמש שנים לאחר הנקישה ההרסנית, הנוקמים ששרדו מוציאים לפועל 'שוד זמן' דרך מימד הקוונטים כדי להשיג את אבני האינסוף מציר הזמן בעבר.",
                            "סגירת מעגלים מיתולוגית: קפטן אמריקה מרים את הפטיש מיולניר; סצנת הפורטלים המאחדת את כל גיבורי מארוול; והקרבתו העליונה של טוני סטארק ('ואני... איירון מן').",
                            "שיא קופות עולמי: שבר לזמן מסוים את שיא ההכנסות בכל הזמנים והכניס כ-2.798 מיליארד דולר ברחבי העולם."
                        ]
                    },
                    {
                        "title": "שש אבני האינסוף והכוחות שלהן",
                        "points": [
                            "אבן המרחב (כחולה): טלפורטציה ומעבר מיידי בין ממדים (שכנה בטסרקט).",
                            "אבן המחשבה (צהובה): תודעה ושליטה מוחית (בשרביט של לוקי, ובהמשך במצחו של ויז'ן).",
                            "אבן המציאות (אדומה): שינוי חומר וחוקי הפיזיקה (הופיעה כנוזל האת'ר).",
                            "אבן הכוח (סגולה): אנרגיה הרסנית המסוגלת להחריב כוכבי לכת (בתוך האורב).",
                            "אבן הזמן (ירוקה): מניפולציה וראיית העבר והעתיד (בתוך עין אגאמוטו).",
                            "אבן הנשמה (כתומה): שליטה בחיים ובמוות; דורשת הקרבת אדם אהוב על צוקי כוכב וורמיר."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "בכמה צירי זמן עתידיים צפה דוקטור סטריינג' בעזרת אבן הזמן על כוכב טיטאן כדי למצוא את התרחיש היחיד שבו הנוקמים מנצחים?",
                        "options": ["14,000,605 תרחישים", "1,000,000 תרחישים", "500,000 תרחישים", "140,000,000 תרחישים"],
                        "correct": 0,
                        "explanation": "דוקטור סטריינג' צפה ב-14,000,605 אפשרויות עתידיות ומצא כי רק בתרחיש אחד בודד הנוקמים יגברו על תאנוס."
                    },
                    {
                        "q": "מי מהנוקמים מקריבה את חייה על צוקי כוכב וורמיר כדי לאפשר להוקאיי לקבל את אבן הנשמה ב'סוף המשחק'?",
                        "options": ["נטשה רומנוף (האלמנה השחורה)", "נביולה", "גאמורה", "וונדה מקסימוף"],
                        "correct": 0,
                        "explanation": "נטשה רומנוף מקריבה את עצמה בקפיצה מהצוק בוורמיר כדי להשיג את אבן הנשמה ולהציל את היקום."
                    },
                    {
                        "q": "איזה כלי נשק אגדי מזמן קפטן אמריקה ונלחם באמצעותו מול תאנוס ברגע השיא של 'סוף המשחק'?",
                        "options": ["מיולניר (הפטיש של תור)", "סטורמברייקר (הגרזן של תור)", "כפפת האינסוף", "חרב הדרקון של ואלקירי"],
                        "correct": 0,
                        "explanation": "סטיב רוג'רס מוכיח שהוא ראוי ומרים את מיולניר, מה שגורם לתור לקרוא בשמחה: 'ידעתי את זה!'."
                    },
                    {
                        "q": "איזה משפט מפורסם אומר טוני סטארק רגע לפני שהוא נוקש באצבעותיו ומפורר את תאנוס וצבאו ב'סוף המשחק'?",
                        "options": ["'ואני... איירון מן' (And I... am... Iron Man)", "'אני הוא הבלתי נמנע'", "'הנוקמים, להתאחד!'", "'אנחנו הנוקמים'"],
                        "correct": 0,
                        "explanation": "לאחר שתאנוס מכריז 'אני בלתי נמנע', טוני מציג את האבנים על חליפתו ועונה 'ואני... איירון מן'."
                    },
                    {
                        "q": "לאיזה מקום שלו פורש תאנוס לחיות כאיכר פשוט לאחר שהשמיד מחצית מהיקום ב'מלחמת האינסוף'?",
                        "options": ["הגן (The Garden / Planet 0259-S)", "ראש-שום-מקום (Knowhere)", "טיטאן", "נידאווליר"],
                        "correct": 0,
                        "explanation": "תאנוס פורש לכוכב שליו המכונה 'הגן' ותולה את שריון הקרב שלו כדחליל בשדה."
                    },
                    {
                        "q": "באמצעות איזה מנגנון חוזרים הנוקמים בזמן לשנים 2012, 2013 ו-2014 בסרט 'סוף המשחק'?",
                        "options": ["מימד הקוונטים וחלקיקי פים (Pym Particles)", "טבעות השיגור של דוקטור סטריינג'", "גשר הביפרוסט של אסגרד", "מנוע טסרקט משודרג"],
                        "correct": 0,
                        "explanation": "בעזרת הידע של סקוט לאנג וחלקיקי פים, טוני סטארק מפתח 'GPS למרחב-זמן' המאפשר ניווט במימד הקוונטים."
                    },
                    {
                        "q": "איזה ביטוי מתוק אומרת בתו של טוני סטארק, מורגן, שהפך לאחד המשפטים המרגשים ביותר בסרט 'סוף המשחק'?",
                        "options": ["'אני אוהבת אותך 3,000' (I love you 3,000)", "'אתה הגיבור שלי'", "'אוהבת אותך עד הירח ובחזרה'", "'קודם כל צ'יזבורגר'"],
                        "correct": 0,
                        "explanation": "המשפט נלקח ישירות מחייו האמיתיים של רוברט דאוני ג'וניור, שילדיו נהגו לומר לו 'I love you 3,000'."
                    },
                    {
                        "q": "מי מפעיל את כבשן הכוכב הגוסס על נידאווליר וחושל את גרזן הקרב 'סטורמברייקר' עבור תור ב'מלחמת האינסוף'?",
                        "options": ["איטרי מלך הגמדים (פיטר דינקלג')", "הגראנדמאסטר", "האספן", "היימדל"],
                        "correct": 0,
                        "explanation": "איטרי מלך הננסים (אותו גילם פיטר דינקלג') מפעיל מחדש את הכבשן הקוסמי של נידאווליר."
                    },
                    {
                        "q": "מי אומר לתוך מכשיר הקשר את קריאת הקרב המיוחלת 'הנוקמים... התאחדו' (Avengers Assemble) ב'סוף המשחק'?",
                        "options": ["קפטן אמריקה (סטיב רוג'רס)", "איירון מן (טוני סטארק)", "תור", "ניק פיורי"],
                        "correct": 0,
                        "explanation": "סטיב רוג'רס לוחש 'Avengers... assemble' ברגע שבו כל צבאות הגיבורים מסתערים על צבאו של תאנוס."
                    },
                    {
                        "q": "כיצד נקראת בפי אזרחי העולם תקופת 5 השנים שבין היעלמות מחצית מהאוכלוסייה לחזרתם ב-2023?",
                        "options": ["הבליפ (The Blip)", "הדממה הגדולה", "עידן הריק", "החצי האפל"],
                        "correct": 0,
                        "explanation": "בעולם ה-MCU (כפי שהוצג ב'ספיידרמן: רחוק מהבית'), ההיעלמות והחזרה הפתאומית מכונות בשם 'הבליפ'."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 4: The Multiverse Saga & Modern Hits (2021–Present)
            # =================================================================
            {
                "id": "multiverse_saga_modern",
                "title": "סאגת המולטיוורס, ספיידרמן ודדפול (2021 ועד היום)",
                "description": "חציית יקומים מקבילים, רשות משתני הזמן (TVA) ומפגשי ענק היסטוריים.",
                "cards": [
                    {
                        "title": "ספיידרמן: אין דרך הביתה (No Way Home, 2021)",
                        "points": [
                            "ציון IMDb: 8.2/10 | בימוי: ג'ון וואטס | בכיכובם של טום הולנד, זנדאיה ובנדיקט קמברבאץ'.",
                            "איחוד רב-דורי היסטורי: הפגיש על המסך שלושה דורות של ספיידרמן: טובי מגווייר (סרטי סם ריימי), אנדרו גארפילד (סרטי מארק ווב) וטום הולנד (ה-MCU).",
                            "חזרת נבלים מיתולוגיים: וילם דפו (הגובלין הירוק), אלפרד מולינה (דוק אוק) וג'יימי פוקס (אלקטרו) חזרו לתפקידיהם דרך קרעים במולטיוורס.",
                            "סיום דרמטי: כדי למנוע את קריסת היקומים, פיטר פארקר מקריב את כל חייו האישיים ומבקש מדוקטור סטריינג' להטיל כישוף שיגרום לכל העולם לשכוח לחלוטין מיהו פיטר פארקר."
                        ]
                    },
                    {
                        "title": "דדפול & וולברין (Deadpool & Wolverine, 2024)",
                        "points": [
                            "ציון IMDb: 7.8/10 | בימוי: שון לוי | בכיכובם של ראיין ריינולדס (ווייד וילסון / דדפול) ויו ג'קמן (לוגאן / וולברין).",
                            "ציון דרך למבוגרים: הסרט הראשון בדירוג R (למבוגרים בלבד) ביקום הקולנועי של מארוול, שהכניס מעל 1.3 מיליארד דולר ברחבי העולם.",
                            "עלילה ותמות: דדפול נשלף מציר הזמן שלו על ידי ה-TVA, ומגייס גרסה פגועה של וולברין מיקום מקביל כדי להציל את עולמו מהשמדה באזור 'הריק' (The Void).",
                            "הופעות אורח מיתולוגיות: וסלי סנייפס שב כבלייד, צ'נינג טייטום כגמביט, כריס אוונס כג'וני סטורם, וג'ניפר גארנר כאלקטרה."
                        ]
                    },
                    {
                        "title": "שומרי הגלקסיה: חלק 3 (Vol. 3, 2023)",
                        "points": [
                            "ציון IMDb: 7.9/10 | תסריט ובימוי: ג'יימס גאן.",
                            "עלילה ורגש: שיר הפרידה המרגש של הרכב השומרים המקורי, החושף את עברו הטרגי של רוקט ראקון ויצירתו הגנטית בידי 'הוד התפתחותו' (High Evolutionary).",
                            "שיא גינס: שבר את שיא גינס הרשמי במספר פריטי האיפור התותב שנוצרו לסרט בודד (מעל 22,500 פריטי פרוסטטיקה ליותר מ-1,000 שחקנים)."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "אילו שלושה שחקנים הופיעו יחד על המסך כשלוש גרסאות שונות של פיטר פארקר ב'ספיידרמן: אין דרך הביתה' (2021)?",
                        "options": ["טום הולנד, טובי מגווייר ואנדרו גארפילד", "טום הולנד, מיילס מוראלס וניקולס קייג'", "טובי מגווייר, ג'ייק ג'ילנהול ואנדרו גארפילד", "טום הולנד, כריס פיין ושמייק מור"],
                        "correct": 0,
                        "explanation": "שלושת השחקנים שגילמו את ספיידרמן לאורך 20 שנה התאחדו על המסך כפיטר 1, פיטר 2 ופיטר 3."
                    },
                    {
                        "q": "איזה שחקן חזר לתפקיד הגובלין הירוק / נורמן אוסבורן ב'אין דרך הביתה' וביצע בעצמו את כל פעלולי הקרבות בגיל 66?",
                        "options": ["וילם דפו", "אלפרד מולינה", "תומאס היידן צ'רץ'", "ריס איוואנס"],
                        "correct": 0,
                        "explanation": "וילם דפו התעקש לבצע בעצמו את סצנות הקרב הפיזיות מול טום הולנד כנורמן אוסבורן."
                    },
                    {
                        "q": "איזה דירוג צפייה תקדימי קיבל הסרט 'דדפול & וולברין' (2024), בהיותו הסרט הראשון מסוג זה ב-MCU?",
                        "options": ["דירוג R (למבוגרים בלבד)", "דירוג PG-13", "דירוג NC-17", "דירוג G (לכל המשפחה)"],
                        "correct": 0,
                        "explanation": "'דדפול & וולברין' היה הסרט הראשון ב-MCU שקיבל דירוג R למבוגרים בלבד, ושבר את שיא ההכנסות לסרטי R בכל הזמנים."
                    },
                    {
                        "q": "איזו דמות קומיקס אגדית גילם צ'נינג טייטום בהופעת אורח מדוברת במיוחד בסרט 'דדפול & וולברין'?",
                        "options": ["גמביט (Gambit / רמי לבו)", "סייקלופס", "נייטקרולר", "בישופ"],
                        "correct": 0,
                        "explanation": "לאחר שנים של פיתוח סרט סולו שבוטל, צ'נינג טייטום הופיע כגמביט הזורק קלפי אנרגיה קינטית."
                    },
                    {
                        "q": "מי מתגלה כיוצרו האכזרי והאובססיבי של רוקט ראקון בסרט 'שומרי הגלקסיה: חלק 3'?",
                        "options": ["הוד התפתחותו (The High Evolutionary)", "הגראנדמאסטר", "אגו הכוכב החי", "רונאן המאשים"],
                        "correct": 0,
                        "explanation": "צ'וקוודי איווג'י גילם את 'הוד התפתחותו', מדען אכזר המשעבד יצורים חיים לצורך הנדסת גזע מושלם."
                    },
                    {
                        "q": "מה גורם הכישוף האחרון של דוקטור סטריינג' ב'אין דרך הביתה' כדי למנוע את פריצת המולטיוורס?",
                        "options": ["גורם לכל העולם לשכוח לחלוטין את קיומו של פיטר פארקר", "מוחק את קיומו של ספיידרמן", "מוחק את זכרונות הקרב על ניו יורק", "נועל את כדור הארץ בממד מקביל"],
                        "correct": 0,
                        "explanation": "הכישוף מוחק מזיכרון כולם את העובדה שפיטר פארקר קיים, ומשאיר את פיטר בודד ואנונימי לחלוטין."
                    },
                    {
                        "q": "איזה ארגון פועל מחוץ למרחב ולזמן כדי לפקח על צירי זמן ולגזום יקומים סוררים ב-MCU?",
                        "options": ["רשות משתני הזמן (TVA)", "חיל נובה (Nova Corps)", "הבוזזים (Ravagers)", "מועצת הזקנים העליונה"],
                        "correct": 0,
                        "explanation": "ה-TVA (Time Variance Authority) מפקחת על קווי הזמן ומנטרלת חריגות העלולות לגרום למלחמת יקומים."
                    },
                    {
                        "q": "איזה שחקן הפתיע את הקהל ב'דדפול & וולברין' כששב לגלם את ג'וני סטורם ('הלפיד האנושי') במקום את קפטן אמריקה?",
                        "options": ["כריס אוונס", "מייקל בי. ג'ורדן", "סבסטיאן סטן", "אנתוני מאקי"],
                        "correct": 0,
                        "explanation": "כריס אוונס חזר לתפקידו הישן משנת 2005 כג'וני סטורם מ'ארבעת המופלאים' וקרא 'Flame On!'."
                    },
                    {
                        "q": "איזה שיא גינס רשמי נשבר על ידי צוות ההפקה של 'שומרי הגלקסיה: חלק 3' (2023)?",
                        "options": ["מספר פריטי האיפור התותב (פרוסטטיקה) שנוצרו לסרט בודד (מעל 22,500)", "מספר הפעלולנים שהוצתו באש בסצנה אחת", "מספר מודלי ה-CGI שפותחו לקרבות חלל", "שוט ה-IMAX הרציף הארוך ביותר"],
                        "correct": 0,
                        "explanation": "צוות האיפור והאפקטים ייצר מעל 22,500 חלקי איפור ופרוסטטיקה עבור יותר מ-1,000 חייזרים וניצבים."
                    },
                    {
                        "q": "איזה במאי אימה מיתולוגי ביים את הסרט 'דוקטור סטריינג' בממדי הטירוף' (2022)?",
                        "options": ["סם ריימי", "סקוט דריקסון", "ג'יימס וואן", "גיירמו דל טורו"],
                        "correct": 0,
                        "explanation": "סם ריימי, במאי 'מוות אכזרי' וטרילוגיית 'ספיידרמן' המקורית, ביים את מותחן האימה הקוסמי של דוקטור סטריינג'."
                    }
                ]
            },
            # =================================================================
            # CATEGORY 5: Marvel Lore, Stan Lee Cameos & Behind-The-Scenes Secrets
            # =================================================================
            {
                "id": "lore_cameos_secrets",
                "title": "סודות מארוול, הופעות סטן לי וטריוויה מאחורי הקלעים",
                "description": "איסטר אגס, מחוות ליוצרי הקומיקס וליהוקים כמעט-אחרים ששינו את תולדות הקולנוע.",
                "cards": [
                    {
                        "title": "סטן לי: אבי הופעות האורח הקולנועיות של מארוול",
                        "points": [
                            "מורשת אגדית: יוצר הקומיקס המיתולוגי סטן לי (1922–2018) הופיע ב-22 סרטי MCU החל מ'איירון מן' (2008) ועד להופעתו האחרונה לאחר מותו ב'סוף המשחק' (כנהג היפי משנות ה-70).",
                            "תיאוריית 'הצופים' (The Watchers): ב'שומרי הגלקסיה: חלק 2', סטן לי מוצג בחליפת חלל כשהוא מדווח על הרפתקאותיו בכדור הארץ לגזע 'הצופים' הקוסמי, מה שאימת את תיאוריית המעריצים שהוא מגלם את אותו סוכן מידע קוסמי בכל הסרטים."
                        ]
                    },
                    {
                        "title": "ליהוקים שכמעט קרו ב-MCU",
                        "points": [
                            "איירון מן: הנהלת מארוול התנגדה בתחילה לרוברט דאוני ג'וניור ורצתה את טום קרוז או ניקולס קייג', אך ג'ון פאברו נלחם בעקשנות עבור דאוני.",
                            "האלמנה השחורה: אמילי בלאנט לוהקה במקור לתפקיד נטשה רומנוף ב'איירון מן 2', אך נאלצה לפרוש עקב מחויבות חוזית לסרט 'מסעות גוליבר', מה שפתח את הדלת לסקרלט ג'והנסון.",
                            "סטאר לורד: גלן האוורטון (דניס ב'פילדלפיה זורחת') היה הבחירה השנייה של ג'יימס גאן אם כריס פראט היה מסרב."
                        ]
                    },
                    {
                        "title": "מסורת סצנות אחרי-הכתוביות",
                        "points": [
                            "מנהג חובה: החל מניק פיורי ב-2008, סצנות אחרי-הכתוביות הפכו לחלק בלתי נפרד מחוויית הצפייה בקולנוע.",
                            "המבנה הכפול: מארוול פיתחה מבנה מקובל של שתי סצנות: סצנת אמצע-הכתוביות המקדמת קווי עלילה עתידיים, וסצנת סיום-כתוביות קומית המעניקה בדיחה או איסטר אג (כגון קפטן אמריקה שמדבר על סבלנות בסיום 'ספיידרמן: השיבה הביתה')."
                        ]
                    }
                ],
                "questions": [
                    {
                        "q": "באיזה סרט MCU הופיע סטן לי בהופעת האורח הקולנועית האחרונה שלו שיצאה לאקרנים לאחר מותו?",
                        "options": ["הנוקמים: סוף המשחק (2019)", "ספיידרמן: רחוק מהבית (2019)", "קפטן מארוול (2019)", "הנוקמים: מלחמת האינסוף (2018)"],
                        "correct": 0,
                        "explanation": "הופעתו האחרונה של סטן לי הייתה ב'סוף המשחק', שבה הופיע בגרסה צעירה דיגיטלית כנהג היפי שנוסע ליד בסיס צבאי וצועק 'Hey man, make love, not war!'."
                    },
                    {
                        "q": "איזו שחקנית לוהקה במקור לתפקיד האלמנה השחורה ב'איירון מן 2' אך נאלצה לפרוש עקב התנגשות בלוחות זמנים?",
                        "options": ["אמילי בלאנט", "ג'סיקה צ'סטיין", "שרליז ת'רון", "רייצ'ל מקאדמס"],
                        "correct": 0,
                        "explanation": "אמילי בלאנט נאלצה לפרוש עקב חוזה קודם לצילומי 'מסעות גוליבר', והתפקיד עבר לסקרלט ג'והנסון."
                    },
                    {
                        "q": "ב'שומרי הגלקסיה: חלק 2', עם איזה גזע קוסמי עתיק יושב סטן לי ומספר על עלילותיו בכדור הארץ?",
                        "options": ["הצופים (The Watchers)", "הסלסטיאלים (The Celestials)", "זקני היקום", "הבינה העליונה של הקרי"],
                        "correct": 0,
                        "explanation": "סטן לי נראה בחליפת אסטרונאוט משוחח עם גזע 'הצופים' (The Watchers), המתעדים את כל מאורעות היקום מבלי להתערב."
                    },
                    {
                        "q": "על איזה נושא מדבר קפטן אמריקה בסרטון הדרכה קומי בסצנת סיום הכתוביות של 'ספיידרמן: השיבה הביתה' (2017)?",
                        "options": ["מעלת הסבלנות (תוך עקיצה על הקהל שמחכה לסצנות אחרי הכתוביות)", "חשיבות אכילת ארוחות צהריים בבית הספר", "שמירה על היגיינת שיניים", "מדוע טיפוס על חבל בשיעור ספורט בונה אופי"],
                        "correct": 0,
                        "explanation": "קפטן אמריקה פונה ישירות לקהל באולם ומסביר שסבלנות היא מעלה חשובה, אך לעיתים ממתינים זמן רב למשהו מאכזב."
                    },
                    {
                        "q": "איזו דמות ביקום גילם הבמאי טאיקה וואיטיטי בעצמו בחליפת לכידת תנועה בסרט 'תור: ראגנארוק'?",
                        "options": ["קורג (הגלדיאטור העשוי אבן)", "מיק", "סירטיר (Surtur)", "הזאב פנריס"],
                        "correct": 0,
                        "explanation": "טאיקה וואיטיטי לבש חליפת לכידת תנועה ודיבב במבטא ניו זילנדי עדין את דמותו של קורג איש האבן."
                    },
                    {
                        "q": "איזה שיר של להקת AC/DC טועה פיטר פארקר לחשוב שהוא של 'לד זפלין' ב'ספיידרמן: רחוק מהבית'?",
                        "options": ["Back in Black", "Highway to Hell", "Thunderstruck", "TNT"],
                        "correct": 0,
                        "explanation": "כשהפי הוגאן מנגן את השיר המפורסם 'Back in Black' של AC/DC, פיטר מתלהב וקורא: 'אני מת על לד זפלין!'."
                    },
                    {
                        "q": "כיצד נקרא גשר האור הקוסמי של אסגרד המופעל בידי היימדל ומשגר לוחמים בין תשעת העולמות?",
                        "options": ["הביפרוסט (The Bifrost)", "קרן איגדרסיל", "שער ולהאלה", "צינור אסגרד"],
                        "correct": 0,
                        "explanation": "הביפרוסט (The Bifrost) הוא גשר הקשת הקוסמי שבאמצעותו משתגרים בני אסגרד באופן מיידי ברחבי היקום."
                    },
                    {
                        "q": "איזה יצור חייזרי מסוכן היא החתולה הג'ינג'ית גוס בסרט 'קפטן מארוול' (2019)?",
                        "options": ["פלרקן (Flerken)", "סקרול", "כלב צ'יטאורי", "חיית קרי"],
                        "correct": 0,
                        "explanation": "גוס נראית כחתולה תמימה אך היא למעשה פלרקן (Flerken) – יצור בעל זרועות ענק וממדים פנימיים המסוגל לבלוע אובייקטים עצומים."
                    },
                    {
                        "q": "מיהו נשיא אולפני מארוול והארכיטקט הראשי שהוביל והפיק את כל סרטי היקום הקולנועי מאז 2008?",
                        "options": ["קווין פייגי", "אבי ארד", "בוב איגר", "לואי ד'אספוסיטו"],
                        "correct": 0,
                        "explanation": "קווין פייגי הוא המוח והמפיק הראשי מאחורי בניית היקום הקולנועי המצליח ביותר בהיסטוריה."
                    },
                    {
                        "q": "איזה פריט מפורסם מרסק תאנוס בחרבו הדו-להבית בקרב האלים מול שלושת הגיבורים ב'סוף המשחק'?",
                        "options": ["מגן הויברניום של קפטן אמריקה", "קסדת הננו-טק של איירון מן", "ידית העץ של סטורמברייקר", "הקשת הטקטית של הוקאיי"],
                        "correct": 0,
                        "explanation": "תאנוס מכה שוב ושוב בחרבו הדו-להבית הכבדה ומנפץ לשניים את מגן הויברניום של קפטן אמריקה."
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
    print(f"Wrote English MCU topic to {TARGET_EN}")

    with open(TARGET_HE, 'w', encoding='utf-8') as f:
        yaml.dump(he_data, f, allow_unicode=True, sort_keys=False, width=120)
    print(f"Wrote Hebrew MCU topic to {TARGET_HE}")

if __name__ == "__main__":
    create_mcu_datasets()
