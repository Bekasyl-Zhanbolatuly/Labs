import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_face = pygame.image.load("C:\\Users\\ADMIN\\Git labs\\Labs\\lab7\\mickeyclock.jpeg") 
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))

minute_hand = pygame.Surface((10, 100), pygame.SRCALPHA)
second_hand = pygame.Surface((5, 120), pygame.SRCALPHA)
pygame.draw.rect(minute_hand, (0, 0, 0), (4, 0, 2, 100))
pygame.draw.rect(second_hand, (255, 0, 0), (2, 0, 2, 120))  

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    now = datetime.datetime.now()
    minutes_angle = -(now.minute * 12)
    seconds_angle = -(now.second * 12)

    rotated_minute = pygame.transform.rotate(minute_hand, minutes_angle)
    rotated_second = pygame.transform.rotate(second_hand, seconds_angle)
    
    minute_rect = rotated_minute.get_rect(center=(WIDTH//2, HEIGHT//2))
    second_rect = rotated_second.get_rect(center=(WIDTH//2, HEIGHT//2))
    
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.delay(1000)  
pygame.quit()
