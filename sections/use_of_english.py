import streamlit as st

from data import USE_OF_ENGLISH, CAMBRIDGE_TEST_1
from components.state import add_score


def render():
    st.title("🎯 Use of English")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Part 4 — Key Word Transformation",
            "Part 3 — Word Formation",
            "Part 1 — Multiple Choice Cloze",
            "Part 2 — Open Cloze",
            "📋 Cambridge Exam Test 1",
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
            ans = st.text_input("Your answer:", key=f"kwt_input_{idx}")
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
            ans = st.text_input("Your answer:", key=f"wf_input_{idx}")
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

    # ── Cambridge Exam Test 1 ────────────────────────────────────────────────
    with tab5:
            st.markdown(f"### {CAMBRIDGE_TEST_1['title']}")
            cam_p1, cam_p2, cam_p3, cam_p4 = st.tabs([
                "Part 1 — MCC",
                "Part 2 — Open Cloze",
                "Part 3 — Word Formation",
                "Part 4 — KWT",
            ])

            # ── Cambridge Part 1 ────────────────────────────────────────────────
            with cam_p1:
                p1 = CAMBRIDGE_TEST_1["Part 1"]
                st.markdown(f"**{p1['title']}**")
                st.markdown("*Choose the best option (A, B, C or D) for each gap.*")
                st.markdown(f'<div class="example-box">📝 {p1["text"]}</div>', unsafe_allow_html=True)
                st.markdown("---")
                gap_idx = st.session_state.cam1_idx
                gap = p1["gaps"][gap_idx]
                st.markdown(f"*Gap {gap['num']} of {len(p1['gaps'])}*")
                st.progress((gap_idx + 1) / len(p1["gaps"]))
                sel = st.radio(f"Gap ({gap['num']}):", gap["options"], index=None, key=f"cam1_radio_{gap_idx}")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Check", use_container_width=True, key="cam1_chk"):
                        st.session_state.cam1_sel = sel
                        st.session_state.cam1_checked = True
                        add_score(sel is not None and sel[0] == gap["answer"])
                        st.rerun()
                with c2:
                    if st.button("➡️ Next", use_container_width=True, key="cam1_nxt"):
                        st.session_state.cam1_idx = (gap_idx + 1) % len(p1["gaps"])
                        st.session_state.cam1_sel = None
                        st.session_state.cam1_checked = False
                        st.rerun()
                if st.session_state.cam1_checked and st.session_state.cam1_sel:
                    if st.session_state.cam1_sel[0] == gap["answer"]:
                        st.success(f"✅ Correct! **{gap['answer']}** — {gap['explanation']}")
                    else:
                        st.error(f"❌ Correct: **{gap['answer']}** — {gap['explanation']}")

            # ── Cambridge Part 2 ────────────────────────────────────────────────
            with cam_p2:
                p2 = CAMBRIDGE_TEST_1["Part 2"]
                st.markdown(f"**{p2['title']}**")
                st.markdown("*Fill each gap (9–16) with ONE word.*")
                st.markdown(f'<div class="example-box">📝 {p2["text"]}</div>', unsafe_allow_html=True)
                st.markdown("**Your answers:**")
                user_cam2 = {}
                cols = st.columns(4)
                for i, num in enumerate(p2["answers"]):
                    with cols[i % 4]:
                        user_cam2[num] = st.text_input(
                            f"Gap ({num}):", key=f"cam2_{num}",
                        )
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Check all", use_container_width=True, key="cam2_chk"):
                        st.session_state.cam2_answers = user_cam2
                        st.session_state.cam2_checked = True
                        st.rerun()
                with c2:
                    if st.button("🔄 Reset", use_container_width=True, key="cam2_rst"):
                        st.session_state.cam2_answers = {}
                        st.session_state.cam2_checked = False
                        for num in p2["answers"]:
                            st.session_state[f"cam2_{num}"] = ""
                        st.rerun()
                if st.session_state.cam2_checked:
                    accepted = p2.get("accepted", {})
                    right = 0
                    for num, correct in p2["answers"].items():
                        val = st.session_state.cam2_answers.get(num, "").strip().lower()
                        valid = [correct.lower()] + [a.lower() for a in accepted.get(num, [])]
                        if val in valid:
                            right += 1
                    total = len(p2["answers"])
                    if right == total:
                        st.success(f"✅ Perfect! {right}/{total}")
                    else:
                        st.warning(f"**{right}/{total} correct**")
                    for num, correct in p2["answers"].items():
                        val = st.session_state.cam2_answers.get(num, "").strip()
                        valid = [correct.lower()] + [a.lower() for a in accepted.get(num, [])]
                        if val.lower() in valid:
                            st.success(f"Gap ({num}): **{val}** ✅")
                        else:
                            alts = "/".join([correct] + accepted.get(num, []))
                            st.error(f"Gap ({num}): *{val or '—'}* → **{alts}**")
                    with st.expander("💡 Tips"):
                        st.markdown(p2["tips"])

            # ── Cambridge Part 3 ────────────────────────────────────────────────
            with cam_p3:
                p3 = CAMBRIDGE_TEST_1["Part 3"]
                st.markdown(f"**{p3['title']}**")
                st.markdown("*Use the word in CAPITALS to form a word that fits the gap.*")
                items3 = p3["items"]
                idx3 = st.session_state.cam3_idx
                ex3 = items3[idx3]
                st.markdown(f"*{idx3+1} of {len(items3)}*")
                st.progress((idx3 + 1) / len(items3))
                st.markdown(f'<div class="example-box">📝 {ex3["prompt"]}</div>', unsafe_allow_html=True)
                ans3 = st.text_input("Your answer:", key=f"cam3_input_{idx3}")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Check", use_container_width=True, key="cam3_chk"):
                        st.session_state.cam3_ans = ans3
                        st.session_state.cam3_checked = True
                        add_score(ans3.strip().lower() == ex3["answer"].lower())
                        st.rerun()
                with c2:
                    if st.button("➡️ Next", use_container_width=True, key="cam3_nxt"):
                        st.session_state.cam3_idx = (idx3 + 1) % len(items3)
                        st.session_state.cam3_ans = ""
                        st.session_state.cam3_checked = False
                        st.rerun()
                if st.session_state.cam3_checked:
                    if st.session_state.cam3_ans.strip().lower() == ex3["answer"].lower():
                        st.success(f"✅ Correct! **{ex3['answer']}**")
                    else:
                        st.error(f"❌ Correct form: **{ex3['answer']}**")

            # ── Cambridge Part 4 ────────────────────────────────────────────────
            with cam_p4:
                p4 = CAMBRIDGE_TEST_1["Part 4"]
                st.markdown("*Rewrite each sentence using the key word. Use 3–6 words including the key word unchanged.*")
                items4 = p4["items"]
                idx4 = st.session_state.cam4_idx
                ex4 = items4[idx4]
                st.markdown(f"*{idx4+1} of {len(items4)}*")
                st.progress((idx4 + 1) / len(items4))
                st.markdown(f'<div class="example-box">📝 {ex4["sentence"]}</div>', unsafe_allow_html=True)
                st.markdown(f"**Key word: `{ex4['key']}`**")
                ans4 = st.text_input("Your answer:", key=f"cam4_input_{idx4}")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Check", use_container_width=True, key="cam4_chk"):
                        st.session_state.cam4_ans = ans4
                        st.session_state.cam4_checked = True
                        add_score(ans4.strip().lower().rstrip(".") == ex4["answer"].strip().lower().rstrip("."))
                        st.rerun()
                with c2:
                    if st.button("➡️ Next", use_container_width=True, key="cam4_nxt"):
                        st.session_state.cam4_idx = (idx4 + 1) % len(items4)
                        st.session_state.cam4_ans = ""
                        st.session_state.cam4_checked = False
                        st.rerun()
                if st.session_state.cam4_checked:
                    st.success(f"**Model answer:** {ex4['answer']}")
                    if "pattern" in ex4:
                        st.caption(f"🏷️ Pattern: *{ex4['pattern']}*")
                    if ans4.strip().lower().rstrip(".") == ex4["answer"].strip().lower().rstrip("."):
                        st.success("✅ Perfect match!")
                    else:
                        st.warning("⚠️ Compare carefully — minor variations may also be acceptable.")
