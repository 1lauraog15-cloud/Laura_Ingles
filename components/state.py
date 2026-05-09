import random
import streamlit as st

from data import (
    VOCABULARY, PHRASAL_VERBS, VERBS_PREPOSITIONS, COLLOCATIONS,
    CONNECTORS,
)


def init_state():
    defaults = {
        # scores
        "score_correct": 0, "score_total": 0,
        # vocab flashcard
        "vocab_idx": 0, "vocab_revealed": False,
        # vocab fill
        "vocab_fill_idx": random.randint(0, len(VOCABULARY) - 1),
        "vocab_fill_ans": "", "vocab_fill_checked": False,
        # vocab quiz
        "vocab_quiz_idx": random.randint(0, len(VOCABULARY) - 1),
        "vocab_quiz_options": [], "vocab_quiz_selected": None, "vocab_quiz_checked": False,
        # phrasal verbs flashcard
        "pv_idx": 0, "pv_revealed": False,
        # phrasal verbs fill
        "pv_fill_idx": random.randint(0, len(PHRASAL_VERBS) - 1),
        "pv_fill_ans": "", "pv_fill_checked": False,
        # verbs+preps flashcard
        "vp_idx": 0, "vp_revealed": False,
        # verbs+preps fill
        "vp_fill_idx": random.randint(0, len(VERBS_PREPOSITIONS) - 1),
        "vp_fill_ans": "", "vp_fill_checked": False,
        # collocations
        "coll_idx": 0, "coll_revealed": False,
        "coll_fill_idx": random.randint(0, len(COLLOCATIONS) - 1),
        "coll_fill_ans": "", "coll_fill_checked": False,
        # connectors
        "conn_fill_flat_idx": 0, "conn_fill_ans": "", "conn_fill_checked": False,
        # grammar
        "gram_topic_idx": 0, "gram_ex_idx": 0,
        "gram_ans": "", "gram_revealed": False,
        # kwt
        "kwt_idx": 0, "kwt_ans": "", "kwt_checked": False,
        # word formation
        "wf_idx": 0, "wf_ans": "", "wf_checked": False,
        # mcc
        "mcc_idx": 0, "mcc_selected": None, "mcc_checked": False,
        # open cloze
        "oc_idx": 0, "oc_answers": {}, "oc_checked": False,
        # idioms
        "idiom_idx": 0, "idiom_revealed": False,
        "idiom_fill_idx": 0, "idiom_fill_ans": "", "idiom_fill_checked": False,
        # confusing expressions
        "conf_topic": "I can tell / You can tell",
        "conf_ex_idx": 0, "conf_ans": "", "conf_revealed": False,
        # Cambridge Test 1 — Part 1 MCC
        "cam1_idx": 0, "cam1_sel": None, "cam1_checked": False,
        # Cambridge Test 1 — Part 2 Open Cloze
        "cam2_answers": {}, "cam2_checked": False,
        # Cambridge Test 1 — Part 3 Word Formation
        "cam3_idx": 0, "cam3_ans": "", "cam3_checked": False,
        # Cambridge Test 1 — Part 4 KWT
        "cam4_idx": 0, "cam4_ans": "", "cam4_checked": False,
        # Reading section
        "rdg_part": "Part 5",
        "rdg5_idx": 0, "rdg5_sel": {}, "rdg5_checked": False,
        "rdg6_sel": {}, "rdg6_checked": False,
        "rdg7_sel": {}, "rdg7_checked": False,
        "rdg8_sel": {}, "rdg8_checked": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def add_score(correct: bool):
    st.session_state.score_total += 1
    if correct:
        st.session_state.score_correct += 1
