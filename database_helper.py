import sqlite3

# Grabs the database. Duh :D
def get_db():
    conn = sqlite3.connect("bot.db")
    conn.row_factory = sqlite3.Row
    return conn


# Adds a user and birthday to the database
def add_user(user_id: int, name: str, birthday: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, name, birthday)
        VALUES (?, ?, ?)
    """, (user_id, name, birthday))
    conn.commit()
    conn.close()


# Gets the user name and birthday from the database
def get_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row


# Deletes a user row from the database specified by user_id
def delete_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    conn.commit()


# Grabs birthdays that match todays date in month and day. Ignores year
def get_birthdays_today():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_id, birthday
        FROM users
        WHERE strftime('%m-%d', birthday) = strftime('%m-%d', 'now')
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows