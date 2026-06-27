# 🚀 ChoiceIQ – AI Decision Resolver

> A Multi-Agent AI Decision Support System that resolves conflicting recommendations from multiple Large Language Models (LLMs) using Retrieval-Augmented Generation (RAG), evidence-based reasoning, and a decision matrix.

---

## 📖 Overview

Different AI models often provide different answers for the same question, making it difficult for users to decide which recommendation to trust.

**ChoiceIQ** addresses this problem by:

- Retrieving relevant evidence from the web
- Querying multiple LLMs
- Detecting conflicts between their responses
- Scoring each recommendation
- Selecting the best decision using a decision matrix
- Providing a clear explanation for the final recommendation

---

## ✨ Features

- 🤖 Multi-Agent Architecture
- 🔍 Retrieval-Augmented Generation (RAG)
- 🌐 DuckDuckGo Web Search
- 📚 FAISS Vector Database
- 🧠 Multiple LLM Integration
- ⚖️ Conflict Detection
- 📊 Decision Matrix Scoring
- 💡 Explainable Final Recommendation
- 🧩 Modular LangGraph Workflow

---

## 🏗️ Architecture

```
                    User Question
                          │
                          ▼
                 Context Agent
                          │
                          ▼
                 Evidence Agent
                          │
                          ▼
                Evidence Summarizer
                          │
                          ▼
                   Multiple LLMs
          ┌──────────┬──────────┬──────────┐
          │          │          │
        GPT       Gemini     Claude
          └──────────┴──────────┴──────────┘
                          │
                          ▼
                 Conflict Detection
                          │
                          ▼
                  Scoring Agent
                          │
                          ▼
                  Decision Matrix
                          │
                          ▼
                 Explanation Agent
                          │
                          ▼
                Final Recommendation
```

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| AI Workflow | LangGraph |
| LLM Framework | LangChain |
| Vector Database | FAISS |
| Search | DuckDuckGo Search |
| Embeddings | OpenAI Embeddings |
| LLM APIs | OpenRouter |
| Prompting | Prompt Engineering |

---

## 📂 Project Structure

```
choiceiq-ai-decision-resolver/
│
├── agents/
│   ├── context_agent.py
│   ├── evidence_agent.py
│   ├── summarizer_agent.py
│   ├── llm_agent.py
│   ├── conflict_agent.py
│   ├── scoring_agent.py
│   ├── decision_matrix_agent.py
│   └── explanation_agent.py
│
├── services/
├── workflow/
├── prompts/
├── utils/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. User submits a question.
2. Context Agent gathers relevant context.
3. Evidence Agent retrieves supporting information.
4. Evidence is summarized.
5. Multiple LLMs generate independent recommendations.
6. Conflict Agent identifies disagreements.
7. Scoring Agent evaluates responses.
8. Decision Matrix selects the best recommendation.
9. Explanation Agent generates a transparent final answer.

---

## 🧠 Multi-Agent System

| Agent | Responsibility |
|--------|----------------|
| Context Agent | Collects user context |
| Evidence Agent | Retrieves relevant evidence |
| Evidence Summarizer | Summarizes retrieved documents |
| LLM Agent | Queries multiple LLMs |
| Conflict Agent | Detects conflicting responses |
| Scoring Agent | Scores recommendations |
| Decision Matrix Agent | Chooses the best option |
| Explanation Agent | Generates the final explanation |

---

## 📚 RAG Pipeline

```
User Question
      │
      ▼
DuckDuckGo Search
      │
      ▼
Document Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Search
      │
      ▼
Relevant Evidence
      │
      ▼
Evidence Summary
      │
      ▼
LLMs
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/roshinipininti/choiceiq-ai-decision-resolver.git
```

Navigate into the project:

```bash
cd choiceiq-ai-decision-resolver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENROUTER_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python app.py
```

---

## 💬 Example

**Input**

```
Should I focus on DSA or Generative AI for placements?
```

**Output**

```
Recommendation:
Focus on DSA while gradually learning Generative AI.

Reason:
Most companies still evaluate DSA during coding interviews,
while GenAI provides long-term career advantages.

Confidence: 91%
```

---

## 🎯 Future Improvements

- Support additional LLM providers
- Live web search integration
- Confidence calibration
- User feedback learning
- Parallel LLM execution
- Decision history dashboard
- Visualization of agent workflow

---

## 📌 Key Learnings

- Multi-Agent AI Systems
- LangGraph Workflow Design
- Retrieval-Augmented Generation (RAG)
- Vector Search with FAISS
- Prompt Engineering
- Evidence-Based Reasoning
- Explainable AI
- Modular Software Architecture

---

## 👩‍💻 Author

**Roshini Pininti**

GitHub: https://github.com/roshinipininti

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
