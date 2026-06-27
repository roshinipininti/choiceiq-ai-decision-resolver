import json

from config.models import MODELS
from services.llm_service import chat


def ask_all_models(state):

    responses = {}

    context = ""

    for question, answer in state["context_answers"].items():
        context += f"{question}: {answer}\n"

    evidence = state["evidence_summary"]

    for model in MODELS:

        print(f"\nQuerying {model['name']}...")

        try:

            answer = chat(
                model=model["id"],
                messages=[
                    {
                        "role": "system",
                        "content": """
You are an expert decision advisor.

Return ONLY valid JSON.

{
    "recommendation":"...",
    "reason":"...",
    "confidence":90
}
"""
                    },
                    {
                        "role": "user",
                        "content": f"""
Question

{state["question"]}

Context

{context}

Evidence Summary

{evidence}

Use both the context and evidence to make the recommendation.

Return ONLY JSON.
"""
                    }
                ]
            )

            responses[model["name"]] = json.loads(answer)

        except Exception as e:

            print(e)

            responses[model["name"]] = None

    state["responses"] = responses

    return state