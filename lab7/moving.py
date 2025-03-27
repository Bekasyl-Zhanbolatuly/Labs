import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

circle_radius = 25
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_color = (255, 0, 0)
speed = 20

running = True
while running:
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and circle_y - speed - circle_radius >= 0:
                circle_y -= speed
            elif event.key == pygame.K_DOWN and circle_y + speed + circle_radius <= HEIGHT:
                circle_y += speed
            elif event.key == pygame.K_LEFT and circle_x - speed - circle_radius >= 0:
                circle_x -= speed
            elif event.key == pygame.K_RIGHT and circle_x + speed + circle_radius <= WIDTH:
                circle_x += speed
    
    pygame.display.flip()
    pygame.time.delay(50) 

pygame.quit()
