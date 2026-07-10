# RUN ONLY ONCE when initializing the database.

import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    birthday DATE,
)
""")

conn.commit()
conn.close()
