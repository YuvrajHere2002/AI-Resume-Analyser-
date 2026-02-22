import streamlit as st

from resume_parser import extract_resume_text
from matcher import calculate_semantic_score
from database import create_tables, insert_result

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="centered"
)

st.title("AI Resume Analyzer & Job Recommendation System")

# ---------------- INIT DB ----------------
create_tables()

# ---------------- SKILL SET ----------------
SKILL_SET = [
    "python", "java", "c++", "sql", "flask", "django", "fastapi",
    "machine learning", "deep learning", "nlp",
    "data analysis", "pandas", "numpy", "scikit-learn",
    "html", "css", "javascript", "react",
    "git", "docker", "api", "rest"
]

def extract_skills(text):
    text = text.lower()
    return sorted({skill for skill in SKILL_SET if skill in text})

# ---------------- INPUT SECTION ----------------
st.subheader("📥 Upload Resumes & Job Description")

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF or DOCX) – Max 5",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description here",
    height=160
)

st.divider()

# ---------------- ANALYSIS ----------------
if st.button("🔍 Analyze Resumes", use_container_width=True):

    if not uploaded_files:
        st.error("Please upload at least one resume.")
        st.stop()

    if len(uploaded_files) > 5:
        st.error("Please upload at most 5 resumes.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a job description.")
        st.stop()

    st.info("Analyzing resumes using semantic NLP…")

    results = []
    jd_skills = extract_skills(job_description)

    for file in uploaded_files:
        resume_text = extract_resume_text(file)
        if not resume_text.strip():
            continue

        resume_skills = extract_skills(resume_text)
        matched = sorted(set(resume_skills) & set(jd_skills))
        missing = sorted(set(jd_skills) - set(resume_skills))

        semantic_score = calculate_semantic_score(
            resume_text,
            job_description
        )

        # ✅ Store FULL resume in DB (backend only)
        insert_result(
            file.name,
            resume_text,
            semantic_score,
            matched,
            missing
        )

        results.append({
            "filename": file.name,
            "score": semantic_score,
            "matched": matched,
            "missing": missing
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.success("Analysis completed successfully")
    st.subheader("🏆 Resume Ranking Results")

    # ---------------- RESULTS DISPLAY ----------------
    for rank, res in enumerate(results, start=1):
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"### Rank {rank}: {res['filename']}")

            with col2:
                st.metric("Score", f"{round(res['score'], 2)}%")

            st.markdown("**✅ Matched Skills**")
            st.write(", ".join(res["matched"]) if res["matched"] else "None")

            st.markdown("**❌ Missing Skills**")
            st.write(", ".join(res["missing"]) if res["missing"] else "None")
