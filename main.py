from services.decision_service import analyze_question


def main():

    print("=" * 70)
    print("ChoiceIQ - AI Decision Clash Resolver")
    print("=" * 70)

    question = input("\nEnter your question: ")

    state = analyze_question(question)

    print()
    print(state["final_report"])


if __name__ == "__main__":
    main()