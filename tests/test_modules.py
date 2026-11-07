"""
Unit Tests for AI Resume Matcher Modules
=========================================
Run with:
    pytest tests/ -v
"""

import sys
import os
import json

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from text_processor import (
    clean_text,
    remove_stop_words,
    tokenize,
    preprocess_text,
    extract_sentences,
    get_word_frequency,
)
from matcher import calculate_match_score, get_top_matching_terms, get_detailed_analysis
from skills_extractor import extract_skills, get_flat_skills, compare_skills
from recommendations import generate_recommendations


# ─── Sample Texts for Testing ───────────────────────────────────────────────────

SAMPLE_RESUME = """
Arjun Sharma - Software Engineer
arjun@email.com | Bengaluru, India

Summary:
Experienced Software Engineer with 4+ years in Python, Django, and AWS cloud services.

Technical Skills:
Python, JavaScript, SQL, Django, Flask, FastAPI, React, PostgreSQL, MySQL, Redis,
Docker, Kubernetes, AWS, Terraform, Git, GitHub, Jenkins, CI/CD, Agile, Scrum,
Microservices, REST API Design, Linux, Unit Testing, TDD.

Experience:
- Built RESTful APIs using Django and Flask
- Deployed applications on AWS with Docker and Kubernetes
- Managed PostgreSQL databases
- Implemented CI/CD pipelines using Jenkins
"""

SAMPLE_JD = """
Senior Python Developer - TechCorp Inc.

Requirements:
- 5+ years Python development experience
- Strong experience with Django or Flask web frameworks
- RESTful API design and development
- SQL databases (PostgreSQL, MySQL)
- Docker and containerization
- AWS cloud services (EC2, S3, Lambda)
- Git version control and CI/CD pipelines
- Unit testing and test-driven development
- Microservices architecture
- Communication and problem-solving skills

Nice to have:
- Redis and caching
- Kubernetes
- GraphQL
- Terraform
"""


# ═══════════════════════════════════════════════════════════════════════════════
# Text Processor Tests
# ═══════════════════════════════════════════════════════════════════════════════

class TestTextProcessor:
    """Tests for the text_processor module."""

    def test_clean_text_basic(self):
        result = clean_text("  Hello   World!  ")
        assert "hello" in result
        assert "world" in result

    def test_clean_text_removes_urls(self):
        result = clean_text("Visit https://example.com for more info")
        assert "https" not in result
        assert "example.com" not in result

    def test_clean_text_removes_emails(self):
        result = clean_text("Contact us at test@example.com today")
        assert "test@example.com" not in result

    def test_clean_text_empty(self):
        assert clean_text("") == ""
        assert clean_text(None) == ""

    def test_remove_stop_words(self):
        result = remove_stop_words("this is a test of the system")
        assert "this" not in result.split()
        assert "test" in result.split()
        assert "system" in result.split()

    def test_remove_stop_words_empty(self):
        assert remove_stop_words("") == ""

    def test_tokenize(self):
        result = tokenize("hello world python")
        assert result == ["hello", "world", "python"]

    def test_tokenize_empty(self):
        assert tokenize("") == []

    def test_preprocess_text(self):
        result = preprocess_text("This is a TEST string with URLs https://example.com")
        assert "this" not in result.split()  # stop word removed
        assert "https" not in result

    def test_extract_sentences(self):
        result = extract_sentences("Hello world. How are you? I am fine!")
        assert len(result) == 3

    def test_extract_sentences_empty(self):
        assert extract_sentences("") == []

    def test_get_word_frequency(self):
        result = get_word_frequency("python java python machine learning python")
        assert result["python"] == 3
        assert result["java"] == 1


# ═══════════════════════════════════════════════════════════════════════════════
# Matcher Tests
# ═══════════════════════════════════════════════════════════════════════════════

class TestMatcher:
    """Tests for the matcher module."""

    def test_match_score_range(self):
        score = calculate_match_score(SAMPLE_RESUME, SAMPLE_JD)
        assert 0 <= score <= 100

    def test_match_score_identical(self):
        """Identical texts should have a very high score."""
        score = calculate_match_score(SAMPLE_JD, SAMPLE_JD)
        assert score >= 90

    def test_match_score_different(self):
        """Completely unrelated texts should have a low score."""
        resume = "I love cooking pasta and baking bread for my family every weekend."
        jd = "Looking for a senior Python developer with AWS experience."
        score = calculate_match_score(resume, jd)
        assert score < 30

    def test_match_score_empty_raises(self):
        """Empty inputs should raise ValueError."""
        import pytest
        with pytest.raises(ValueError):
            calculate_match_score("", SAMPLE_JD)
        with pytest.raises(ValueError):
            calculate_match_score(SAMPLE_RESUME, "")

    def test_match_score_not_hardcoded(self):
        """Score should change with different inputs."""
        score1 = calculate_match_score(SAMPLE_RESUME, SAMPLE_JD)
        score2 = calculate_match_score(
            "I am a chef with 10 years of experience in Italian cuisine",
            SAMPLE_JD,
        )
        assert score1 != score2

    def test_top_matching_terms(self):
        terms = get_top_matching_terms(SAMPLE_RESUME, SAMPLE_JD, top_n=10)
        assert isinstance(terms, list)
        assert len(terms) <= 10
        if terms:
            assert isinstance(terms[0], tuple)
            assert len(terms[0]) == 2

    def test_detailed_analysis(self):
        result = get_detailed_analysis(SAMPLE_RESUME, SAMPLE_JD)
        assert "score" in result
        assert "top_terms" in result
        assert "jd_coverage" in result
        assert "common_term_count" in result


