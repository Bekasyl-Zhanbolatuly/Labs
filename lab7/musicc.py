import pygame
import os
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Музыкальный плеер с клавиатурным управлением")
pygame.mixer.init()

music_folder = "C:\\Users\\ADMIN\\Git labs\\Labs\\lab7"
playlist = [os.path.join(music_folder, "Lofi_Chill_Hip_Hop_Beat_-_Transformation_77865020.mp3")]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pygame.mixer.music.get_busy():
                    play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
