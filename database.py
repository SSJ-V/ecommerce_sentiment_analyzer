import sqlite3

def init_db():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            score REAL NOT NULL,
            age_group TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_review(review, sentiment, score, age_group):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO reviews (review, sentiment, score, age_group)
        VALUES (?, ?, ?, ?)
    ''', (review, sentiment, score, age_group))

    conn.commit()
    conn.close()

def get_all_reviews():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()

    c.execute('SELECT review, sentiment, score, age_group FROM reviews ORDER BY id DESC')
    rows = c.fetchall()

    conn.close()
    return rows
