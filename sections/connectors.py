import random
import streamlit as st

from data import CONNECTORS
from components.state import add_score


def render():
    st.title("🔀 Connectors & Linkers")
    tab1, tab2 = st.tabs(["Study by Category", "Fill in the Blank"])

    with tab1:
        cat = st.selectbox("Select category:", list(CONNECTORS.keys()))
        for item in CONNECTORS[cat]:
            with st.expander(f"**{item['word']}** — 🇪🇸 *{item['translation']}*"):
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)

    with tab2:
        flat = [{"cat": cat, **item} for cat, items in CONNECTORS.items() for item in items]
        fi = st.session_state.conn_fill_flat_idx % len(flat)
        item = flat[fi]
        st.markdown(f"**Category hint: *{item['cat']}* | 🇪🇸 *{item['translation']}***")
        st.markdown(f'<div class="example-box">{item["fill"]}</div>', unsafe_allow_html=True)
        ans = st.text_input("Your connector:", key="conn_fill_input")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="conn_chk"):
                st.session_state.conn_fill_ans = ans
                st.session_state.conn_fill_checked = True
                add_score(ans.strip().lower() in item["word"].lower())
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="conn_nxt"):
                st.session_state.conn_fill_flat_idx = random.randint(0, len(flat) - 1)
                st.session_state.conn_fill_ans = ""
                st.session_state.conn_fill_checked = False
                st.session_state["conn_fill_input"] = ""
                st.rerun()
        if st.session_state.conn_fill_checked:
            if st.session_state.conn_fill_ans.strip().lower() in item["word"].lower():
                st.success(f"✅ Correct! **{item['word']}**")
            else:
                st.error(f"❌ The answer is: **{item['word']}**")
                st.markdown(f'<div class="example-box">💬 <em>{item["example"]}</em></div>', unsafe_allow_html=True)
