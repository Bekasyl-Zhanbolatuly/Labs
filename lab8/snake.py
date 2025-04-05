import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

font = pygame.font.SysFont(None, 30)

score = 0
level = 1

snake = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]
direction = pygame.K_RIGHT

def generate_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        food = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        if food not in snake:
            return food

food = generate_food()

speed = 10

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                direction = event.key

    
    head = snake[0].copy()
    if direction == pygame.K_UP:
        head.y -= CELL_SIZE
    elif direction == pygame.K_DOWN:
        head.y += CELL_SIZE
    elif direction == pygame.K_LEFT:
        head.x -= CELL_SIZE
    elif direction == pygame.K_RIGHT:
        head.x += CELL_SIZE

    
    if head.x < 0 or head.y < 0 or head.x >= WIDTH or head.y >= HEIGHT:
        print("Game Over: Столкновение со стеной!")
        running = False

    
    if head in snake:
        print("Game Over: Змейка съела сама себя!")
        running = False      

    
    snake.insert(0, head)

    if head.colliderect(food):
        score += 1
        food = generate_food()

        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop() 

    screen.fill(GRAY)


    pygame.draw.rect(screen, RED, food)

    
    for part in snake:
        pygame.draw.rect(screen, GREEN, part)

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()

pygame.quit()
