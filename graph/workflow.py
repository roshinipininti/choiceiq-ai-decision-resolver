from langgraph.graph import StateGraph, END
from state.state import ChoiceIQState
from agents.context_agent import collect_context
from agents.evidence_agent import collect_evidence
from agents.evidence_summarizer import summarize_evidence
from agents.llm_agent import ask_all_models
from agents.conflict_agent import detect_conflict
from agents.scoring_agent import calculate_scores
from agents.decision_matrix_agent import generate_decision_matrix
from agents.explanation_agent import generate_explanation

def build_context_workflow():

    workflow = StateGraph(ChoiceIQState)

    workflow.add_node("context", collect_context)

    workflow.set_entry_point("context")

    workflow.add_edge("context", END)

    return workflow.compile()


def build_analysis_workflow():

    workflow = StateGraph(ChoiceIQState)

    workflow.add_node("evidence", collect_evidence)

    workflow.add_node("summary", summarize_evidence)

    workflow.add_node("llm", ask_all_models)

    workflow.add_node("conflict", detect_conflict)

    workflow.add_node("scoring", calculate_scores)

    workflow.add_node("decision_matrix", generate_decision_matrix)

    workflow.add_node("explanation", generate_explanation)

    workflow.set_entry_point("evidence")

    workflow.add_edge("evidence", "summary")

    workflow.add_edge("summary", "llm")

    workflow.add_edge("llm", "conflict")

    workflow.add_edge("conflict", "scoring")

    workflow.add_edge("scoring", "decision_matrix")

    workflow.add_edge("decision_matrix", "explanation")

    workflow.add_edge("explanation", END)

    return workflow.compile()