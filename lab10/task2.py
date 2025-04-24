import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="1234abcd"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")
conn.commit()

username = input("Enter your username: ")

cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    cur.execute("""
        SELECT score, level FROM user_score
        WHERE user_id = %s
        ORDER BY saved_at DESC LIMIT 1
    """, (user_id,))
    result = cur.fetchone()
    if result:
        print(f"Welcome back, {username}!")
        print(f"Your current level: {result[1]}, score: {result[0]}")
    else:
        print(f"No saved data found for {username}.")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print(f"New user created: {username}")

input("Press Enter to save game progress...")

current_score = 100
current_level = 2

cur.execute("""
    INSERT INTO user_score (user_id, score, level, saved_at)
    VALUES (%s, %s, %s, %s)
""", (user_id, current_score, current_level, datetime.now()))

conn.commit()
print("Game progress saved.")

cur.close()
conn.close()
