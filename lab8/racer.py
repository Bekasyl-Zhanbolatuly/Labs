import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("C:\\Users\\ADMIN\\Git labs\\Labs\\lab8\\AnimatedStreet.png")  
player_image = pygame.image.load("C:\\Users\\ADMIN\\Git labs\\Labs\\lab8\\Player.png")  
coin_image = pygame.image.load("C:\\Users\\ADMIN\\Git labs\\Labs\\lab8\\Coin.png")  

player_rect = player_image.get_rect(center=(200, 500))
player_speed = 5

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.reset_position()

    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)

coins = pygame.sprite.Group()
for _ in range(3):  
    coins.add(Coin())

score = 0
font = pygame.font.SysFont(None, 36)

def draw_score():
    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (WIDTH - 150, 10))

running = True
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed

    coins.update()
    coins.draw(screen)

    for coin in coins:
        if player_rect.colliderect(coin.rect):
            score += 1
            coin.reset_position()

    screen.blit(player_image, player_rect)
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
