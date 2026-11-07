"""
Tests for the report_generator module.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from report_generator import generate_report


class TestReportGenerator:
    """Tests for the report_generator module."""

    def test_generate_report_returns_bytes(self):
        """Report should return PDF bytes."""
        skill_comparison = {
            "matching_skills": {"Programming Languages": ["python"]},
            "missing_skills": {"Cloud & DevOps": ["docker"]},
            "matching_count": 1,
            "missing_count": 1,
            "total_jd_skills": 2,
            "skill_match_percentage": 50.0,
        }
        recs = {
            "overall_assessment": "Good match.",
            "priority_skills": ["Docker"],
            "skill_recommendations": [
                {
                    "skill": "Docker",
                    "priority": "High",
                    "suggestion": "Learn Docker.",
                    "time_estimate": "2-3 weeks",
                }
            ],
            "action_plan": ["Learn Docker first."],
            "estimated_time": "About 3 weeks",
            "matching_skill_count": 1,
            "missing_skill_count": 1,
        }
        result = generate_report(
            match_score=55.0,
            skill_comparison=skill_comparison,
            recommendations=recs,
        )
        assert isinstance(result, (bytes, bytearray))
        assert len(result) > 100
        # PDF magic bytes
        assert bytes(result)[:5] == b"%PDF-"

    def test_generate_report_with_detailed_analysis(self):
        """Report with detailed analysis should still produce valid PDF."""
        skill_comparison = {
            "matching_skills": {},
            "missing_skills": {},
            "matching_count": 0,
            "missing_count": 0,
            "total_jd_skills": 0,
            "skill_match_percentage": 0,
        }
        recs = {
            "overall_assessment": "Low match.",
            "priority_skills": [],
            "skill_recommendations": [],
            "action_plan": ["Improve skills."],
            "estimated_time": "N/A",
            "matching_skill_count": 0,
            "missing_skill_count": 0,
        }
        detailed = {
            "jd_coverage": 10.0,
            "common_term_count": 5,
            "jd_term_count": 50,
            "resume_term_count": 30,
        }
        result = generate_report(
            match_score=10.0,
            skill_comparison=skill_comparison,
            recommendations=recs,
            detailed_analysis=detailed,
        )
        assert bytes(result)[:5] == b"%PDF-"
