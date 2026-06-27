def detect_conflict(state):

    recommendations = []

    for response in state["responses"].values():

        if response is None:
            continue

        recommendations.append(
            response["recommendation"]
        )

    if len(set(recommendations)) <= 1:

        state["conflict"] = "AGREE"

    else:

        state["conflict"] = "DISAGREE"

    return state