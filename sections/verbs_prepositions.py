import random
import streamlit as st

from data import VERBS_PREPOSITIONS
from components.state import add_score


def render():
    try:
        st.title("🔗 Verbs & Prepositions")
        tab1, tab2 = st.tabs(["Flashcards", "Fill in the Blank"])

        with tab1:
            idx = st.session_state.vp_idx
            vp = VERBS_PREPOSITIONS[idx]
            st.markdown(f"*{idx+1} of {len(VERBS_PREPOSITIONS)}*")
            st.progress((idx + 1) / len(VERBS_PREPOSITIONS))
            st.markdown(f"""<div class="flashcard">
                <div class="word-title">{vp['verb'].upper()} + ___?</div>
                <div class="translation">🇪🇸 {vp['translation']}</div>
            </div>""", unsafe_allow_html=True)
            if st.session_state.vp_revealed:
                st.success(f"**{vp['verb']} {vp['prep']}** — {vp['meaning']}")
                st.markdown(f'<div class="example-box">💬 <em>{vp["example"]}</em></div>', unsafe_allow_html=True)
            else:
                if st.button("👁️ Reveal preposition & meaning", use_container_width=True, key="vp_reveal"):
                    st.session_state.vp_revealed = True
                    st.rerun()
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("⬅️ Previous", use_container_width=True, key="vp_prev"):
                    st.session_state.vp_idx = (idx - 1) % len(VERBS_PREPOSITIONS)
                    st.session_state.vp_revealed = False
                    st.rerun()
            with c2:
                if st.button("🔀 Random", use_container_width=True, key="vp_rand"):
                    st.session_state.vp_idx = random.randint(0, len(VERBS_PREPOSITIONS) - 1)
                    st.session_state.vp_revealed = False
                    st.rerun()
            with c3:
                if st.button("Next ➡️", use_container_width=True, key="vp_next_fc"):
                    st.session_state.vp_idx = (idx + 1) % len(VERBS_PREPOSITIONS)
                    st.session_state.vp_revealed = False
                    st.rerun()

        with tab2:
            fi = st.session_state.vp_fill_idx
            vp = VERBS_PREPOSITIONS[fi]
            st.markdown("**Fill in the missing preposition:**")
            st.markdown(f'<div class="example-box">{vp["fill"]}</div>', unsafe_allow_html=True)
            st.markdown(f"*Verb: **{vp['verb']}** + ?* | 🇪🇸 *{vp['translation']}*")
            ans = st.text_input("Preposition:", key="vp_fill_input")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check", use_container_width=True, key="vp_fill_chk"):
                    st.session_state.vp_fill_ans = ans
                    st.session_state.vp_fill_checked = True
                    add_score(ans.strip().lower() == vp["prep"].lower())
                    st.rerun()
            with c2:
                if st.button("➡️ Next", use_container_width=True, key="vp_fill_nxt"):
                    st.session_state.vp_fill_idx = random.randint(0, len(VERBS_PREPOSITIONS) - 1)
                    st.session_state.vp_fill_ans = ""
                    st.session_state.vp_fill_checked = False
                    st.session_state["vp_fill_input"] = ""
                    st.rerun()
            if st.session_state.vp_fill_checked:
                if st.session_state.vp_fill_ans.strip().lower() == vp["prep"].lower():
                    st.success(f"✅ Correct! **{vp['verb']} {vp['prep']}** — {vp['meaning']}")
                else:
                    st.error(f"❌ Preposition: **{vp['prep']}** → *{vp['verb']} {vp['prep']}* — {vp['meaning']}")
    except Exception as e:
        import traceback
        st.error(str(e))
        st.code(traceback.format_exc())
