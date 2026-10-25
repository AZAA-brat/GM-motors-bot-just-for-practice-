import psycopg
import os

connection = psycopg.connect(
    database="gm_motors",
    user="gm_bot",
    password=os.getenv("SQL_PASSWORD"),
    host="localhost",
    port=5432,
)
cursor = connection.cursor()

def create_users():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
        user_id BIGINT PRIMARY KEY,
        language TEXT NOT NULL DEFAULT 'uz' CHECK (language IN ('uz', 'ru', 'en')),      
        created_at TIMESTAMPTZ NOT NULL DEFAULT now()
        );
        """
    )
    connection.commit()
    connection.close()


