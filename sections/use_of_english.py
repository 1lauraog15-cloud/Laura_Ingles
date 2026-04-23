import streamlit as st

from data import USE_OF_ENGLISH
from components.state import add_score


def render():
    st.title("🎯 Use of English")
    tab1, tab2, tab3, tab4 = st.tabs([
        "Part 4 — Key Word Transformation",
        "Part 3 — Word Formation",
        "Part 1 — Multiple Choice Cloze",
        "Part 2 — Open Cloze",
    ])

    # ── Part 4: Key Word Transformation ─────────────────────────────────────
    with tab1:
        st.markdown("**Rewrite the sentence using the key word. Do not change the key word. Use 3–6 words.**")
        kwt = USE_OF_ENGLISH["Key Word Transformation"]
        idx = st.session_state.kwt_idx
        ex = kwt[idx]
        st.markdown(f"*{idx+1} of {len(kwt)}*")
        st.progress((idx + 1) / len(kwt))
        st.markdown(f'<div class="example-box">📝 {ex["sentence"]}</div>', unsafe_allow_html=True)
        st.markdown(f"**Key word: `{ex['key']}`**")
        ans = st.text_input("Your answer:", key=f"kwt_input_{idx}", value=st.session_state.kwt_ans)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="kwt_chk"):
                st.session_state.kwt_ans = ans
                st.session_state.kwt_checked = True
                add_score(ans.strip().lower().rstrip(".") == ex["answer"].strip().lower().rstrip("."))
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="kwt_nxt"):
                st.session_state.kwt_idx = (idx + 1) % len(kwt)
                st.session_state.kwt_ans = ""
                st.session_state.kwt_checked = False
                st.rerun()
        if st.session_state.kwt_checked:
            st.success(f"**Model answer:** {ex['answer']}")
            if "pattern" in ex:
                st.caption(f"🏷️ Pattern tested: *{ex['pattern']}*")
            user_norm = st.session_state.kwt_ans.strip().lower().rstrip(".")
            ans_norm = ex["answer"].strip().lower().rstrip(".")
            if user_norm == ans_norm:
                st.success("✅ Perfect match!")
            else:
                st.warning("⚠️ Compare carefully with the model answer above — minor variations may also be acceptable.")

    # ── Part 3: Word Formation ───────────────────────────────────────────────
    with tab2:
        st.markdown("**Use the word in capitals to form a new word that fits the gap.**")
        wf = USE_OF_ENGLISH["Word Formation"]
        idx = st.session_state.wf_idx
        ex = wf[idx]
        st.markdown(f"*{idx+1} of {len(wf)}*")
        st.progress((idx + 1) / len(wf))
        st.markdown(f'<div class="example-box">📝 {ex["prompt"]}</div>', unsafe_allow_html=True)
        ans = st.text_input("Your answer:", key=f"wf_input_{idx}", value=st.session_state.wf_ans)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="wf_chk"):
                st.session_state.wf_ans = ans
                st.session_state.wf_checked = True
                add_score(ans.strip().lower() == ex["answer"].lower())
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="wf_nxt"):
                st.session_state.wf_idx = (idx + 1) % len(wf)
                st.session_state.wf_ans = ""
                st.session_state.wf_checked = False
                st.rerun()
        if st.session_state.wf_checked:
            if st.session_state.wf_ans.strip().lower() == ex["answer"].lower():
                st.success(f"✅ Correct! **{ex['answer']}**")
            else:
                st.error(f"❌ Correct form: **{ex['answer']}**")

    # ── Part 1: Multiple Choice Cloze ────────────────────────────────────────
    with tab3:
        st.markdown("**Choose the best option (A, B, C or D) to complete the sentence.**")
        mcc = USE_OF_ENGLISH["Multiple Choice Cloze"]
        idx = st.session_state.mcc_idx
        ex = mcc[idx]
        st.markdown(f"*{idx+1} of {len(mcc)}*")
        st.progress((idx + 1) / len(mcc))
        st.markdown(f'<div class="example-box">📝 {ex["sentence"]}</div>', unsafe_allow_html=True)
        sel = st.radio("Choose:", ex["options"], index=None, key=f"mcc_radio_{idx}")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check", use_container_width=True, key="mcc_chk"):
                st.session_state.mcc_selected = sel
                st.session_state.mcc_checked = True
                add_score(sel is not None and sel[0] == ex["answer"])
                st.rerun()
        with c2:
            if st.button("➡️ Next", use_container_width=True, key="mcc_nxt"):
                st.session_state.mcc_idx = (idx + 1) % len(mcc)
                st.session_state.mcc_selected = None
                st.session_state.mcc_checked = False
                st.rerun()
        if st.session_state.mcc_checked and st.session_state.mcc_selected:
            if st.session_state.mcc_selected[0] == ex["answer"]:
                st.success(f"✅ Correct! — {ex['explanation']}")
            else:
                st.error(f"❌ Correct answer: **{ex['answer']}** — {ex['explanation']}")

    # ── Part 2: Open Cloze ───────────────────────────────────────────────────
    with tab4:
        st.markdown("**Fill each gap with ONE word. No contractions.**")
        oc_list = USE_OF_ENGLISH["Open Cloze"]
        idx = st.session_state.oc_idx
        oc = oc_list[idx]
        st.markdown(f"*Text {idx+1} of {len(oc_list)}: **{oc['title']}***")
        st.markdown(f'<div class="example-box">📝 {oc["text"]}</div>', unsafe_allow_html=True)
        st.markdown("**Your answers:**")
        user_oc = {}
        cols = st.columns(3)
        for i, (num, _correct) in enumerate(oc["answers"].items()):
            with cols[i % 3]:
                user_oc[num] = st.text_input(
                    f"Gap ({num}):", key=f"oc_{idx}_{num}",
                    value=st.session_state.oc_answers.get(num, ""),
                )
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Check all", use_container_width=True, key="oc_chk"):
                st.session_state.oc_answers = user_oc
                st.session_state.oc_checked = True
                st.rerun()
        with c2:
            if st.button("➡️ Next text", use_container_width=True, key="oc_nxt"):
                st.session_state.oc_idx = (idx + 1) % len(oc_list)
                st.session_state.oc_answers = {}
                st.session_state.oc_checked = False
                st.rerun()
        if st.session_state.oc_checked:
            right = sum(
                1 for num, correct in oc["answers"].items()
                if st.session_state.oc_answers.get(num, "").strip().lower() == correct.lower()
            )
            total = len(oc["answers"])
            if right == total:
                st.success(f"✅ Perfect! {right}/{total} correct!")
            else:
                st.warning(f"**{right}/{total} correct**")
            for num, correct in oc["answers"].items():
                user_val = st.session_state.oc_answers.get(num, "").strip()
                if user_val.lower() == correct.lower():
                    st.success(f"Gap ({num}): **{correct}** ✅")
                else:
                    st.error(f"Gap ({num}): your answer *{user_val or '—'}* → correct: **{correct}**")
            if "tips" in oc:
                with st.expander("💡 Gap-by-gap tips"):
                    st.markdown(oc["tips"])
