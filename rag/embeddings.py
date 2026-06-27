from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def embed_documents(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings


def embed_query(query):

    return model.encode(
        [query],
        convert_to_numpy=True
    )[0]