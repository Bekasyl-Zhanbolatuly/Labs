import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Lab 9")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]  
color_names = ["R", "G", "B", "Eraser"]
current_color = BLACK
drawing = False
shape = "rect"
start_pos = None

font = pygame.font.SysFont("Verdana", 20)
screen.fill(WHITE)

def draw_triangle_right(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(screen, color, [(x1, y2), (x2, y2), (x2, y1)])

def draw_triangle_eq(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    base = abs(x2 - x1)
    height = int(base * math.sqrt(3) / 2)
    if y2 < y1:
        height = -height
    pygame.draw.polygon(screen, color, [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)])

def draw_rhombus(screen, start, end, color):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(screen, color, points)

def draw_ui():
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i * 50, 10, 40, 40))
        label = font.render(color_names[i], True, BLACK if c != BLACK else WHITE)
        screen.blit(label, (10 + i * 50, 55))
    if current_color == WHITE:
        pygame.draw.rect(screen, (200, 200, 200), (10 + 3 * 50, 10, 40, 40), 4) 

running = True
while running:
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if my < 60:
                for i in range(len(colors)):
                    if 10 + i * 50 <= mx <= 50 + i * 50:
                        current_color = colors[i]
            else:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_pos = event.pos
            if current_color == WHITE:
                pygame.draw.line(screen, WHITE, start_pos, end_pos, 20)
            else:
                if shape == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    pygame.draw.rect(screen, current_color, pygame.Rect(min(x1, x2), min(y1, y2),
                                                                        abs(x2 - x1), abs(y2 - y1)), 2)
                elif shape == "square":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, current_color, pygame.Rect(x1, y1, side, side), 2)
                elif shape == "triangle_right":
                    draw_triangle_right(screen, start_pos, end_pos, current_color)
                elif shape == "triangle_eq":
                    draw_triangle_eq(screen, start_pos, end_pos, current_color)
                elif shape == "rhombus":
                    draw_rhombus(screen, start_pos, end_pos, current_color)
            drawing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "rect"
            elif event.key == pygame.K_2:
                shape = "square"
            elif event.key == pygame.K_3:
                shape = "triangle_right"
            elif event.key == pygame.K_4:
                shape = "triangle_eq"
            elif event.key == pygame.K_5:
                shape = "rhombus"
            elif event.key == pygame.K_c:
                screen.fill(WHITE)

    pygame.display.flip()

pygame.quit()
