import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd

from services.decision_service import (
    generate_context_questions,
    analyze_question
)

st.set_page_config(
    page_title="ChoiceIQ",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ChoiceIQ")
st.subheader("AI Decision Clash Resolver")

st.markdown("---")

# -------------------------
# Session State
# -------------------------

if "question" not in st.session_state:
    st.session_state.question = ""

if "context_questions" not in st.session_state:
    st.session_state.context_questions = []

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

if "state" not in st.session_state:
    st.session_state.state = None

# -------------------------
# User Question
# -------------------------

question = st.text_input(
    "Enter your question",
    value=st.session_state.question,
    placeholder="Example: Should I learn DSA or GenAI?"
)

# -------------------------
# Generate Questions
# -------------------------

if st.button("Generate Follow-up Questions"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    st.session_state.question = question

    with st.spinner("Generating questions..."):

        state = generate_context_questions(question)

    st.session_state.context_questions = state["context_questions"]

    st.session_state.analysis_complete = False

# -------------------------
# Show Questions
# -------------------------

if len(st.session_state.context_questions) > 0:

    st.markdown("---")

    st.header("Answer these questions")

    answers = {}

    for q in st.session_state.context_questions:

        answers[q] = st.text_input(q)

    if st.button("Analyze Decision"):

        with st.spinner("Running AI Agents..."):

            result = analyze_question(
                st.session_state.question,
                answers
            )

        st.session_state.state = result

        st.session_state.analysis_complete = True

# -------------------------
# Results
# -------------------------

if st.session_state.analysis_complete:

    state = st.session_state.state

    st.markdown("---")

    st.header("🎯 Final Recommendation")

    st.success(state["final_recommendation"])

    st.markdown("---")

    st.header("⚔ Model Conflict")

    st.info(state["conflict"])

    st.markdown("---")

    st.header("📊 Scores")

    score_df = pd.DataFrame(
        {
            "Recommendation": list(state["scores"].keys()),
            "Score": list(state["scores"].values())
        }
    )

    st.dataframe(
        score_df,
        use_container_width=True
    )
    st.markdown("---")

    ##############################
    # Model Responses
    ##############################

    st.header("🤖 Model Opinions")

    responses = state["responses"]

    cols = st.columns(len(responses))

    for col, (model, response) in zip(cols, responses.items()):

        with col:

            st.subheader(model)

            if response is None:

                st.error("No Response")

            else:

                st.metric(
                    "Recommendation",
                    response["recommendation"]
                )

                st.metric(
                    "Confidence",
                    f'{response["confidence"]}%'
                )

                st.write("**Reason**")

                st.write(response["reason"])

    st.markdown("---")

    ##############################
    # Evidence Summary
    ##############################

    with st.expander(
        "📚 Evidence Summary",
        expanded=True
    ):

        st.write(state["evidence_summary"])

    ##############################
    # Decision Matrix
    ##############################

    with st.expander(
        "📈 Decision Matrix",
        expanded=True
    ):

        matrix = state["decision_matrix"]

        if isinstance(matrix, dict) and "factors" in matrix:

            df = pd.DataFrame(matrix["factors"])

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.write(matrix)

    ##############################
    # Context Answers
    ##############################

    with st.expander(
        "📝 Context Answers"
    ):

        st.json(state["context_answers"])

    ##############################
    # Full Report
    ##############################

    with st.expander(
        "📄 Final Report"
    ):

        st.write(state["final_report"])

    ##############################
    # Download
    ##############################

    st.download_button(
        label="⬇ Download Report",
        data=state["final_report"],
        file_name="choiceiq_report.txt",
        mime="text/plain",
        use_container_width=True
    )