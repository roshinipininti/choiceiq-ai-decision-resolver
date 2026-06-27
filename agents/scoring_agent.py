def calculate_scores(state):

    scores = {}

    for model, response in state["responses"].items():

        if response is None:
            continue

        recommendation = response["recommendation"]

        confidence = response["confidence"]

        scores.setdefault(
            recommendation,
            0
        )

        scores[recommendation] += confidence

    state["scores"] = scores

    if scores:

        state["final_recommendation"] = max(
            scores,
            key=scores.get
        )

    return state