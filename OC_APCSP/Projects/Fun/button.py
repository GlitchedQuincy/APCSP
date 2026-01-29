import pygame
import random

pygame.init()

SCREEN_SIZE = (1000, 1000)
BG = (30, 30, 30)
BTN_BG = (50, 50, 215)
SAFE = (50, 255, 50)
BOOM_COLOR = (255, 50, 50)

GRID_N = 5
CELL = 100
STEP = 175
OFFSET_X = 100
OFFSET_Y = 100

total_cells = GRID_N * GRID_N
boom_index = random.randrange(total_cells)
# print(boom_index)  # debug: show mine position

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("mine gambling")
clock = pygame.time.Clock()
running = True

# create rects in a grid
rects = []
for row in range(GRID_N):
    for col in range(GRID_N):
        rects.append(pygame.Rect(OFFSET_X + STEP * col, OFFSET_Y + STEP * row, CELL, CELL))

# track revealed squares and score
revealed = [False] * total_cells
score = 0
font = pygame.font.SysFont(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, r in enumerate(rects):
                if r.collidepoint(event.pos):
                    if i == boom_index:
                        print(f"boom (square {i+1})")
                        pygame.draw.rect(screen, BOOM_COLOR, r)
                        pygame.display.flip()
                        pygame.time.delay(500)
                        running = False
                    else:
                        if not revealed[i]:
                            score += 1
                            revealed[i] = True
                        pygame.draw.rect(screen, SAFE, r)
                        pygame.display.flip()
                    break

    if not running:
        break

    screen.fill(BG)

    # draw grid according to revealed state
    for i, r in enumerate(rects):
        color = SAFE if revealed[i] else BTN_BG
        pygame.draw.rect(screen, color, r)

    # draw score
    score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
