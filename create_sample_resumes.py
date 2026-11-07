"""
Generate sample resume PDFs for testing.
Run this script once to create sample PDF resumes in the sample_resumes/ folder.

Usage:
    python create_sample_resumes.py
"""

from fpdf import FPDF
import os

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "sample_resumes")
os.makedirs(SAMPLE_DIR, exist_ok=True)


def create_resume_1():
    """Software Engineer with Python & Cloud experience."""
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Arjun Sharma", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "arjun.sharma@email.com | +91 98765 43210 | Bengaluru, India", ln=True, align="C")
    pdf.cell(0, 6, "github.com/arjunsharma | linkedin.com/in/arjunsharma", ln=True, align="C")
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Professional Summary", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Experienced Software Engineer with 4+ years of expertise in Python, Django, "
        "and cloud technologies. Passionate about building scalable web applications "
        "and RESTful APIs. Strong background in SQL databases and DevOps practices."
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Technical Skills", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Programming Languages: Python, JavaScript, SQL, Bash\n"
        "Web Frameworks: Django, Flask, FastAPI, React\n"
        "Databases: PostgreSQL, MySQL, Redis, MongoDB\n"
        "Cloud & DevOps: AWS (EC2, S3, Lambda, RDS), Docker, Kubernetes, "
        "Terraform, Jenkins, GitHub Actions, CI/CD\n"
        "Tools: Git, GitHub, Jira, VS Code, Linux, Postman\n"
        "Methodologies: Agile, Scrum, TDD, Microservices, REST API Design"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Work Experience", ln=True)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Software Engineer - CloudTech Solutions, Bengaluru", ln=True)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "June 2021 - Present", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Developed and maintained RESTful APIs using Django and Flask serving 50K+ daily users\n"
        "- Designed and implemented microservices architecture reducing system latency by 40%\n"
        "- Managed PostgreSQL databases with complex queries and performance optimization\n"
        "- Built CI/CD pipelines using Jenkins and GitHub Actions for automated deployments\n"
        "- Deployed applications on AWS using Docker containers and Kubernetes orchestration\n"
        "- Implemented unit testing with pytest achieving 85% code coverage\n"
        "- Conducted code reviews and mentored 3 junior developers"
    )
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Junior Developer - WebApps India, Hyderabad", ln=True)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "July 2019 - May 2021", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Built web applications using Python and Django framework\n"
        "- Created REST APIs consumed by React frontend applications\n"
        "- Wrote SQL queries for MySQL and PostgreSQL databases\n"
        "- Used Git for version control and participated in Agile sprints\n"
        "- Containerized applications using Docker for consistent deployments"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Education", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "B.Tech in Computer Science and Engineering\n"
        "National Institute of Technology, Warangal - 2019\n"
        "CGPA: 8.5/10"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Certifications", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- AWS Solutions Architect Associate\n"
        "- Python Professional Certificate (Coursera)\n"
        "- Docker Certified Associate"
    )

    path = os.path.join(SAMPLE_DIR, "arjun_sharma_software_engineer.pdf")
    pdf.output(path)
    print(f"Created: {path}")


