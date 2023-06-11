from typing import Optional
from fastapi import FastAPI
import requests
import psycopg2
from . config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE = DB_NAME
USER = DB_USER
PASSWORD = DB_PASS
HOST = DB_HOST
PORT = DB_PORT


app = FastAPI()


def get_questions(count: int) -> Optional[dict]:
    url = f'https://jservice.io/api/random?count={count}'
    response = requests.get(url)
    if response.ok:
        return response.json()
    return None


def check_question_exist(cursor, question: str) -> bool:
    sql = 'SELECT question_id FROM questions WHERE question_text = %s'
    cursor.execute(sql, (question,))
    result = cursor.fetchone()
    if result:
        return True
    return False


def save_question(cursor, question: dict) -> int:
    sql = 'INSERT INTO questions(question_id, question_text, answer_text, created_at) VALUES (%s, %s, %s, %s) RETURNING id'
    cursor.execute(sql, (question['id'], question['question'], question['answer'], question['created_at']))
    return cursor.fetchone()[0]


def get_last_question(cursor) -> Optional[dict]:
    sql = 'SELECT * FROM questions ORDER BY id DESC LIMIT 1'
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return {
            'id': result[0],
            'question': result[1],
            'answer': result[2],
            'created_at': result[3]
        }
    return None


def get_connection():
    conn = psycopg2.connect(
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    return conn


@app.post('/quiz')
def quiz(questions_num: int):
    conn = get_connection()
    cursor = conn.cursor()

    for i in range(questions_num):
        question = None
        while not question:
            question = get_questions(1)
            exist = check_question_exist(cursor, question[0]['question'])
            if exist:
                question = None

        save_question(cursor, question[0])

    conn.commit()
    last_question = get_last_question(cursor)
    cursor.close()
    conn.close()
    return last_question