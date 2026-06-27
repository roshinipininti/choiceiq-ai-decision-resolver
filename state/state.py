from typing import TypedDict


class ChoiceIQState(TypedDict):

    question: str

    context_questions: list[str]

    context_answers: dict[str, str]

    evidence: list[str]

    evidence_summary: str

    responses: dict

    scores: dict

    decision_matrix: dict

    final_report: str

    conflict: str | None

    final_recommendation: str | None


def create_state(question: str) -> ChoiceIQState:

    return {

        "question": question,

        "context_questions": [],

        "context_answers": {},

        "evidence": [],

        "evidence_summary": "",

        "responses": {},

        "scores": {},

        "decision_matrix": {},

        "final_report": "",

        "conflict": None,

        "final_recommendation": None

    }