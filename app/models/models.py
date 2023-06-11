from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()


questions = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("question_id", Integer),
    Column("question_text", String),
    Column("answer_text", String),
    Column("created_at", TIMESTAMP),
)    
