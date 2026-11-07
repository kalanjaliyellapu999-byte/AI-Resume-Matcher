"""
Skills Extractor Module
=======================
Extracts and categorizes technical skills from resumes and job descriptions.
Identifies matching and missing skills for gap analysis.
"""

import re
from typing import Dict, List, Set, Tuple

from text_processor import clean_text


# ─── Comprehensive Skill Database ───────────────────────────────────────────────
# Each category maps to a set of known skill names (lowercase).

SKILL_DATABASE: Dict[str, Set[str]] = {
    "Programming Languages": {
        "python", "java", "javascript", "typescript", "c", "c++", "c#",
        "ruby", "go", "golang", "rust", "swift", "kotlin", "scala",
        "php", "perl", "r", "matlab", "dart", "lua", "haskell",
        "elixir", "clojure", "groovy", "objective-c", "assembly",
        "visual basic", "vb.net", "fortran", "cobol", "julia",
        "shell", "bash", "powershell", "sql", "pl/sql", "t-sql",
    },
    "Web Frameworks": {
        "react", "reactjs", "react.js", "angular", "angularjs", "vue",
        "vuejs", "vue.js", "django", "flask", "fastapi", "express",
        "expressjs", "express.js", "spring", "spring boot", "springboot",
        "rails", "ruby on rails", "laravel", "asp.net", ".net",
        "dotnet", "next.js", "nextjs", "nuxt.js", "nuxtjs", "svelte",
        "gatsby", "ember", "backbone", "jquery", "bootstrap",
        "tailwind", "tailwindcss", "material ui", "chakra ui",
        "streamlit", "gradio",
    },
    "Databases": {
        "mysql", "postgresql", "postgres", "mongodb", "redis", "sqlite",
        "oracle", "sql server", "mssql", "cassandra", "dynamodb",
        "couchdb", "neo4j", "mariadb", "elasticsearch", "influxdb",
        "firebase", "firestore", "supabase", "cockroachdb", "snowflake",
        "bigquery", "redshift", "hbase", "memcached",
    },
    "Cloud & DevOps": {
        "aws", "amazon web services", "azure", "gcp",
        "google cloud", "google cloud platform", "docker", "kubernetes",
        "k8s", "terraform", "ansible", "jenkins", "circleci",
        "github actions", "gitlab ci", "travis ci", "cloudformation",
        "helm", "prometheus", "grafana", "datadog", "splunk",
        "nginx", "apache", "heroku", "vercel", "netlify",
        "digitalocean", "linode", "vagrant", "puppet", "chef",
        "argo cd", "argocd", "istio", "consul",
    },
    "Data Science & ML": {
        "machine learning", "deep learning", "artificial intelligence",
        "neural network", "neural networks", "natural language processing",
        "nlp", "computer vision", "reinforcement learning",
        "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn",
        "xgboost", "lightgbm", "catboost", "pandas", "numpy", "scipy",
        "matplotlib", "seaborn", "plotly", "tableau", "power bi",
        "jupyter", "jupyter notebook", "colab", "hugging face",
        "huggingface", "transformers", "bert", "gpt", "llm",
        "large language model", "generative ai", "gen ai",
        "random forest", "svm", "support vector machine",
        "logistic regression", "linear regression", "clustering",
        "classification", "regression", "feature engineering",
        "model deployment", "mlops", "mlflow", "kubeflow",
        "data pipeline", "data pipelines", "etl", "airflow",
        "apache spark", "spark", "hadoop", "hive", "kafka",
        "data warehouse", "data lake", "data modeling",
        "statistical analysis", "statistics", "a/b testing",
        "ab testing", "hypothesis testing", "time series",
        "recommendation system", "recommendation systems",
        "opencv", "yolo", "object detection", "image classification",
        "langchain", "rag", "retrieval augmented generation",
        "stable diffusion", "openai", "chatgpt",
    },
    "Mobile Development": {
        "android", "ios", "react native", "flutter", "xamarin",
        "ionic", "cordova", "swiftui", "jetpack compose",
        "kotlin multiplatform", "expo",
    },
    "Tools & Platforms": {
        "git", "github", "gitlab", "bitbucket", "jira", "confluence",
        "slack", "trello", "asana", "notion", "figma", "sketch",
        "postman", "swagger", "linux", "unix", "windows",
        "macos", "vim", "vs code", "vscode", "intellij",
        "eclipse", "pycharm", "webpack", "vite", "babel",
        "npm", "yarn", "pip", "conda", "poetry",
        "docker compose", "makefile", "cmake",
    },
    "Soft Skills & Methodologies": {
        "agile", "scrum", "kanban", "waterfall", "devops", "ci/cd",
        "cicd", "continuous integration", "continuous deployment",
        "test driven development", "tdd", "pair programming",
        "code review", "microservices", "rest", "restful", "graphql",
        "grpc", "soap", "api design", "system design",
        "object oriented programming", "oop", "functional programming",
        "design patterns", "solid principles", "clean code",
        "data structures", "algorithms", "problem solving",
        "communication", "leadership", "teamwork", "mentoring",
        "project management", "time management",
    },
    "Cybersecurity": {
        "cybersecurity", "penetration testing", "ethical hacking",
        "owasp", "siem", "soc", "firewall", "ids", "ips",
        "encryption", "ssl", "tls", "oauth", "jwt", "saml",
        "sso", "mfa", "two factor authentication",
        "vulnerability assessment", "incident response",
        "security audit", "compliance", "gdpr", "hipaa",
    },
}

