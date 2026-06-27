import json

from config.settings import CONTEXT_MODEL
from services.llm_service import chat


def collect_context(state):

    print("\nGenerating follow-up questions...\n")

    prompt = f"""
You are the Context Collection Agent of ChoiceIQ.

The user asked:

{state["question"]}

Your task is to understand the decision category and ask the MOST RELEVANT follow-up questions.

Possible categories include (but are not limited to):
- Career
- Placements
- Higher Studies
- Buying Products
- Finance
- Travel
- Health & Fitness
- Learning
- Business
- Productivity
- Technology
- General

Rules:
1. First identify the category.
2. Ask ONLY the questions needed to make a better recommendation.
3. Maximum 3 questions.
4. Questions should be short.
5. Do NOT answer the user's question.
6. Return ONLY valid JSON.

Format:

{{
    "category":"Career",
    "questions":[
        "...",
        "...",
        "..."
    ]
}}
"""

    try:

        response = chat(
            model=CONTEXT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        data = json.loads(response)

    except Exception:

        data = {
            "category": "General",
            "questions": [
                "What is your main goal?",
                "What is your timeline?",
                "Any important constraints?"
            ]
        }

    state["category"] = data["category"]

    state["context_questions"] = data["questions"]

    return state