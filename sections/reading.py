import streamlit as st
from components.state import add_score

# ── Part 5 data ───────────────────────────────────────────────────────────────
PART5 = {
    "title": "The Return of Analogue",
    "text": """There is something almost paradoxical about the twenty-first century's growing obsession
with the analogue. In an age when everything from our music to our photographs exists as a series of
ones and zeros, an increasing number of people are choosing to engage with the world through formats
that were supposedly made obsolete decades ago. Vinyl record sales have risen for the sixteenth
consecutive year. Film cameras are being produced again after years out of manufacture. Independent
bookshops are flourishing. And the humble paper diary has experienced something of a renaissance.

Commentators have been quick to offer explanations. The most common suggestion is that these analogue
formats offer a sense of authenticity that digital alternatives cannot match. A vinyl record, with its
warm crackle and its physical weight, engages the listener in a way that a streaming playlist simply
does not. A photograph taken on film, with its imperfections and the uncertainty of not knowing quite
how it will turn out, captures something that the instant gratification of a digital image lacks.

Yet this explanation may be too straightforward. For many younger consumers — people who have grown
up with smartphones and have no nostalgic attachment to physical formats — the appeal appears to lie
not in authenticity but in resistance. To choose a vinyl record is, in some sense, to refuse the
logic of a world in which everything is instant, frictionless and algorithmically curated.
The slowness is the point.

There is also a social dimension to consider. Listening to a vinyl record, developing a roll of film,
or writing in a paper diary are all activities that resist multitasking. They demand a kind of
focused, singular attention that is increasingly rare. And that very rarity, it seems, has become
its own form of luxury.

Whether this trend represents a meaningful cultural shift or merely a cyclical fashion remains to be
seen. What is clear is that the analogue revival is not, as it might first appear, a retreat from
modernity. It is, rather, a highly modern response to some of the more troubling aspects of
digital life.""",
    "questions": [
    {
            "q": "What point does the writer make in the opening paragraph?",
            "options": [
                "A) Analogue formats have never really disappeared from everyday life.",
                "B) Digital technology has failed to deliver on its early promise.",
                "C) The growing popularity of analogue formats is unexpected given the era we live in.",
                "D) Most people now prefer analogue formats to digital alternatives.",
            ],
            "answer": "C",
            "explanation": "The writer describes it as 'almost paradoxical' and notes these formats were 'supposedly made obsolete', highlighting the unexpected nature of their revival.",
    },
    {
            "q": "What does the writer suggest about vinyl records in the second paragraph?",
            "options": [
                "A) They produce objectively superior sound quality to streaming services.",
                "B) Their tangible, imperfect qualities create a more engaging listening experience.",
                "C) Listeners are mainly drawn to them for reasons of nostalgia.",
                "D) They are more socially acceptable than streaming among older consumers.",
            ],
            "answer": "B",
            "explanation": "'Physical weight' and 'warm crackle' engage the listener in a way that a playlist cannot — emphasising the sensory, physical qualities of the format.",
    },
    {
            "q": "The phrase 'too straightforward' (paragraph 3) implies that the writer considers the authenticity argument to be…",
            "options": [
                "A) entirely convincing.",
                "B) an oversimplification of a more complex phenomenon.",
                "C) irrelevant to the majority of analogue consumers.",
                "D) based on inaccurate research.",
            ],
            "answer": "B",
            "explanation": "'May be too straightforward' signals that the explanation captures part of the truth but doesn't account for everything — especially the behaviour of younger consumers.",
    },
    {
            "q": "What does the writer say motivates many younger consumers to choose analogue formats?",
            "options": [
                "A) A desire to connect with the experiences of older generations.",
                "B) Dissatisfaction with the sound and image quality of digital products.",
                "C) A conscious rejection of the values associated with instant digital culture.",
                "D) A belief that analogue formats represent better value for money.",
            ],
            "answer": "C",
            "explanation": "'To refuse the logic of a world in which everything is instant, frictionless and algorithmically curated' — the choice is an act of resistance, not nostalgia.",
    },
    {
            "q": "What does the writer mean when describing focused attention as 'its own form of luxury'?",
            "options": [
                "A) Analogue products are expensive and therefore exclusive to wealthy consumers.",
                "B) Undivided attention has become so uncommon in modern life that it now feels special.",
                "C) People are increasingly prepared to pay a premium for slower experiences.",
                "D) Luxury brands have recognised the marketing potential of analogue aesthetics.",
            ],
            "answer": "B",
            "explanation": "The 'rarity' referred to is that of 'focused, singular attention' — because it is rare in the digital age, the ability to experience it has acquired the status of a luxury.",
    },
    {
            "q": "What overall conclusion does the writer reach about the analogue revival?",
            "options": [
                "A) It reflects a widespread and deep-seated rejection of modern technology.",
                "B) It is a short-lived trend that will fade as digital technology improves.",
                "C) It represents a thoughtful, contemporary response to the downsides of digital life.",
                "D) It is driven primarily by commercial interests in the music and publishing industries.",
            ],
            "answer": "C",
            "explanation": "'Not a retreat from modernity… a highly modern response to some of the more troubling aspects of digital life' — the revival is framed as sophisticated engagement, not escapism.",
    },
    ],
}

