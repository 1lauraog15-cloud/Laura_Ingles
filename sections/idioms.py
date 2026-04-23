import random
import streamlit as st

from data import IDIOMS
from components.state import add_score


def render():
    st.title("💬 Idioms & Expressions")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.idiom_idx
        item = IDIOMS[idx]
        st.markdown(f"*{idx+1} of {len(IDIOMS)}*")
        st.progress((idx + 1) / len(IDIOMS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">💬 {item['idiom'].upper()}</div>
            <div class="translation">🇪🇸 {item['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.idiom_revealed:
            st.success(f"**Meaning:** {item['meaning']}")
            st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal meaning & example", use_container_width=True, key="idiom_reveal"):
                st.session_state.idiom_revealed = True
                st.rerun()
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="idiom_prev"):
                st.session_state.idiom_idx = (idx - 1) % len(IDIOMS)
                st.session_state.idiom_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="idiom_rand"):
                st.session_state.idiom_idx = random.randint(0, len(IDIOMS) - 1)
                st.session_state.idiom_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="idiom_next"):
                st.session_state.idiom_idx = (idx + 1) % len(IDIOMS)
                st.session_state.idiom_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.idiom_fill_idx % len(IDIOMS)
        item = IDIOMS[fi]
        st.markdown("**Complete the sentence with the correct idiom:**")
        st.markdown(f'<div class="example-box">{item["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{item['translation']}*")
        ans = st.text_input("Your idiom:", key=f"idiom_fill_{fi}", value=st.session_state.idiom_fill_ans)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="idiom_chk"):
                st.session_state.idiom_fill_ans = ans
                st.session_state.idiom_fill_checked = True
                correct = (
                    ans.strip().lower() in item["idiom"].lower()
                    or item["idiom"].lower() in ans.strip().lower()
                )
                add_score(correct)
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="idiom_fill_nxt"):
                st.session_state.idiom_fill_idx = random.randint(0, len(IDIOMS) - 1)
                st.session_state.idiom_fill_ans = ""
                st.session_state.idiom_fill_checked = False
                st.rerun()
        if st.session_state.idiom_fill_checked:
            saved = st.session_state.idiom_fill_ans
            if saved.strip().lower() in item["idiom"].lower() or item["idiom"].lower() in saved.strip().lower():
                st.success(f"✅ Correct! **{item['idiom']}**")
            else:
                st.error(f"❌ The idiom is: **{item['idiom']}**")
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)
