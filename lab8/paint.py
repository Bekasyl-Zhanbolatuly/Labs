import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLACK, (255, 0, 0), (0, 255, 0), (0, 0, 255)]
current_color = COLORS[0]

drawing = False
tool = 'rectangle'  
start_pos = None

def draw_palette():
    for i, color in enumerate(COLORS):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
    pygame.draw.rect(screen, (200, 200, 200), (200, 10, 100, 30))
    screen.blit(pygame.font.SysFont(None, 20).render("Eraser", True, BLACK), (210, 15))

running = True
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if y <= 40:
                if 10 <= x < 10 + len(COLORS)*40:
                    index = (x - 10) // 40
                    current_color = COLORS[index]
                    tool = 'draw'
                elif 200 <= x <= 300:
                    tool = 'eraser'
            else:
                start_pos = event.pos
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if drawing:
                if tool == 'rectangle':
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                       min(start_pos[1], end_pos[1]),
                                       abs(start_pos[0] - end_pos[0]),
                                       abs(start_pos[1] - end_pos[1]))
                    pygame.draw.rect(screen, current_color, rect, 2)

                elif tool == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2,
                              (start_pos[1] + end_pos[1]) // 2)
                    radius = max(abs(start_pos[0] - end_pos[0]) // 2,
                                 abs(start_pos[1] - end_pos[1]) // 2)
                    pygame.draw.circle(screen, current_color, center, radius, 2)
            drawing = False

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = 'rectangle'
            elif event.key == pygame.K_c:
                tool = 'circle'
            elif event.key == pygame.K_e:
                tool = 'eraser'

    if tool == 'eraser' and pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(screen, WHITE, (mx, my), 10)

    draw_palette()
    pygame.display.flip()

pygame.quit()