# ═══════════════════════════════════════════════════════════════════════════════
# Skills Extractor Tests
# ═══════════════════════════════════════════════════════════════════════════════

class TestSkillsExtractor:
    """Tests for the skills_extractor module."""

    def test_extract_skills_finds_python(self):
        result = extract_skills("I am proficient in Python and JavaScript")
        flat = get_flat_skills("I am proficient in Python and JavaScript")
        assert "python" in flat
        assert "javascript" in flat

    def test_extract_skills_categorized(self):
        result = extract_skills("Experience with Python, Django, PostgreSQL, Docker, and AWS")
        assert "Programming Languages" in result
        assert "python" in result["Programming Languages"]
        assert "Databases" in result
        assert "postgresql" in result["Databases"]

    def test_extract_skills_empty(self):
        result = extract_skills("")
        assert result == {}

    def test_compare_skills(self):
        result = compare_skills(SAMPLE_RESUME, SAMPLE_JD)
        assert "matching_skills" in result
        assert "missing_skills" in result
        assert "matching_count" in result
        assert "missing_count" in result
        assert "skill_match_percentage" in result
        assert result["matching_count"] >= 0
        assert result["skill_match_percentage"] >= 0

    def test_compare_skills_matching(self):
        """Known skills in both should appear as matching."""
        result = compare_skills(SAMPLE_RESUME, SAMPLE_JD)
        matching_flat = set()
        for skills in result["matching_skills"].values():
            matching_flat.update(skills)
        # Python is in both resume and JD
        assert "python" in matching_flat

    def test_compare_skills_missing(self):
        """Skills in JD but not resume should appear as missing."""
        resume = "I know Python and Git"
        jd = "Requires Python, Docker, Kubernetes, and AWS"
        result = compare_skills(resume, jd)
        missing_flat = set()
        for skills in result["missing_skills"].values():
            missing_flat.update(skills)
        assert "docker" in missing_flat
        assert "kubernetes" in missing_flat

    def test_skill_match_percentage(self):
        result = compare_skills(SAMPLE_RESUME, SAMPLE_JD)
        assert 0 <= result["skill_match_percentage"] <= 100


# ═══════════════════════════════════════════════════════════════════════════════
# Recommendations Tests
# ═══════════════════════════════════════════════════════════════════════════════

class TestRecommendations:
    """Tests for the recommendations module."""

    def test_generate_recommendations_structure(self):
        missing = {"Cloud & DevOps": ["docker", "kubernetes"]}
        matching = {"Programming Languages": ["python", "javascript"]}
        result = generate_recommendations(missing, matching, 55.0)

        assert "overall_assessment" in result
        assert "priority_skills" in result
        assert "skill_recommendations" in result
        assert "action_plan" in result
        assert "estimated_time" in result

    def test_high_score_assessment(self):
        result = generate_recommendations({}, {"Programming Languages": ["python"]}, 85.0)
        assert "excellent" in result["overall_assessment"].lower() or \
               "align" in result["overall_assessment"].lower()

    def test_low_score_assessment(self):
        missing = {"Cloud & DevOps": ["docker", "aws", "kubernetes"]}
        result = generate_recommendations(missing, {}, 15.0)
        assert "low" in result["overall_assessment"].lower()

    def test_recommendations_have_suggestions(self):
        missing = {"Programming Languages": ["python"], "Cloud & DevOps": ["docker"]}
        result = generate_recommendations(missing, {}, 40.0)
        recs = result["skill_recommendations"]
        assert len(recs) >= 2
        for rec in recs:
            assert "skill" in rec
            assert "priority" in rec
            assert "suggestion" in rec
            assert "time_estimate" in rec

    def test_action_plan_not_empty(self):
        missing = {"Programming Languages": ["python"]}
        matching = {"Databases": ["postgresql"]}
        result = generate_recommendations(missing, matching, 50.0)
        assert len(result["action_plan"]) > 0

    def test_no_missing_skills(self):
        """When no skills are missing, recommendations should be minimal."""
        result = generate_recommendations({}, {"Programming Languages": ["python"]}, 90.0)
        assert result["missing_skill_count"] == 0
        assert result["matching_skill_count"] == 1
