# 🧠 AI Resume Analyzer & Job Recommendation System

An AI-powered web application that automates resume screening and job matching using Natural Language Processing (NLP) and semantic similarity techniques. The system helps recruiters and organizations quickly identify suitable candidates by analyzing resumes against job descriptions and providing explainable results.

---

## 🚀 Features

* Upload multiple resumes (PDF/DOCX)
* Enter job description for analysis
* Semantic resume–job matching using AI
* Resume ranking based on relevance score
* Matched skills & missing skills detection
* Secure storage of results in database
* Clean and interactive web interface
* Privacy-friendly output (resume content not displayed)

---

## 🧠 Problem Statement

Manual resume screening is time-consuming and often inaccurate due to dependency on keyword-based filtering. Many Applicant Tracking Systems fail to understand context and may reject qualified candidates.
This project aims to automate resume analysis using AI and NLP to provide accurate, fair, and explainable candidate ranking.

---

## 🛠 Tech Stack

**Frontend:**

* Streamlit (Python Web UI)

**Backend:**

* Python

**Libraries & Tools:**

* spaCy
* NLTK
* Sentence-BERT (Semantic similarity)
* scikit-learn
* Pandas

**Database:**

* SQLite

---

## ⚙️ How It Works

1. User uploads resumes (PDF/DOCX)
2. User enters job description
3. System extracts text from resumes
4. NLP preprocessing is applied
5. Skills are extracted from resumes and job description
6. Sentence-BERT generates embeddings
7. Cosine similarity calculates match score
8. System displays:

   * Resume score (percentage)
   * Matched skills
   * Missing skills
9. Results stored securely in database

---

## 📊 Output Example

* Resume match score: **85%**
* Matched skills: Python, SQL, Machine Learning
* Missing skills: AWS, Docker

---

## 💻 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```
