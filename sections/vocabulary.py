import re
import random
import streamlit as st

from data import VOCABULARY
from components.state import add_score


def render():
    try:
        st.write("debug: render called")
        st.title("📚 Vocabulary")
        tab1, tab2, tab3 = st.tabs(["Flashcards", "Fill in the Blank", "Multiple Choice Quiz"])

        # ── Flashcards ──────────────────────────────────────────────────────────
        with tab1:
            idx = st.session_state.vocab_idx
            w = VOCABULARY[idx]
            st.markdown(f"*Word {idx+1} of {len(VOCABULARY)}*")
            st.progress((idx + 1) / len(VOCABULARY))
            st.markdown(f"""<div class="flashcard">
                <div class="word-title">🃏 {w['word'].upper()}</div>
                <div class="translation">🇪🇸 {w['translation']}</div>
            </div>""", unsafe_allow_html=True)
            if st.session_state.vocab_revealed:
                st.success(f"**Definition:** {w['definition']}")
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**Synonyms:** " + " · ".join([f"`{s}`" for s in w['synonyms']]))
                with c2:
                    st.markdown("**Antonyms:** " + " · ".join([f"`{s}`" for s in w['antonyms']]))
                st.markdown(f'<div class="example-box">💬 <em>{w["example"]}</em></div>', unsafe_allow_html=True)
                st.markdown(f"📎 **Collocation:** *{w['collocation']}*")
            else:
                if st.button("👁️ Reveal definition, synonyms & example", use_container_width=True, key="vocab_reveal"):
                    st.session_state.vocab_revealed = True
                    st.rerun()
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("⬅️ Previous", use_container_width=True, key="vocab_prev"):
                    st.session_state.vocab_idx = (idx - 1) % len(VOCABULARY)
                    st.session_state.vocab_revealed = False
                    st.rerun()
            with col2:
                if st.button("🔀 Random", use_container_width=True, key="vocab_rand"):
                    st.session_state.vocab_idx = random.randint(0, len(VOCABULARY) - 1)
                    st.session_state.vocab_revealed = False
                    st.rerun()
            with col3:
                if st.button("Next ➡️", use_container_width=True, key="vocab_nxt_fc"):
                    st.session_state.vocab_idx = (idx + 1) % len(VOCABULARY)
                    st.session_state.vocab_revealed = False
                    st.rerun()

        # ── Fill in the Blank ────────────────────────────────────────────────────
        with tab2:
            fi = st.session_state.vocab_fill_idx
            fw = VOCABULARY[fi]
            hidden = re.sub(re.escape(fw["word"]), "___________", fw["example"], count=1, flags=re.IGNORECASE)
            st.markdown("**Complete the sentence with the correct word:**")
            st.markdown(f'<div class="example-box">{hidden}</div>', unsafe_allow_html=True)
            st.markdown(f"🇪🇸 *{fw['translation']}* | 📖 *{fw['definition']}*")
            ans = st.text_input("Your answer:", key="vocab_fill_input")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check", use_container_width=True, key="vf_check"):
                    st.session_state.vocab_fill_ans = ans
                    st.session_state.vocab_fill_checked = True
                    add_score(ans.strip().lower() == fw["word"].lower())
                    st.rerun()
            with c2:
                if st.button("➡️ Next sentence", use_container_width=True, key="vf_next"):
                    st.session_state.vocab_fill_idx = random.randint(0, len(VOCABULARY) - 1)
                    st.session_state.vocab_fill_ans = ""
                    st.session_state.vocab_fill_checked = False
                    st.session_state["vocab_fill_input"] = ""
                    st.rerun()
            if st.session_state.vocab_fill_checked:
                if st.session_state.vocab_fill_ans.strip().lower() == fw["word"].lower():
                    st.success(f"✅ Correct! **{fw['word']}** — {fw['definition']}")
                else:
                    st.error(f"❌ The answer is: **{fw['word']}**")
                    st.markdown("**Synonyms:** " + " · ".join([f"`{s}`" for s in fw['synonyms']]))

        # ── Multiple Choice Quiz ─────────────────────────────────────────────────
        with tab3:
            qi = st.session_state.vocab_quiz_idx
            qw = VOCABULARY[qi]
            if not st.session_state.vocab_quiz_options:
                wrong = random.sample([v for v in VOCABULARY if v["word"] != qw["word"]], 3)
                opts = [qw["definition"]] + [v["definition"] for v in wrong]
                random.shuffle(opts)
                st.session_state.vocab_quiz_options = opts
            st.markdown("**What is the meaning of this word?**")
            st.markdown(f"""<div class="flashcard" style="padding:1.2rem 2rem;">
                <div class="word-title">{qw['word'].upper()}</div>
                <div class="translation">🇪🇸 {qw['translation']}</div>
            </div>""", unsafe_allow_html=True)
            sel = st.radio("Choose the correct definition:", st.session_state.vocab_quiz_options,
                           index=None, key=f"vocab_quiz_{qi}")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("✅ Check", use_container_width=True, key="vq_check"):
                    st.session_state.vocab_quiz_selected = sel
                    st.session_state.vocab_quiz_checked = True
                    add_score(sel == qw["definition"])
                    st.rerun()
            with c2:
                if st.button("➡️ Next word", use_container_width=True, key="vq_next"):
                    st.session_state.vocab_quiz_idx = random.randint(0, len(VOCABULARY) - 1)
                    st.session_state.vocab_quiz_options = []
                    st.session_state.vocab_quiz_selected = None
                    st.session_state.vocab_quiz_checked = False
                    st.rerun()
            if st.session_state.vocab_quiz_checked:
                if st.session_state.vocab_quiz_selected == qw["definition"]:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Correct definition: **{qw['definition']}**")
                st.markdown(f'<div class="example-box">💬 <em>{qw["example"]}</em></div>', unsafe_allow_html=True)
    except Exception as e:
        import traceback
        st.error(str(e))
        st.code(traceback.format_exc())
