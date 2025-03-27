import pygame
import os

pygame.init()
pygame.mixer.init()


MUSIC_FOLDER = "lab7/Кайрат Нуртас - Сени Суйем.mp3usic"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
current_song = 0


def play_song(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[index]))
    pygame.mixer.music.play()

if songs:
    play_song(current_song)


running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
            elif event.key == pygame.K_RIGHT: 
                current_song = (current_song + 1) % len(songs)
                play_song(current_song)
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(songs)
                play_song(current_song)
            elif event.key == pygame.K_ESCAPE: 
                running = False

pygame.quit()
