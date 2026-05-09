USE_OF_ENGLISH = {
    # ── PART 4: Key Word Transformation ─────────────────────────────────────
    # 8 key patterns tested (>90% of exam questions):
    # 1. Passive/Reporting  2. Conditionals  3. Reported Speech
    # 4. Time expressions   5. Modal verbs   6. Causative have/get
    # 7. Cleft / emphasis   8. Set phrases / collocations
    "Key Word Transformation": [
        # PATTERN 1 — Passive & Reporting
        {"sentence":"They say he is the best candidate for the role.","key":"said","answer":"He is said to be the best candidate for the role.","pattern":"Passive reporting"},
        {"sentence":"Nobody told me about the change of plans.","key":"informed","answer":"I was not informed about the change of plans.","pattern":"Passive"},
        {"sentence":"The manager made everyone stay late.","key":"made","answer":"Everyone was made to stay late by the manager.","pattern":"Passive causative"},
        {"sentence":"People believe that the suspect has fled the country.","key":"believed","answer":"The suspect is believed to have fled the country.","pattern":"Passive reporting"},
        {"sentence":"Experts report that the company is struggling financially.","key":"reported","answer":"The company is reported to be struggling financially.","pattern":"Passive reporting"},
        {"sentence":"It is thought that the ancient temple was built in 300 BC.","key":"thought","answer":"The ancient temple is thought to have been built in 300 BC.","pattern":"Passive reporting"},
        # PATTERN 2 — Conditionals & Unless
        {"sentence":"If you don't hurry, you'll miss the train.","key":"unless","answer":"Unless you hurry, you'll miss the train.","pattern":"Conditional"},
        {"sentence":"She regrets not studying medicine.","key":"wishes","answer":"She wishes she had studied medicine.","pattern":"Unreal past / wish"},
        {"sentence":"I regret telling her the news so abruptly.","key":"wish","answer":"I wish I hadn't told her the news so abruptly.","pattern":"Wish + past perfect"},
        {"sentence":"Had I known about the problem, I would have helped.","key":"if","answer":"If I had known about the problem, I would have helped.","pattern":"Inverted conditional → standard"},
        {"sentence":"Provided that you study regularly, you will pass the exam.","key":"long","answer":"As long as you study regularly, you will pass the exam.","pattern":"Conditional connector"},
        # PATTERN 3 — Reported Speech
        {"sentence":"'I didn't take the money,' the accused said.","key":"denied","answer":"The accused denied taking the money.","pattern":"Reported speech — deny"},
        {"sentence":"'Why don't we meet earlier?' she said.","key":"suggested","answer":"She suggested meeting earlier.","pattern":"Reported speech — suggest"},
        {"sentence":"My friend advised me to see a doctor.","key":"suggested","answer":"My friend suggested that I (should) see a doctor.","pattern":"Reported speech — suggest"},
        {"sentence":"'I'll definitely finish by Friday,' she promised.","key":"promised","answer":"She promised to finish by Friday.","pattern":"Reported speech — promise"},
        {"sentence":"'You really should take a break,' he told me.","key":"urged","answer":"He urged me to take a break.","pattern":"Reported speech — urge"},
        # PATTERN 4 — Time expressions
        {"sentence":"I haven't spoken to her since last year.","key":"time","answer":"The last time I spoke to her was last year.","pattern":"Time expression"},
        {"sentence":"He started working here six months ago.","key":"for","answer":"He has been working here for six months.","pattern":"Present perfect + for"},
        {"sentence":"It was three years since she had visited her hometown.","key":"three","answer":"She hadn't visited her hometown for three years.","pattern":"Time expression"},
        {"sentence":"She immediately signed the contract on arriving at the office.","key":"sooner","answer":"No sooner had she arrived at the office than she signed the contract.","pattern":"No sooner… than (inversion)"},
        {"sentence":"He had barely sat down when his phone rang.","key":"sooner","answer":"No sooner had he sat down than his phone rang.","pattern":"No sooner… than (inversion)"},
        # PATTERN 5 — Modal verbs
        {"sentence":"It's possible that she has already left.","key":"may","answer":"She may have already left.","pattern":"Modal — possibility"},
        {"sentence":"It wasn't necessary for her to attend the meeting.","key":"need","answer":"She needn't have attended the meeting.","pattern":"Modal — needn't have"},
        {"sentence":"It was wrong of him to shout at the staff.","key":"shouldn't","answer":"He shouldn't have shouted at the staff.","pattern":"Modal — past criticism"},
        {"sentence":"He is unlikely to arrive before midnight.","key":"chance","answer":"There is little chance of him arriving before midnight.","pattern":"Modal — unlikelihood"},
        {"sentence":"It's possible that the package was lost in transit.","key":"might","answer":"The package might have been lost in transit.","pattern":"Modal — past possibility"},
        # PATTERN 6 — Causative have / get
        {"sentence":"A mechanic repaired her car.","key":"had","answer":"She had her car repaired (by a mechanic).","pattern":"Causative have"},
        {"sentence":"Someone stole his wallet while he was on the bus.","key":"had","answer":"He had his wallet stolen while he was on the bus.","pattern":"Causative have — negative event"},
        {"sentence":"The dentist is going to remove two of her teeth next week.","key":"get","answer":"She is going to get two of her teeth removed next week.","pattern":"Causative get"},
        # PATTERN 7 — Emphasis & Set expressions
        {"sentence":"It was such a boring film that I fell asleep.","key":"so","answer":"The film was so boring that I fell asleep.","pattern":"So… that"},
        {"sentence":"She spoke so quietly that nobody could hear her.","key":"audible","answer":"Her voice was barely audible to anyone in the room.","pattern":"Collocation — barely audible"},
        {"sentence":"I find it impossible to understand his motives.","key":"beyond","answer":"His motives are beyond my understanding.","pattern":"Set expression — beyond understanding"},
        {"sentence":"I have rarely seen such a dedicated team.","key":"rarely","answer":"Rarely have I seen such a dedicated team.","pattern":"Inversion with rarely"},
        {"sentence":"Not only was she late, she also forgot the documents.","key":"not","answer":"Not only was she late, but she also forgot the documents.","pattern":"Inversion — Not only"},
        # PATTERN 8 — Collocations & formal register
        {"sentence":"Despite working hard, he didn't pass the exam.","key":"although","answer":"Although he worked hard, he didn't pass the exam.","pattern":"Connector transformation"},
        {"sentence":"The project failed because the team lacked resources.","key":"due","answer":"The project failed due to a lack of resources.","pattern":"Connector transformation"},
        {"sentence":"We had to think carefully about all the options before deciding.","key":"consideration","answer":"We had to take all the options into consideration before deciding.","pattern":"Formal collocation"},
        {"sentence":"She can't stand people who arrive late to meetings.","key":"put","answer":"She can't put up with people who arrive late to meetings.","pattern":"Phrasal verb"},
        {"sentence":"He ignored all the advice his doctor gave him.","key":"notice","answer":"He took no notice of the advice his doctor gave him.","pattern":"Set expression — take no notice"},
        {"sentence":"The two scientists are working on the project jointly.","key":"collaboration","answer":"The two scientists are working on the project in collaboration.","pattern":"Formal register"},
    ],

    # ── PART 3: Word Formation ───────────────────────────────────────────────
    # Patterns: -ment (20%), un-/in- negatives (15%), -tion/-sion (15%),
    # person nouns -er/-or/-ist, adjectives -ive/-ous/-ful/-less/-able
    "Word Formation": [
        # Nouns from verbs
        {"base":"rely","prompt":"Her ___ on technology has grown significantly over the past decade. (RELY)","answer":"reliance"},
        {"base":"achieve","prompt":"The ___ of such outstanding results required years of dedication. (ACHIEVE)","answer":"achievement"},
        {"base":"persist","prompt":"Her ___ in the face of repeated setbacks was truly admirable. (PERSIST)","answer":"persistence"},
        {"base":"respond","prompt":"The government's ___ to the crisis was widely criticised as too slow. (RESPOND)","answer":"response"},
        {"base":"innovate","prompt":"The company's reputation for ___ has attracted investors worldwide. (INNOVATE)","answer":"innovation"},
        {"base":"consider","prompt":"She gave the matter careful ___ before reaching her conclusion. (CONSIDER)","answer":"consideration"},
        {"base":"appreciate","prompt":"Her ___ of classical music grew during her years studying in Vienna. (APPRECIATE)","answer":"appreciation"},
        {"base":"persevere","prompt":"___ is the key quality that distinguishes successful researchers. (PERSEVERE)","answer":"Perseverance"},
        {"base":"commit","prompt":"Her ___ to the project inspired everyone around her. (COMMIT)","answer":"commitment"},
        {"base":"manage","prompt":"Effective ___ of resources is crucial for any organisation. (MANAGE)","answer":"management"},
        {"base":"fulfil","prompt":"The sense of ___ she felt after the performance was overwhelming. (FULFIL)","answer":"fulfilment"},
        {"base":"judge","prompt":"His ___ of the situation turned out to be completely wrong. (JUDGE)","answer":"judgement"},
        # Nouns from adjectives
        {"base":"signify","prompt":"There has been no ___ improvement in air quality since the new regulations. (SIGNIFY)","answer":"significant"},
        {"base":"scrutinise","prompt":"The accounts have been subjected to intense public ___. (SCRUTINISE)","answer":"scrutiny"},
        {"base":"affluent","prompt":"The gap between ___ and poverty has widened considerably. (AFFLUENT)","answer":"affluence"},
        {"base":"subtle","prompt":"The distinction between the two concepts is one of ___. (SUBTLE)","answer":"subtlety"},
        {"base":"ambiguous","prompt":"There is some ___ in the wording of the contract. (AMBIGUOUS)","answer":"ambiguity"},
        {"base":"tolerant","prompt":"The city is known for its cultural ___ and openness. (TOLERANT)","answer":"tolerance"},
        {"base":"diverse","prompt":"The report highlights the ___ of approaches taken across different regions. (DIVERSE)","answer":"diversity"},
        # Adjectives from nouns/verbs
        {"base":"contradict","prompt":"The two studies produced entirely ___ findings. (CONTRADICT)","answer":"contradictory"},
        {"base":"knowledge","prompt":"She is exceptionally ___ about twentieth-century European history. (KNOWLEDGE)","answer":"knowledgeable"},
        {"base":"oblige","prompt":"Attendance at the seminar is ___ for all registered students. (OBLIGE)","answer":"obligatory"},
        {"base":"controversy","prompt":"The decision to close the hospital proved highly ___. (CONTROVERSY)","answer":"controversial"},
        {"base":"prevail","prompt":"The ___ view among experts is that further cuts are unavoidable. (PREVAIL)","answer":"prevailing"},
        {"base":"access","prompt":"The new ramp made the building fully ___ to wheelchair users. (ACCESS)","answer":"accessible"},
        {"base":"sustain","prompt":"Governments need to invest in ___ energy sources. (SUSTAIN)","answer":"sustainable"},
        # Adverbs
        {"base":"overwhelm","prompt":"The response to the charity appeal was ___ positive. (OVERWHELM)","answer":"overwhelmingly"},
        {"base":"consequent","prompt":"The factory closed, and ___ hundreds of workers lost their jobs. (CONSEQUENT)","answer":"consequently"},
        {"base":"remark","prompt":"She performed ___ well under pressure. (REMARK)","answer":"remarkably"},
        # Negatives with prefixes (un-, in-, dis-, mis-, ir-)
        {"base":"predict","prompt":"The long-term effects of the policy remain largely ___. (PREDICT)","answer":"unpredictable"},
        {"base":"responsible","prompt":"Driving under the influence is dangerously ___. (RESPONSIBLE)","answer":"irresponsible"},
        {"base":"approve","prompt":"The board expressed ___ of the proposed changes. (APPROVE)","answer":"disapproval"},
        {"base":"lead","prompt":"The advertising campaign was found to be deliberately ___. (LEAD)","answer":"misleading"},
        {"base":"avoidable","prompt":"Many of the complications were entirely ___. (AVOIDABLE)","answer":"unavoidable"},
        # Person nouns
        {"base":"investigate","prompt":"The case was handed over to a senior ___. (INVESTIGATE)","answer":"investigator"},
        {"base":"advocate","prompt":"She is a passionate ___ of prison reform. (ADVOCATE)","answer":"advocate"},
        {"base":"reside","prompt":"Long-term ___ of the neighbourhood opposed the development. (RESIDE)","answer":"residents"},
    ],

    # ── PART 1: Multiple Choice Cloze ────────────────────────────────────────
    # Tests vocabulary: collocations, fixed expressions, phrasal verbs, register
    "Multiple Choice Cloze": [
        {"sentence":"The new policy was met with widespread ___ from the business community.","options":["A) approval","B) resistance","C) compliance","D) encouragement"],"answer":"B","explanation":"'Resistance' collocates with 'met with' when something is opposed. This tests fixed collocations with 'met with'."},
        {"sentence":"She managed to ___ a deal with the investors at the very last minute.","options":["A) close","B) strike","C) make","D) take"],"answer":"B","explanation":"'Strike a deal' is a fixed collocation. This tests knowledge of verbs that collocate with 'deal'."},
        {"sentence":"The documentary ___ light on a rarely discussed social issue.","options":["A) put","B) cast","C) shed","D) threw"],"answer":"C","explanation":"'Shed light on' = make something clearer. A common Cambridge fixed expression."},
        {"sentence":"His behaviour was ___ out of character for someone so professional.","options":["A) distinctly","B) largely","C) highly","D) entirely"],"answer":"D","explanation":"'Entirely out of character' is the natural collocation. Tests adverb–adjective collocations."},
        {"sentence":"The research findings ___ into question the effectiveness of the treatment.","options":["A) called","B) brought","C) drew","D) cast"],"answer":"A","explanation":"'Call into question' = cast doubt on. Fixed phrase tested very frequently in Cambridge exams."},
        {"sentence":"The committee reached a ___ that the proposal should be withdrawn.","options":["A) resolution","B) conclusion","C) decision","D) settlement"],"answer":"B","explanation":"'Reach a conclusion' is the fixed collocation here. 'Decision' needs 'make', not 'reach', in this context."},
        {"sentence":"The organisation has gone to great ___ to ensure full transparency.","options":["A) lengths","B) distances","C) measures","D) levels"],"answer":"A","explanation":"'Go to great lengths' = make great efforts. A fixed idiomatic expression."},
        {"sentence":"She has a ___ grasp of the technical aspects of the project.","options":["A) solid","B) firm","C) tight","D) hard"],"answer":"A","explanation":"'A solid grasp of something' = thorough understanding. Tests adjective–noun collocations."},
        {"sentence":"The prime minister came ___ considerable criticism after the announcement.","options":["A) across","B) under","C) upon","D) through"],"answer":"B","explanation":"'Come under criticism/pressure/fire' is a fixed prepositional phrase meaning to be subjected to."},
        {"sentence":"The findings of the report ___ with official government statistics.","options":["A) contrast","B) compete","C) collide","D) clash"],"answer":"D","explanation":"'Clash with' = conflict with or be incompatible with. Tests verb–preposition collocations."},
        {"sentence":"The charity aims to raise ___ of the risks of social isolation.","options":["A) consciousness","B) awareness","C) understanding","D) knowledge"],"answer":"B","explanation":"'Raise awareness' is a fixed collocation. 'Raise consciousness' exists but is less common in this context."},
        {"sentence":"Her speech made a ___ impression on everyone who attended.","options":["A) lasting","B) remaining","C) continuing","D) staying"],"answer":"A","explanation":"'Make a lasting impression' is a fixed collocation. The others don't collocate with 'impression' in this way."},
        {"sentence":"The board ___ a decision to restructure the company after months of debate.","options":["A) did","B) made","C) took","D) reached"],"answer":"C","explanation":"'Take a decision' (formal British English) = 'make a decision'. Both are correct but 'take' is the key word tested here."},
        {"sentence":"His composure under pressure was ___ admired by his colleagues.","options":["A) widely","B) broadly","C) largely","D) greatly"],"answer":"A","explanation":"'Widely admired' is the fixed adverb–past participle collocation. 'Greatly' would also work but 'widely' is the stronger collocation here."},
        {"sentence":"The new initiative ___ a significant shift in government policy.","options":["A) signals","B) marks","C) shows","D) displays"],"answer":"B","explanation":"'Mark a shift/change/turning point' is a fixed collocation used in formal writing."},
    ],

    # ── PART 2: Open Cloze ───────────────────────────────────────────────────
    # Tests: articles, prepositions, pronouns, conjunctions, auxiliary verbs,
    # quantifiers, relative pronouns, linkers — ONE word per gap
    "Open Cloze": [
        {
            "title":"Technology & Society",
            "text":"The rapid pace of technological change has (1)___ rise to a range of ethical questions that society is only beginning to grapple (2)___. Critics argue that artificial intelligence, far (3)___ being a neutral tool, reflects the biases of those who create it. (4)___ is more, the concentration of data in the hands of a few corporations poses risks (5)___ democratic oversight. (6)___ these concerns are taken seriously, there is little doubt that regulation will need to keep pace with innovation.",
            "answers":{"1":"given","2":"with","3":"from","4":"What","5":"to","6":"Unless"},
            "tips":"Gap 1: fixed phrase 'give rise to'. Gap 2: 'grapple WITH'. Gap 3: 'far FROM being'. Gap 4: 'What is more' = connector. Gap 5: 'pose risks TO'. Gap 6: linker of condition."
        },
        {
            "title":"Urban Migration",
            "text":"It (1)___ widely acknowledged that urbanisation has transformed the social fabric of many countries. (2)___ growing numbers of people migrate from rural areas, cities face mounting pressure on housing and infrastructure. (3)___ all the challenges this entails, urban centres continue to attract those (4)___ seek better economic opportunities. Policymakers are increasingly aware (5)___ the need to strike a balance between economic growth and social cohesion, (6)___ as to avoid deepening existing inequalities.",
            "answers":{"1":"is","2":"As","3":"Despite","4":"who","5":"of","6":"so"},
            "tips":"Gap 1: passive structure 'It IS acknowledged'. Gap 2: linker showing simultaneous situation. Gap 3: concession preposition. Gap 4: relative pronoun for people. Gap 5: 'aware OF'. Gap 6: 'so as to' = purpose."
        },
        {
            "title":"The Value of Failure",
            "text":"Failure is (1)___ often perceived as something to be avoided at all costs. Yet (2)___ closer inspection, it becomes clear that setbacks play a crucial (3)___ in personal development. Some of the most successful entrepreneurs attribute (4)___ achievements not to their triumphs, but to the lessons learnt from their mistakes. (5)___ is not to say that failure should be welcomed for its (6)___ sake, but rather that our response to it defines our capacity for growth.",
            "answers":{"1":"all","2":"on","3":"role","4":"their","5":"This","6":"own"},
            "tips":"Gap 1: 'all too often' = fixed intensifying phrase. Gap 2: 'on closer inspection' = fixed expression. Gap 3: 'play a role'. Gap 4: possessive pronoun. Gap 5: referencing pronoun. Gap 6: 'for its own sake' = fixed phrase."
        },
        {
            "title":"The Future of Work",
            "text":"Automation is transforming the workplace at a pace (1)___ has few historical precedents. While many jobs are (2)___ to disappear, others will evolve, and entirely new roles will emerge. The key challenge facing governments and businesses (3)___ is how to equip workers with the skills they will need. (4)___ simply retraining existing workers, some economists argue that a more fundamental rethink of education is called (5)___. Without such investment, there is a real risk (6)___ large segments of the population will be left behind.",
            "answers":{"1":"that","2":"likely","3":"alike","4":"Beyond","5":"for","6":"that"},
            "tips":"Gap 1: relative pronoun for 'pace'. Gap 2: 'likely to disappear' = adverb. Gap 3: 'governments and businesses ALIKE' = fixed phrase. Gap 4: 'Beyond X-ing' = going further than. Gap 5: 'called FOR' = required. Gap 6: 'risk THAT' = introducing a that-clause."
        },
        {
            "title":"Cultural Heritage",
            "text":"Preserving cultural heritage has become (1)___ of the most pressing concerns of our time. Monuments and traditions that have survived (2)___ centuries are now threatened by climate change, urban development, and neglect. Governments (3)___ the world over have pledged resources to address this issue, (4)___ progress has been slow. Critics argue that without sustained funding, many sites will be lost (5)___ good. (6)___ the case may be, there can be no doubt that swift action is needed.",
            "answers":{"1":"one","2":"for","3":"across","4":"yet","5":"for","6":"Whatever"},
            "tips":"Gap 1: 'one of the most…' = superlative structure. Gap 2: 'survived FOR centuries'. Gap 3: 'across the world over' — no, 'ACROSS the world'. Gap 4: concessive connector. Gap 5: 'lost FOR good' = permanently. Gap 6: 'Whatever the case may be' = fixed concessive expression."
        },
    ],
}

