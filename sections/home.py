import streamlit as st

from data import (
    VOCABULARY, PHRASAL_VERBS, VERBS_PREPOSITIONS, COLLOCATIONS,
    CONNECTORS, IDIOMS, GRAMMAR_EXERCISES,
)


def render():
    st.title("🎓 Laura_Inglés")
    st.markdown("#### Cambridge C1/C2 — Your personalised preparation tool")
    st.markdown("---")
    cols = st.columns(4)
    sections_info = [
            ("📚", "Vocabulary", f"{len(VOCABULARY)} words",
             "Translations · synonyms · antonyms · collocations · flashcards · fill-in-the-blanks · quiz"),
            ("⚡", "Phrasal Verbs", f"{len(PHRASAL_VERBS)} phrasal verbs",
             "Translations · flashcards · fill-in-the-blanks"),
            ("🔗", "Verbs & Prepositions", f"{len(VERBS_PREPOSITIONS)} combinations",
             "Translations · flashcards · fill-in-the-blanks"),
            ("🤝", "Collocations", f"{len(COLLOCATIONS)} collocations",
             "Translations · flashcards · fill-in-the-blanks"),
            ("🔀", "Connectors", f"{sum(len(v) for v in CONNECTORS.values())} connectors",
             "7 categories · study · fill-in-the-blanks"),
            ("💬", "Idioms & Expressions", f"{len(IDIOMS)} idioms",
             "Translations · flashcards · fill-in-the-blanks"),
            ("🔤", "Confusing Expressions", "7 topics",
             "I can tell · I'm afraid · May/Might/Should · used to · make vs do · False Friends · look/seem"),
            ("✍️", "Grammar", f"{len(GRAMMAR_EXERCISES)} topics",
             "Advanced structures · exercises"),
            ("🎯", "Use of English", "4 exercise types",
             "KWT · Word Formation · MCC · Open Cloze"),
    ]
    for i, (icon, name, count, desc) in enumerate(sections_info):
            with cols[i % 4]:
                st.info(f"{icon} **{name}**\n\n*{count}*\n\n{desc}")
    st.markdown("---")
    st.markdown(
            "💡 **Tips:** Work through sections in order. "
            "Track your score in the sidebar."
    )
