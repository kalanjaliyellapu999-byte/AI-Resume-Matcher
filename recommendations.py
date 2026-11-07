"""
Recommendations Module
======================
Generates personalized skill improvement recommendations and
actionable suggestions based on the skill gap analysis.
"""

from typing import Dict, List


# ─── Learning Resource Suggestions ──────────────────────────────────────────────

LEARNING_RESOURCES: Dict[str, Dict[str, str]] = {
    "python": {
        "priority": "High",
        "suggestion": "Complete a Python course on platforms like Coursera, Udemy, or freeCodeCamp.",
        "time_estimate": "4-6 weeks",
    },
    "java": {
        "priority": "High",
        "suggestion": "Take a Java programming course and build projects using Spring Boot.",
        "time_estimate": "6-8 weeks",
    },
    "javascript": {
        "priority": "High",
        "suggestion": "Learn modern JavaScript (ES6+) through freeCodeCamp or The Odin Project.",
        "time_estimate": "4-6 weeks",
    },
    "typescript": {
        "priority": "Medium",
        "suggestion": "Learn TypeScript after JavaScript fundamentals. Official docs are excellent.",
        "time_estimate": "2-3 weeks",
    },
    "react": {
        "priority": "High",
        "suggestion": "Build projects with React following the official tutorial and build a portfolio app.",
        "time_estimate": "4-6 weeks",
    },
    "angular": {
        "priority": "Medium",
        "suggestion": "Complete the Angular Tour of Heroes tutorial and build a CRUD application.",
        "time_estimate": "4-6 weeks",
    },
    "django": {
        "priority": "Medium",
        "suggestion": "Follow the Django official tutorial and build a full-stack web application.",
        "time_estimate": "3-4 weeks",
    },
    "flask": {
        "priority": "Medium",
        "suggestion": "Build REST APIs with Flask. Miguel Grinberg's Flask Mega-Tutorial is recommended.",
        "time_estimate": "2-3 weeks",
    },
    "fastapi": {
        "priority": "Medium",
        "suggestion": "Learn FastAPI for modern Python API development. Official docs are comprehensive.",
        "time_estimate": "2-3 weeks",
    },
    "sql": {
        "priority": "High",
        "suggestion": "Practice SQL on LeetCode, HackerRank, or Mode Analytics SQL tutorial.",
        "time_estimate": "2-4 weeks",
    },
    "mysql": {
        "priority": "Medium",
        "suggestion": "Set up MySQL locally and practice queries. Try MySQL Workbench for GUI access.",
        "time_estimate": "2-3 weeks",
    },
    "postgresql": {
        "priority": "Medium",
        "suggestion": "Learn PostgreSQL through official documentation and hands-on practice.",
        "time_estimate": "2-3 weeks",
    },
    "mongodb": {
        "priority": "Medium",
        "suggestion": "Complete MongoDB University free courses and build a NoSQL application.",
        "time_estimate": "2-3 weeks",
    },
    "docker": {
        "priority": "High",
        "suggestion": "Learn Docker fundamentals: images, containers, volumes, and Docker Compose.",
        "time_estimate": "2-3 weeks",
    },
    "kubernetes": {
        "priority": "Medium",
        "suggestion": "Learn Kubernetes after Docker. Try Minikube for local practice.",
        "time_estimate": "4-6 weeks",
    },
    "aws": {
        "priority": "High",
        "suggestion": "Start with AWS Cloud Practitioner certification, then Solutions Architect Associate.",
        "time_estimate": "6-8 weeks",
    },
    "azure": {
        "priority": "Medium",
        "suggestion": "Pursue Azure Fundamentals (AZ-900) certification through Microsoft Learn.",
        "time_estimate": "4-6 weeks",
    },
    "gcp": {
        "priority": "Medium",
        "suggestion": "Complete Google Cloud Skills Boost labs and pursue Associate Cloud Engineer.",
        "time_estimate": "6-8 weeks",
    },
    "git": {
        "priority": "High",
        "suggestion": "Master Git through interactive tutorials like learngitbranching.js.org.",
        "time_estimate": "1-2 weeks",
    },
    "machine learning": {
        "priority": "High",
        "suggestion": "Take Andrew Ng's Machine Learning course on Coursera. Implement algorithms from scratch.",
        "time_estimate": "8-12 weeks",
    },
    "deep learning": {
        "priority": "High",
        "suggestion": "Complete the Deep Learning Specialization on Coursera by Andrew Ng.",
        "time_estimate": "8-12 weeks",
    },
    "tensorflow": {
        "priority": "Medium",
        "suggestion": "Follow TensorFlow official tutorials and build image classification projects.",
        "time_estimate": "4-6 weeks",
    },
    "pytorch": {
        "priority": "Medium",
        "suggestion": "Learn PyTorch through official tutorials and fast.ai practical deep learning course.",
        "time_estimate": "4-6 weeks",
    },
    "natural language processing": {
        "priority": "Medium",
        "suggestion": "Study NLP fundamentals with Hugging Face course and Stanford CS224N lectures.",
        "time_estimate": "6-8 weeks",
    },
    "computer vision": {
        "priority": "Medium",
        "suggestion": "Learn OpenCV and build projects like object detection and image segmentation.",
        "time_estimate": "6-8 weeks",
    },
    "agile": {
        "priority": "Medium",
        "suggestion": "Learn Agile and Scrum methodologies. Consider a Scrum Master certification.",
        "time_estimate": "2-3 weeks",
    },
    "ci/cd": {
        "priority": "Medium",
        "suggestion": "Set up CI/CD pipelines using GitHub Actions or Jenkins for your projects.",
        "time_estimate": "2-3 weeks",
    },
    "microservices": {
        "priority": "Medium",
        "suggestion": "Study microservices architecture patterns and build a multi-service application.",
        "time_estimate": "4-6 weeks",
    },
    "graphql": {
        "priority": "Low",
        "suggestion": "Learn GraphQL fundamentals through How to GraphQL tutorial.",
        "time_estimate": "1-2 weeks",
    },
    "linux": {
        "priority": "Medium",
        "suggestion": "Practice Linux commands daily. Try Linux administration on a virtual machine.",
        "time_estimate": "3-4 weeks",
    },
    "terraform": {
        "priority": "Medium",
        "suggestion": "Learn Infrastructure as Code with Terraform through HashiCorp Learn.",
        "time_estimate": "3-4 weeks",
    },
    "data structures": {
        "priority": "High",
        "suggestion": "Practice data structures on LeetCode, solving problems daily.",
        "time_estimate": "6-8 weeks",
    },
    "algorithms": {
        "priority": "High",
        "suggestion": "Study algorithms through CLRS textbook and practice on competitive coding platforms.",
        "time_estimate": "6-8 weeks",
    },
    "system design": {
        "priority": "Medium",
        "suggestion": "Study system design through 'Designing Data-Intensive Applications' and mock interviews.",
        "time_estimate": "4-6 weeks",
    },
    "spark": {
        "priority": "Medium",
        "suggestion": "Learn Apache Spark for big data processing. Practice with PySpark.",
        "time_estimate": "4-6 weeks",
    },
    "kafka": {
        "priority": "Medium",
        "suggestion": "Learn Apache Kafka for event streaming. Build a producer-consumer application.",
        "time_estimate": "2-3 weeks",
    },
    "redis": {
        "priority": "Low",
        "suggestion": "Learn Redis for caching and session management. Try Redis University.",
        "time_estimate": "1-2 weeks",
    },
    "elasticsearch": {
        "priority": "Low",
        "suggestion": "Learn Elasticsearch for full-text search. Build a search engine project.",
        "time_estimate": "2-3 weeks",
    },
    "flutter": {
        "priority": "Medium",
        "suggestion": "Complete Flutter official codelabs and build a cross-platform mobile app.",
        "time_estimate": "4-6 weeks",
    },
    "react native": {
        "priority": "Medium",
        "suggestion": "Learn React Native after React basics. Build and deploy a mobile app.",
        "time_estimate": "4-6 weeks",
    },
}

