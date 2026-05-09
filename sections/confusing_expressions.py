import streamlit as st

from data import CONFUSING_EXPRESSIONS


def render():
    st.title("🔤 Confusing Expressions")
    st.markdown("*Master the expressions that cause the most confusion for Spanish speakers.*")

    topic_key = st.selectbox(
        "Choose a topic:",
        list(CONFUSING_EXPRESSIONS.keys()),
        index=list(CONFUSING_EXPRESSIONS.keys()).index(st.session_state.conf_topic),
    )
    if topic_key != st.session_state.conf_topic:
        st.session_state.conf_topic = topic_key
        st.session_state.conf_ex_idx = 0
        st.session_state.conf_ans = ""
        st.session_state.conf_revealed = False
        st.rerun()

    topic = CONFUSING_EXPRESSIONS[topic_key]
    tab1, tab2 = st.tabs(["📖 Study & Examples", "✏️ Exercises"])

    with tab1:
        with st.expander("📖 Explanation — click to expand", expanded=True):
            st.markdown(topic["explanation"])
        st.markdown("---")
        st.markdown("### Forms & Examples")
        for form in topic["forms"]:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"""<div class="flashcard" style="padding:0.8rem 1.2rem; margin:0.3rem 0;">
                    <div style="font-size:1rem; font-weight:700;">{form['expression']}</div>
                    <div style="font-size:0.9rem; color:#a8d8f0;">🇪🇸 {form['spanish']}</div>
                </div>""", unsafe_allow_html=True)
            with col2:
                st.markdown(
                    f'<div class="example-box" style="margin-top:0.6rem;">💬 <em>{form["example"]}</em>'
                    f'<br><small>📝 {form["note"]}</small></div>',
                    unsafe_allow_html=True,
                )

    with tab2:
        exercises = topic["exercises"]
        ei = st.session_state.conf_ex_idx % len(exercises)
        ex = exercises[ei]
        st.markdown(f"**Exercise {ei+1} of {len(exercises)}**")

        if "situation" in ex:
            st.info(f"🎭 **Situation:** {ex['situation']}")
            st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)

        user_ans = st.text_input(
            "Your answer:",
            key=f"conf_input_{topic_key}_{ei}",
        )
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("👁️ Show answer", use_container_width=True, key="conf_show"):
                st.session_state.conf_ans = user_ans
                st.session_state.conf_revealed = True
                st.rerun()
        with c2:
            if st.button("⬅️ Previous", use_container_width=True, key="conf_prev"):
                st.session_state.conf_ex_idx = (ei - 1) % len(exercises)
                st.session_state.conf_ans = ""
                st.session_state.conf_revealed = False
                st.rerun()
        with c3:
            if st.button("Next ➡️", use_container_width=True, key="conf_next"):
                st.session_state.conf_ex_idx = (ei + 1) % len(exercises)
                st.session_state.conf_ans = ""
                st.session_state.conf_revealed = False
                st.rerun()

        if st.session_state.conf_revealed:
            st.success(f"✅ **Model answer:** {ex['answer']}")
            if user_ans.strip():
                user_norm = user_ans.strip().lower()
                ans_norm = ex["answer"].strip().lower()
                if user_norm in ans_norm or any(part.strip() in user_norm for part in ans_norm.split("/")):
                    st.success("✅ Your answer looks correct!")
                else:
                    st.warning("⚠️ Compare your answer with the model above.")
