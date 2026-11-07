# 📄 AI Resume Matcher & Skill Gap Analyzer

An AI-powered application that helps job seekers evaluate how well their resumes match specific job descriptions, identify missing skills, and get personalized improvement recommendations.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/kalanjaliyellapu999-byte/AI-Resume-Matcher/main/app.py)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

> 🚀 **Live Demo:** Click to open the app directly: **[Launch AI Resume Matcher](https://share.streamlit.io/kalanjaliyellapu999-byte/AI-Resume-Matcher/main/app.py)**

---

## 🎯 Features

- **📤 Resume Upload** — Upload resumes in PDF format with automatic text extraction via PyMuPDF.
- **📋 Job Description Input** — Paste any job description for analysis.
- **📊 Match Score** — TF-IDF vectorization + Cosine Similarity for an objective similarity percentage.
- **✅ Skill Extraction** — Identifies 300+ technical skills across 9 categories (languages, frameworks, databases, cloud, ML/AI, mobile, tools, methodologies, security).
- **❌ Skill Gap Analysis** — Pinpoints missing skills with categorical breakdowns.
- **🎯 Recommendations** — Personalized learning suggestions with priorities and time estimates.
- **📥 PDF Report** — Downloadable professional analysis report.
- **📈 Visualizations** — Interactive gauge charts, pie charts, and bar charts via Plotly.

---

## 🏗️ Project Architecture

```
AI_Resume_Matcher/
├── app.py                  # Streamlit dashboard (main entry point)
├── resume_parser.py        # PDF upload, validation & text extraction
├── text_processor.py       # NLP text cleaning, stop-word removal, tokenization
├── matcher.py              # TF-IDF vectorization & Cosine Similarity scoring
├── skills_extractor.py     # Skill extraction, categorization & gap comparison
├── recommendations.py      # Personalized learning recommendations engine
├── report_generator.py     # PDF report generation with fpdf2
├── create_sample_resumes.py# Script to generate sample resume PDFs
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── sample_resumes/         # Sample resume PDFs for testing
├── datasets/               # Sample job descriptions (JSON)
│   └── sample_job_descriptions.json
└── tests/                  # Unit tests
    └── test_modules.py
```

---

## 🛠️ Technology Stack

| Component       | Technology                                  |
|-----------------|---------------------------------------------|
| **Language**     | Python 3.9+                                |
| **NLP / ML**     | Scikit-learn (TF-IDF, Cosine Similarity)   |
| **Data**         | Pandas, NumPy                              |
| **PDF Parsing**  | PyMuPDF (fitz)                             |
| **Frontend**     | Streamlit, Custom CSS                      |
| **Visualizations** | Plotly                                  |
| **Reports**      | fpdf2                                      |
| **Testing**      | pytest                                     |

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Resume_Matcher.git
cd AI_Resume_Matcher
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Generate Sample Resumes (Optional)

```bash
python create_sample_resumes.py
```

This creates 3 sample resume PDFs in `sample_resumes/` for testing.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📖 How to Use

1. **Upload Resume** — Click the upload area and select your PDF resume.
2. **Paste Job Description** — Copy a job description and paste it into the text area.
3. **Click "Analyze Resume"** — The system processes both documents.
4. **Review Results:**
   - **Match Score** — Overall textual similarity percentage.
   - **Matching Skills** — Skills found in both your resume and the JD.
   - **Missing Skills** — Skills required by the JD but absent from your resume.
   - **Skill Gap Charts** — Visual breakdown by category.
   - **Recommendations** — Prioritized learning plan with time estimates.
5. **Download Report** — Click the download button for a PDF report.

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

Expected output:

```
tests/test_modules.py::TestTextProcessor::test_clean_text_basic PASSED
tests/test_modules.py::TestMatcher::test_match_score_range PASSED
tests/test_modules.py::TestSkillsExtractor::test_extract_skills_finds_python PASSED
tests/test_modules.py::TestRecommendations::test_generate_recommendations_structure PASSED
...
```

---

## 📊 How the Matching Works

1. **Text Extraction** — PyMuPDF extracts raw text from the PDF resume.
2. **Preprocessing** — Text is cleaned (lowercased, URLs/emails removed, special characters stripped, stop words removed).
3. **TF-IDF Vectorization** — Both documents are converted into numerical vectors using Term Frequency–Inverse Document Frequency with unigram + bigram features.
4. **Cosine Similarity** — The angle between the two TF-IDF vectors is measured; smaller angle = higher similarity.
5. **Skill Matching** — A database of 300+ skills is searched against both documents to find matches and gaps.
6. **Recommendations** — Missing skills are prioritized and paired with learning resources and time estimates.

> **Note:** The match score represents textual similarity, not the probability of getting hired. It is a guide for improving your resume's alignment with a specific job description.

---

## 🔒 Privacy

- Uploaded resumes are processed **in-memory only**.
- No files are permanently stored on the server.
- All data is discarded after the browser session ends.

---

## 📝 Sample Job Descriptions

The `datasets/sample_job_descriptions.json` file contains 3 sample JDs for testing:

1. **Senior Python Developer** — Backend-focused with Django, AWS, Docker.
2. **Data Scientist (ML)** — ML/DL with TensorFlow, PyTorch, NLP.
3. **Full Stack Web Developer** — React, Node.js, MongoDB, TypeScript.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Built as a final-year B.Tech AI & ML portfolio project demonstrating:
- Python programming & modular software design
- Natural Language Processing (NLP)
- Machine Learning concepts (TF-IDF, Cosine Similarity)
- Data processing with Pandas & NumPy
- Full-stack web development with Streamlit
- PDF generation & interactive data visualization