def create_resume_2():
    """Data Scientist with ML and NLP experience."""
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Priya Patel", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "priya.patel@email.com | +91 87654 32109 | Mumbai, India", ln=True, align="C")
    pdf.cell(0, 6, "github.com/priyapatel | linkedin.com/in/priyapatel", ln=True, align="C")
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Professional Summary", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Data Scientist with 3+ years of experience in machine learning, deep learning, "
        "and natural language processing. Skilled in building and deploying ML models at "
        "scale. Strong statistical analysis background with expertise in Python and cloud platforms."
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Technical Skills", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Programming: Python, R, SQL, Java\n"
        "ML/DL Frameworks: TensorFlow, PyTorch, Scikit-learn, Keras, XGBoost\n"
        "NLP: Natural Language Processing, BERT, Transformers, Hugging Face, LLM\n"
        "Data Tools: Pandas, NumPy, SciPy, Matplotlib, Seaborn, Plotly, Tableau\n"
        "Databases: PostgreSQL, MongoDB, Redis, Elasticsearch\n"
        "Big Data: Apache Spark, Hadoop, Kafka, Airflow\n"
        "Cloud: AWS (SageMaker, S3, EC2), GCP (Vertex AI, BigQuery)\n"
        "MLOps: MLflow, Docker, Kubernetes, CI/CD\n"
        "Methods: Statistical Analysis, Hypothesis Testing, A/B Testing, "
        "Feature Engineering, Deep Learning, Neural Networks, Computer Vision"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Work Experience", ln=True)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Data Scientist - AnalyticsPro, Mumbai", ln=True)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "March 2022 - Present", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Built and deployed machine learning models for customer churn prediction (92% accuracy)\n"
        "- Developed NLP pipelines for sentiment analysis processing 100K+ reviews daily\n"
        "- Implemented recommendation systems using collaborative filtering and deep learning\n"
        "- Created data visualizations and dashboards using Plotly and Tableau\n"
        "- Deployed ML models on AWS SageMaker with automated retraining pipelines\n"
        "- Conducted A/B testing for feature optimization and product decisions\n"
        "- Collaborated with engineering to integrate ML models into production systems"
    )
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Junior Data Analyst - DataWorks, Pune", ln=True)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "August 2020 - February 2022", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Performed exploratory data analysis and statistical modeling\n"
        "- Built classification and regression models using Scikit-learn\n"
        "- Created ETL data pipelines using Python and Apache Spark\n"
        "- Designed Tableau dashboards for business intelligence reporting\n"
        "- Queried and analyzed data from PostgreSQL and MongoDB databases"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Education", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "M.Tech in Artificial Intelligence\n"
        "Indian Institute of Technology, Bombay - 2020\n"
        "CGPA: 9.0/10\n\n"
        "B.Tech in Computer Science\n"
        "VJTI Mumbai - 2018\n"
        "CGPA: 8.7/10"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Publications & Projects", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Published paper on 'Transformer-based Text Classification' at EMNLP Workshop\n"
        "- Open-source NLP toolkit for Indian languages (500+ GitHub stars)\n"
        "- Kaggle Competitions Master with 2 gold medals"
    )

    path = os.path.join(SAMPLE_DIR, "priya_patel_data_scientist.pdf")
    pdf.output(path)
    print(f"Created: {path}")


def create_resume_3():
    """Fresh graduate — frontend-leaning full stack developer."""
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Rahul Verma", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "rahul.verma@email.com | +91 76543 21098 | Delhi, India", ln=True, align="C")
    pdf.cell(0, 6, "github.com/rahulverma | linkedin.com/in/rahulverma", ln=True, align="C")
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Objective", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Recent B.Tech graduate seeking a Full Stack Developer position. "
        "Experienced in JavaScript, React, and Python with a passion for building "
        "user-friendly web applications. Quick learner eager to grow in a professional environment."
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Technical Skills", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "Languages: JavaScript, Python, HTML, CSS, SQL\n"
        "Frontend: React.js, Bootstrap, Tailwind CSS, jQuery\n"
        "Backend: Node.js, Express.js, Flask\n"
        "Databases: MongoDB, MySQL\n"
        "Tools: Git, GitHub, VS Code, Postman, npm\n"
        "Other: REST API, JSON, Responsive Design, Agile"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Projects", ln=True)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "E-Commerce Web Application", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Built a full-stack e-commerce app with React frontend and Express.js backend\n"
        "- Implemented user authentication, product catalog, and shopping cart\n"
        "- Used MongoDB for data storage and deployed on Heroku\n"
        "- Technologies: React, Node.js, Express, MongoDB, JWT"
    )
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Weather Dashboard", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Created a responsive weather dashboard using React and OpenWeather API\n"
        "- Implemented location search, 5-day forecast, and data visualization\n"
        "- Used Tailwind CSS for modern UI design\n"
        "- Technologies: React, JavaScript, Tailwind CSS, REST API"
    )
    pdf.ln(3)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Blog Platform", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Developed a blogging platform with Flask backend and MySQL database\n"
        "- Features: user registration, CRUD operations, markdown support\n"
        "- Technologies: Python, Flask, MySQL, Bootstrap, Git"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Internship", ln=True)
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Web Development Intern - StartupXYZ, Delhi", ln=True)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "January 2023 - June 2023", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "- Developed frontend components using React.js\n"
        "- Built REST API endpoints with Express.js\n"
        "- Participated in daily stand-ups and sprint planning\n"
        "- Wrote unit tests for JavaScript modules"
    )
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, "Education", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 5,
        "B.Tech in Computer Science and Engineering\n"
        "Delhi Technological University - 2023\n"
        "CGPA: 8.2/10"
    )

    path = os.path.join(SAMPLE_DIR, "rahul_verma_fullstack_developer.pdf")
    pdf.output(path)
    print(f"Created: {path}")


if __name__ == "__main__":
    create_resume_1()
    create_resume_2()
    create_resume_3()
    print("\nAll sample resumes created successfully!")
