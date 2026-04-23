import streamlit as st

_CSS = """
<style>
.flashcard {
    background: linear-gradient(135deg, #1e3a5f 0%, #2d6a9f 100%);
    border-radius: 16px; padding: 2rem 2.5rem; margin: 1rem 0;
    color: white; box-shadow: 0 8px 24px rgba(0,0,0,0.2);
}
.word-title { font-size: 2.2rem; font-weight: 800; letter-spacing: 1px; margin-bottom: 0.3rem; }
.translation { font-size: 1.1rem; color: #a8d8f0; font-style: italic; margin-bottom: 1rem; }
.tag { display: inline-block; background: rgba(255,255,255,0.15); border-radius: 20px;
       padding: 2px 10px; font-size: 0.82rem; margin: 2px; }
.section-header { font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; }
.example-box { background: #f0f7ff; border-left: 4px solid #2d6a9f;
               padding: 0.8rem 1rem; border-radius: 0 8px 8px 0; margin: 0.5rem 0; color: #1a1a2e; }
.score-box { background: #e8f5e9; border-radius: 10px; padding: 0.5rem 1rem;
             display: inline-block; font-weight: 600; color: #2e7d32; }
</style>
"""

def inject_styles():
    st.markdown(_CSS, unsafe_allow_html=True)
