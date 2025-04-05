import pygame
import sys

pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Movement with Arrow Keys")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2

move_speed = 20

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= move_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius < screen_height:
        ball_y += move_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= move_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < screen_width:
        ball_x += move_speed

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