# ── Part 6 data ───────────────────────────────────────────────────────────────
PART6 = {
    "title": "Four writers on arts education in schools",
    "texts": [
    {
            "label": "A",
            "name": "Maria Santos",
            "text": (
                "The systematic removal of arts subjects from school timetables in favour of "
                "so-called STEM subjects is a trend that concerns me deeply. There is robust "
                "evidence that engagement with the arts develops qualities — creativity, empathy, "
                "the ability to think laterally — that are essential not just for personal "
                "wellbeing but for a functioning society. By treating the arts as a luxury rather "
                "than a necessity, we are impoverishing future generations. Arts education needs "
                "to be protected, not merely tolerated as a reluctant concession to tradition."
            ),
    },
    {
            "label": "B",
            "name": "James Okafor",
            "text": (
                "Much of the debate around arts versus STEM in schools is, I think, based on a "
                "false premise. These are not competing priorities. The most innovative companies "
                "in the world actively seek people who combine technical skills with the kind of "
                "lateral thinking that arts subjects foster. Rather than asking which is more "
                "important, we should be asking how schools can integrate them more effectively. "
                "Removing arts from the curriculum would, paradoxically, make students less "
                "equipped for the modern workplace, not more."
            ),
    },
    {
            "label": "C",
            "name": "Elena Petrov",
            "text": (
                "I have some sympathy with those who argue for the value of arts education, but "
                "we must be realistic. Core academic subjects must come first. If arts subjects "
                "are to have a place in the school day, it should be as a complement to academic "
                "study, not a substitute for it. We also have a responsibility to advise students "
                "honestly about career prospects in the creative industries, which, for most, are "
                "limited. Enthusiasm alone is not sufficient preparation for adult life."
            ),
    },
    {
            "label": "D",
            "name": "Tom Walsh",
            "text": (
                "What troubles me most about arts education today is not that it is under-resourced, "
                "but that it has been corrupted by utilitarian thinking. Schools now justify the "
                "teaching of art, music and drama in terms of employability and transferable skills. "
                "This fundamentally misses the point. The arts should be taught because they are "
                "intrinsically valuable — because they teach students something about what it means "
                "to be human — not because they produce more versatile workers."
            ),
    },
    ],
    "questions": [
    {
            "q": "Which writer shares Writer A's view that current educational trends are harming arts subjects?",
            "answer": "B",
            "explanation": "Both A and B are concerned that STEM priorities are crowding out arts — B calls it a 'false premise' to see them as competing, while A warns of 'impoverishing future generations'.",
    },
    {
            "q": "Which writer, unlike Writers A, B and D, emphasises practical career considerations in the debate?",
            "answer": "C",
            "explanation": "C explicitly argues for 'honest' advice about limited career prospects — the other writers do not prioritise employability outcomes in this way.",
    },
    {
            "q": "Which writer disagrees with Writer D about how arts education should be justified?",
            "answer": "C",
            "explanation": "C justifies arts in terms of its complementary value to core subjects and career outcomes. D explicitly rejects justifying arts through employability — the very approach C advocates.",
    },
    {
            "q": "Which writer expresses a view similar to Writer B about the relationship between arts and other disciplines?",
            "answer": "A",
            "explanation": "Both A and B reject the idea that arts and other subjects are in opposition. A argues arts develop qualities 'essential for society'; B says combining arts and technical skills is an advantage.",
    },
    ],
}

