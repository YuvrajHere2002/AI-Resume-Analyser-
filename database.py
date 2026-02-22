import sqlite3
from datetime import datetime

DB_NAME = "resume_analyzer.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            resume_text TEXT,
            semantic_score REAL,
            matched_skills TEXT,
            missing_skills TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_result(filename, resume_text, score, matched, missing):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO results
        (filename, resume_text, semantic_score, matched_skills, missing_skills, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        filename,
        resume_text,
        score,
        ", ".join(matched),
        ", ".join(missing),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()
