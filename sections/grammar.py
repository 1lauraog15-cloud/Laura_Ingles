import streamlit as st

from data import GRAMMAR_EXERCISES


def render():
    st.title("✍️ Grammar Practice")
    topic_names = [t["topic"] for t in GRAMMAR_EXERCISES]
    sel_topic = st.selectbox("Choose a grammar topic:", topic_names, index=st.session_state.gram_topic_idx)
    ti = topic_names.index(sel_topic)
    if ti != st.session_state.gram_topic_idx:
        st.session_state.gram_topic_idx = ti
        st.session_state.gram_ex_idx = 0
        st.session_state.gram_ans = ""
        st.session_state.gram_revealed = False
        st.rerun()

    topic = GRAMMAR_EXERCISES[ti]
    with st.expander("📖 Grammar explanation — click to expand", expanded=False):
        st.markdown(topic["explanation"])
    st.markdown("---")

    ei = st.session_state.gram_ex_idx
    ex = topic["exercises"][ei]
    st.markdown(f"**Exercise {ei+1} of {len(topic['exercises'])}**")
    st.markdown(f"*{ex['instruction']}*")
    st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)

    user_ans = st.text_area(
        "Your answer:",
        key=f"gram_input_{ti}_{ei}", height=90,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("👁️ Show answer", use_container_width=True, key="gram_show"):
            st.session_state.gram_revealed = True
            st.session_state.gram_ans = user_ans
            st.rerun()
    with c2:
        if st.button("⬅️ Previous ex.", use_container_width=True, key="gram_prev"):
            st.session_state.gram_ex_idx = (ei - 1) % len(topic["exercises"])
            st.session_state.gram_ans = ""
            st.session_state.gram_revealed = False
            st.rerun()
    with c3:
        if st.button("Next ex. ➡️", use_container_width=True, key="gram_nxt"):
            st.session_state.gram_ex_idx = (ei + 1) % len(topic["exercises"])
            st.session_state.gram_ans = ""
            st.session_state.gram_revealed = False
            st.rerun()

    if st.session_state.gram_revealed:
        st.success(f"✅ **Model answer:** {ex['answer']}")
