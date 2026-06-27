from config.settings import DECISION_MODEL
from services.llm_service import chat
import json


def generate_decision_matrix(state):

    print("\nGenerating decision matrix...\n")

    prompt = f"""
You are a Decision Matrix Generator.

Question:
{state["question"]}

Context:
{state["context_answers"]}

Evidence Summary:
{state["evidence_summary"]}

Final Recommendation:
{state["final_recommendation"]}

Create a comparison matrix.

Return ONLY valid JSON.

Format:

{{
    "factors": [
        {{
            "factor": "Placement ROI",
            "option1": "High",
            "option2": "Medium"
        }},
        {{
            "factor": "Learning Time",
            "option1": "Medium",
            "option2": "High"
        }},
        {{
            "factor": "Long-Term Growth",
            "option1": "Medium",
            "option2": "High"
        }}
    ]
}}

Do not include markdown.
"""

    try:

        response = chat(
            model=DECISION_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        state["decision_matrix"] = json.loads(response)

    except Exception:

        state["decision_matrix"] = {
            "factors": [
                {
                    "factor": "Placement ROI",
                    "option1": "Unknown",
                    "option2": "Unknown"
                }
            ]
        }

    return state