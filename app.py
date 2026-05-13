import streamlit as st
from components.styles import inject_styles
from components.state import init_state
from components.sidebar import render_sidebar
import sections.home, sections.vocabulary, sections.phrasal_verbs
import sections.verbs_prepositions, sections.collocations, sections.connectors
import sections.idioms, sections.confusing_expressions
import sections.grammar, sections.use_of_english, sections.reading

st.set_page_config(page_title="Laura_Inglés", page_icon="🎓", layout="wide")

try:
    inject_styles()
except Exception as e:
    import traceback
    st.error(f"inject_styles() failed: {e}")
    st.code(traceback.format_exc())
    st.stop()

try:
    init_state()
except Exception as e:
    import traceback
    st.error(f"init_state() failed: {e}")
    st.code(traceback.format_exc())
    st.stop()

try:
    section = render_sidebar()
except Exception as e:
    import traceback
    st.error(f"render_sidebar() failed: {e}")
    st.code(traceback.format_exc())
    st.stop()

st.write("debug: section =", section)

ROUTES = {
    "🏠 Home": sections.home.render,
    "📚 Vocabulary": sections.vocabulary.render,
    "⚡ Phrasal Verbs": sections.phrasal_verbs.render,
    "🔗 Verbs & Prepositions": sections.verbs_prepositions.render,
    "🤝 Collocations": sections.collocations.render,
    "🔀 Connectors": sections.connectors.render,
    "💬 Idioms & Expressions": sections.idioms.render,
    "🔤 Confusing Expressions": sections.confusing_expressions.render,
    "✍️ Grammar": sections.grammar.render,
    "🎯 Use of English": sections.use_of_english.render,
    "📖 Reading": sections.reading.render,
}
ROUTES[section]()
