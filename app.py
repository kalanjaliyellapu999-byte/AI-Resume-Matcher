"""
AI Resume Matcher & Skill Gap Analyzer
=======================================
Main Streamlit application with a professional SaaS-style dashboard.

Run with:
    streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import tempfile
import os

from resume_parser import extract_text_from_bytes, validate_uploaded_file
from text_processor import preprocess_text
from matcher import calculate_match_score, get_detailed_analysis
from skills_extractor import compare_skills, extract_skills
from recommendations import generate_recommendations
from report_generator import generate_report


# ─── Page Configuration ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────────

st.markdown("""
<style>
    /* Global font & background */
    .main { background-color: #f7f9fc; }

    /* Hide default streamlit branding */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #192a56 0%, #273c75 100%);
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #ffffff !important;
    }

    /* Score card */
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(102,126,234,0.25);
        margin-bottom: 20px;
    }
    .score-card h1 {
        font-size: 3.5rem;
        margin: 0;
        font-weight: 800;
        color: white !important;
    }
    .score-card p {
        font-size: 1rem;
        margin-top: 5px;
        opacity: 0.9;
    }

    /* Metric cards */
    .metric-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 1px solid #e8ecf1;
    }
    .metric-card h2 {
        font-size: 2rem;
        color: #192a56;
        margin: 0;
    }
    .metric-card p {
        color: #636e72;
        font-size: 0.9rem;
        margin: 4px 0 0 0;
    }

    /* Skill tags */
    .skill-tag-match {
        display: inline-block;
        background: #00b894;
        color: white !important;
        padding: 5px 14px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .skill-tag-missing {
        display: inline-block;
        background: #d63031;
        color: white !important;
        padding: 5px 14px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .skill-tag-extra {
        display: inline-block;
        background: #0984e3;
        color: white !important;
        padding: 5px 14px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    /* Section headers */
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #192a56;
        margin-top: 30px;
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }

    /* Recommendation cards */
    .rec-card {
        background: #ffffff;
        border-left: 4px solid #667eea;
        border-radius: 8px;
        padding: 15px 20px;
        margin: 10px 0;
        box-shadow: 0 1px 6px rgba(0,0,0,0.04);
    }
    .rec-card-high {
        border-left-color: #d63031;
    }
    .rec-card-medium {
        border-left-color: #fdcb6e;
    }
    .rec-card-low {
        border-left-color: #00b894;
    }

    /* Upload area */
    [data-testid="stFileUploader"] {
        border: 2px dashed #667eea;
        border-radius: 12px;
        padding: 10px;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
        color: white;
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ─────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 📄 AI Resume Matcher")
    st.markdown("---")
    st.markdown("### Navigation")

    page = st.radio(
        "Go to",
        ["🏠 Dashboard", "📖 How It Works", "ℹ️ About"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("### Quick Tips")
    st.markdown("""
    - Upload your resume as **PDF**
    - Paste the **full** job description
    - Review matching & missing skills
    - Download your analysis report
    """)
    st.markdown("---")
    st.markdown(
        "<p style='font-size:0.8rem; opacity:0.6; text-align:center;'>"
        "Built with Python, Scikit-learn & Streamlit</p>",
        unsafe_allow_html=True,
    )


# ─── How It Works Page ──────────────────────────────────────────────────────────

if page == "📖 How It Works":
    st.markdown("# 📖 How It Works")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1️⃣ Upload & Extract")
        st.markdown(
            "Upload your resume in PDF format. The system extracts text "
            "using PyMuPDF for accurate content parsing."
        )
        st.markdown("### 2️⃣ Text Processing")
        st.markdown(
            "Both your resume and the job description undergo NLP preprocessing: "
            "cleaning, normalization, and stop-word removal."
        )
        st.markdown("### 3️⃣ TF-IDF Vectorization")
        st.markdown(
            "Documents are transformed into numerical vectors using "
            "Term Frequency–Inverse Document Frequency (TF-IDF), "
            "which captures word importance."
        )

    with col2:
        st.markdown("### 4️⃣ Cosine Similarity")
        st.markdown(
            "The match score is computed as the cosine similarity between "
            "the TF-IDF vectors of your resume and the job description."
        )
        st.markdown("### 5️⃣ Skill Extraction")
        st.markdown(
            "Technical skills are extracted from both documents using a "
            "comprehensive skill database covering 300+ technologies."
        )
        st.markdown("### 6️⃣ Gap Analysis & Recommendations")
        st.markdown(
            "Missing skills are identified and personalized learning "
            "recommendations with time estimates are generated."
        )

    st.info(
        "**Note:** The match score represents textual similarity, not the probability "
        "of getting hired. Use it as a guide to improve your resume."
    )


# ─── About Page ──────────────────────────────────────────────────────────────────

elif page == "ℹ️ About":
    st.markdown("# ℹ️ About This Project")
    st.markdown("---")
    st.markdown("""
    **AI Resume Matcher & Skill Gap Analyzer** is an AI-powered tool that helps
    job seekers evaluate how well their resumes match specific job descriptions.

    ### Technology Stack
    | Component | Technology |
    |-----------|-----------|
    | Backend | Python, Scikit-learn, Pandas, NumPy |
    | NLP | TF-IDF, Cosine Similarity, Text Preprocessing |
    | PDF Parsing | PyMuPDF (fitz) |
    | Frontend | Streamlit, Plotly |
    | Reports | FPDF2 |

    ### Features
    - ✅ PDF resume upload & text extraction
    - ✅ TF-IDF + Cosine Similarity matching
    - ✅ Technical skill extraction (300+ skills)
    - ✅ Skill gap analysis with categories
    - ✅ Personalized learning recommendations
    - ✅ Downloadable PDF reports
    - ✅ Interactive visualizations

    ### Privacy
    Your resume data is processed in-memory and is **never stored permanently**.
    All uploaded files are discarded after analysis.

    ---
    *Built as a portfolio project demonstrating Python, NLP, ML, and full-stack development.*
    """)


# ─── Dashboard Page (Main) ──────────────────────────────────────────────────────

elif page == "🏠 Dashboard":
    st.markdown(
        "<h1 style='text-align:center; color:#192a56;'>📄 AI Resume Matcher & Skill Gap Analyzer</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; color:#636e72; font-size:1.1rem;'>"
        "Upload your resume, paste a job description, and get instant AI-powered analysis.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # ── Input Section ────────────────────────────────────────────────────────
    col_upload, col_jd = st.columns(2, gap="large")

    with col_upload:
        st.markdown('<p class="section-header">📤 Upload Resume (PDF)</p>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Choose your resume",
            type=["pdf"],
            help="Upload a PDF resume (max 10 MB).",
            label_visibility="collapsed",
        )
        if uploaded_file:
            st.success(f"✅ Uploaded: **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")

    with col_jd:
        st.markdown('<p class="section-header">📋 Paste Job Description</p>', unsafe_allow_html=True)
        job_description = st.text_area(
            "Paste the job description here",
            height=250,
            placeholder="Paste the full job description here...\n\nInclude required skills, qualifications, responsibilities, etc.",
            label_visibility="collapsed",
        )

    # ── Analyze Button ───────────────────────────────────────────────────────
    st.markdown("")
    col_btn_l, col_btn_c, col_btn_r = st.columns([1, 2, 1])
    with col_btn_c:
        analyze_clicked = st.button("🔍  Analyze Resume", use_container_width=True)

    # ── Analysis Logic ───────────────────────────────────────────────────────
    if analyze_clicked:
        # Validate inputs
        errors = []
        if not uploaded_file:
            errors.append("Please upload your resume in PDF format.")
        else:
            is_valid, msg = validate_uploaded_file(uploaded_file)
            if not is_valid:
                errors.append(msg)

        if not job_description or not job_description.strip():
            errors.append("Please paste a job description.")

        if errors:
            for err in errors:
                st.error(f"❌ {err}")
        else:
            with st.spinner("🔄 Analyzing your resume... This may take a moment."):
                try:
                    # 1. Extract resume text
                    resume_bytes = uploaded_file.read()
                    resume_text = extract_text_from_bytes(resume_bytes)

                    # 2. Calculate match score & detailed analysis
                    match_score = calculate_match_score(resume_text, job_description)
                    detailed = get_detailed_analysis(resume_text, job_description)

                    # 3. Skill comparison
                    skill_comparison = compare_skills(resume_text, job_description)

                    # 4. Recommendations
                    recs = generate_recommendations(
                        missing_skills=skill_comparison["missing_skills"],
                        matching_skills=skill_comparison["matching_skills"],
                        match_score=match_score,
                    )

                    # 5. Generate PDF report
                    report_bytes = generate_report(
                        match_score=match_score,
                        skill_comparison=skill_comparison,
                        recommendations=recs,
                        detailed_analysis=detailed,
                    )

                    # Store results in session state
                    st.session_state["results"] = {
                        "resume_text": resume_text,
                        "match_score": match_score,
                        "detailed": detailed,
                        "skill_comparison": skill_comparison,
                        "recommendations": recs,
                        "report_bytes": report_bytes,
                    }

                except ValueError as e:
                    st.error(f"❌ {str(e)}")
                except Exception as e:
                    st.error(f"❌ An unexpected error occurred: {str(e)}")

    # ── Display Results ──────────────────────────────────────────────────────
    if "results" in st.session_state:
        results = st.session_state["results"]
        match_score = results["match_score"]
        detailed = results["detailed"]
        skill_comparison = results["skill_comparison"]
        recs = results["recommendations"]
        report_bytes = results["report_bytes"]

        st.markdown("---")

        # ── Score Card ───────────────────────────────────────────────────────
        score_color_class = (
            "#00b894" if match_score >= 70
            else "#fdcb6e" if match_score >= 40
            else "#d63031"
        )

        st.markdown(
            f"""
            <div class="score-card">
                <p>Resume Match Score</p>
                <h1>{match_score}%</h1>
                <p>Based on TF-IDF Cosine Similarity — measures textual alignment, not hiring probability.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Metric Cards Row ─────────────────────────────────────────────────
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(
                f'<div class="metric-card"><h2>{skill_comparison["matching_count"]}</h2>'
                f'<p>Matching Skills</p></div>',
                unsafe_allow_html=True,
            )
        with m2:
            st.markdown(
                f'<div class="metric-card"><h2>{skill_comparison["missing_count"]}</h2>'
                f'<p>Missing Skills</p></div>',
                unsafe_allow_html=True,
            )
        with m3:
            st.markdown(
                f'<div class="metric-card"><h2>{skill_comparison["skill_match_percentage"]}%</h2>'
                f'<p>Skill Match Rate</p></div>',
                unsafe_allow_html=True,
            )
        with m4:
            st.markdown(
                f'<div class="metric-card"><h2>{detailed["jd_coverage"]}%</h2>'
                f'<p>JD Keyword Coverage</p></div>',
                unsafe_allow_html=True,
            )

        st.markdown("")

        # ── Visualizations Row ───────────────────────────────────────────────
        viz1, viz2 = st.columns(2)

        with viz1:
            st.markdown('<p class="section-header">📊 Match Score Gauge</p>', unsafe_allow_html=True)
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=match_score,
                title={"text": "Resume Match %", "font": {"size": 16, "color": "#192a56"}},
                gauge={
                    "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": "#192a56"},
                    "bar": {"color": "#667eea"},
                    "bgcolor": "white",
                    "steps": [
                        {"range": [0, 40], "color": "#ffeaa7"},
                        {"range": [40, 70], "color": "#81ecec"},
                        {"range": [70, 100], "color": "#55efc4"},
                    ],
                    "threshold": {
                        "line": {"color": "#d63031", "width": 4},
                        "thickness": 0.75,
                        "value": match_score,
                    },
                },
            ))
            fig_gauge.update_layout(
                height=300,
                margin=dict(l=30, r=30, t=50, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                font={"family": "Arial"},
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        with viz2:
            st.markdown('<p class="section-header">📈 Skill Gap Breakdown</p>', unsafe_allow_html=True)
            labels = ["Matching Skills", "Missing Skills"]
            values = [skill_comparison["matching_count"], skill_comparison["missing_count"]]
            colors = ["#00b894", "#d63031"]

            if sum(values) > 0:
                fig_pie = go.Figure(data=[go.Pie(
                    labels=labels,
                    values=values,
                    hole=0.5,
                    marker=dict(colors=colors),
                    textinfo="label+value",
                    textfont=dict(size=13),
                    hovertemplate="%{label}: %{value} skills<extra></extra>",
                )])
                fig_pie.update_layout(
                    height=300,
                    margin=dict(l=20, r=20, t=30, b=20),
                    paper_bgcolor="rgba(0,0,0,0)",
                    showlegend=False,
                    annotations=[dict(
                        text=f"{skill_comparison['skill_match_percentage']}%",
                        x=0.5, y=0.5, font_size=22, font_color="#192a56",
                        showarrow=False,
                    )],
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("No skills detected to visualize.")

        # ── Category-wise skill bar chart ────────────────────────────────────
        matching_skills = skill_comparison.get("matching_skills", {})
        missing_skills = skill_comparison.get("missing_skills", {})

        all_categories = sorted(set(list(matching_skills.keys()) + list(missing_skills.keys())))
        if all_categories:
            st.markdown('<p class="section-header">📊 Skills by Category</p>', unsafe_allow_html=True)

            cat_match_counts = [len(matching_skills.get(c, [])) for c in all_categories]
            cat_miss_counts = [len(missing_skills.get(c, [])) for c in all_categories]

            fig_bar = go.Figure()
            fig_bar.add_trace(go.Bar(
                name="Matching", x=all_categories, y=cat_match_counts,
                marker_color="#00b894",
            ))
            fig_bar.add_trace(go.Bar(
                name="Missing", x=all_categories, y=cat_miss_counts,
                marker_color="#d63031",
            ))
            fig_bar.update_layout(
                barmode="group",
                height=350,
                margin=dict(l=20, r=20, t=30, b=80),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis_tickangle=-30,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                font=dict(family="Arial", size=12),
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        # ── Matching Skills ──────────────────────────────────────────────────
        st.markdown('<p class="section-header">✅ Matching Skills</p>', unsafe_allow_html=True)
        if matching_skills:
            for category, skills in matching_skills.items():
                st.markdown(f"**{category}**")
                tags_html = "".join(
                    f'<span class="skill-tag-match">{s.title()}</span>' for s in skills
                )
                st.markdown(tags_html, unsafe_allow_html=True)
                st.markdown("")
        else:
            st.warning("No matching skills found between your resume and the job description.")

        # ── Missing Skills ───────────────────────────────────────────────────
        st.markdown('<p class="section-header">❌ Missing Skills</p>', unsafe_allow_html=True)
        if missing_skills:
            for category, skills in missing_skills.items():
                st.markdown(f"**{category}**")
                tags_html = "".join(
                    f'<span class="skill-tag-missing">{s.title()}</span>' for s in skills
                )
                st.markdown(tags_html, unsafe_allow_html=True)
                st.markdown("")
        else:
            st.success("🎉 No missing skills! Your resume covers all the required skills.")

        # ── Extra Skills (Bonus) ─────────────────────────────────────────────
        extra_skills = skill_comparison.get("extra_skills", [])
        if extra_skills:
            st.markdown('<p class="section-header">💡 Your Additional Skills</p>', unsafe_allow_html=True)
            tags_html = "".join(
                f'<span class="skill-tag-extra">{s.title()}</span>' for s in extra_skills
            )
            st.markdown(tags_html, unsafe_allow_html=True)
            st.markdown("")

        # ── Overall Assessment ───────────────────────────────────────────────
        st.markdown('<p class="section-header">📝 Overall Assessment</p>', unsafe_allow_html=True)
        st.info(recs["overall_assessment"])

        # ── Recommendations ──────────────────────────────────────────────────
        st.markdown('<p class="section-header">🎯 Skill Improvement Recommendations</p>', unsafe_allow_html=True)

        skill_recs = recs.get("skill_recommendations", [])
        if skill_recs:
            for rec in skill_recs:
                priority = rec["priority"]
                css_class = {
                    "High": "rec-card rec-card-high",
                    "Medium": "rec-card rec-card-medium",
                    "Low": "rec-card rec-card-low",
                }.get(priority, "rec-card")

                priority_badge = {
                    "High": "🔴 High",
                    "Medium": "🟡 Medium",
                    "Low": "🟢 Low",
                }.get(priority, priority)

                st.markdown(
                    f"""<div class="{css_class}">
                        <strong>{rec['skill']}</strong> &nbsp; <em>{priority_badge} Priority</em><br>
                        <span style="color:#636e72">{rec['suggestion']}</span><br>
                        <small style="color:#b2bec3">⏱ Estimated time: {rec['time_estimate']}</small>
                    </div>""",
                    unsafe_allow_html=True,
                )
        else:
            st.success("No specific recommendations — your skills align well!")

        # ── Action Plan ──────────────────────────────────────────────────────
        st.markdown('<p class="section-header">🗺️ Action Plan</p>', unsafe_allow_html=True)
        action_plan = recs.get("action_plan", [])
        for i, step in enumerate(action_plan, 1):
            st.markdown(f"**Step {i}.** {step}")

        if recs.get("estimated_time"):
            st.markdown(f"**⏱ {recs['estimated_time']}**")

        # ── Download Report ──────────────────────────────────────────────────
        st.markdown("---")
        col_dl_l, col_dl_c, col_dl_r = st.columns([1, 2, 1])
        with col_dl_c:
            st.download_button(
                label="📥  Download Analysis Report (PDF)",
                data=bytes(report_bytes),
                file_name="resume_analysis_report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

        # ── Extracted Resume Preview (Collapsed) ─────────────────────────────
        with st.expander("📄 View Extracted Resume Text"):
            st.text(results["resume_text"][:5000])
            if len(results["resume_text"]) > 5000:
                st.caption("(Showing first 5000 characters)")