# Priority ordering for sorting
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def generate_recommendations(
    missing_skills: Dict[str, list],
    matching_skills: Dict[str, list],
    match_score: float,
) -> Dict:
    """
    Generate personalized recommendations based on skill gap analysis.

    Args:
        missing_skills: Dict of category -> list of missing skills.
        matching_skills: Dict of category -> list of matching skills.
        match_score: Overall resume match score (0-100).

    Returns:
        Dictionary with:
            - overall_assessment: Text summary of the candidate's standing.
            - priority_skills: List of high-priority skills to learn.
            - skill_recommendations: Detailed per-skill recommendations.
            - action_plan: Ordered list of actionable steps.
            - estimated_time: Total estimated learning time.
    """
    # Flatten missing skills
    all_missing = []
    for skills_list in missing_skills.values():
        all_missing.extend(skills_list)

    # Flatten matching skills
    all_matching = []
    for skills_list in matching_skills.values():
        all_matching.extend(skills_list)

    # ── Overall Assessment ───────────────────────────────────────────────────
    if match_score >= 80:
        assessment = (
            "Excellent match! Your resume aligns very well with this job description. "
            "Focus on highlighting your relevant experience and fine-tuning keywords."
        )
    elif match_score >= 60:
        assessment = (
            "Good match. Your resume covers many of the required areas, but there are "
            "some gaps that could strengthen your application. Consider addressing the "
            "missing skills below."
        )
    elif match_score >= 40:
        assessment = (
            "Moderate match. Your resume has relevant experience, but there are significant "
            "skill gaps. Prioritize learning the high-priority skills listed below to "
            "improve your competitiveness."
        )
    elif match_score >= 20:
        assessment = (
            "Below average match. There is a notable gap between your current profile and "
            "the job requirements. A focused learning plan is recommended before applying."
        )
    else:
        assessment = (
            "Low match. Your current resume does not closely align with this job description. "
            "Consider whether this role matches your career goals, or invest in substantial "
            "upskilling in the areas listed below."
        )

    # ── Per-skill Recommendations ────────────────────────────────────────────
    skill_recommendations = []
    for skill in all_missing:
        if skill in LEARNING_RESOURCES:
            info = LEARNING_RESOURCES[skill]
            skill_recommendations.append({
                "skill": skill.title(),
                "priority": info["priority"],
                "suggestion": info["suggestion"],
                "time_estimate": info["time_estimate"],
            })
        else:
            skill_recommendations.append({
                "skill": skill.title(),
                "priority": "Medium",
                "suggestion": f"Learn {skill.title()} through online courses, official documentation, and hands-on projects.",
                "time_estimate": "2-4 weeks",
            })

    # Sort by priority
    skill_recommendations.sort(key=lambda x: PRIORITY_ORDER.get(x["priority"], 1))

    # ── Priority Skills ──────────────────────────────────────────────────────
    priority_skills = [
        rec["skill"] for rec in skill_recommendations
        if rec["priority"] == "High"
    ]

    # ── Action Plan ──────────────────────────────────────────────────────────
    action_plan = _build_action_plan(
        all_missing, all_matching, match_score, skill_recommendations
    )

    # ── Time Estimate ────────────────────────────────────────────────────────
    total_weeks = 0
    for rec in skill_recommendations:
        time_str = rec.get("time_estimate", "2-4 weeks")
        # Parse the upper bound of the time estimate
        parts = time_str.replace("weeks", "").replace("week", "").strip().split("-")
        try:
            total_weeks += int(parts[-1].strip())
        except ValueError:
            total_weeks += 4  # default

    if total_weeks <= 4:
        estimated_time = f"About {total_weeks} weeks of focused learning"
    elif total_weeks <= 12:
        estimated_time = f"About {total_weeks // 4}-{(total_weeks + 3) // 4} months of consistent learning"
    else:
        months = total_weeks // 4
        estimated_time = f"About {months} months of dedicated study (can be reduced by focusing on high-priority skills first)"

    return {
        "overall_assessment": assessment,
        "priority_skills": priority_skills,
        "skill_recommendations": skill_recommendations,
        "action_plan": action_plan,
        "estimated_time": estimated_time,
        "matching_skill_count": len(all_matching),
        "missing_skill_count": len(all_missing),
    }


