import streamlit as st

SECTIONS = [
    "🏠 Home",
    "📚 Vocabulary",
    "⚡ Phrasal Verbs",
    "🔗 Verbs & Prepositions",
    "🤝 Collocations",
    "🔀 Connectors",
    "💬 Idioms & Expressions",
    "🔤 Confusing Expressions",
    "✍️ Grammar",
    "🎯 Use of English",
    "📖 Reading",
]


def render_sidebar() -> str:
    st.sidebar.title("🎓 Laura_Inglés")
    st.sidebar.markdown("**Cambridge C1/C2 Trainer**")

    if st.session_state.score_total > 0:
        pct = int(100 * st.session_state.score_correct / st.session_state.score_total)
        st.sidebar.markdown(
            f"**Score:** {st.session_state.score_correct}/{st.session_state.score_total} ({pct}%)"
        )
        st.sidebar.progress(st.session_state.score_correct / st.session_state.score_total)

    st.sidebar.markdown("---")
    section = st.sidebar.radio("Navigate", SECTIONS)

    if st.sidebar.button("🔄 Reset score"):
        st.session_state.score_correct = 0
        st.session_state.score_total = 0
        st.rerun()

    return section
