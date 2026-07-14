# RUN ONLY ONCE when initializing the database. Creates a new database
import sqlite3


#Creates the bot_token.py file to store the bot token and channel id's for functions
with open("bot_token.py", "a") as f:
    f.write('BOT_TOKEN = "Insert your bot token here"\n')
    f.write('BIRTHDAY_MESSAGE_CHANNEL_ID = #Insert your channel id here\n')


# Creates and defines bot.db
conn = sqlite3.connect("bot.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    birthday TEXT
)
""")
conn.commit()
conn.close()