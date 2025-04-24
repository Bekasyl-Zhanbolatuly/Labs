import pygame
import random
import time
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="1234abcd"
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);""")
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
        score = result[0]
        level = result[1]
    else:
        score = 0
        level = 1
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    score = 0
    level = 1

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Lab 9")

font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

snake = [(100, 100)]
snakecolor = (0, 255, 0)
dx, dy = CELL_SIZE, 0
food_timer = 0
food_lifetime = 10000
speed = 5

if level == 2:
    speed = 8
elif level >= 3:
    speed = 11

def generate_food():
    while True:
        pos = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
               random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        if pos not in snake:
            value = random.choice([1, 3, 5])
            return {"pos": pos, "value": value, "time": pygame.time.get_ticks()}

food = generate_food()

running = True
while running:
    screen.fill((0, 0, 0))
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL_SIZE, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL_SIZE, 0
    elif keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL_SIZE
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL_SIZE
    elif keys[pygame.K_p]:
        cur.execute("""
            INSERT INTO user_score (user_id, score, level, saved_at)
            VALUES (%s, %s, %s, %s)
        """, (user_id, score, level, datetime.now()))
        conn.commit()

    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    if (new_head in snake) or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        cur.execute("""
            INSERT INTO user_score (user_id, score, level, saved_at)
            VALUES (%s, %s, %s, %s)
        """, (user_id, score, level, datetime.now()))
        conn.commit()
        cur.close()
        conn.close()
        pygame.quit()
        exit()

    snake.insert(0, new_head)

    if new_head == food["pos"]:
        score += food["value"]
        food = generate_food()
        if score % 5 == 0 and score > 0:
            snakecolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            snakecolor = (0, 255, 0)
    else:
        snake.pop()

    if now - food["time"] > food_lifetime:
        food = generate_food()

    if score >= 10:
        level = 2
        speed = 8
    if score >= 20:
        level = 3
        speed = 11

    for s in snake:
        pygame.draw.rect(screen, snakecolor, (*s, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (255, 0, 0), (*food["pos"], CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
