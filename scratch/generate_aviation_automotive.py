#!/usr/bin/env python3
"""
Generates the Automotive & Aviation Pioneers (aviation_automotive) topic
in both English (aviation_automotive_en.yaml) and Hebrew (aviation_automotive_he.yaml).
Follows rich storytelling format, 100% 4-option multiple choice, domain-aligned distractors,
and dedicated 'explanation' fields for Learn More context.
"""
import os
import yaml

TARGET_EN = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/aviation_automotive_en.yaml"
TARGET_HE = "/Users/orishmuel/Library/CloudStorage/GoogleDrive-ori.shmuel@gmail.com/My Drive/Apps/Shmuel's Trivia App/topics/aviation_automotive_he.yaml"

def create_aviation_automotive_datasets():
    # -------------------------------------------------------------------------
    # ENGLISH DATASET
    # -------------------------------------------------------------------------
    aa_en = {
        "id": "aviation_automotive_en",
        "title": "Aviation & Automotive Pioneers",
        "description": "From the sands of Kitty Hawk and the rumble of the first assembly lines to supersonic jets and iconic supercars: explore the daring engineers and record-breaking machines that conquered land and sky.",
        "lang": "en",
        "audience": "family",
        "categories": [
            # =================================================================
            # CATEGORY 1: Important Facts
            # =================================================================
            {
                "id": "important_facts",
                "title": "Important Facts & Milestones",
                "description": "Essential historical milestones and revolutionary engineering breakthroughs in flight and road transport.",
                "cards": [
                    {
                        "title": "The Wright Brothers (1903)",
                        "points": [
                            "On December 17, 1903, at Kitty Hawk, North Carolina, Orville and Wilbur Wright achieved the first sustained, controlled, powered heavier-than-air flight.",
                            "Their crucial breakthrough was not raw horsepower, but 3-axis aerodynamic control: wing-warping for roll, an elevator for pitch, and a rudder for yaw.",
                            "Orville made the historic first flight, staying airborne for 12 seconds and covering 120 feet (36.5 meters) in the Wright Flyer I.",
                            "Wilbur completed the longest flight of that day, flying 852 feet (260 meters) in 59 seconds."
                        ]
                    },
                    {
                        "title": "Henry Ford & The Moving Assembly Line (1913)",
                        "points": [
                            "In 1913, Henry Ford introduced the moving assembly line at the Highland Park plant in Michigan, revolutionizing global manufacturing.",
                            "The assembly line reduced the time required to build a single Model T automobile from 12 hours down to just 93 minutes.",
                            "Mass production allowed Ford to slash the car's price from $850 in 1908 to under $300 in the 1920s, making car ownership accessible to everyday workers.",
                            "Ford paid his workers an unprecedented $5 per day (double the industry average), creating an empowered middle-class consumer base."
                        ]
                    },
                    {
                        "title": "Breaking the Sound Barrier: Chuck Yeager (1947)",
                        "points": [
                            "On October 14, 1947, US Air Force test pilot Chuck Yeager became the first human to officially break the sound barrier (Mach 1.0).",
                            "He flew the rocket-powered Bell X-1, nicknamed 'Glamorous Glennis' after his wife, reaching Mach 1.06 (700 mph / 1,127 km/h) at 43,000 feet.",
                            "The Bell X-1 was shaped like a .50-caliber machine gun bullet, known to be aerodynamically stable at supersonic speeds.",
                            "Yeager flew the historic mission with two broken ribs sustained in a horseback riding accident two nights prior."
                        ]
                    },
                    {
                        "title": "The Boeing 747 'Queen of the Skies' (1969)",
                        "points": [
                            "First flown in 1969, the Boeing 747 was the world's first wide-body commercial airliner (the 'Jumbo Jet').",
                            "Its distinctive upper-deck hump was designed because engineers anticipated supersonic airliners would make passenger jets obsolete, allowing easy conversion into a nose-loading cargo freighter.",
                            "The 747 could seat over 400 passengers, slashing per-seat flight costs and democratizing international travel for millions worldwide.",
                            "It remained the world's largest passenger aircraft for 37 consecutive years until the Airbus A380 debuted in 2005."
                        ]
                    },
                    {
                        "title": "The Concorde: Supersonic Commercial Travel (1969)",
                        "points": [
                            "Developed jointly by Britain and France, the Concorde flew passengers across the Atlantic Ocean at Mach 2.04 (1,354 mph / 2,179 km/h) — over twice the speed of sound.",
                            "A flight from London or Paris to New York took less than 3.5 hours, allowing travelers to arrive in New York 'earlier' local time than when they departed Europe.",
                            "Cruising at 60,000 feet (18,000 meters), passengers could clearly see the curvature of the Earth and the blackness of space above.",
                            "Friction with air at Mach 2 heated the aircraft's aluminum skin up to 127°C, causing the fuselage to expand by 15 to 30 cm (6 to 12 inches) in mid-flight!"
                        ]
                    },
                    {
                        "title": "The Lockheed SR-71 Blackbird (1964)",
                        "points": [
                            "The SR-71 Blackbird remains the fastest air-breathing manned aircraft in history, capable of sustained flight above Mach 3.3 (2,200+ mph / 3,540 km/h) at 85,000 feet.",
                            "Built with 93% titanium to withstand atmospheric friction temperatures exceeding 300°C, the US secretly procured titanium from the Soviet Union through dummy companies.",
                            "Because titanium expands when heated, the fuel tanks were designed with loose gaps that leaked jet fuel on the runway until friction heated and sealed the skin during flight.",
                            "If an enemy surface-to-air missile was fired at the SR-71, the standard evasion protocol was simple: pilot just pushed the throttle forward and outran the missile!"
                        ]
                    },
                    {
                        "title": "The McLaren F1: Analogue Supercar Perfection (1992)",
                        "points": [
                            "Designed by Formula 1 genius Gordon Murray, the McLaren F1 set a world production car top speed record of 240.1 mph (386.4 km/h) in 1998.",
                            "It featured a revolutionary 3-seat cockpit with the driver positioned centrally in the middle for perfect visibility and weight distribution.",
                            "Its engine bay was lined with 16 grams of pure 24-karat gold foil to serve as the ultimate lightweight heat reflector for the BMW 6.1-liter V12 engine.",
                            "It was the first production road car built with a full carbon-fiber monocoque chassis."
                        ]
                    },
                    {
                        "title": "The Electric Revolution: Tesla Model S (2012)",
                        "points": [
                            "Launched in 2012, the Tesla Model S proved that electric vehicles could outperform traditional gas-powered luxury sedans in range, speed, and safety.",
                            "Placing the heavy lithium-ion battery pack flat along the floorpan created a low center of gravity and eliminated the front engine, creating a front trunk ('frunk') and superior crash crumple zones.",
                            "Equipped with dual electric motors, its 'Ludicrous' and 'Plaid' modes achieved 0–60 mph acceleration times under 2.0 seconds, out-accelerating multimillion-dollar hypercars.",
                            "It pioneered over-the-air (OTA) software updates, enabling vehicles to receive performance boosts and autonomous driving improvements overnight."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What was the key aerodynamic breakthrough the Wright Brothers patented that enabled controlled flight in 1903?",
                        "options": [
                            "Three-axis aerodynamic control (roll, pitch, and yaw) via wing-warping, elevator, and rudder",
                            "Jet turbine propulsion with afterburners",
                            "Pressurized aluminum fuselages",
                            "Automatic satellite GPS navigation"
                        ],
                        "correct": 0,
                        "explanation": "While earlier inventors focused only on engine power, the Wright Brothers designed 3-axis aerodynamic flight control (wing-warping for roll, elevator for pitch, rudder for yaw), which remains the basis for all modern aircraft."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In what year and location did the Wright Brothers achieve the world's first sustained, powered heavier-than-air flight?",
                        "options": [
                            "1903 at Kitty Hawk, North Carolina",
                            "1912 in Paris, France",
                            "1895 in Dayton, Ohio",
                            "1920 in London, England"
                        ],
                        "correct": 0,
                        "explanation": "On December 17, 1903, on the sandy dunes of Kitty Hawk, North Carolina, Orville Wright flew 120 feet in 12 seconds aboard the Wright Flyer I."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How dramatically did Henry Ford's moving assembly line reduce the production time of a single Model T car in 1913?",
                        "options": [
                            "From 12 hours down to just 93 minutes",
                            "From 30 days down to 24 hours",
                            "From 5 hours down to 4 hours",
                            "From 2 weeks down to 10 days"
                        ],
                        "correct": 0,
                        "explanation": "By bringing the car to the worker via a continuous moving conveyor line, Ford slashed Model T assembly time from 12 hours to just 93 minutes."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Who was the test pilot who first broke the sound barrier in level flight aboard the Bell X-1 in 1947?",
                        "options": [
                            "Chuck Yeager",
                            "Neil Armstrong",
                            "Charles Lindbergh",
                            "Howard Hughes"
                        ],
                        "correct": 0,
                        "explanation": "On October 14, 1947, US Air Force Captain Chuck Yeager piloted the rocket-powered Bell X-1 past Mach 1.0 (700 mph) at 43,000 feet."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why was the Boeing 747 originally designed with its iconic upper-deck cockpit hump?",
                        "options": [
                            "To allow the front nose to swing open for cargo loading in case supersonic airliners replaced passenger jets",
                            "To house a luxury passenger cocktail bar and swimming pool",
                            "To hold an emergency parachute for the entire aircraft",
                            "To store spare jet engine parts"
                        ],
                        "correct": 0,
                        "explanation": "Boeing anticipated supersonic passenger jets (like Concorde) would take over passenger routes, so they designed the 747's cockpit high up to allow the nose to open for cargo containers."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How long did a supersonic transatlantic crossing on the Concorde take between London/Paris and New York?",
                        "options": [
                            "Under 3.5 hours",
                            "About 7 hours",
                            "12 hours",
                            "1 hour"
                        ],
                        "correct": 0,
                        "explanation": "Cruising at Mach 2.04 (over 1,350 mph), the Concorde made the transatlantic crossing in approximately 3 hours and 15 to 30 minutes (compared to ~8 hours on conventional jets)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What unusual metal comprised 93% of the supersonic Lockheed SR-71 Blackbird's airframe to withstand 300°C friction heat?",
                        "options": [
                            "Titanium",
                            "Cast iron",
                            "Lead",
                            "Pure copper"
                        ],
                        "correct": 0,
                        "explanation": "The SR-71 was built almost entirely of lightweight titanium alloy, covertly purchased by the CIA from the Soviet Union through dummy overseas corporations."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What unique cockpit seating layout was designed for the legendary 1992 McLaren F1 supercar?",
                        "options": [
                            "A central driver seat flanked by two passenger seats set slightly back",
                            "Two tandem seats with the driver in front of the passenger",
                            "A single seat with no passenger capacity",
                            "Four bucket seats in a 2+2 arrangement"
                        ],
                        "correct": 0,
                        "explanation": "Gordon Murray designed the McLaren F1 with a central driver seat for optimal visibility, pedal alignment, and vehicle weight distribution."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why was pure 24-karat gold foil used inside the engine compartment of the McLaren F1?",
                        "options": [
                            "As an exceptionally efficient lightweight thermal heat reflector to shield the carbon fiber body",
                            "To add luxury aesthetics for high-paying buyers",
                            "To conduct electricity between the spark plugs and battery",
                            "To increase the resale auction price"
                        ],
                        "correct": 0,
                        "explanation": "Gold is one of the best reflectors of infrared heat in physics; 16 grams of gold foil lined each engine bay to protect the carbon-fiber monocoque from the roaring V12 exhaust heat."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What standard defense protocol was used by SR-71 Blackbird pilots when targeted by enemy surface-to-air missiles?",
                        "options": [
                            "Accelerate and outrun the missile at speeds exceeding Mach 3.2",
                            "Deploy radar-guided anti-missile flares",
                            "Dive into low-altitude canyons to hide from radar",
                            "Perform sharp 360-degree aerial barrel rolls"
                        ],
                        "correct": 0,
                        "explanation": "Because the SR-71 flew at 85,000 feet above Mach 3.2, its evasion protocol was simply accelerating; no missile in history ever caught an operational Blackbird."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What happened to the physical length of the supersonic Concorde during flight due to aerodynamic friction heat?",
                        "options": [
                            "The fuselage expanded in length by 15 to 30 cm (6 to 12 inches)",
                            "The aircraft shrank by 2 meters due to high atmospheric pressure",
                            "The wings detached and folded backwards automatically",
                            "The tail fin rotated 90 degrees"
                        ],
                        "correct": 0,
                        "explanation": "Skin friction at Mach 2 heated the airframe up to 127°C, causing the aluminum structure to thermally expand by up to 30 cm, creating visible gaps inside the cabin floorboards during flight."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In what year did Henry Ford introduce his famous $5 per day wage, doubling the standard industrial pay rate?",
                        "options": [
                            "1914",
                            "1939",
                            "1890",
                            "1960"
                        ],
                        "correct": 0,
                        "explanation": "In January 1914, Ford announced the $5-a-day wage for an 8-hour workday, drastically reducing worker turnover and allowing factory workers to buy the very cars they built."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What was the top speed record achieved by the naturally aspirated McLaren F1 XP5 prototype in 1998?",
                        "options": [
                            "240.1 mph (386.4 km/h)",
                            "190.5 mph (306.5 km/h)",
                            "304.7 mph (490.4 km/h)",
                            "155.0 mph (249.4 km/h)"
                        ],
                        "correct": 0,
                        "explanation": "Driver Andy Wallace reached 240.1 mph at the Ehra-Lessien test track in Germany, cementing the McLaren F1 as the fastest naturally aspirated production car in history."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What design feature of modern electric vehicles (like the Tesla Model S) provides an exceptionally low center of gravity?",
                        "options": [
                            "A heavy flat battery pack mounted along the bottom floorpan of the chassis",
                            "A lightweight titanium rear spoiler",
                            "Narrow aerodynamic carbon fiber wheels",
                            "A cast-iron transmission gearbox"
                        ],
                        "correct": 0,
                        "explanation": "Mounting the massive lithium-ion battery pack as a flat slab between the axles along the vehicle floor creates an ultra-low center of gravity, virtually eliminating rollover risk and enhancing cornering grip."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What was the name of the historic single-engine aircraft in which Charles Lindbergh completed the first solo nonstop transatlantic flight in 1927?",
                        "options": [
                            "Spirit of St. Louis",
                            "Glamorous Glennis",
                            "Wright Flyer",
                            "Enola Gay"
                        ],
                        "correct": 0,
                        "explanation": "Charles Lindbergh flew the custom-built 'Spirit of St. Louis' from Long Island, New York to Paris, France on May 20–21, 1927, completing the 3,600-mile flight in 33.5 hours."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 2: Aviation Legends & Historic Aircraft
            # =================================================================
            {
                "id": "aviation_legends",
                "title": "Aviation Legends & Breakthrough Aircraft",
                "description": "The most famous and iconic flying machines that revolutionized warfare, commercial flight, and stealth technology.",
                "cards": [
                    {
                        "title": "The Douglas DC-3 (1935)",
                        "points": [
                            "Introduced in 1935, the Douglas DC-3 is widely regarded as the plane that created the modern commercial airline industry.",
                            "It was the first passenger aircraft capable of making airline travel profitable on passenger fares alone, without government mail subsidies.",
                            "During World War II, over 10,000 military transport versions (the C-47 Skytrain / Dakota) were built, dropping paratroopers on D-Day.",
                            "Its rugged twin-engine design was so durable that hundreds of original DC-3s are still flying commercial cargo and passenger routes today, nearly 90 years later!"
                        ]
                    },
                    {
                        "title": "The Supermarine Spitfire (1936)",
                        "points": [
                            "Designed by R.J. Mitchell, the Spitfire was the iconic British single-seat fighter that defended the UK during the 1940 Battle of Britain.",
                            "It featured distinctive thin Elliptical Wings designed to minimize aerodynamic induced drag while accommodating eight machine guns and landing gear.",
                            "Powered by the legendary Rolls-Royce Merlin V12 engine, its distinct supercharger whine became a symbol of British wartime resilience.",
                            "It was continuously upgraded throughout the war, flying from an initial top speed of 360 mph up to over 450 mph in later variants."
                        ]
                    },
                    {
                        "title": "The Lockheed SR-71 Blackbird (1964)",
                        "points": [
                            "Engineered at Lockheed's top-secret 'Skunk Works' under Kelly Johnson, the SR-71 performed strategic high-altitude reconnaissance.",
                            "Its Pratt & Whitney J58 engines functioned as conventional turbojets at low speeds, but converted into continuous-bleed Ramjets above Mach 2.",
                            "At Mach 3+, the cockpit windshield reached 330°C and was made of special 1.25-inch thick quartz crystal glass.",
                            "Pilots wore full high-altitude pressurized space suits equipped with 100% oxygen systems, virtually identical to astronaut gear."
                        ]
                    },
                    {
                        "title": "The B-2 Spirit Stealth Bomber (1989)",
                        "points": [
                            "The Northrop Grumman B-2 Spirit is a long-range flying-wing stealth bomber with no vertical tail fin.",
                            "Its radar cross-section is smaller than a large bumblebee, allowing it to penetrate sophisticated integrated air defense networks undetected.",
                            "It utilizes continuous-curvature smooth surfaces and radar-absorbent radar-ferrite coatings to scatter and absorb electromagnetic waves.",
                            "With an original cost of over $2 billion per aircraft, it is the most expensive airplane ever built."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What aerodynamic wing design gave the Supermarine Spitfire exceptional turning agility and low induced drag during the Battle of Britain?",
                        "options": [
                            "Elliptical wings",
                            "Delta swept-back wings",
                            "Variable-geometry swing wings",
                            "Biplane staggered wings"
                        ],
                        "correct": 0,
                        "explanation": "R.J. Mitchell chose thin elliptical wings to give the Spitfire the lowest possible induced drag while providing internal volume for guns and ammunition."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is the Douglas DC-3 (introduced in 1935) considered the most influential airliner in early commercial aviation?",
                        "options": [
                            "It was the first airliner capable of making a profit carrying passengers alone without government mail subsidies",
                            "It was the first jet-powered aircraft to cross the Pacific Ocean",
                            "It featured nuclear propulsion",
                            "It had sleeping berths for 200 passengers"
                        ],
                        "correct": 0,
                        "explanation": "The DC-3 was fast, comfortable, and reliable; its economics allowed airlines to turn a profit on ticket sales alone, establishing commercial passenger travel worldwide."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How small is the radar cross-section of the massive B-2 Spirit Stealth Bomber on radar screens?",
                        "options": [
                            "About the size of a large bumblebee or bird",
                            "About the size of an ocean cruise ship",
                            "About the size of a football stadium",
                            "About the size of a standard school bus"
                        ],
                        "correct": 0,
                        "explanation": "Despite having a 172-foot wingspan, the B-2's flying-wing geometry and radar-absorbent materials reduce its radar cross-section to approximately 0.001 square meters (similar to a bumblebee)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What iconic engine powered both the British Supermarine Spitfire and the American P-51 Mustang fighters during World War II?",
                        "options": [
                            "Rolls-Royce Merlin V12",
                            "Pratt & Whitney J58",
                            "General Electric GE90",
                            "BMW 801 Radial"
                        ],
                        "correct": 0,
                        "explanation": "The liquid-cooled 27-liter Rolls-Royce Merlin V12 engine was legendary for its reliability and two-stage supercharged high-altitude power."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "How did the Pratt & Whitney J58 engines on the SR-71 Blackbird operate at speeds above Mach 2?",
                        "options": [
                            "They diverted bypass air around the compressor directly into the afterburner, acting effectively as Ramjets",
                            "They turned off the turbines and fired solid rocket boosters",
                            "They switched to hydrogen fuel cell electrical motors",
                            "They opened water-injection steam vents"
                        ],
                        "correct": 0,
                        "explanation": "Above Mach 2, six bypass bleed tubes routed high-pressure air directly into the afterburner, turning the turbojet into a turboramjet for extreme efficiency at Mach 3+."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary function of the 'droop snoot' movable nose on the supersonic Concorde airliner?",
                        "options": [
                            "To lower the nose during takeoff and landing so pilots could see the runway over the high angle-of-attack delta wing",
                            "To catch rainwater for internal cooling",
                            "To deploy a forward laser radar sensor",
                            "To serve as an aerodynamic air brake during supersonic cruise"
                        ],
                        "correct": 0,
                        "explanation": "Because delta-wing aircraft land at a steep nose-up angle, the Concorde featured a hydraulically lowered nose cone so pilots could see the runway during approach and taxi."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What famous engineering division at Lockheed, led by Kelly Johnson, developed the U-2, SR-71 Blackbird, and F-117 Nighthawk?",
                        "options": [
                            "Skunk Works (Advanced Development Programs)",
                            "Phantom Works",
                            "Bell Labs",
                            "Bratwurst Works"
                        ],
                        "correct": 0,
                        "explanation": "Lockheed's legendary 'Skunk Works' pioneered rapid prototyping and top-secret aerospace engineering, producing the world's most advanced spy planes and stealth fighters."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the world's largest commercial passenger airliner ever built (a full double-deck aircraft)?",
                        "options": [
                            "Airbus A380",
                            "Boeing 747-400",
                            "Concorde",
                            "Antonov An-225"
                        ],
                        "correct": 0,
                        "explanation": "The Airbus A380, introduced in 2005, features a full-length double-deck cabin capable of carrying over 850 passengers in maximum single-class configuration."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What was the first operational military aircraft to utilize stealth technology with faceted reflective panels?",
                        "options": [
                            "Lockheed F-117 Nighthawk",
                            "F-22 Raptor",
                            "B-52 Stratofortress",
                            "F-16 Fighting Falcon"
                        ],
                        "correct": 0,
                        "explanation": "First flying in 1981, the F-117 Nighthawk 'Stealth Fighter' used faceted flat angled surfaces calculated by computer algorithms to reflect radar beams away from receiver antennas."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which heavy cargo aircraft, destroyed in 2022, held the record as the heaviest and longest wingspan operational airplane ever built?",
                        "options": [
                            "Antonov An-225 Mriya",
                            "Boeing C-17 Globemaster",
                            "Lockheed C-5 Galaxy",
                            "Airbus BelugaXL"
                        ],
                        "correct": 0,
                        "explanation": "The six-engine Antonov An-225 'Mriya' (Dream) had a maximum takeoff weight of 640 tonnes and held world records for the heaviest single piece of airlifted cargo."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 3: Automotive Pioneers & Iconic Supercars
            # =================================================================
            {
                "id": "automotive_pioneers_supercars",
                "title": "Automotive Pioneers & Iconic Supercars",
                "description": "The evolution of the automobile from three-wheeled motor carriages to 1,000-horsepower hypercars and mid-engine engineering marvels.",
                "cards": [
                    {
                        "title": "Karl Benz & The Benz Patent-Motorwagen (1886)",
                        "points": [
                            "Karl Benz is recognized as the inventor of the modern gasoline automobile with his 1886 German patent #37435.",
                            "The three-wheeled Motorwagen featured a 0.75-horsepower single-cylinder four-stroke engine and tubular steel chassis.",
                            "In August 1888, his wife Bertha Benz took the car on the world's first long-distance road trip (66 miles / 106 km) without telling him, buying cleaning benzine from pharmacies as fuel and fixing the brakes with leather shoe sole pads!",
                            "Bertha's historic journey generated global headlines, proving that the horseless carriage was practical transportation rather than a toy."
                        ]
                    },
                    {
                        "title": "The Lamborghini Miura: Birth of the Supercar (1966)",
                        "points": [
                            "Unveiled at the 1966 Geneva Motor Show, the Lamborghini Miura is widely recognized as the world's first true mid-engine Supercar.",
                            "Designed by Marcello Gandini at Bertone, it housed a transverse mid-mounted 3.9-liter V12 engine positioned directly behind the driver's head.",
                            "Prior to the Miura, high-performance sports cars placed engines in the front; the Miura brought race-car mid-engine balance and exotic styling to the street.",
                            "With a top speed of 174 mph (280 km/h), it was the fastest production road car in the world when launched."
                        ]
                    },
                    {
                        "title": "The Ferrari 250 GTO (1962)",
                        "points": [
                            "Only 36 Ferrari 250 GTOs were handcrafted between 1962 and 1964 to compete in the FIA Group 3 Grand Touring car category.",
                            "Powered by a 3.0-liter Tipo 168 Colombo V12 producing 300 horsepower, it dominated sports car endurance racing worldwide.",
                            "Buyers originally had to be personally approved by Enzo Ferrari and paid an initial price of $18,000 in 1962.",
                            "Today, the 250 GTO is the most valuable collector car in history, with individual examples selling at private auction for over $70 million!"
                        ]
                    },
                    {
                        "title": "The Bugatti Veyron 16.4: The 1,000-Horsepower Monster (2005)",
                        "points": [
                            "Volkswagen Group Chairman Ferdinand Piëch set an impossible engineering challenge: build a production road car with over 1,000 hp that could exceed 250 mph (400 km/h) yet drive comfortably to the opera.",
                            "The Veyron was powered by an 8.0-liter quad-turbocharged W16 engine producing 1,001 metric horsepower and 1,250 Nm of torque.",
                            "To keep the engine and transmission from melting, it required 10 separate cooling radiators and specialized Michelin tires that cost $25,000 per set.",
                            "It set a Guinness World Record top speed of 253.81 mph (408.47 km/h), followed by the Super Sport variant at 267.85 mph (431 km/h)."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "Who undertook the world's first long-distance automobile journey in 1888, proving the practical value of the motor car?",
                        "options": [
                            "Bertha Benz (wife of Karl Benz)",
                            "Henry Ford",
                            "Enzo Ferrari",
                            "Ferdinand Porsche"
                        ],
                        "correct": 0,
                        "explanation": "Bertha Benz drove the Patent-Motorwagen 66 miles from Mannheim to Pforzheim in August 1888, purchasing solvent fuel from pharmacies along the way and inventing brake lining pads."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which car is universally credited with creating the modern mid-engine exotic supercar layout when launched in 1966?",
                        "options": [
                            "Lamborghini Miura",
                            "Ford Model T",
                            "Volkswagen Beetle",
                            "Chevrolet Corvette"
                        ],
                        "correct": 0,
                        "explanation": "The 1966 Lamborghini Miura mounted its glorious 3.9L V12 transversely behind the cockpit, establishing the mid-engine architecture for all modern supercars."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What engine configuration was engineered for the 250+ mph Bugatti Veyron in 2005?",
                        "options": [
                            "8.0-liter quad-turbocharged W16 engine",
                            "Naturally aspirated inline-4 engine",
                            "Single-rotor Wankel rotary engine",
                            "Twin-cylinder two-stroke diesel engine"
                        ],
                        "correct": 0,
                        "explanation": "The Bugatti Veyron utilized a quad-turbocharged W16 engine (essentially two V8 engines sharing a common crankshaft) producing 1,001 horsepower."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Why is the 1962–1964 Ferrari 250 GTO considered the 'Holy Grail' of collector cars, fetching over $70 million at auction?",
                        "options": [
                            "Only 36 were built, combining unmatched racing pedigree, handmade aluminum bodywork, and a screaming Colombo V12",
                            "It was the first automobile equipped with automatic transmission",
                            "It had solar panels built into the roof",
                            "It was manufactured entirely out of solid titanium"
                        ],
                        "correct": 0,
                        "explanation": "With only 36 cars handcrafted, multiple World Championship victories, and breathtaking styling by Scaglietti, the 250 GTO is the most coveted and valuable collector car in history."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What iconic German sports car, debuted in 1963 with a rear-mounted flat-6 'boxer' engine, remains in continuous production today?",
                        "options": [
                            "Porsche 911",
                            "BMW M3",
                            "Mercedes-Benz 300SL",
                            "Audi R8"
                        ],
                        "correct": 0,
                        "explanation": "Designed by Ferdinand 'Butzi' Porsche, the Porsche 911 debuted in 1963 with its signature rear-engine layout and timeless silhouette, evolving through eight generations over 60+ years."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What feature earned the 1954 Mercedes-Benz 300 SL its legendary 'Gullwing' nickname?",
                        "options": [
                            "Upward-opening roof-hinged doors required by its high-silled tubular spaceframe chassis",
                            "Feathered wings attached to the trunk for downforce",
                            "A horn that imitated bird calls",
                            "An exhaust pipe shaped like an eagle beak"
                        ],
                        "correct": 0,
                        "explanation": "Because the 300 SL's rigid tubular spaceframe chassis ran high along the sides, conventional doors were impossible, leading to the iconic roof-hinged upward-opening 'Gullwing' doors."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "In what year was the revolutionary Ford Model T introduced, leading to over 15 million sales worldwide?",
                        "options": [
                            "1908",
                            "1935",
                            "1880",
                            "1955"
                        ],
                        "correct": 0,
                        "explanation": "Henry Ford introduced the rugged, affordable Model T in October 1908, putting the world on wheels and transforming global transportation."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What was the landmark technical innovation of the original 1959 British Motor Corporation (BMC) Mini designed by Alec Issigonis?",
                        "options": [
                            "A transverse front-engine, front-wheel-drive layout maximizing cabin space (80% of floorplan for passengers and luggage)",
                            "A mid-engine V8 powertrain",
                            "A four-wheel-steering diesel hybrid drivetrain",
                            "A wooden chassis with pneumatic brakes"
                        ],
                        "correct": 0,
                        "explanation": "Alec Issigonis mounted the engine sideways (transversely) over the front wheels with the gearbox in the sump, establishing the blueprint for 90% of modern compact economy cars."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What Swedish automaker invented the modern 3-point seatbelt in 1959 and gifted the patent to all automakers for free?",
                        "options": [
                            "Volvo (inventor Nils Bohlin)",
                            "Saab",
                            "Koenigsegg",
                            "Scania"
                        ],
                        "correct": 0,
                        "explanation": "Volvo engineer Nils Bohlin invented the 3-point lap/shoulder seatbelt in 1959; Volvo opened the patent royalty-free to all competitors, saving over an estimated 1 million lives to date."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the primary function of an automotive Turbocharger?",
                        "options": [
                            "Using hot exhaust gases to spin a turbine that forces compressed air into the engine cylinders for more power",
                            "Spraying water directly into the fuel tank to cool the radiator",
                            "Rotating the rear wheels using battery energy",
                            "Cleaning the catalytic converter using electrostatic magnets"
                        ],
                        "correct": 0,
                        "explanation": "A turbocharger uses otherwise wasted exhaust gas energy to drive a compressor, cramming dense oxygen into the combustion chambers to generate massive horsepower from smaller engine displacements."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 4: Speed Records & Motorsport Legends
            # =================================================================
            {
                "id": "speed_records_motorsport",
                "title": "Speed Records & Motorsport Triumphs",
                "description": "Supersonic land speed records, the 24 Hours of Le Mans Ford vs Ferrari duel, Formula 1 technological leaps, and bullet trains.",
                "cards": [
                    {
                        "title": "ThrustSSC: The First Supersonic Car (1997)",
                        "points": [
                            "On October 15, 1997, in the Black Rock Desert of Nevada, the British team ThrustSSC became the first land vehicle to officially break the sound barrier.",
                            "Driven by Royal Air Force fighter pilot Andy Green, ThrustSSC achieved a land speed record of 763.035 mph (1,227.985 km/h / Mach 1.016).",
                            "It was powered by two Rolls-Royce Spey turbofan engines from an F-4 Phantom jet fighter, producing 110,000 horsepower and consuming 4.8 gallons of fuel per second!",
                            "Spectators on the desert floor heard a thunderous double sonic boom as the twin-jet car blasted across the measured mile."
                        ]
                    },
                    {
                        "title": "Ford vs. Ferrari at Le Mans (1966)",
                        "points": [
                            "After Enzo Ferrari walked away from a buyout deal by Ford in 1963, Henry Ford II vowed to defeat Ferrari at the world's most prestigious endurance race: the 24 Hours of Le Mans.",
                            "Carroll Shelby and driver/engineer Ken Miles refined the Ford GT40 with a massive 7.0-liter (427 cu in) American V8 engine and aerodynamic redesigns.",
                            "At the 1966 24 Hours of Le Mans, Ford GT40s made racing history by taking 1st, 2nd, and 3rd place in a legendary photo-finish, ending Ferrari's 6-year winning streak.",
                            "The GT40 went on to win Le Mans four consecutive times from 1966 to 1969."
                        ]
                    },
                    {
                        "title": "The Shinkansen: Japan's Bullet Train (1964)",
                        "points": [
                            "Inaugurated for the 1964 Tokyo Olympics, the Tokaido Shinkansen was the world's first dedicated high-speed commercial railway line.",
                            "Running between Tokyo and Osaka at speeds of 210 km/h (130 mph), it reduced travel time from nearly 7 hours down to under 4 hours.",
                            "Shinkansen trains operate on dedicated wide standard-gauge tracks with zero grade crossings, advanced automatic train control (ATC), and airtight pressurized cabins for tunnels.",
                            "In over 60 years of operation carrying over 10 billion passengers, the Shinkansen has maintained a perfect safety record with zero passenger fatalities due to derailments or collisions!"
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "What vehicle became the first land vehicle to officially break the sound barrier on land in 1997?",
                        "options": [
                            "ThrustSSC (driven by Andy Green at 763 mph)",
                            "Bluebird-Proteus CN7",
                            "Spirit of America",
                            "Bloodhound LSR"
                        ],
                        "correct": 0,
                        "explanation": "On October 15, 1997, RAF pilot Andy Green drove the twin-jet ThrustSSC to 763.035 mph (Mach 1.016) in the Nevada desert, producing the first supersonic land record."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "Which American racing car achieved a historic 1-2-3 podium sweep at the 1966 24 Hours of Le Mans, dethroning Ferrari?",
                        "options": [
                            "Ford GT40 Mk II",
                            "Chevrolet Corvette Stingray",
                            "Shelby Cobra Daytona Coupe",
                            "Dodge Viper GTS-R"
                        ],
                        "correct": 0,
                        "explanation": "Engineered by Carroll Shelby and Ken Miles, the 7.0-liter Ford GT40 Mk II won Le Mans in 1966 with a legendary 1-2-3 finish, repeating victories through 1969."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the remarkable 60-year safety record of Japan's high-speed Shinkansen bullet train network?",
                        "options": [
                            "Zero passenger fatalities from derailments or collisions across over 10 billion passenger journeys",
                            "It has suffered only one derailment per decade",
                            "It operates at reduced speeds during rainfall",
                            "It requires passengers to wear racing helmets"
                        ],
                        "correct": 0,
                        "explanation": "Since opening in 1964, the Shinkansen has carried over 10 billion passengers with zero fatal derailments or collisions, maintaining an average delay of less than 1 minute."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the 'Triple Crown of Motorsport'?",
                        "options": [
                            "Winning the Monaco Grand Prix (Formula 1), the 24 Hours of Le Mans, and the Indianapolis 500",
                            "Winning the Daytona 500, the Dakar Rally, and the Isle of Man TT",
                            "Winning three Formula 1 World Championships in a row",
                            "Setting three land speed records in the same year"
                        ],
                        "correct": 0,
                        "explanation": "Graham Hill is the only driver in racing history to achieve the Triple Crown of Motorsport: winning the Monaco GP (or F1 World Championship), the 24 Hours of Le Mans, and the Indy 500."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What downforce-generating aerodynamic phenomenon, pioneered by Colin Chapman's Lotus 78/79 in Formula 1, is known as 'Ground Effect'?",
                        "options": [
                            "Using shaped underbody venturi tunnels and side skirts to create low pressure that literally sucks the car to the asphalt",
                            "Adding heavy lead weights to the front bumper",
                            "Ejecting exhaust air backwards to push the rear tires down",
                            "Inflating tires with heavy xenon gas"
                        ],
                        "correct": 0,
                        "explanation": "Ground effect channels air through shaped underfloor venturi tunnels (Bernoulli's principle), creating massive suction downforce with minimal drag penalty."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What dangerous motorcycle road race, held on public roads around a 37.73-mile mountain course since 1907, is considered the most perilous in the world?",
                        "options": [
                            "Isle of Man TT (Tourist Trophy)",
                            "Monaco Grand Prix",
                            "Bathurst 1000",
                            "Pikes Peak International Hill Climb"
                        ],
                        "correct": 0,
                        "explanation": "The Isle of Man TT features superbike riders racing between stone walls and lampposts at speeds exceeding 200 mph (320 km/h) over a 37.73-mile closed public road course."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What safety innovation, introduced to Formula 1 in 2018, consists of a titanium cockpit hoop that has saved numerous drivers from flying debris and rollovers?",
                        "options": [
                            "The Halo",
                            "The HANS Device",
                            "The Roll Bar",
                            "The Skid Plate"
                        ],
                        "correct": 0,
                        "explanation": "The Halo is a curved titanium bar mounted above the driver's helmet capable of supporting 12 tonnes of impact weight (the weight of two London double-decker buses)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is the prestigious annual endurance race held in Indiana since 1911 known as 'The Greatest Spectacle in Racing'?",
                        "options": [
                            "The Indianapolis 500 (Indy 500)",
                            "The Daytona 500",
                            "The 12 Hours of Sebring",
                            "The Baja 1000"
                        ],
                        "correct": 0,
                        "explanation": "The Indy 500 challenges 33 open-wheel race cars across 200 laps (500 miles) at speeds topping 230+ mph at the iconic Indianapolis Motor Speedway 'Brickyard'."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What tradition is famously performed by the winner of the Indianapolis 500 in Victory Lane?",
                        "options": [
                            "Drinking and pouring a bottle of cold milk over their head",
                            "Drinking expensive French champagne",
                            "Kissing a live racing pigeon",
                            "Smashing a watermelon with a sledgehammer"
                        ],
                        "correct": 0,
                        "explanation": "Started by Louis Meyer in 1936 who drank buttermilk to refresh himself after the hot race, winning drivers traditionally drink from a glass bottle of dairy milk in Victory Lane."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "What is 'Regenerative Braking' in modern hybrid and electric racing and road vehicles (like F1 MGU-K systems)?",
                        "options": [
                            "Using electric motors as generators during deceleration to convert kinetic energy back into stored battery electricity",
                            "Spraying liquid nitrogen on ceramic disc brakes",
                            "Deploying a rear parachute to slow down at pit stops",
                            "Reversing the combustion firing order of the engine cylinders"
                        ],
                        "correct": 0,
                        "explanation": "Regenerative braking reverses electric motor torque to slow the wheels, converting the vehicle's kinetic momentum into electrical power and storing it in the battery."
                    }
                ]
            }
        ]
    }

    # -------------------------------------------------------------------------
    # HEBREW DATASET
    # -------------------------------------------------------------------------
    aa_he = {
        "id": "aviation_automotive_he",
        "title": "חלוצי התעופה והרכב",
        "description": "מדיונות החול של קיטי הוק ורעם פסי הייצור הראשונים ועד למטוסי סילון על-קוליים ומכוניות-על אקזוטיות: סיפורם של המהנדסים הנועזים והמכונות שכבשו את היבשה והשמיים.",
        "lang": "he",
        "audience": "family",
        "categories": [
            # =================================================================
            # CATEGORY 1: Important Facts
            # =================================================================
            {
                "id": "important_facts",
                "title": "עובדות ואבני דרך היסטוריות",
                "description": "אבני הדרך החשובות ביותר ופריצות הדרך ההנדסיות ששינו את פני התעופה והתחבורה היבשתית.",
                "cards": [
                    {
                        "title": "האחים רייט (1903)",
                        "points": [
                            "ב-17 בדצמבר 1903, בקיטי הוק שבצפון קרוליינה, אורוויל ווילבור רייט ביצעו את הטיסה הממונעת, הנשלטת והמתמשכת הראשונה בהיסטוריה בכלי טיס הכבד מן האוויר.",
                            "פריצת הדרך המרכזית שלהם לא הייתה עוצמת המנוע, אלא מערכת שליטה אווירודינמית בשלושה צירים: עיוות כנף לסבסוב (Roll), הגה גובה לעלייה וירידה (Pitch), והגה כיוון (Yaw).",
                            "אורוויל ביצע את הטיסה הראשונה, כשהוא שוהה באוויר 12 שניות ועובר מרחק של 36.5 מטרים במטוס 'Wright Flyer I'.",
                            "באותו יום, וילבור השלים את הטיסה הארוכה ביותר: 260 מטרים ב-59 שניות."
                        ]
                    },
                    {
                        "title": "הנרי פורד ופס הייצור הנע (1913)",
                        "points": [
                            "בשנת 1913, הנרי פורד הציג את פס הייצור הנע במפעל היילנד פארק במישיגן, ושינה לתמיד את פני התעשייה העולמית.",
                            "פס הייצור קיצר את זמן ההרכבה של מכונית פורד מודל T מ-12 שעות ל-93 דקות בלבד.",
                            "הייצור ההמוני אפשר לפורד להוזיל את מחיר המכונית מ-850 דולר ב-1908 לפחות מ-300 דולר בשנות ה-20, והפך את הרכב ממוצר מותרות לכלי נגיש לכל פועל.",
                            "פורד העלה את שכר עובדיו ל-5 דולר ליום (כפול מהשכר המקובל), ובכך יצר מעמד ביניים של צרכנים המסוגלים לרכוש את המכוניות שהם מייצרים."
                        ]
                    },
                    {
                        "title": "שבירת מחסום הקול: צ'אק ייגר (1947)",
                        "points": [
                            "ב-14 באוקטובר 1947, טייס הניסוי האמריקאי צ'אק ייגר הפך לאדם הראשון ששבר רשמית את מחסום הקול בטיסה אופקית (מאך 1.0).",
                            "הוא הטיס את המטוס הרקטי Bell X-1, שזכה לכינוי 'Glamorous Glennis' על שם אשתו, והגיע למהירות של מאך 1.06 (כ-1,127 קמ״ש) בגובה 43,000 רגל.",
                            "חרטום המטוס עוצב במבנה של קליע רובה 0.50 אינץ', שהיה ידוע ביציבותו האווירודינמית במהירויות על-קוליות.",
                            "ייגר טס במשימה ההיסטורית כשהוא סובל משתי צלעות שבורות עקב תאונת רכיבה על סוס יומיים קודם לכן."
                        ]
                    },
                    {
                        "title": "בואינג 747 'מלכת השמיים' (1969)",
                        "points": [
                            "מטוס הבואינג 747 טס לראשונה בשנת 1969 והיה מטוס הנוסעים רחב-הגוף (ג'מבו ג'ט) הראשון בעולם.",
                            "הגיבנת המפורסמת בסיפון העליון תוכננה מכיוון שמהנדסים שיערו שמטוסי נוסעים על-קוליים יחליפו את מטוסי הסילון הרגילים, מה שיאפשר להסב את ה-747 למטוס מטען שהחרטום שלו נפתח כלפי מעלה.",
                            "המטוס הכיל מעל 400 נוסעים, הוזיל משמעותית את עלות הכרטיס למושב, והפך טיסות בינלאומיות לנגישות למיליוני משפחות בעולם.",
                            "ה-747 החזיק בתואר מטוס הנוסעים הגדול בעולם במשך 37 שנים רצופות עד להגעת האיירבוס A380 ב-2005."
                        ]
                    },
                    {
                        "title": "הקונקורד: תעופת נוסעים על-קולית (1969)",
                        "points": [
                            "מטוס הקונקורד הבריטי-צרפתי הטיס נוסעים מעל האוקיינוס האטלנטי במהירות של מאך 2.04 (כ-2,179 קמ״ש) - יותר מפי שניים ממהירות הקול.",
                            "טיסה מלונדון או פריז לניו יורק ארכה פחות מ-3.5 שעות, מה שאפשר לנוסעים לנחות בניו יורק 'מוקדם יותר' לפי השעון המקומי מאשר שעת ההמראה מאירופה.",
                            "בגובה שיוט של 60,000 רגל (18 ק״מ), הנוסעים יכלו להבחין בבירור בעקמומיות כדור הארץ ובשמי החלל השחורים שמעליהם.",
                            "החיכוך עם האוויר במהירות מאך 2 חימם את מעטפת האלומיניום ל-127 מעלות, מה שגרם לגוף המטוס להתארך פיזית ב-15 עד 30 ס״מ במהלך הטיסה!"
                        ]
                    },
                    {
                        "title": "הציפור השחורה: לוקהיד SR-71 (1964)",
                        "points": [
                            "ה-SR-71 Blackbird נותר מטוס הסילון המאויש המהיר ביותר בהיסטוריה, שטס במהירות של מעל מאך 3.3 (מעל 3,540 קמ״ש) בגובה של 85,000 רגל.",
                            "גוף המטוס נבנה מ-93% טיטניום כדי לעמוד בחום החיכוך שעלה על 300 מעלות; ארה״ב רכשה את הטיטניום בחשאי מברית המועצות באמצעות חברות קש.",
                            "בשל התרחבות הטיטניום בחום, מכלי הדלק דלפו על מסלול ההמראה כשהמטוס היה קר, ונסגרו הרמטית רק לאחר שחום החיכוך באוויר הרחיב את לוחות המתכת.",
                            "נוהל ההתחמקות מטיל קרקע-אוויר שנורה לעבר המטוס היה פשוט: הטייס לחץ על המצערת עד הסוף וטס מהר יותר מהטיל!"
                        ]
                    },
                    {
                        "title": "מקלארן F1: שלמות מכנית אנלוגית (1992)",
                        "points": [
                            "תוכננה על ידי מהנדס הפורמולה 1 הגאון גורדון מארי, וקבעה שיא מהירות עולמי למכונית סדרתית של 386.4 קמ״ש (240.1 מייל/שעה) ב-1998.",
                            "המכונית כללה תא נהג מהפכני עם 3 מושבים, כאשר הנהג יושב בדיוק במרכז הרכב לשדה ראייה מושלם וחלוקת משקל אידיאלית.",
                            "תא המנוע צופה ב-16 גרם של עלי זהב טהור 24 קראט כדי לשמש כמחזיר החום הקל והיעיל ביותר עבור מנוע ה-V12 של BMW.",
                            "הייתה מכונית הכביש הסדרתית הראשונה בעולם שנבנתה כולה משלדת מונוקוק מסיבי פחמן (Carbon Fiber)."
                        ]
                    },
                    {
                        "title": "מהפכת הרכב החשמלי: טסלה מודל S (2012)",
                        "points": [
                            "הושקה בשנת 2012 והוכיחה שרכב חשמלי יכול להתעלות על מכוניות בנזין בביצועים, טווח נסיעה ובטיחות.",
                            "סוללת הליתיום-יון הכבדה מוקמה כמשטח שטוח בתחתית השלדה, מה שיצר מרכז כובד נמוך במיוחד ומנע התהפכויות, תוך פינוי תא מטען קדמי (Frunk).",
                            "בדגמי הביצועים (Plaid / Ludicrous), תאוצת הרכב מ-0 ל-100 קמ״ש ירדה מתחת ל-2.0 שניות - מהר יותר ממכוניות-על שעולות מיליוני דולרים.",
                            "החדירה את מודל עדכוני התוכנה מרחוק (OTA), המאפשר לשפר את ביצועי הרכב ומערכות הנהיגה האוטונומית בין לילה."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מה הייתה פריצת הדרך האווירודינמית המרכזית שפיתחו האחים רייט ואפשרה טיסה מבוקרת ב-1903?",
                        "options": [
                            "שליטה בשלושה צירים (סבסוב, עלרוד וסחרור) באמצעות עיוות כנף והגאים",
                            "הנעת סילון עם מבער אחורי",
                            "תא נוסעים מדוחס מאלומיניום",
                            "ניווט לוויני אוטומטי מבוסס GPS"
                        ],
                        "correct": 0,
                        "explanation": "האחים רייט הבינו שהאתגר האמיתי אינו רק עוצמת מנוע אלא שליטה תלת-ממדית באוויר; פיתוח עיוות הכנף (Roll), הגה הגובה (Pitch) והגה הכיוון (Yaw) מהווה את הבסיס לכל כלי הטיס עד היום."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "באיזו שנה ובאיזה מקום ביצעו האחים רייט את הטיסה הממונעת הראשונה בהיסטוריה?",
                        "options": [
                            "1903 בקיטי הוק, צפון קרוליינה",
                            "1912 בפריז, צרפת",
                            "1895 בדייטון, אוהיו",
                            "1920 בלונדון, אנגליה"
                        ],
                        "correct": 0,
                        "explanation": "ב-17 בדצמבר 1903, בדיונות החול של קיטי הוק בצפון קרוליינה, אורוויל רייט שהה באוויר 12 שניות במטוס ה-Wright Flyer I."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "בכמה קיצר פס הייצור הנע של הנרי פורד את זמן ההרכבה של מכונית מודל T ב-1913?",
                        "options": [
                            "מ-12 שעות ל-93 דקות בלבד",
                            "מחודש ימים ל-24 שעות",
                            "מ-5 שעות ל-4 שעות",
                            "משבועיים ל-10 ימים"
                        ],
                        "correct": 0,
                        "explanation": "באמצעות שינוע הרכב על גבי מסוע רציף בין תחנות עבודה, פורד קיצר את זמן הרכבת הרכב מ-12 שעות ל-93 דקות בלבד."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מי היה טייס הניסוי ששבר לראשונה את מחסום הקול בטיסה אופקית במטוס הרקטי Bell X-1 בשנת 1947?",
                        "options": [
                            "צ'אק ייגר",
                            "ניל ארמסטרונג",
                            "צ'ארלס לינדברג",
                            "הווארד יוז"
                        ],
                        "correct": 0,
                        "explanation": "ב-14 באוקטובר 1947, קפטן צ'אק ייגר מחיל האוויר האמריקאי הטיס את ה-Bell X-1 מעבר למאך 1.0 (מעל 1,100 קמ״ש) בגובה 43,000 רגל."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע עוצב מטוס הבואינג 747 מלכתחילה עם גיבנת תא הטייס המפורסמת בסיפון העליון?",
                        "options": [
                            "כדי לאפשר לחרטום המטוס להיפתח כלפי מעלה להעמסת מטען במקרה שמטוסים על-קוליים יחליפו את טיסות הנוסעים",
                            "כדי לאכלס בריכת שחייה ובר קוקטיילים לנוסעים",
                            "כדי לאחסן מצנח חירום לכל המטוס",
                            "כדי לאחסן מנועי סילון חלופיים"
                        ],
                        "correct": 0,
                        "explanation": "בואינג שיערה שמטוסי נוסעים על-קוליים (כמו הקונקורד) ישלטו בקווים, ולכן תכננה את תא הטייס מוגבה כדי לאפשר פתיחת חרטום קדמי להובלת מטענים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כמה זמן ארכה טיסה על-קולית ממוצעת במטוס הקונקורד בין לונדון או פריז לניו יורק?",
                        "options": [
                            "פחות מ-3.5 שעות",
                            "כ-7 שעות",
                            "12 שעות",
                            "שעה אחת"
                        ],
                        "correct": 0,
                        "explanation": "הקונקורד טס במהירות של מאך 2.04 (כ-2,180 קמ״ש) וחצה את האוקיינוס האטלנטי בכ-3 שעות ו-20 דקות בממוצע (לעומת כ-8 שעות במטוס רגיל)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מתכת קלת-משקל ועמידה בחום היוותה 93% מגוף מטוס הריגול לוקהיד SR-71?",
                        "options": [
                            "טיטניום",
                            "ברזל יצוק",
                            "עופרת",
                            "נחושת טהורה"
                        ],
                        "correct": 0,
                        "explanation": "ה-SR-71 נבנה כמעט כולו מטיטניום כדי לעמוד בחום החיכוך שעלה על 300 מעלות במהירות מאך 3+, מתכת שנרכשה בחשאי מהסובייטים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו סידור המושבים המהפכני שעיצב גורדון מארי במכונית-העל מקלארן F1 משנת 1992?",
                        "options": [
                            "מושב נהג מרכזי באמצע עם שני מושבי נוסעים משני צדדיו ומעט מאחור",
                            "שני מושבים בטור זה אחר זה",
                            "מושב יחיד ללא מקום לנוסעים כלל",
                            "ארבעה מושבים בתצורת 2+2"
                        ],
                        "correct": 0,
                        "explanation": "גורדון מארי מיקם את מושב הנהג בדיוק במרכז הרכב כדי להעניק שדה ראייה פנורמי מושלם, מיקום דוושות ישר וחלוקת משקל מאוזנת."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע צופה תא המנוע של המקלארן F1 בעלי זהב טהור 24 קראט?",
                        "options": [
                            "הזהב משמש כמחזיר קרינת חום אינפרא-אדום קל-משקל ויעיל במיוחד להגנה על שלדת סיבי הפחמן",
                            "כדי להרשים רוכשים עשירים בתערוכות רכב",
                            "כדי להוליך חשמל בין המצתים למצבר",
                            "כדי להעלות את מחיר המכונית במכירות פומביות"
                        ],
                        "correct": 0,
                        "explanation": "זהב הוא אחד ממחזירי החום הטובים בטבע; 16 גרם של עלי זהב דקיקים ציפו את תא המנוע כדי להגן על גוף סיבי הפחמן מחום פליטת מנוע ה-V12."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה היה נוהל ההתחמקות העיקרי של טייסי ה-SR-71 Blackbird כאשר זוהה שיגור טיל קרקע-אוויר לעברם?",
                        "options": [
                            "האצה וטיסה מהירה יותר מהטיל במהירות של מעל מאך 3.2",
                            "פיזור נורי הטעיה ומלכודות מכ״ם",
                            "צלילה לגובה נמוך בין קניונים כדי להסתתר מהמכ״ם",
                            "ביצוע גלגול חבית של 360 מעלות"
                        ],
                        "correct": 0,
                        "explanation": "מכיוון שהמטוס שייט בגובה של 85,000 רגל במהירות של מעל 3,500 קמ״ש, נוהל ההתחמקות היה פשוט להאיץ; אף טיל בהיסטוריה לא הצליח להשיג מטוס SR-71 מבצעי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה קרה לאורך הפיזי של מטוס הקונקורד במהלך טיסה על-קולית עקב חום החיכוך באוויר?",
                        "options": [
                            "גוף המטוס התארך פיזית ב-15 עד 30 ס״מ",
                            "המטוס התכווץ ב-2 מטרים בשל הלחץ האטמוספרי",
                            "הכנפיים התקפלו לאחור באופן אוטומטי",
                            "מייצב הכיוון הסתובב ב-90 מעלות"
                        ],
                        "correct": 0,
                        "explanation": "החיכוך במהירות מאך 2 חימם את מעטפת המטוס ל-127 מעלות, מה שגרם להתפשטות תרמית של האלומיניום ולהתארכות גוף המטוס בעד 30 ס״מ."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "באיזו שנה הציג הנרי פורד את שכר ה-'5 דולר ליום', שהכפיל את השכר התעשייתי המקובל באותה תקופה?",
                        "options": [
                            "1914",
                            "1939",
                            "1890",
                            "1960"
                        ],
                        "correct": 0,
                        "explanation": "בינואר 1914 הכריז פורד על שכר של 5 דולר ליום עבודה בן 8 שעות, מה שהפחית את נטישת העובדים ואפשר לפועלים לחסוך ולרכוש את המכוניות שייצרו."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה היה שיא המהירות המרבי שקבעה מכונית-העל מקלארן F1 בשנת 1998?",
                        "options": [
                            "386.4 קמ״ש (240.1 מייל/שעה)",
                            "306.5 קמ״ש (190.5 מייל/שעה)",
                            "490.4 קמ״ש (304.7 מייל/שעה)",
                            "249.4 קמ״ש (155.0 מייל/שעה)"
                        ],
                        "correct": 0,
                        "explanation": "הנהג אנדי וואלאס הגיע למהירות של 386.4 קמ״ש במסלול הניסוי אהרה-לסיאן בגרמניה, שיא שהפך את ה-F1 למכונית האטמוספרית המהירה בעולם."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מאפיין תכנוני ברכבים חשמליים מודרניים (כמו טסלה מודל S) מעניק להם מרכז כובד נמוך במיוחד?",
                        "options": [
                            "סוללת ליתיום-יון כבדה המותקנת כמשטח שטוח בתחתית השלדה",
                            "ספוילר אחורי קל-משקל מטיטניום",
                            "חישוקי גלגלים צרים מסיבי פחמן",
                            "תיבת הילוכים מברזל יצוק"
                        ],
                        "correct": 0,
                        "explanation": "התקנת הסוללה הכבדה ברצפת הרכב בין הסרנים מייצרת מרכז כובד נמוך ביותר, מה שממזער את סכנת ההתהפכות ומשפר את האחיזה בעיקולים."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה היה שמו של המטוס החד-מנועי שבו השלים צ'ארלס לינדברג את טיסת הסולו הטרנס-אטלנטית הרצופה הראשונה ב-1927?",
                        "options": [
                            "רוחו של סנט לואיס (Spirit of St. Louis)",
                            "גלמורוס גלניס (Glamorous Glennis)",
                            "רייט פלייר (Wright Flyer)",
                            "אנולה גיי (Enola Gay)"
                        ],
                        "correct": 0,
                        "explanation": "צ'ארלס לינדברג הטיס את ה-'Spirit of St. Louis' מניו יורק לפריז ב-20–21 במאי 1927, כשהוא עובר 5,800 ק״מ ב-33.5 שעות טיסה רצופות."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 2: Aviation Legends & Historic Aircraft
            # =================================================================
            {
                "id": "aviation_legends",
                "title": "אגדות תעופה וכלי טיס היסטוריים",
                "description": "כלי הטיס המפורסמים והמשפיעים ביותר שחוללו מהפכה בקרבות אוויר, בתעופה אזרחית ובטכנולוגיות חמקנות.",
                "cards": [
                    {
                        "title": "דאגלס DC-3 (1935)",
                        "points": [
                            "הוצג בשנת 1935 ונחשב למטוס שיצר את תעשיית התעופה המסחרית המודרנית.",
                            "היה מטוס הנוסעים הראשון שאפשר לחברות תעופה להרוויח כסף ממכירת כרטיסי טיסה בלבד, ללא צורך בסובסידיות ממשלתיות להובלת דואר.",
                            "במלחמת העולם השנייה יוצרו מעל 10,000 מטוסים בגרסה הצבאית (C-47 דקוטה), שהצניחה כוחות בפלישה לנורמנדי (D-Day).",
                            "המבנה הדו-מנועי החסון שלו היה כה עמיד, עד שמאות מטוסי DC-3 מקוריים עדיין טסים כיום במשימות תובלה ונוסעים ברחבי העולם!"
                        ]
                    },
                    {
                        "title": "סופרמרין ספיטפייר (1936)",
                        "points": [
                            "תוכנן על ידי ר.ג'. מיטשל, והיה מטוס הקרב החד-מושבי הבריטי האגדי שהגן על שמי בריטניה בקרב על בריטניה ב-1940.",
                            "התאפיין בכנפיים אליפטיות דקות וייחודיות שנועדו לצמצם גרר מושרה ולאפשר התקנת שמונה מקלעים וכני נסע.",
                            "הונע על ידי מנוע ה-Rolls-Royce Merlin V12 האגדי, ששריקת מגדש הטורבו שלו הפכה לסמל העמידה הבריטית במלחמה.",
                            "שודרג ברציפות לאורך שנות המלחמה, כשהוא מזנק ממהירות מרבית של 360 מייל/שעה לדגמים מאוחרים של מעל 450 מייל/שעה."
                        ]
                    },
                    {
                        "title": "לוקהיד SR-71 (1964)",
                        "points": [
                            "הונדס בסדנת 'Skunk Works' הסודית של לוקהיד בראשות קלי ג'ונסון לצורך ביצוע משימות סיור ואיסוף מודיעין מגובה רב.",
                            "מנועי ה-Pratt & Whitney J58 שלו פעלו כטורבו-סילון במהירות נמוכה, אך הוסבו למנועי מגח-סילון (Ramjet) במהירויות של מעל מאך 2.",
                            "במהירות מאך 3+, שמשת תא הטייס הגיעה לחום של 330 מעלות ונבנתה מזכוכית קוורץ בעובי 3.2 ס״מ.",
                            "הטייסים לבשו חליפות לחץ מלאות עם אספקת 100% חמצן, הדומות לחליפות אסטרונאוטים בחלל."
                        ]
                    },
                    {
                        "title": "מפציץ החמקן B-2 Spirit (1989)",
                        "points": [
                            "ה-B-2 Spirit הוא מפציץ חמקן ארוך-טווח בתצורת 'כנף מעופפת' ללא מייצב כיוון אנכי.",
                            "שטח חתך המכ״ם שלו קטן משל דבורה גדולה, מה שמאפשר לו לחדור מבעד למערכי הגנה אווירית מתקדמים מבלי להתגלות.",
                            "משתמש במשטחים רציפים וחומרים בולעי קרינת מכ״ם (RAM) המפזרים ובולעים גלים אלקטרומגנטיים.",
                            "בעלות ייצור של מעל 2 מיליארד דולר למטוס בודד, הוא המטוס היקר ביותר שנבנה אי פעם."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "איזה מבנה כנף העניק למטוס הספיטפייר הבריטי זריזות פנייה יוצאת דופן וגרר מושרה נמוך בקרב על בריטניה?",
                        "options": [
                            "כנפיים אליפטיות",
                            "כנפי דלתא משוכות לאחור",
                            "כנפיים בעלות גאומטריה משתנה",
                            "כנפיים דו-כנפיות מדורגות"
                        ],
                        "correct": 0,
                        "explanation": "ר.ג'. מיטשל בחר בכנפיים אליפטיות כדי להקנות לספיטפייר גרר אווירודינמי מינימלי ונפח פנימי מספיק לנשיאת מקלעים ותחמושת."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע נחשב מטוס הדאגלס DC-3 (משנת 1935) למטוס המשפיע ביותר בראשית התעופה האזרחית?",
                        "options": [
                            "היה מטוס הנוסעים הראשון שהרוויח כסף מהטסת נוסעים בלבד ללא צורך בסובסידיות ממשלתיות להובלת דואר",
                            "היה מטוס הסילון הראשון שחצה את האוקיינוס השקט",
                            "היה בעל הנעה גרעינית",
                            "כלל תאי שינה עבור 200 נוסעים"
                        ],
                        "correct": 0,
                        "explanation": "ה-DC-3 שילב מהירות, נוחות ואמינות כלכלית שאפשרו לחברות תעופה להרוויח ממכירת כרטיסים בלבד, ויצר את תעשיית הנוסעים המודרנית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כמה קטן שטח חתך המכ״ם (RCS) של מפציץ החמקן הענק B-2 Spirit על גבי מסכי מכ״ם?",
                        "options": [
                            "כגודלה של דבורה גדולה או ציפור קטנה",
                            "כגודלה של ספינת תענוגות",
                            "כגודלו של אצטדיון כדורגל",
                            "כגודלו של אוטובוס בית ספר"
                        ],
                        "correct": 0,
                        "explanation": "למרות מוטת כנפיים של מעל 52 מטרים, צורת הכנף המעופפת והחומרים בולעי המכ״ם מקטינים את חתימת המכ״ם שלו לכ-0.001 מ״ר (כשל דבורה)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מנוע אגדי הניע הן את מטוס הספיטפייר הבריטי והן את מטוס המוסטנג P-51 האמריקאי במלחמת העולם השנייה?",
                        "options": [
                            "רולס-רויס מרלין V12 (Rolls-Royce Merlin)",
                            "פראט אנד וויטני J58",
                            "ג'נרל אלקטריק GE90",
                            "ב.מ.וו 801 כוכבי"
                        ],
                        "correct": 0,
                        "explanation": "מנוע ה-Rolls-Royce Merlin בעל 12 הצילינדרים ומגדש הטורבו הדו-שלבי היה מנוע הבוכנה האגדי והאמין ביותר של בעלות הברית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "כיצד פעלו מנועי ה-J58 של מטוס ה-SR-71 במהירויות שמעל מאך 2?",
                        "options": [
                            "צינורות מעקף ניתבו אוויר דחוס ישירות למבער האחורי, והפכו את המנוע למגח-סילון (Ramjet)",
                            "הם כיבו את הטורבינות והפעילו מנועי רקטה מוצקים",
                            "הם עברו למנועים חשמליים מבוססי תאי דלק מימני",
                            "הם הזריקו קיטור מים למערכת הפליטה"
                        ],
                        "correct": 0,
                        "explanation": "במהירות של מעל מאך 2, שישה שסתומי מעקף העבירו אוויר דחוס ישירות למבער האחורי, והמירו את הטורבו-סילון למנוע Ramjet יעיל להפליא במהירות מאך 3+."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה היה תפקידו של החרטום המתכוונן (Droop Snoot) במטוס הקונקורד העל-קולי?",
                        "options": [
                            "להנמיך את חרטום המטוס בעת המראה ונחיתה כדי לאפשר לטייסים לראות את מסלול הנחיתה מעל כנף הדלתא",
                            "לאסוף מי גשמים לקירור תא הנוסעים",
                            "להפעיל חיישן לייזר קדמי",
                            "לשמש כמעצור אוויר בעת שיוט על-קולי"
                        ],
                        "correct": 0,
                        "explanation": "בשל זווית ההתקפה הגבוהה של כנף הדלתא בנחיתה, חרטום הקונקורד הונמך הידראולית ב-12.5 מעלות כדי להעניק לטייסים שדה ראייה למסלול."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו חטיבת הנדסה מפורסמת בלוקהיד, בראשות קלי ג'ונסון, פיתחה את מטוסי ה-U-2, ה-SR-71 וה-F-117?",
                        "options": [
                            "סדנת הבואש (Skunk Works)",
                            "סדנת הפנטום (Phantom Works)",
                            "מעבדות בל",
                            "חטיבת מנועי פראט"
                        ],
                        "correct": 0,
                        "explanation": "חטיבת 'Skunk Works' של לוקהיד התמחתה בפיתוח מהיר וסודי של מטוסי ביון וחמקנות מתקדמים ששינו את פני ההיסטוריה הצבאית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו מטוס הנוסעים המסחרי הגדול ביותר שנבנה אי פעם (בעל סיפון כפול מלא לכל אורכו)?",
                        "options": [
                            "איירבוס A380",
                            "בואינג 747-400",
                            "קונקורד",
                            "אנטונוב An-225"
                        ],
                        "correct": 0,
                        "explanation": "האיירבוס A380 הוא מטוס הנוסעים הענק בעל הסיפון הכפול המלא, המסוגל לשאת מעל 850 נוסעים בתצורת מחלקה יחידה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה כלי טיס צבאי מבצעי היה הראשון שהשתמש בטכנולוגיית חמקנות באמצעות לוחות שטוחים זויתיים?",
                        "options": [
                            "לוקהיד F-117 נייטהוק (Nighthawk)",
                            "F-22 ראפטור",
                            "מפציץ B-52",
                            "F-16 פלקון"
                        ],
                        "correct": 0,
                        "explanation": "ה-F-117 נייטהוק, שטס לראשונה ב-1981, השתמש במשטחים שטוחים וזוויות חדות שתוכננו במחשב כדי להחזיר גלי מכ״ם הרחק מהמקלט."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מטוס מטען ענק בעל 6 מנועים החזיק בשיא המטוס הכבד ביותר ובעל מוטת הכנפיים המבצעית הגדולה בעולם עד להריסתו ב-2022?",
                        "options": [
                            "אנטונוב An-225 מריה (Mriya)",
                            "בואינג C-17 גלובמאסטר",
                            "לוקהיד C-5 גלקסי",
                            "איירבוס בלוגה XL"
                        ],
                        "correct": 0,
                        "explanation": "ה-An-225 'מריה' האוקראיני היה בעל משקל המראה מרבי של 640 טונות ונבנה במקור לנשיאת מעבורת החלל הסובייטית 'בוראן'."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 3: Automotive Pioneers & Iconic Supercars
            # =================================================================
            {
                "id": "automotive_pioneers_supercars",
                "title": "חלוצי הרכב ומכוניות-על איקוניות",
                "description": "התפתחות הרכב מכרכרות ממונעות בעלות שלושה גלגלים ועד למכוניות-על בעלות 1,000 כוחות סוס והנדסת מנוע מרכזי.",
                "cards": [
                    {
                        "title": "קרל בנץ וה-Motorwagen (1886)",
                        "points": [
                            "קרל בנץ מוכר כממציא מכונית הבנזין המודרנית הראשונה הודות לפטנט הגרמני מס' 37435 משנת 1886.",
                            "כרכרת ה-Motorwagen התלת-גלגלית הונעה על ידי מנוע ארבע פעימות בעל צילינדר בודד שהפיק 0.75 כוחות סוס.",
                            "באוגוסט 1888, אשתו ברטה בנץ לקחה את המכונית למסע הדרכים הבין-עירוני הראשון בהיסטוריה (106 ק״מ) מבלי לספר לו, כשהיא קונה בנזין ניקוי בבתי מרקחת ומתקנת את הבלמים עם רפידות עור של סנדלר!",
                            "המסע של ברטה חולל כותרות עולמיות והוכיח שהמכונית היא כלי תחבורה מעשי ולא סתם צעצוע הנדסי."
                        ]
                    },
                    {
                        "title": "למבורגיני מיורה: הולדת מכונית-העל (1966)",
                        "points": [
                            "הוצגה בתערוכת ז'נבה ב-1966 ונחשבת למכונית-העל (Supercar) האמיתית הראשונה בהיסטוריה בעלת מנוע מרכזי.",
                            "עוצבה על ידי מרצ'לו גנדיני מסדנת ברטונה, וכללה מנוע V12 בנפח 3.9 ליטר שהותקן לרוחב בדיוק מאחורי ראש הנהג.",
                            "עד המיורה, מכוניות ספורט הציבו את המנוע מלפנים; המיורה העבירה את הנדסת המנוע המרכזי ממסלולי המרוצים ישירות לכביש הציבורי.",
                            "עם מהירות מרבית של 280 קמ״ש, היא הייתה מכונית הכביש הסדרתית המהירה ביותר בעולם בעת השקתה."
                        ]
                    },
                    {
                        "title": "פרארי 250 GTO (1962)",
                        "points": [
                            "רק 36 מכוניות פרארי 250 GTO יוצרו בעבודת יד בין השנים 1962 ל-1964 לצורך מרוצי מכוניות גראנד טורינג (FIA Group 3).",
                            "הונעה על ידי מנוע Colombo V12 בנפח 3.0 ליטר שהפיק 300 כוחות סוס, ושלטה ללא עוררין במרוצי סיבולת בעולם.",
                            "רוכשי המכונית היו חייבים לקבל אישור אישי מאנזו פרארי ושילמו 18,000 דולר ב-1962.",
                            "כיום, ה-250 GTO היא מכונית האספנות היקרה ביותר בהיסטוריה, כאשר פריטים בודדים נמכרו במכירות פומביות ביותר מ-70 מיליון דולר!"
                        ]
                    },
                    {
                        "title": "בוגאטי ויירון 16.4: מפלצת 1,000 כוחות הסוס (2005)",
                        "points": [
                            "יו״ר קונצרן פולקסווגן פרדיננד פייך הציב אתגר הנדסי שנחשב לבלתי אפשרי: לבנות מכונית סדרתית עם מעל 1,000 כ״ס שתעבור את ה-400 קמ״ש אך תהיה נוחה לנסיעה יומיומית.",
                            "הוויירון הונעה על ידי מנוע W16 בנפח 8.0 ליטרים עם 4 מגדשי טורבו, שהפיק 1,001 כוחות סוס ומומנט מפלצתי של 1,250 ניוטון-מטר.",
                            "כדי למנוע מהמנוע ותיבת ההילוכים להתמוסס מחום, הרכב צויד ב-10 רדיאטורי קירור נפרדים ובצמיגי מישלן מיוחדים בעלות של 25,000 דולר לסט.",
                            "המכונית קבעה שיא גינס רשמי של 408.47 קמ״ש, ודגם ה-Super Sport הגיע בהמשך ל-431 קמ״ש."
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "מי ביצעה את מסע הרכב הבין-עירוני הראשון בהיסטוריה בשנת 1888, והוכיחה את אמינות המכונית בעולם?",
                        "options": [
                            "ברטה בנץ (אשתו של קרל בנץ)",
                            "הנרי פורד",
                            "אנזו פרארי",
                            "פרדיננד פורשה"
                        ],
                        "correct": 0,
                        "explanation": "ברטה בנץ נהגה במכונית ה-Motorwagen למרחק של 106 ק״מ ממנהיים לפפורצהיים באוגוסט 1888, רכשה דלק בבתי מרקחת והמציאה רפידות בלימה מעור."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מכונית נחשבת למכונית-העל (Supercar) המודרנית הראשונה בעלת מנוע מרכזי כשהוצגה ב-1966?",
                        "options": [
                            "למבורגיני מיורה (Lamborghini Miura)",
                            "פורד מודל T",
                            "חיפושית פולקסווגן",
                            "שברולט קורבט"
                        ],
                        "correct": 0,
                        "explanation": "הלמבורגיני מיורה הציבה מנוע V12 רוחבי מאחורי תא הנהג, וקבעה את תצורת המנוע המרכזי המגדירה את כל מכוניות-העל עד היום."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו תצורת מנוע פותחה עבור מכונית-העל בוגאטי ויירון שהגיעה למהירות של מעל 400 קמ״ש בשנת 2005?",
                        "options": [
                            "מנוע W16 בנפח 8.0 ליטר עם 4 מגדשי טורבו (Quad-Turbo)",
                            "מנוע 4 צילינדרים בטור אטמוספרי",
                            "מנוע רוטורי וואנקל בודד",
                            "מנוע דיזל דו-פעימתי"
                        ],
                        "correct": 0,
                        "explanation": "הבוגאטי ויירון צוידה במנוע W16 מרובע-מגדשים (שילוב של שני מנועי V8 על גל ארכובה משותף) שהפיק 1,001 כוחות סוס."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מדוע מכונית הפרארי 250 GTO משנות ה-60 נחשבת למכונית האספנות היקרה בעולם, הנמכרת במעל 70 מיליון דולר?",
                        "options": [
                            "רק 36 מכוניות נבנו בעבודת יד, ששילבו מורשת מרוצים עולמית, גוף אלומיניום מרהיב ומנוע Colombo V12 צורח",
                            "היא הייתה המכונית הראשונה עם תיבת הילוכים אוטומטית",
                            "היא כללה גג סולארי פוטו-וולטאי",
                            "היא יוצרה מטיטניום מלא"
                        ],
                        "correct": 0,
                        "explanation": "עם 36 יחידות בלבד, ניצחונות באליפויות עולם ועיצוב עוצר נשימה מבית סקאליאטי, ה-250 GTO היא מכונית האספנות הנחשקת והיקרה ביותר בתולדות האנושות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מכונית ספורט גרמנית איקונית, שהוצגה ב-1963 עם מנוע 'בוקסר' אחורי בעל 6 צילינדרים, מיוצרת ברציפות עד היום?",
                        "options": [
                            "פורשה 911 (Porsche 911)",
                            "ב.מ.וו M3",
                            "מרצדס-בנץ 300SL",
                            "אאודי R8"
                        ],
                        "correct": 0,
                        "explanation": "הפורשה 911 עוצבה על ידי פרדיננד 'בוצי' פורשה והושקה ב-1963; תצורת המנוע האחורי הייחודית שלה ממשיכה ברציפות כבר שמונה דורות מעל 60 שנה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מאפיין העניק למרצדס-בנץ 300 SL משנת 1954 את הכינוי האגדי 'כנפי שחף' (Gullwing)?",
                        "options": [
                            "דלתות הנפתחות כלפי מעלה מצירי הגג בשל שלדת צינורות מרחבית גבוהה",
                            "כנפיים מנוצות שהותקנו על תא המטען",
                            "צופר שהשמיע קולות של עופות ים",
                            "צינור פליטה בצורת מקור נשר"
                        ],
                        "correct": 0,
                        "explanation": "שלדת הצינורות המרחבית הקשיחה של ה-300 SL עברה גבוה לאורך הדפנות, מה שמנע התקנת דלתות רגילות וחייב דלתות הנפתחות מעלה כמו כנפי שחף."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "באיזו שנה הוצגה מכונית הפורד מודל T המהפכנית, שמכרה מעל 15 מיליון יחידות ברחבי העולם?",
                        "options": [
                            "1908",
                            "1935",
                            "1880",
                            "1955"
                        ],
                        "correct": 0,
                        "explanation": "באוקטובר 1908 הנרי פורד השיק את המודל T האמינה והזולה, שהעלתה את העולם על גלגלים וחוללה מהפכה תחבורתית."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מה היה החידוש התכנוני המהפכני של מכונית המיני המקורית מ-1959 שעיצב אלק איסיגוניס?",
                        "options": [
                            "הצבת המנוע לרוחב עם הנעה קדמית כדי למקסם 80% משטח הרצפה לנוסעים ומטען",
                            "מנוע V8 מרכזי מאחורי הנהג",
                            "מערכת היגוי לארבעת הגלגלים עם מנוע דיזל היברידי",
                            "שלדת עץ עם בלמים פנאומטיים"
                        ],
                        "correct": 0,
                        "explanation": "איסיגוניס התקין את המנוע לרוחב מעל הגלגלים הקדמיים עם תיבת הילוכים באגן השמן, וקבע את התצורה המשרתת כיום מעל 90% מהמכוניות הקומפקטיות בעולם."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו יצרנית רכב שוודית המציאה את חגורת הבטיחות המודרנית בעלת 3 נקודות עיגון ב-1959 והעניקה את הפטנט בחינם לכל המתחרים?",
                        "options": [
                            "וולוו (Volvo - המהנדס נילס בוהלין)",
                            "סאאב",
                            "קוניגסג",
                            "סקניה"
                        ],
                        "correct": 0,
                        "explanation": "מהנדס וולוו נילס בוהלין המציא את חגורת 3 הנקודות ב-1959; וולוו ויתרה על זכויות הפטנט כדי להציל חיים, המצאה שהצילה מעל מיליון בני אדם עד היום."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו תפקידו העיקרי של מגדש טורבו (Turbocharger) ברכב?",
                        "options": [
                            "ניצול גזי הפליטה הלוהטים לסיבוב טורבינה הדוחסת אוויר עשיר בחמצן לצילינדרים להפקת כוח רב יותר",
                            "הזרקת מים למכל הדלק לקירור הרדיאטור",
                            "סיבוב הגלגלים האחוריים באמצעות אנרגיית סוללה",
                            "ניקוי הממיר הקטליטי באמצעות מגנטים אלקטרוסטטיים"
                        ],
                        "correct": 0,
                        "explanation": "מגדש טורבו מנצל את אנרגיית גזי הפליטה כדי לדחוס כמות גדולה יותר של אוויר לתוך תאי השריפה, ומאפשר להפיק הספק עצום ממנועים קטנים וחסכוניים."
                    }
                ]
            },

            # =================================================================
            # CATEGORY 4: Speed Records & Motorsport Legends
            # =================================================================
            {
                "id": "speed_records_motorsport",
                "title": "שיאי מהירות ואגדות ספורט מוטורי",
                "description": "שבירת מחסום הקול ביבשה, הקרב האגדי של פורד מול פרארי בלה-מאן, פריצות דרך בפורמולה 1 ורכבות קליע מהירות.",
                "cards": [
                    {
                        "title": "ThrustSSC: המכונית העל-קולית הראשונה (1997)",
                        "points": [
                            "ב-15 באוקטובר 1997, במדבר הסלע השחור בנבאדה, רכב הסילון הבריטי ThrustSSC הפך לרכב היבשתי הראשון בהיסטוריה ששבר רשמית את מחסום הקול.",
                            "נהוג בידי טייס הקרב של חיל האוויר המלכותי אנדי גרין, ה-ThrustSSC קבע שיא מהירות יבשתי של 1,227.985 קמ״ש (763.035 מייל/שעה / מאך 1.016).",
                            "הרכב הונע על ידי שני מנועי טורבו-מניפה של רולס-רויס ממטוס קרב F-4 פנטום, שהפיקו 110,000 כוחות סוס וצרכו 18 ליטר דלק בכל שנייה!",
                            "הצופים במדבר שמעו בום על-קולי כפול מוחץ כאשר מכונית הסילון חלפה במיל המדוד."
                        ]
                    },
                    {
                        "title": "פורד מול פרארי במרוץ 24 השעות של לה-מאן (1966)",
                        "points": [
                            "לאחר שאנזו פרארי ביטל ברגע האחרון עסקת רכישה על ידי פורד ב-1963, הנרי פורד השני נשבע להביס את פרארי במרוץ הסיבולת היוקרתי בעולם: 24 השעות של לה-מאן.",
                            "קרול שלבי והנהג/מהנדס קן מיילס שכללו את הפורד GT40 עם מנוע V8 אמריקאי ענק בנפח 7.0 ליטר ועיצוב אווירודינמי מחודש.",
                            "במרוץ לה-מאן 1966, שלוש מכוניות פורד GT40 חצו את קו הסיום במקומות 1, 2 ו-3 בסיום מושלם שקטע רצף של 6 שנות ניצחון של פרארי.",
                            "ה-GT40 המשיכה וזכתה בלה-מאן ארבע פעמים ברציפות בין השנים 1966 ל-1969."
                        ]
                    },
                    {
                        "title": "השינקנסן: רכבת הקליע של יפן (1964)",
                        "points": [
                            "נחנכה לקראת אולימפיאדת טוקיו 1964, והייתה קו הרכבת המהיר המסחרי הייעודי הראשון בעולם.",
                            "הרכבת שנסעה בין טוקיו לאוסקה במהירות של 210 קמ״ש קיצרה את זמן הנסיעה מכמעט 7 שעות לפחות מ-4 שעות.",
                            "רכבות השינקנסן פועלות על מסילות ייעודיות רחבות ללא מפגשי כביש-מסילה, עם בקרת רכבות אוטומטית (ATC) ותאים מדוחסים למנהרות.",
                            "במעל 60 שנות פעילות שבהן נסעו מעל 10 מיליארד נוסעים, השינקנסן שומרת על שיא בטיחות מושלם של אפס הרוגים מתאונות או שימוטי רכבת!"
                        ]
                    }
                ],
                "trivia": [
                    {
                        "type": "multiple_choice",
                        "question": "איזה רכב הפך לרכב היבשתי הראשון בהיסטוריה ששבר את מחסום הקול ביבשה בשנת 1997?",
                        "options": [
                            "ThrustSSC (נהוג בידי אנדי גרין במהירות 1,228 קמ״ש)",
                            "Bluebird-Proteus CN7",
                            "Spirit of America",
                            "Bloodhound LSR"
                        ],
                        "correct": 0,
                        "explanation": "ב-15 באוקטובר 1997, טייס ה-RAF אנדי גרין נהג ב-ThrustSSC בעל שני מנועי הסילון למהירות של 1,227.985 קמ״ש (מאך 1.016) במדבר נבאדה."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מכונית מרוץ אמריקאית השיגה ניצחון היסטורי במקומות 1, 2 ו-3 במרוץ 24 השעות של לה-מאן בשנת 1966 והביסה את פרארי?",
                        "options": [
                            "פורד GT40 Mk II",
                            "שברולט קורבט סטינגריי",
                            "שלבי קוברה דייטונה קופה",
                            "דודג' וייפר GTS-R"
                        ],
                        "correct": 0,
                        "explanation": "מכונית הפורד GT40 בעלת מנוע ה-7.0 ליטר שפותחה על ידי קרול שלבי וקן מיילס הביסה את פרארי בלה-מאן 1966 בסיום 1-2-3 מרהיב."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו שיא הבטיחות המדהים של רכבת הקליע היפנית (שינקנסן) ב-60 שנות פעילותה?",
                        "options": [
                            "אפס הרוגים משימוטי מסילה או התנגשויות לאורך מעל 10 מיליארד נוסעים",
                            "תאונה קטלנית אחת בלבד בכל עשור",
                            "היא נוסעת במהירות איטית במיוחד בעת גשם",
                            "נוסעים מחויבים לחבוש קסדות מרוץ"
                        ],
                        "correct": 0,
                        "explanation": "מאז חניכתה ב-1964, רשת השינקנסן הסיעה מעל 10 מיליארד נוסעים עם אפס הרוגים מתאונות או שימוטי רכבת, ובדיוק זמנים ממוצע של שניות בודדות."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו 'הכתר המשולש' של הספורט המוטורי (Triple Crown of Motorsport)?",
                        "options": [
                            "ניצחון בגרנד פרי מונקו (F1), במרוץ 24 השעות של לה-מאן, ובאינדיאנפוליס 500",
                            "ניצחון בראלי דקר, בדייטונה 500, ובאי מאן TT",
                            "זכייה בשלוש אליפויות עולם רצופות בפורמולה 1",
                            "קביעת שלושה שיאי מהירות יבשתיים באותה שנה"
                        ],
                        "correct": 0,
                        "explanation": "גרהאם היל הוא הנהג היחיד בהיסטוריה שזכה בכתר המשולש: ניצחון בגרנד פרי מונקו (או אליפות F1), ב-24 השעות של לה-מאן, ובאינדי 500."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו תופעה אווירודינמית שיזם קולין צ'פמן במכוניות לוטוס 78/79 בפורמולה 1 ידועה בשם 'אפקט הקרקע' (Ground Effect)?",
                        "options": [
                            "שימוש במנהרות ונטורי תחתיות וחצאיות צד ליצירת תת-לחץ שיונק את המכונית לאספלט",
                            "הוספת משקולות עופרת כבדות לפגוש הקדמי",
                            "פליטת גזי מפלט לאחור כדי להצמיד את הצמיגים",
                            "מילוי צמיגים בגז קסנון כבד"
                        ],
                        "correct": 0,
                        "explanation": "אפקט הקרקע מנצל את חוק ברנולי במנהרות זרימה מתחת לרצפת הרכב כדי ליצור כוח הצמדה (Downforce) עצום ללא גרר מיותר."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה מרוץ אופנועים היסטורי ומסוכן, המתקיים מאז 1907 בכבישים ציבוריים לאורך 37.73 מייל בהרים, נחשב למסוכן בעולם?",
                        "options": [
                            "מרוץ האי מאן TT (Isle of Man Tourist Trophy)",
                            "גרנד פרי מונקו",
                            "מרוץ באת'רסט 1000",
                            "טיפוס הגבעה הבינלאומי בפייקס פיק"
                        ],
                        "correct": 0,
                        "explanation": "מרוץ ה-Isle of Man TT מתקיים בכבישים כפריים צרים בין חומות אבן ועמודי חשמל במהירויות של מעל 320 קמ״ש."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזה רכיב בטיחות מטיטניום שהוכנס לפורמולה 1 ב-2018 הציל את חייהם של נהגים רבים מפגיעות עצמים והתהפכויות?",
                        "options": [
                            "קשת ה-Halo (ההילה)",
                            "התקן ה-HANS לצוואר",
                            "קשת ההתהפכות הקלאסית",
                            "לוח החלקה תחתון"
                        ],
                        "correct": 0,
                        "explanation": "ה-Halo הוא מבנה טיטניום מעוקל מעל ראש הנהג המסוגל לשאת עומס פגיעה של 12 טונות (משקלם של שני אוטובוסים לונדוניים קומותיים)."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהו מרוץ הסיבולת האמריקאי היוקרתי שנערך באינדיאנה מאז 1911 ומכונה 'The Greatest Spectacle in Racing'?",
                        "options": [
                            "אינדיאנפוליס 500 (Indy 500)",
                            "דייטונה 500",
                            "12 השעות של סברינג",
                            "באחה 1000"
                        ],
                        "correct": 0,
                        "explanation": "מרוץ האינדי 500 מאתגר 33 נהגים ב-200 הקפות (500 מייל) במהירויות של מעל 370 קמ״ש במסלול האובלי ההיסטורי של אינדיאנפוליס."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "איזו מסורת חגיגית מפורסמת מבצע מנצח מרוץ האינדיאנפוליס 500 בבמת המנצחים?",
                        "options": [
                            "שתייה ומזיגה של בקבוק חלב קר על ראשו",
                            "שתיית שמפניה צרפתית יקרה",
                            "נשיקה ליונת מרוץ חיה",
                            "ניפוץ אבטיח בפטיש ענק"
                        ],
                        "correct": 0,
                        "explanation": "המסורת החלה על ידי לואי מאייר ב-1936 ששתה חלב חמאה לרענון בסיום המרוץ הלוהט; מאז המנצח שותה מבקבוק חלב זכוכית מסורתי."
                    },
                    {
                        "type": "multiple_choice",
                        "question": "מהי 'בלימה רגנרטיבית' (Regenerative Braking) ברכבים היברידיים וחשמליים ובמערכות F1 MGU-K?",
                        "options": [
                            "הפעלת המנועים החשמליים כגנרטורים בעת האטה להמרת אנרגיה קינטית בחזרה לחשמל הנאגר בסוללה",
                            "התזת חנקן נוזלי על בלמי הדיסק",
                            "פרישת מצנח אחורי בעת עצירה ברחבת הטיפולים",
                            "היפוך סדר ההצתה בצילינדרים של המנוע"
                        ],
                        "correct": 0,
                        "explanation": "בלימה רגנרטיבית מנצלת את התנגדות המנוע החשמלי כדי להאט את הרכב, וממירה את התנע הקינטי של הרכב לטעינה חשמלית בסוללה."
                    }
                ]
            }
        ]
    }

    # Write English file
    with open(TARGET_EN, "w", encoding="utf-8") as f:
        yaml.safe_dump(aa_en, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_EN}")

    # Write Hebrew file
    with open(TARGET_HE, "w", encoding="utf-8") as f:
        yaml.safe_dump(aa_he, f, allow_unicode=True, sort_keys=False, width=100)
    print(f"Generated {TARGET_HE}")

if __name__ == "__main__":
    create_aviation_automotive_datasets()
