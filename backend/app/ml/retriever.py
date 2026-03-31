from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def build_embeddings(sentences):
    return model.encode(sentences, convert_to_tensor=True)


def retrieve(query, sentences, embeddings, top_k=3):
    query_embedding = model.encode(query, convert_to_tensor=True)

    similarities = util.cos_sim(query_embedding, embeddings)[0]

    k = min(top_k, len(sentences))
    top_results = similarities.topk(k=k)

    results = []
    for idx in top_results.indices:
        idx = int(idx)
        results.append({
            "sentence": sentences[idx],
            "score": float(similarities[idx])
        })

    return results