# ── Cambridge C1 Advanced — Test 1 ──────────────────────────────────────────
CAMBRIDGE_TEST_1 = {
    "title": "Cambridge C1 Advanced — Test 1",

    # Part 1 — Multiple Choice Cloze
    "Part 1": {
        "title": "The camera never lies",
        "text": (
            "In 1917, Arthur Conan Doyle, the creator of Sherlock Holmes, provided the (1)___ "
            "for one of the most remarkable cases of self-deception in photographic history. "
            "Two young girls from Cottingley, Yorkshire, claimed to have photographed real fairies "
            "in their garden. Rather than (2)___ the images to the work of an imaginative child, "
            "Doyle — himself a convinced spiritualist — publicly endorsed them as genuine. "
            "The photographs were, of course, (3)___: the 'fairies' were paper cut-outs from a "
            "children's book that had been (4)___ in front of a garden stream. What the case "
            "(5)___ illustrates is how powerful the desire to believe can be. Ironically, the "
            "whole affair (6)___ the very principles of rational enquiry that Doyle's most famous "
            "character, Sherlock Holmes, supposedly embodied. The episode also had the unintended "
            "effect of (7)___ others to attempt similar hoaxes using photographic technology. "
            "Decades later, the Cottingley Fairies entered popular culture as a (8)___ that has "
            "never quite lost its power to intrigue."
        ),
        "gaps": [
            {
                "num": 1,
                "options": ["A) venue", "B) setting", "C) background", "D) surrounding"],
                "answer": "B",
                "explanation": "'Provide the setting for' is a fixed collocation meaning to create the backdrop or context for an event.",
            },
            {
                "num": 2,
                "options": ["A) calling", "B) naming", "C) attributing", "D) acknowledging"],
                "answer": "C",
                "explanation": "'Attributing sth to sth' = assigning the cause of something to something else. The others don't take the 'to' complement in this way.",
            },
            {
                "num": 3,
                "options": ["A) false", "B) faulty", "C) fake", "D) fictional"],
                "answer": "C",
                "explanation": "'Fake' = deliberately made to deceive. 'Faulty' means defective; 'fictional' belongs to stories; 'false' is more abstract.",
            },
            {
                "num": 4,
                "options": ["A) arranged", "B) spaced", "C) settled", "D) distributed"],
                "answer": "A",
                "explanation": "'Arranged in front of' = positioned deliberately. The others don't collocate naturally with 'in front of a backdrop'.",
            },
            {
                "num": 5,
                "options": ["A) categorically", "B) unavoidably", "C) substantially", "D) undeniably"],
                "answer": "D",
                "explanation": "'Undeniably illustrates' = without doubt demonstrates. 'Categorically' pairs with 'deny/state'; 'unavoidably' is less idiomatic here.",
            },
            {
                "num": 6,
                "options": ["A) weakens", "B) undermines", "C) demolishes", "D) dismantles"],
                "answer": "B",
                "explanation": "'Undermine principles/faith/confidence' is the strong collocation. 'Demolish' and 'dismantle' suggest complete destruction; 'weaken' is vaguer.",
            },
            {
                "num": 7,
                "options": ["A) letting", "B) supporting", "C) enabling", "D) empowering"],
                "answer": "C",
                "explanation": "'Enabling sb to do sth' = making it possible. 'Letting' takes bare infinitive; 'empowering' has a positive connotation unsuitable for 'hoaxers'.",
            },
            {
                "num": 8,
                "options": ["A) fantasy", "B) legend", "C) dream", "D) myth"],
                "answer": "D",
                "explanation": "'Myth' = a widely believed but false story. It perfectly captures something that entered culture as a false belief, unlike 'legend' (implies some historical truth) or 'fantasy' (purely imaginary).",
            },
        ],
    },

    # Part 2 — Open Cloze
    "Part 2": {
        "title": "Online passwords",
        "text": (
            "Almost (9)___ who uses the internet today will be familiar with the problems of "
            "online security. Password theft has become so common that services (10)___ banks "
            "and social media platforms now urge users to change their passwords regularly. "
            "Experts recommend that users should (11)___ their passwords as hard to guess as "
            "possible, ideally using a random combination of letters, numbers and symbols. "
            "It is also advisable to use a different password (12)___ each account you hold "
            "online. Passwords can also be strengthened (13)___ adding a series of random "
            "characters at the end. The difficulty is that many people simply (14)___ too many "
            "passwords to remember, which has led to the rise of specialist password management "
            "software. Such apps store all your passwords in one place, freeing (15)___ space "
            "in your memory for more important things. If you ever suspect that a password has "
            "been stolen, you should find (16)___ immediately whether your other accounts have "
            "also been compromised."
        ),
        "answers": {
            "9": "anyone",
            "10": "like",
            "11": "make",
            "12": "for",
            "13": "by",
            "14": "have",
            "15": "up",
            "16": "out",
        },
        "accepted": {
            "9": ["anyone", "everybody"],
            "10": ["like", "such as"],
        },
        "tips": (
            "Gap 9: 'Almost anyone who…' — general person reference. "
            "Gap 10: 'services LIKE/SUCH AS banks' — giving examples. "
            "Gap 11: 'make sth as hard as possible' — fixed comparative structure. "
            "Gap 12: 'a different password FOR each account' — preposition. "
            "Gap 13: 'strengthened BY adding' — agent/means preposition. "
            "Gap 14: 'people HAVE too many passwords' — simple present auxiliary. "
            "Gap 15: 'freeing UP space' — phrasal verb. "
            "Gap 16: 'find OUT whether' — phrasal verb meaning to discover."
        ),
    },

    # Part 3 — Word Formation
    "Part 3": {
        "title": "Too many climbers on Mount Everest",
        "items": [
            {"num": 17, "base": "FAVOUR",    "prompt": "The weather conditions were far from (17)___ for an attempt on the summit. (FAVOUR)",    "answer": "favourable"},
            {"num": 18, "base": "EXPECT",    "prompt": "The team suffered several (18)___ setbacks on their way to the higher camps. (EXPECT)",    "answer": "unexpected"},
            {"num": 19, "base": "BEGIN",     "prompt": "The route now attracts not only seasoned climbers but also (19)___ with very little experience. (BEGIN)",   "answer": "beginners"},
            {"num": 20, "base": "DESPERATE", "prompt": "In their (20)___ to reach the summit, many climbers ignore clear safety warnings. (DESPERATE)", "answer": "desperation"},
            {"num": 21, "base": "DANGER",    "prompt": "Overcrowding on the upper slopes may (21)___ the lives of every climber on the mountain. (DANGER)",   "answer": "endanger"},
            {"num": 22, "base": "SOLVE",     "prompt": "Finding a workable (22)___ to the problem of overcrowding has proved extremely difficult. (SOLVE)",    "answer": "solution"},
            {"num": 23, "base": "ALTERNATE", "prompt": "(23)___, some climbers choose to attempt less-crowded peaks of a similar height. (ALTERNATE)", "answer": "Alternatively"},
            {"num": 24, "base": "MOUNTAIN",  "prompt": "Experienced (24)___ warn that Everest should never be treated as a tourist attraction. (MOUNTAIN)",  "answer": "mountaineers"},
        ],
    },

    # Part 4 — Key Word Transformation
    "Part 4": {
        "items": [
            {
                "num": 25,
                "sentence": "She was told she should stop her children watching so much TV.",
                "key": "let",
                "answer": "She was advised not to let her children watch so much TV.",
                "pattern": "stop + -ing → not let + bare infinitive",
            },
            {
                "num": 26,
                "sentence": "Driving in the city centre after 10 pm is now against the law.",
                "key": "illegal",
                "answer": "It has been made illegal to drive in the city centre after 10 pm.",
                "pattern": "against the law → make it illegal to",
            },
            {
                "num": 27,
                "sentence": "He was late, which meant he missed the last train.",
                "key": "time",
                "answer": "If he had left in time, he would not have missed the last train.",
                "pattern": "past result → third conditional with 'in time'",
            },
            {
                "num": 28,
                "sentence": "The new edition of the book has been thoroughly revised.",
                "key": "thorough",
                "answer": "The new edition of the book appears to be a thorough revision of the original.",
                "pattern": "adverb + past participle → noun phrase with adjective",
            },
            {
                "num": 29,
                "sentence": "The temperature rose gradually over the following weeks.",
                "key": "gradual",
                "answer": "There was a gradual rise in temperature over the following weeks.",
                "pattern": "verb + adverb → there was + adjective + noun",
            },
            {
                "num": 30,
                "sentence": "The new law didn't make any difference to the unemployment figures.",
                "key": "consequence",
                "answer": "The new law had no consequences for the unemployment figures.",
                "pattern": "make no difference → have no consequences for",
            },
        ],
    },
}
