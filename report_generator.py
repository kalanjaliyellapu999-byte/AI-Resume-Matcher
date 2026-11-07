"""
Report Generator Module
=======================
Generates downloadable PDF analysis reports using fpdf2.
"""

from fpdf import FPDF
from typing import Dict, List
import os
import tempfile
from datetime import datetime


class ReportPDF(FPDF):
    """Custom PDF class with header and footer."""

    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(25, 42, 86)  # Dark navy
        self.cell(0, 10, "AI Resume Matcher - Analysis Report", ln=True, align="C")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(120, 120, 120)
        self.cell(
            0, 6,
            f"Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}",
            ln=True, align="C",
        )
        self.ln(4)
        # Horizontal line
        self.set_draw_color(25, 42, 86)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), self.w - 10, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(160, 160, 160)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        """Add a section title with styling."""
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(25, 42, 86)
        self.cell(0, 10, title, ln=True)
        self.set_draw_color(70, 130, 220)
        self.set_line_width(0.3)
        self.line(10, self.get_y(), 80, self.get_y())
        self.ln(4)

    def body_text(self, text: str):
        """Add body text."""
        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def skill_tag(self, skill: str, color: tuple = (70, 130, 220)):
        """Add a colored skill tag inline."""
        self.set_font("Helvetica", "", 9)
        width = self.get_string_width(skill) + 6
        x = self.get_x()
        y = self.get_y()

        # Check if we need to wrap to next line
        if x + width > self.w - 10:
            self.ln(8)
            x = self.get_x()
            y = self.get_y()

        self.set_fill_color(*color)
        self.set_text_color(255, 255, 255)
        self.set_xy(x, y)
        self.cell(width, 7, skill, fill=True, ln=0)
        self.set_x(x + width + 3)


def _safe_text(text: str) -> str:
    """Encode text safely for FPDF (latin-1 compatible)."""
    return text.encode("latin-1", errors="replace").decode("latin-1")


def generate_report(
    match_score: float,
    skill_comparison: Dict,
    recommendations: Dict,
    detailed_analysis: Dict = None,
) -> bytes:
    """
    Generate a PDF analysis report.

    Args:
        match_score: Resume match score (0-100).
        skill_comparison: Output from skills_extractor.compare_skills().
        recommendations: Output from recommendations.generate_recommendations().
        detailed_analysis: Optional output from matcher.get_detailed_analysis().

    Returns:
        PDF file content as bytes.
    """
    pdf = ReportPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # ── 1. Match Score Summary ───────────────────────────────────────────────
    pdf.section_title("1. Resume Match Score")

    score_color = (
        (46, 160, 67) if match_score >= 70
        else (227, 171, 36) if match_score >= 40
        else (218, 54, 51)
    )

    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*score_color)
    pdf.cell(0, 15, f"{match_score}%", ln=True, align="C")

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(
        0, 8,
        "This score represents textual similarity between your resume and the job description.",
        ln=True, align="C",
    )
    pdf.ln(4)

    # Score interpretation
    pdf.body_text(_safe_text(recommendations.get("overall_assessment", "")))

    # ── 2. Detailed Metrics (if available) ───────────────────────────────────
    if detailed_analysis:
        pdf.section_title("2. Detailed Metrics")
        metrics_text = (
            f"- JD Keyword Coverage: {detailed_analysis.get('jd_coverage', 0)}%\n"
            f"- Common Terms Found: {detailed_analysis.get('common_term_count', 0)}\n"
            f"- Total JD Terms: {detailed_analysis.get('jd_term_count', 0)}\n"
            f"- Total Resume Terms: {detailed_analysis.get('resume_term_count', 0)}"
        )
        pdf.body_text(metrics_text)

    # ── 3. Skill Match Overview ──────────────────────────────────────────────
    section_num = 3 if detailed_analysis else 2
    pdf.section_title(f"{section_num}. Skill Match Overview")

    matching_count = skill_comparison.get("matching_count", 0)
    missing_count = skill_comparison.get("missing_count", 0)
    total_jd = skill_comparison.get("total_jd_skills", 0)
    skill_pct = skill_comparison.get("skill_match_percentage", 0)

    pdf.body_text(
        f"Skills found in both resume and job description: {matching_count}\n"
        f"Skills required but missing from resume: {missing_count}\n"
        f"Total skills identified in job description: {total_jd}\n"
        f"Skill match rate: {skill_pct}%"
    )

    # ── 4. Matching Skills ───────────────────────────────────────────────────
    section_num += 1
    pdf.section_title(f"{section_num}. Matching Skills")

    matching_skills = skill_comparison.get("matching_skills", {})
    if matching_skills:
        for category, skills in matching_skills.items():
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 8, _safe_text(category), ln=True)
            pdf.set_x(15)
            for skill in skills:
                pdf.skill_tag(_safe_text(skill.title()), color=(46, 160, 67))
            pdf.ln(10)
    else:
        pdf.body_text("No matching skills found.")

    # ── 5. Missing Skills ────────────────────────────────────────────────────
    section_num += 1
    pdf.section_title(f"{section_num}. Missing Skills (Skill Gaps)")

    missing_skills = skill_comparison.get("missing_skills", {})
    if missing_skills:
        for category, skills in missing_skills.items():
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 8, _safe_text(category), ln=True)
            pdf.set_x(15)
            for skill in skills:
                pdf.skill_tag(_safe_text(skill.title()), color=(218, 54, 51))
            pdf.ln(10)
    else:
        pdf.body_text("No missing skills identified. Great job!")

    # ── 6. Recommendations ───────────────────────────────────────────────────
    section_num += 1
    pdf.section_title(f"{section_num}. Skill Improvement Recommendations")

    skill_recs = recommendations.get("skill_recommendations", [])
    if skill_recs:
        for i, rec in enumerate(skill_recs, 1):
            pdf.set_font("Helvetica", "B", 10)
            pdf.set_text_color(25, 42, 86)
            priority_emoji = {"High": "[!]", "Medium": "[~]", "Low": "[-]"}.get(rec["priority"], "[-]")
            pdf.cell(
                0, 7,
                _safe_text(f"{i}. {rec['skill']} {priority_emoji} Priority: {rec['priority']}"),
                ln=True,
            )
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(80, 80, 80)
            pdf.set_x(15)
            pdf.multi_cell(0, 5, _safe_text(f"   {rec['suggestion']}"))
            pdf.set_x(15)
            pdf.set_font("Helvetica", "I", 9)
            pdf.cell(0, 5, _safe_text(f"   Estimated time: {rec['time_estimate']}"), ln=True)
            pdf.ln(2)
    else:
        pdf.body_text("No specific recommendations at this time.")

    # ── 7. Action Plan ───────────────────────────────────────────────────────
    section_num += 1
    pdf.section_title(f"{section_num}. Action Plan")

    action_plan = recommendations.get("action_plan", [])
    for i, step in enumerate(action_plan, 1):
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 6, _safe_text(f"Step {i}: {step}"))
        pdf.ln(2)

    # Estimated time
    estimated = recommendations.get("estimated_time", "")
    if estimated:
        pdf.ln(2)
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(25, 42, 86)
        pdf.cell(0, 8, _safe_text(f"Total Estimated Learning Time: {estimated}"), ln=True)

    # ── Disclaimer ───────────────────────────────────────────────────────────
    pdf.ln(8)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(150, 150, 150)
    pdf.multi_cell(
        0, 5,
        "Disclaimer: This analysis is based on textual similarity and keyword matching. "
        "The match score reflects content overlap, not the probability of being hired. "
        "Use this report as a guide to improve your resume and identify areas for growth.",
    )

    return pdf.output()
