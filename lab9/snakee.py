import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Lab 9")

font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

snake = [(100, 100)]
dx, dy = CELL_SIZE, 0
food_timer = 0
food_lifetime = 5000
score = 0
level = 1
speed = 5

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
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL_SIZE, 0
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL_SIZE
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL_SIZE

    new_head = (snake[0][0] + dx, snake[0][1] + dy)

    if (new_head in snake) or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        pygame.quit()
        exit()

    snake.insert(0, new_head)

    if new_head == food["pos"]:
        score += food["value"]
        food = generate_food()
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
        pygame.draw.rect(screen, (0, 255, 0), (*s, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (255, 0, 0), (*food["pos"], CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {score}  Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
