from psycopg_pool import AsyncConnectionPool
import os

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "gm_motors",
    "user": "gm_bot",
    "password": os.getenv("SQL_PASSWORD"),
}

CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    language TEXT NOT NULL DEFAULT 'uz' CHECK (language IN ('uz', 'ru', 'en')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""

def create_pool() -> AsyncConnectionPool:
    return AsyncConnectionPool(
        kwargs=DB_CONFIG,
        min_size=2,
        max_size=10,
        open=False
    )

async def init_db(pool: AsyncConnectionPool) -> None:
    await pool.open()
    await pool.wait()
    async with pool.connection() as conn:
        await conn.execute(CREATE_USERS_TABLE)

async def close_db(pool: AsyncConnectionPool) -> None:
    await pool.close()

async def get_user_language(pool: AsyncConnectionPool, user_id: int) -> str:
    async with pool.connection() as conn:
        cur = await conn.execute(
            "SELECT language FROM users WHERE user_id = %s",
            (user_id,),
        )
        row = await cur.fetchone()
    return row[0] if row else "uz"


async def set_user_language(pool: AsyncConnectionPool, user_id: int, language: str) -> None:
    async with pool.connection() as conn:
        await conn.execute(
            """
            INSERT INTO users (user_id, language)
            VALUES (%s, %s)
            ON CONFLICT (user_id) DO UPDATE SET language = EXCLUDED.language
            """,
            (user_id, language),
        )

async def ensure_user_language(pool: AsyncConnectionPool, user_id: int) -> None:
    async with pool.connection() as conn:
        await conn.execute(
            """
            INSERT INTO users (user_id)
            VALUES (%s)
            ON CONFLICT (user_id) DO NOTHING
            """,
            (user_id,),
        )