# ── Part 7 data ───────────────────────────────────────────────────────────────
PART7 = {
    "title": "Urban Rewilding",
    "text_parts": [
    "In cities across the world, a quiet revolution is taking place. Urban rewilding — the "
    "deliberate restoration of natural habitats within city limits — has moved from a fringe "
    "idea to a mainstream policy goal.",

    "[1]",

    "The movement draws on a simple but powerful insight: that human beings are not separate "
    "from nature but part of it, and that the absence of nature in urban environments has "
    "measurable costs.",

    "[2]",

    "The practical challenges, however, are considerable. Land in cities is scarce and "
    "expensive, and the competing demands of housing, transport and commerce make it difficult "
    "to set aside significant areas for ecological restoration.",

    "[3]",

    "Advocates have responded to these challenges with considerable creativity.",

    "[4]",

    "Green roofs, vertical gardens and pocket parks can provide habitats for insects, birds "
    "and small mammals without requiring the dedication of large plots of land. There are also "
    "wider benefits that are frequently overlooked.",

    "[5]",

    "None of this will happen, of course, without sustained political will and genuine public "
    "engagement.",

    "[6]",

    "The most successful urban rewilding projects are those that involve local communities "
    "from the outset — not as passive beneficiaries, but as active participants in the "
    "planning and long-term maintenance of new green spaces.",
    ],
    "options": {
    "A": "These costs are not merely abstract: they have direct and well-documented implications for physical and mental health, with research consistently linking access to green space to lower rates of anxiety and cardiovascular disease.",
    "B": "The solution, many planners now argue, lies in making better use of spaces that already exist within the urban fabric rather than seeking out entirely new sites.",
    "C": "What was once considered the exclusive concern of environmental campaigners is now firmly on the agenda of urban planners, politicians and developers alike.",
    "D": "By absorbing surface water and reducing the urban heat island effect, green spaces perform vital engineering functions that are both difficult and costly to replicate through built infrastructure.",
    "E": "It is also worth noting that well-designed rewilding projects can attract significant private investment when their long-term economic benefits are clearly communicated to developers.",
    "F": "Without commitment from both local authorities and residents, even the most ambitious and well-funded schemes are liable to stall before they can deliver meaningful results.",
    "G": "Planners must therefore find innovative ways to incorporate nature into the existing fabric of urban development, rather than treating it as an afterthought to be addressed once other priorities have been met.",
    },
    "answers": {"1": "C", "2": "A", "3": "G", "4": "B", "5": "D", "6": "F"},
    "distractor": "E",
    "tips": {
    "1": "C — the sentence explains what 'moved to mainstream policy goal' means by naming the new stakeholders.",
    "2": "A — bridges 'measurable costs' to the specific health research evidence.",
    "3": "G — expands on why scarce land forces creative thinking, leading into the next paragraph.",
    "4": "B — introduces the 'small-scale' creative solutions (roofs, gardens) that follow.",
    "5": "D — the 'wider benefits' referred to = drainage and heat island, not health (already covered).",
    "6": "F — restates the 'political will' point in stronger terms before the positive conclusion.",
    "E (distractor)": "Mentions private investment — interesting but doesn't connect to any gap's surrounding text.",
    },
}

