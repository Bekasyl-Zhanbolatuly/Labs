import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Lab 9")

clock = pygame.time.Clock()

bg_img = pygame.image.load("C:/Users/ADMIN/Git labs/Labs/lab8/AnimatedStreet.png")
bg_y = 0

player_img = pygame.image.load("C:/Users/ADMIN/Git labs/Labs/lab8/Player.png")
enemy_img = pygame.image.load("C:/Users/ADMIN/Git labs/Labs/lab8/Enemy.png")
coin_img = pygame.image.load("C:/Users/ADMIN/Git labs/Labs/lab8/Coin.png")

player_img = pygame.transform.scale(player_img, (50, 100))
enemy_img = pygame.transform.scale(enemy_img, (50, 100))
coin_img = pygame.transform.scale(coin_img, (30, 30))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

pygame.mixer.music.load("C:/Users/ADMIN/Git labs/Labs/lab8/background.wav")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("C:/Users/ADMIN/Git labs/Labs/lab8/coin.mp3")
crash_sound = pygame.mixer.Sound("C:/Users/ADMIN/Git labs/Labs/lab8/crash.wav")

font = pygame.font.SysFont("Verdana", 20)
score = 0
speed = 5

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 110, 50, 100)
enemy = pygame.Rect(random.randint(50, WIDTH - 100), -100, 50, 100)

coins = []

def create_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-200, -50)
    value = random.choice([1, 3, 5])
    rect = pygame.Rect(x, y, 30, 30)
    return {"rect": rect, "value": value}

for _ in range(3):
    coins.append(create_coin())

running = True
while running:
    screen.blit(bg_img, (0, bg_y))
    screen.blit(bg_img, (0, bg_y - HEIGHT))
    bg_y += 3
    if bg_y >= HEIGHT:
        bg_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(5, 0)

    enemy.move_ip(0, speed)
    if enemy.top > HEIGHT:
        enemy.top = -100
        enemy.left = random.randint(50, WIDTH - 100)

    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)

    for coin in coins:
        coin["rect"].move_ip(0, speed)
        screen.blit(coin_img, coin["rect"])
        if coin["rect"].colliderect(player):
            score += coin["value"]
            coin_sound.play()
            coins.remove(coin)
            coins.append(create_coin())

    if player.colliderect(enemy):
        crash_sound.play()
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    if score >= 10:
        speed = 7
    elif score >= 20:
        speed = 9

    score_text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
