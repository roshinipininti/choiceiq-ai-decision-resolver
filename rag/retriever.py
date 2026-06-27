from rag.document_loader import load_document
from rag.chunker import chunk_text
from rag.embeddings import (
    embed_documents,
    embed_query
)
from rag.vector_store import VectorStore


def retrieve(query, urls):

    all_chunks = []

    for url in urls:

        text = load_document(url)

        if text:

            chunks = chunk_text(text)

            all_chunks.extend(chunks)

    if not all_chunks:

        return []

    embeddings = embed_documents(all_chunks)

    dimension = embeddings.shape[1]

    store = VectorStore(dimension)

    store.add(
        embeddings,
        all_chunks
    )

    query_embedding = embed_query(query)

    return store.search(
        query_embedding,
        k=5
    )