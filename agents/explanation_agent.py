from services.llm_service import chat
from config.settings import DEFAULT_MODEL


def generate_explanation(state):

    print("\nGenerating final explanation...\n")

    prompt = f"""
You are ChoiceIQ's Final Decision Agent.

Generate a final report using the following information.

Question:
{state["question"]}

Context:
{state["context_answers"]}

Evidence Summary:
{state["evidence_summary"]}

Model Responses:
{state["responses"]}

Conflict:
{state["conflict"]}

Scores:
{state["scores"]}

Decision Matrix:
{state["decision_matrix"]}

Final Recommendation:
{state["final_recommendation"]}

Write the report in this format:

# Final Recommendation

<recommendation>

## Why?

Explain why this recommendation is best.

## Evidence

Summarize the supporting evidence.

## Model Opinions

Briefly summarize each model's opinion.

## Conflict

Explain whether the models agreed or disagreed.

## Confidence

Mention that the recommendation is based on weighted confidence scores.
"""

    report = chat(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["final_report"] = report

    return state