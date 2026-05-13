import random
import streamlit as st

from data import PHRASAL_VERBS
from components.state import add_score


def render():
    try:
        st.write("debug: render called")
        st.title("⚡ Phrasal Verbs")
        tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

        with tab1:
            idx = st.session_state.pv_idx
            pv = PHRASAL_VERBS[idx]
            st.markdown(f"*{idx+1} of {len(PHRASAL_VERBS)}*")
            st.progress((idx + 1) / len(PHRASAL_VERBS))
            st.markdown(f"""<div class="flashcard">
                <div class="word-title">⚡ {pv['pv'].upper()}</div>
                <div class="translation">🇪🇸 {pv['translation']}</div>
            </div>""", unsafe_allow_html=True)
            if st.session_state.pv_revealed:
                st.success(f"**Meaning:** {pv['meaning']}")
                st.markdown(f'<div class="example-box">💬 <em>{pv["example"]}</em></div>', unsafe_allow_html=True)
            else:
                if st.button("👁️ Reveal meaning & example", use_container_width=True, key="pv_reveal"):
                    st.session_state.pv_revealed = True
                    st.rerun()
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("⬅️ Previous", use_container_width=True, key="pv_prev"):
                    st.session_state.pv_idx = (idx - 1) % len(PHRASAL_VERBS)
                    st.session_state.pv_revealed = False
                    st.rerun()
            with c2:
                if st.button("🔀 Random", use_container_width=True, key="pv_rand"):
                    st.session_state.pv_idx = random.randint(0, len(PHRASAL_VERBS) - 1)
                    st.session_state.pv_revealed = False
                    st.rerun()
            with c3:
                if st.button("Next ➡️", use_container_width=True, key="pv_next_fc"):
                    st.session_state.pv_idx = (idx + 1) % len(PHRASAL_VERBS)
                    st.session_state.pv_revealed = False
                    st.rerun()

        with tab2:
            fi = st.session_state.pv_fill_idx
            pv = PHRASAL_VERBS[fi]
            st.markdown("**Complete the sentence with the correct phrasal verb:**")
            st.markdown(f'<div class="example-box">{pv["fill"]}</div>', unsafe_allow_html=True)
            st.markdown(f"🇪🇸 *{pv['translation']}* | 📖 *{pv['meaning']}*")
            ans = st.text_input("Your answer:", key="pv_fill_input")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check", use_container_width=True, key="pv_fill_check"):
                    st.session_state.pv_fill_ans = ans
                    st.session_state.pv_fill_checked = True
                    add_score(ans.strip().lower() == pv["pv"].lower())
                    st.rerun()
            with c2:
                if st.button("➡️ Next", use_container_width=True, key="pv_fill_next"):
                    st.session_state.pv_fill_idx = random.randint(0, len(PHRASAL_VERBS) - 1)
                    st.session_state.pv_fill_ans = ""
                    st.session_state.pv_fill_checked = False
                    st.session_state["pv_fill_input"] = ""
                    st.rerun()
            if st.session_state.pv_fill_checked:
                if st.session_state.pv_fill_ans.strip().lower() == pv["pv"].lower():
                    st.success(f"✅ Correct! **{pv['pv']}** — {pv['meaning']}")
                else:
                    st.error(f"❌ The phrasal verb is: **{pv['pv']}**\n\n*{pv['example']}*")
    except Exception as e:
        import traceback
        st.error(str(e))
        st.code(traceback.format_exc())
