from config.settings import SUMMARY_MODEL
from services.llm_service import chat


def summarize_evidence(state):

    print("\nSummarizing retrieved evidence...\n")

    evidence = "\n\n".join(state["evidence"])

    if not evidence.strip():

        state["evidence_summary"] = "No supporting evidence found."

        return state

    prompt = f"""
You are an Evidence Summarizer.

Below are semantically retrieved evidence chunks.

Your task is to summarize them.

Rules:

- Maximum 6 bullet points.
- Remove duplicate information.
- Keep only factual information.
- Do NOT recommend any option.
- Do NOT invent facts.
- Keep the summary concise.

Evidence:

{evidence}
"""

    summary = chat(
        model=SUMMARY_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["evidence_summary"] = summary

    return state