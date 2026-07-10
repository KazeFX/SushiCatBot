import sqlite3
from xmlrpc.client import DateTime


def get_db():
    conn = sqlite3.connect("bot.db")
    conn.row_factory = sqlite3.Row
    return conn

def add_user(user_id: int, name: str, birthday: DateTime):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, name, birthday))
        VALUES (?, ?, ?)
    """, (user_id, name, birthday))

    conn.commit()
    conn.close()

def get_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()

    conn.close()
    return row
