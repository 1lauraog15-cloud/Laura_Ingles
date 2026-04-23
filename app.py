import streamlit as st
from components.styles import inject_styles
from components.state import init_state
from components.sidebar import render_sidebar
import sections.home, sections.vocabulary, sections.phrasal_verbs
import sections.verbs_prepositions, sections.collocations, sections.connectors
import sections.idioms, sections.confusing_expressions
import sections.grammar, sections.use_of_english

st.set_page_config(page_title="Laura_Inglés", page_icon="🎓", layout="wide")
inject_styles()
init_state()
section = render_sidebar()

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
}
ROUTES[section]()
