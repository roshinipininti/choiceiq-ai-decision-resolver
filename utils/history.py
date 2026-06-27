import json
from pathlib import Path
from datetime import datetime


HISTORY_FILE = Path("data/history/history.json")


def save_history(state):

    HISTORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if HISTORY_FILE.exists():

        with open(HISTORY_FILE, "r", encoding="utf-8") as f:

            history = json.load(f)

    else:

        history = []

    history.append({

        "timestamp": datetime.now().isoformat(),

        "question": state["question"],

        "recommendation": state["final_recommendation"],

        "scores": state["scores"],

        "conflict": state["conflict"]

    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:

        json.dump(
            history,
            f,
            indent=4
        )