from duckduckgo_search import DDGS

from rag.chunker import chunk_text
from rag.embeddings import embed_documents
from rag.embeddings import embed_query
from rag.vector_store import VectorStore


def collect_evidence(state):

    print("\nSearching the web...\n")

    documents = []

    with DDGS() as ddgs:

        results = ddgs.text(
            state["question"],
            max_results=5
        )

        for result in results:

            title = result.get("title", "")

            body = result.get("body", "")

            text = title + "\n" + body

            chunks = chunk_text(text)

            documents.extend(chunks)

    if not documents:

        state["evidence"] = []

        return state

    embeddings = embed_documents(documents)

    store = VectorStore(
        embeddings.shape[1]
    )

    store.add(
        embeddings,
        documents
    )

    query_embedding = embed_query(
        state["question"]
    )

    retrieved = store.search(
        query_embedding,
        k=5
    )

    state["evidence"] = retrieved

    return state