from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_data = {
    "Data Scientist": "machine learning, data analysis, python, pandas, sklearn, statistics",
    "Web Developer": "html, css, javascript, react, django, web design",
    "AI Engineer": "deep learning, pytorch, tensorflow, NLP, computer vision",
    "Backend Developer": "django, flask, python, postgresql, apis",
    "Frontend Developer": "html, css, javascript, react, ui, ux",
    "Teacher":"bscs,teaching,frontend,backend,bscit",
    "Network Administrator":"ccna,ccnp,cnnie"
}

def match_top_jobs(resume_text, top_n=3):
    jobs = list(job_data.keys())
    descriptions = list(job_data.values())

    documents = [resume_text] + descriptions
    tfidf = TfidfVectorizer().fit_transform(documents)

    # Calculate similarity between resume and each job
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    # Pair job title with similarity
    job_matches = list(zip(jobs, similarity))

    # Sort by best match
    sorted_matches = sorted(job_matches, key=lambda x: x[1], reverse=True)

    # Return top N matches
    return [(job, round(score * 100, 2)) for job, score in sorted_matches[:top_n]]
