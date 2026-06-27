from graph.workflow import (
    build_context_workflow,
    build_analysis_workflow,
)

from state.state import create_state
from utils.history import save_history


context_workflow = build_context_workflow()
analysis_workflow = build_analysis_workflow()


def generate_context_questions(question: str):

    state = create_state(question)

    state = context_workflow.invoke(state)

    return state


def analyze_question(question: str, context_answers: dict):

    state = create_state(question)

    state["context_answers"] = context_answers

    state = analysis_workflow.invoke(state)

    save_history(state)

    return state