# Flatten all skills for fast lookup
ALL_SKILLS: Set[str] = set()
for category_skills in SKILL_DATABASE.values():
    ALL_SKILLS.update(category_skills)


def _normalize(text: str) -> str:
    """Lowercase and strip a text string."""
    return text.lower().strip()


def extract_skills(text: str) -> Dict[str, List[str]]:
    """
    Extract technical skills from text and categorize them.

    Uses a dictionary-based approach: searches for known skill tokens
    within the cleaned text.

    Args:
        text: Raw text (resume or job description).

    Returns:
        Dictionary mapping category names to lists of found skills.
    """
    if not text:
        return {}

    cleaned = clean_text(text)

    found_skills: Dict[str, List[str]] = {}

    for category, skills in SKILL_DATABASE.items():
        matched = []
        for skill in sorted(skills, key=len, reverse=True):
            # Build a regex pattern that matches the skill as a whole word/phrase
            pattern = r"(?<![a-zA-Z0-9\-])" + re.escape(skill) + r"(?![a-zA-Z0-9\-])"
            if re.search(pattern, cleaned):
                # Avoid duplicate sub-matches (e.g., "react" inside "react native")
                already_matched = any(skill in m and skill != m for m in matched)
                if not already_matched:
                    matched.append(skill)

        if matched:
            found_skills[category] = sorted(matched)

    return found_skills


def get_flat_skills(text: str) -> Set[str]:
    """
    Extract all skills from text as a flat set (no categories).

    Args:
        text: Raw text.

    Returns:
        Set of skill names found in the text.
    """
    categorized = extract_skills(text)
    flat = set()
    for skills_list in categorized.values():
        flat.update(skills_list)
    return flat


def compare_skills(
    resume_text: str,
    job_description: str
) -> Dict[str, any]:
    """
    Compare skills found in a resume against those required in a job description.

    Args:
        resume_text: Raw resume text.
        job_description: Raw job description text.

    Returns:
        Dictionary with:
            - resume_skills: categorized skills from resume
            - jd_skills: categorized skills from JD
            - matching_skills: skills found in both
            - missing_skills: skills in JD but not in resume
            - extra_skills: skills in resume but not in JD
            - match_percentage: percentage of JD skills found in resume
    """
    resume_categorized = extract_skills(resume_text)
    jd_categorized = extract_skills(job_description)

    resume_flat = get_flat_skills(resume_text)
    jd_flat = get_flat_skills(job_description)

    matching = resume_flat & jd_flat
    missing = jd_flat - resume_flat
    extra = resume_flat - jd_flat

    # Categorize matching and missing skills
    matching_categorized: Dict[str, List[str]] = {}
    missing_categorized: Dict[str, List[str]] = {}

    for category, skills in SKILL_DATABASE.items():
        cat_matching = sorted(matching & skills)
        cat_missing = sorted(missing & skills)
        if cat_matching:
            matching_categorized[category] = cat_matching
        if cat_missing:
            missing_categorized[category] = cat_missing

    total_jd_skills = len(jd_flat)
    match_pct = round((len(matching) / total_jd_skills * 100) if total_jd_skills > 0 else 0, 2)

    return {
        "resume_skills": resume_categorized,
        "jd_skills": jd_categorized,
        "matching_skills": matching_categorized,
        "missing_skills": missing_categorized,
        "extra_skills": sorted(extra),
        "matching_count": len(matching),
        "missing_count": len(missing),
        "total_jd_skills": total_jd_skills,
        "skill_match_percentage": match_pct,
    }
