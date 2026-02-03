from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def rank_resumes(job_text: str, resume_texts: dict):
    resume_names = list(resume_texts.keys())
    documents = [job_text] + [resume_texts[name] for name in resume_names]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    ranked = sorted(zip(resume_names, scores), key=lambda x: x[1], reverse=True)
    return ranked


def top_match_keywords(job_text: str, resume_text: str, top_n: int = 10):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([job_text, resume_text])

    job_vec = tfidf[0].toarray().flatten()
    res_vec = tfidf[1].toarray().flatten()

    contrib = job_vec * res_vec
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_idx = np.argsort(contrib)[::-1][:top_n]

    results = []
    for i in top_idx:
        if contrib[i] > 0:
            results.append((feature_names[i], float(contrib[i])))

    return results
