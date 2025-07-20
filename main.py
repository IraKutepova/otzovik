from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime
from typing import Optional

app = FastAPI()


# Подключение к SQLite
def get_db_connection():
    conn = sqlite3.connect('reviews.db')
    conn.row_factory = sqlite3.Row
    return conn


# Создаем таблицу при запуске (если ее нет)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


init_db()


# Модель для входящего запроса
class ReviewInput(BaseModel):
    text: str


# Модель для ответа
class ReviewOutput(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str


# Функция определения настроения
def analyze_sentiment(text: str) -> str:
    text_lower = text.lower()
    positive_words = ['хорош', 'отличн', 'прекрасн', 'любл', 'нравит', 'супер', 'замечательн']
    negative_words = ['плох', 'ужасн', 'ненавиж', 'отвратительн', 'мерзк', 'кошмар']

    for word in positive_words:
        if word in text_lower:
            return 'positive'

    for word in negative_words:
        if word in text_lower:
            return 'negative'

    return 'neutral'


# POST endpoint для добавления отзыва
@app.post("/reviews", response_model=ReviewOutput)
async def create_review(review: ReviewInput):
    sentiment = analyze_sentiment(review.text)
    created_at = datetime.utcnow().isoformat()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
        (review.text, sentiment, created_at)
    )
    review_id = cursor.lastrowid
    conn.commit()

    new_review = cursor.execute(
        "SELECT * FROM reviews WHERE id = ?", (review_id,)
    ).fetchone()
    conn.close()

    if new_review is None:
        raise HTTPException(status_code=500, detail="Failed to create review")

    return ReviewOutput(**new_review)


# GET endpoint для получения отзывов
@app.get("/reviews", response_model=list[ReviewOutput])
async def get_reviews(sentiment: Optional[str] = None):
    conn = get_db_connection()

    if sentiment:
        reviews = conn.execute(
            "SELECT * FROM reviews WHERE sentiment = ? ORDER BY created_at DESC",
            (sentiment.lower(),)
        ).fetchall()
    else:
        reviews = conn.execute(
            "SELECT * FROM reviews ORDER BY created_at DESC"
        ).fetchall()

    conn.close()
    return [ReviewOutput(**review) for review in reviews]