# ── Part 8 data ───────────────────────────────────────────────────────────────
PART8 = {
    "title": "Learning a musical instrument as an adult",
    "instruction": "Read the accounts of five adults (A–E) who took up a musical instrument later in life. For questions 47–56, choose from the people (A–E). The people may be chosen more than once.",
    "texts": [
    {
            "label": "A",
            "name": "Rachel",
            "text": (
                "I started learning the violin at forty-two, mainly because my daughter plays and "
                "I wanted to understand what she was going through. I hadn't anticipated how "
                "physically demanding it would be — my fingers ached for weeks, and the bow "
                "control required a degree of precision I simply didn't have. What genuinely "
                "surprised me, though, was discovering a local amateur orchestra that welcomed "
                "adult beginners. I'd expected to practise alone; the sense of community I found "
                "there was something I hadn't bargained for at all."
            ),
    },
    {
            "label": "B",
            "name": "David",
            "text": (
                "Taking up the piano at fifty-five felt like a bold decision, and I'll admit I "
                "was self-conscious about being the oldest student in the class by some distance. "
                "What I've found, though, is that the emotional complexity I've lived through "
                "actually helps me connect with the music in a way that younger students sometimes "
                "struggle to. I practise every morning before work — thirty minutes, without fail. "
                "The discipline of it has become part of my identity in a way I hadn't expected."
            ),
    },
    {
            "label": "C",
            "name": "Yuki",
            "text": (
                "I picked up the guitar at thirty-eight after watching a concert that genuinely "
                "moved me. Progress was agonisingly slow to begin with, and I found formal lessons "
                "less useful than the free online tutorials that let me learn at my own pace. "
                "Three years on, I now perform at small local venues, which still feels slightly "
                "unreal. My only regret is not starting sooner — I sometimes think about what "
                "level I might have reached if I'd begun in my twenties."
            ),
    },
    {
            "label": "D",
            "name": "Patrick",
            "text": (
                "I took up the drums at sixty, which went down rather badly with my family — the "
                "noise was their main objection. I solved that by hiring a soundproofed practice "
                "studio two evenings a week. I have no ambitions to perform publicly; for me, it "
                "is purely about the release it provides after a stressful day. The repetitive, "
                "rhythmic nature of drumming has a meditative quality that I find more effective "
                "than any other method I've tried for managing the pressures of daily life."
            ),
    },
    {
            "label": "E",
            "name": "Sophie",
            "text": (
                "I'd played the cello as a child but abandoned it in my teens, as so many do. "
                "Returning to it at forty-five was a different experience entirely from learning "
                "from scratch — muscle memory is a remarkable thing, and what had once taken me "
                "months came back within weeks. The emotional connection to the instrument was "
                "immediate in a way it had never quite been when I was young. I've since completed "
                "a teaching qualification and now run weekly sessions for other adults who are "
                "returning to instruments they once played."
            ),
    },
    ],
    "questions": [
    {"q": "Which person found that earlier experience made the learning process significantly easier?", "answer": "E"},
    {"q": "Which person was pleasantly surprised by the social dimension of their new activity?", "answer": "A"},
    {"q": "Which person believes that life experience has enhanced their musical understanding?", "answer": "B"},
    {"q": "Which person chose to learn independently rather than through formal instruction?", "answer": "C"},
    {"q": "Which person took up their instrument despite the objections of family members?", "answer": "D"},
    {"q": "Which person now passes on their skill to others?", "answer": "E"},
    {"q": "Which person describes the activity primarily as a way of relieving stress?", "answer": "D"},
    {"q": "Which person mentions physical pain as part of the early learning experience?", "answer": "A"},
    {"q": "Which person now performs in front of an audience?", "answer": "C"},
    {"q": "Which person follows a fixed daily routine in order to practise?", "answer": "B"},
    ],
}


