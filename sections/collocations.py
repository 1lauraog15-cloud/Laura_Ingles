import random
import streamlit as st

from data import COLLOCATIONS
from components.state import add_score


def render():
    st.title("🤝 Collocations")
    tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

    with tab1:
        idx = st.session_state.coll_idx
        c = COLLOCATIONS[idx]
        st.markdown(f"*{idx+1} of {len(COLLOCATIONS)}*")
        st.progress((idx + 1) / len(COLLOCATIONS))
        st.markdown(f"""<div class="flashcard">
            <div class="word-title">🤝 {c['adj_noun'].upper()}</div>
            <div class="translation">🇪🇸 {c['translation']}</div>
        </div>""", unsafe_allow_html=True)
        if st.session_state.coll_revealed:
            st.markdown(f'<div class="example-box">💬 <em>{c["example"]}</em></div>', unsafe_allow_html=True)
        else:
            if st.button("👁️ Reveal example", use_container_width=True, key="coll_reveal"):
                st.session_state.coll_revealed = True
                st.rerun()
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Previous", use_container_width=True, key="coll_prev"):
                st.session_state.coll_idx = (idx - 1) % len(COLLOCATIONS)
                st.session_state.coll_revealed = False
                st.rerun()
        with c2:
            if st.button("🔀 Random", use_container_width=True, key="coll_rand"):
                st.session_state.coll_idx = random.randint(0, len(COLLOCATIONS) - 1)
                st.session_state.coll_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="coll_nxt_fc"):
                st.session_state.coll_idx = (idx + 1) % len(COLLOCATIONS)
                st.session_state.coll_revealed = False
                st.rerun()

    with tab2:
        fi = st.session_state.coll_fill_idx
        col = COLLOCATIONS[fi]
        st.markdown("**Complete with the correct collocation:**")
        st.markdown(f'<div class="example-box">{col["fill"]}</div>', unsafe_allow_html=True)
        st.markdown(f"🇪🇸 *{col['translation']}*")
        ans = st.text_input("Your answer:", key="coll_fill_input", value=st.session_state.coll_fill_ans)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="coll_fill_chk"):
                st.session_state.coll_fill_ans = ans
                st.session_state.coll_fill_checked = True
                add_score(ans.strip().lower() == col["adj_noun"].lower())
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="coll_fill_nxt"):
                st.session_state.coll_fill_idx = random.randint(0, len(COLLOCATIONS) - 1)
                st.session_state.coll_fill_ans = ""
                st.session_state.coll_fill_checked = False
                st.rerun()
        if st.session_state.coll_fill_checked:
            if st.session_state.coll_fill_ans.strip().lower() == col["adj_noun"].lower():
                st.success(f"✅ Correct! **{col['adj_noun']}**")
            else:
                st.error(f"❌ The collocation is: **{col['adj_noun']}**")
                st.markdown(f'<div class="example-box">💬 <em>{col["example"]}</em></div>', unsafe_allow_html=True)
