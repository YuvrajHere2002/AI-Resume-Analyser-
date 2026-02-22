from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_semantic_score(resume_text, job_description):
    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_tensor=True
    )

    score = cosine_similarity(
        embeddings[0].cpu().reshape(1, -1),
        embeddings[1].cpu().reshape(1, -1)
    )[0][0]

    return round(score * 100, 2)