# ── Render ────────────────────────────────────────────────────────────────────
def render():
    # Ensure all state keys exist regardless of when the session was started
    _defaults = {
            "rdg5_idx": 0, "rdg5_sel": {}, "rdg5_checked": False,
            "rdg6_sel": {}, "rdg6_checked": False,
            "rdg7_sel": {}, "rdg7_checked": False,
            "rdg8_sel": {}, "rdg8_checked": False,
    }
    for k, v in _defaults.items():
            if k not in st.session_state:
                st.session_state[k] = v

    st.title("📖 Reading")
    st.caption("Cambridge C1 Advanced — Reading Parts 5–8")

    tab_p5, tab_p6, tab_p7, tab_p8 = st.tabs([
            "Part 5 — Multiple Choice",
            "Part 6 — Cross-text Matching",
            "Part 7 — Gapped Text",
            "Part 8 — Multiple Matching",
    ])

    # ── Part 5 ───────────────────────────────────────────────────────────────
    with tab_p5:
            st.markdown(f"### {PART5['title']}")
            st.markdown("*Read the text. Then answer questions 31–36 by choosing the best option (A, B, C or D).*")
            with st.expander("📄 Read the text", expanded=True):
                for para in PART5["text"].strip().split("\n\n"):
                    st.markdown(para.strip())
            st.markdown("---")

            qs = PART5["questions"]
            idx = st.session_state.rdg5_idx
            q = qs[idx]
            st.markdown(f"**Question {31 + idx}** *(of {len(qs)})*")
            st.progress((idx + 1) / len(qs))
            st.markdown(f"**{q['q']}**")
            sel = st.radio(
                "Select an option:",
                q["options"],
                index=None,
                key=f"rdg5_radio_{idx}",
                label_visibility="collapsed",
            )
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check", use_container_width=True, key="rdg5_chk"):
                    updated = dict(st.session_state.rdg5_sel)
                    updated[idx] = sel
                    st.session_state.rdg5_sel = updated
                    st.session_state.rdg5_checked = True
                    add_score(sel is not None and sel[0] == q["answer"])
                    st.rerun()
            with c2:
                if st.button("➡️ Next question", use_container_width=True, key="rdg5_nxt"):
                    st.session_state.rdg5_idx = (idx + 1) % len(qs)
                    st.session_state.rdg5_checked = False
                    st.rerun()
            if st.session_state.rdg5_checked:
                chosen = st.session_state.rdg5_sel.get(idx)
                if chosen and chosen[0] == q["answer"]:
                    st.success(f"✅ Correct! — {q['explanation']}")
                else:
                    st.error(f"❌ Correct answer: **{q['answer']}** — {q['explanation']}")

    # ── Part 6 ───────────────────────────────────────────────────────────────
    with tab_p6:
            st.markdown(f"### {PART6['title']}")
            st.markdown(
                "*Read the four texts below. Answer questions 37–40 by choosing from writers A–D. "
                "You may choose any writer more than once.*"
            )
            for t in PART6["texts"]:
                with st.expander(f"Writer **{t['label']}** — {t['name']}"):
                    st.markdown(t["text"])
            st.markdown("---")

            writers = ["A", "B", "C", "D"]
            user_p6 = {}
            for i, q in enumerate(PART6["questions"], start=37):
                user_p6[i] = st.radio(
                    f"Q{i}. {q['q']}",
                    writers,
                    index=None,
                    horizontal=True,
                    key=f"rdg6_q{i}",
                )
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check all", use_container_width=True, key="rdg6_chk"):
                    st.session_state.rdg6_sel = dict(user_p6)
                    st.session_state.rdg6_checked = True
                    st.rerun()
            with c2:
                if st.button("🔄 Reset", use_container_width=True, key="rdg6_rst"):
                    st.session_state.rdg6_sel = {}
                    st.session_state.rdg6_checked = False
                    st.rerun()
            if st.session_state.rdg6_checked:
                right = 0
                for i, q in enumerate(PART6["questions"], start=37):
                    chosen = st.session_state.rdg6_sel.get(i)
                    if chosen == q["answer"]:
                        right += 1
                        st.success(f"Q{i}: **{q['answer']}** ✅ — {q['explanation']}")
                    else:
                        st.error(f"Q{i}: you chose *{chosen or '—'}* → correct: **{q['answer']}** — {q['explanation']}")
                st.info(f"**Score: {right}/{len(PART6['questions'])}**")

    # ── Part 7 ───────────────────────────────────────────────────────────────
    with tab_p7:
            st.markdown(f"### {PART7['title']}")
            st.markdown(
                "*Six paragraphs have been removed from the article. Choose from A–G the paragraph "
                "which fits each gap. There is one extra paragraph you do not need to use.*"
            )

            with st.expander("📄 Read the article (with gaps)", expanded=True):
                display = ""
                for part in PART7["text_parts"]:
                    if part.startswith("["):
                        display += f"\n\n**{part}** *(paragraph missing)*\n\n"
                    else:
                        display += f"\n\n{part}"
                st.markdown(display.strip())

            st.markdown("---")
            st.markdown("**Paragraph options:**")
            for letter, text in PART7["options"].items():
                with st.expander(f"**{letter}**"):
                    st.markdown(text)

            st.markdown("---")
            st.markdown("**Your answers — select a paragraph for each gap:**")

            options_list = list(PART7["options"].keys())
            user_p7 = {}
            cols = st.columns(3)
            for i, gap_num in enumerate(PART7["answers"].keys()):
                with cols[i % 3]:
                    user_p7[gap_num] = st.selectbox(
                        f"Gap [{gap_num}]:",
                        ["—"] + options_list,
                        key=f"rdg7_gap{gap_num}",
                    )
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check all", use_container_width=True, key="rdg7_chk"):
                    st.session_state.rdg7_sel = dict(user_p7)
                    st.session_state.rdg7_checked = True
                    st.rerun()
            with c2:
                if st.button("🔄 Reset", use_container_width=True, key="rdg7_rst"):
                    st.session_state.rdg7_sel = {}
                    st.session_state.rdg7_checked = False
                    st.rerun()
            if st.session_state.rdg7_checked:
                right = 0
                for gap_num, correct in PART7["answers"].items():
                    chosen = st.session_state.rdg7_sel.get(gap_num, "—")
                    if chosen == correct:
                        right += 1
                        st.success(f"Gap [{gap_num}]: **{correct}** ✅")
                    else:
                        st.error(f"Gap [{gap_num}]: you chose *{chosen}* → correct: **{correct}**")
                st.info(f"**Score: {right}/{len(PART7['answers'])}**")
                with st.expander("💡 Gap-by-gap explanations"):
                    for gap_num, tip in PART7["tips"].items():
                        st.markdown(f"- **Gap {gap_num}:** {tip}")

    # ── Part 8 ───────────────────────────────────────────────────────────────
    with tab_p8:
            st.markdown(f"### {PART8['title']}")
            st.markdown(f"*{PART8['instruction']}*")

            for t in PART8["texts"]:
                with st.expander(f"**{t['label']} — {t['name']}**"):
                    st.markdown(t["text"])

            st.markdown("---")

            people = ["A", "B", "C", "D", "E"]
            user_p8 = {}
            for i, q in enumerate(PART8["questions"], start=47):
                user_p8[i] = st.radio(
                    f"Q{i}. {q['q']}",
                    people,
                    index=None,
                    horizontal=True,
                    key=f"rdg8_q{i}",
                )
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check all", use_container_width=True, key="rdg8_chk"):
                    st.session_state.rdg8_sel = dict(user_p8)
                    st.session_state.rdg8_checked = True
                    right = sum(
                        1 for i, q in enumerate(PART8["questions"], start=47)
                        if user_p8.get(i) == q["answer"]
                    )
                    add_score(right == len(PART8["questions"]))
                    st.rerun()
            with c2:
                if st.button("🔄 Reset", use_container_width=True, key="rdg8_rst"):
                    st.session_state.rdg8_sel = {}
                    st.session_state.rdg8_checked = False
                    st.rerun()
            if st.session_state.rdg8_checked:
                right = 0
                for i, q in enumerate(PART8["questions"], start=47):
                    chosen = st.session_state.rdg8_sel.get(i)
                    if chosen == q["answer"]:
                        right += 1
                        st.success(f"Q{i}: **{q['answer']}** ✅")
                    else:
                        st.error(f"Q{i}: you chose *{chosen or '—'}* → correct: **{q['answer']}**")
                if right == len(PART8["questions"]):
                    st.balloons()
                st.info(f"**Score: {right}/{len(PART8['questions'])}**")