def _build_action_plan(
    missing: List[str],
    matching: List[str],
    score: float,
    recommendations: List[Dict],
) -> List[str]:
    """
    Build an ordered action plan based on the analysis.

    Returns:
        List of action step strings.
    """
    plan = []

    # Step 1: Resume optimization
    if matching:
        plan.append(
            f"Optimize your resume by prominently featuring your {len(matching)} matching "
            f"skills: {', '.join(s.title() for s in matching[:5])}{'...' if len(matching) > 5 else ''}."
        )

    # Step 2: Quick wins
    quick_wins = [r for r in recommendations if r["time_estimate"].startswith("1")]
    if quick_wins:
        skills_str = ", ".join(r["skill"] for r in quick_wins[:3])
        plan.append(
            f"Start with quick wins (1-2 weeks each): {skills_str}."
        )

    # Step 3: High priority skills
    high_priority = [r for r in recommendations if r["priority"] == "High"]
    if high_priority:
        skills_str = ", ".join(r["skill"] for r in high_priority[:5])
        plan.append(
            f"Focus on high-priority skills next: {skills_str}."
        )

    # Step 4: Medium priority
    medium_priority = [r for r in recommendations if r["priority"] == "Medium"]
    if medium_priority:
        skills_str = ", ".join(r["skill"] for r in medium_priority[:5])
        plan.append(
            f"Then work on medium-priority skills: {skills_str}."
        )

    # Step 5: Projects
    if missing:
        plan.append(
            "Build portfolio projects that demonstrate your newly acquired skills."
        )

    # Step 6: Keywords
    if score < 60:
        plan.append(
            "Tailor your resume to include keywords from the job description "
            "to improve ATS (Applicant Tracking System) compatibility."
        )

    # Step 7: General advice
    plan.append(
        "Keep your GitHub profile active and contribute to open-source projects to "
        "showcase practical experience."
    )

    return plan
