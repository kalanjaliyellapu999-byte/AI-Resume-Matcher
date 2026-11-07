"""
Matcher Module
==============
Implements resume-job description matching using TF-IDF vectorization
and Cosine Similarity from Scikit-learn.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from typing import Dict, List, Tuple

from text_processor import preprocess_text


def calculate_match_score(resume_text: str, job_description: str) -> float:
    """
    Calculate the matching score between a resume and a job description
    using TF-IDF vectorization and Cosine Similarity.

    Args:
        resume_text: Raw or preprocessed resume text.
        job_description: Raw or preprocessed job description text.

    Returns:
        Match score as a percentage (0-100).

    Raises:
        ValueError: If either input is empty.
    """
    if not resume_text or not resume_text.strip():
        raise ValueError("Resume text is empty.")
    if not job_description or not job_description.strip():
        raise ValueError("Job description is empty.")

    # Preprocess both texts
    processed_resume = preprocess_text(resume_text, remove_stops=True)
    processed_jd = preprocess_text(job_description, remove_stops=True)

    if not processed_resume:
        raise ValueError("Resume text contains no meaningful content after preprocessing.")
    if not processed_jd:
        raise ValueError("Job description contains no meaningful content after preprocessing.")

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),    # Unigrams and bigrams
        sublinear_tf=True,     # Apply sublinear TF scaling
    )

    tfidf_matrix = vectorizer.fit_transform([processed_resume, processed_jd])

    # Cosine Similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = float(similarity[0][0]) * 100

    return round(score, 2)


def get_top_matching_terms(
    resume_text: str,
    job_description: str,
    top_n: int = 20
) -> List[Tuple[str, float]]:
    """
    Find the top matching terms between resume and job description
    based on TF-IDF weights.

    Args:
        resume_text: Raw resume text.
        job_description: Raw job description text.
        top_n: Number of top terms to return.

    Returns:
        List of (term, combined_weight) tuples sorted by weight descending.
    """
    processed_resume = preprocess_text(resume_text, remove_stops=True)
    processed_jd = preprocess_text(job_description, remove_stops=True)

    if not processed_resume or not processed_jd:
        return []

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )

    tfidf_matrix = vectorizer.fit_transform([processed_resume, processed_jd])
    feature_names = vectorizer.get_feature_names_out()

    resume_vector = tfidf_matrix[0].toarray().flatten()
    jd_vector = tfidf_matrix[1].toarray().flatten()

    # Find terms present in both documents
    common_mask = (resume_vector > 0) & (jd_vector > 0)
    common_indices = np.where(common_mask)[0]

    if len(common_indices) == 0:
        return []

    # Combined weight: product of TF-IDF weights (higher when both are important)
    combined_weights = resume_vector[common_indices] * jd_vector[common_indices]
    sorted_indices = np.argsort(-combined_weights)[:top_n]

    results = []
    for idx in sorted_indices:
        term_idx = common_indices[idx]
        results.append((feature_names[term_idx], round(float(combined_weights[idx]), 4)))

    return results


def get_detailed_analysis(
    resume_text: str,
    job_description: str
) -> Dict:
    """
    Perform a detailed matching analysis returning score, top terms,
    and coverage metrics.

    Args:
        resume_text: Raw resume text.
        job_description: Raw job description text.

    Returns:
        Dictionary with 'score', 'top_terms', 'jd_coverage', 'resume_coverage'.
    """
    score = calculate_match_score(resume_text, job_description)
    top_terms = get_top_matching_terms(resume_text, job_description, top_n=15)

    processed_resume = preprocess_text(resume_text, remove_stops=True)
    processed_jd = preprocess_text(job_description, remove_stops=True)

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        sublinear_tf=True,
    )
    tfidf_matrix = vectorizer.fit_transform([processed_resume, processed_jd])

    resume_vector = tfidf_matrix[0].toarray().flatten()
    jd_vector = tfidf_matrix[1].toarray().flatten()

    # How many JD terms appear in the resume
    jd_terms = np.sum(jd_vector > 0)
    common_terms = np.sum((resume_vector > 0) & (jd_vector > 0))
    jd_coverage = round((common_terms / jd_terms * 100) if jd_terms > 0 else 0, 2)

    # How many resume terms appear in the JD
    resume_terms = np.sum(resume_vector > 0)
    resume_coverage = round((common_terms / resume_terms * 100) if resume_terms > 0 else 0, 2)

    return {
        "score": score,
        "top_terms": top_terms,
        "jd_coverage": jd_coverage,
        "resume_coverage": resume_coverage,
        "common_term_count": int(common_terms),
        "jd_term_count": int(jd_terms),
        "resume_term_count": int(resume_terms),
    }
