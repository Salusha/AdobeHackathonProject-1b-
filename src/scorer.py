from sentence_transformers import SentenceTransformer, util

# Load once
_model = None
def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

def rank_sections(sections, query, top_k=5):
    """
    sections: list of {"text":..., "page":...}
    query: string (persona + job)
    returns list of sections sorted by relevance
    """
    model = _get_model()
    texts = [s["text"] for s in sections]
    emb_texts = model.encode(texts, convert_to_tensor=True)
    emb_query = model.encode(query, convert_to_tensor=True)
    sims = util.cos_sim(emb_query, emb_texts)[0]
    ranked = sorted(
        zip(sections, sims.tolist()),
        key=lambda x: x[1],
        reverse=True
    )
    # attach importance_rank and similarity score
    return [
        {
            **sec,
            "importance_rank": idx + 1,
            "score": float(score)
        }
        for idx, (sec, score) in enumerate(ranked[:top_k])
    ]
