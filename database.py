import datetime
import sqlite3


def get_db():
    conn = sqlite3.connect("bot.db")
    conn.row_factory = sqlite3.Row
    return conn

def add_user(user_id: int, name: str, birthday: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, name, birthday)
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

def delete_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()

def birthday(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, birthday FROM birthdays WHERE birthday = ?", (datetime.datetime.now(),))