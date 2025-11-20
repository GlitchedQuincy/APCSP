import pygame as pg

pg.init()

# Window dimensions
WIDTH, HEIGHT = 1000, 800

# Sidebar width (left panel where controls live)
SIDEBAR_WIDTH = 200

screen = pg.display.set_mode((WIDTH, HEIGHT)) 
pg.display.set_caption("paint")

# Background color for canvas area
BG_COLOR = (250, 250, 250)

# Rect that defines the drawing canvas (right side)
canvas_rect = pg.Rect(SIDEBAR_WIDTH, 0, WIDTH - SIDEBAR_WIDTH, HEIGHT)

# Brush state
brush_size = 30
MIN_BRUSH, MAX_BRUSH = 5, 100
current_color = (0, 0, 0)

# Color swatches shown in sidebar: (rect_tuple, color)
color_swatches = [((20, 20 + i * 50, 40, 40), c) for i, c in enumerate([
    (0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,255), (255,255,0), (128,0,128)
])]

# Simple '+' and '-' buttons for changing brush size
dec_button = pg.Rect(20, 380, 80, 30)
inc_button = pg.Rect(110, 380, 80, 30)

font = pg.font.SysFont(None, 22)

# Fill once so drawings persist without redrawing entire screen each frame
screen.fill(BG_COLOR)
# Draw sidebar background
pg.draw.rect(screen, (230, 230, 230), (0, 0, SIDEBAR_WIDTH, HEIGHT))
pg.display.update()

def draw_sidebar():
    """Draw the left-hand sidebar (colors, size buttons, preview)."""
    pg.draw.rect(screen, (230, 230, 230), (0, 0, SIDEBAR_WIDTH, HEIGHT))

    # Title
    screen.blit(font.render("Colors", True, (40,40,40)), (20, 0))

    # Color swatches
    for rect_t, col in color_swatches:
        r = pg.Rect(rect_t)
        pg.draw.rect(screen, col, r)
        pg.draw.rect(screen, (100,100,100), r, 2)
        # highlight selected color
        if col == current_color:
            pg.draw.rect(screen, (255,255,255), r.inflate(6,6), 3)

    # Brush size controls
    screen.blit(font.render("Brush size", True, (40,40,40)), (20, 360))

    pg.draw.rect(screen, (200,200,200), dec_button)
    pg.draw.rect(screen, (100,100,100), dec_button, 2)
    screen.blit(font.render("-", True, (40,40,40)), (dec_button.x + 34, dec_button.y + 4))

    pg.draw.rect(screen, (200,200,200), inc_button)
    pg.draw.rect(screen, (100,100,100), inc_button, 2)
    screen.blit(font.render("+", True, (40,40,40)), (inc_button.x + 34, inc_button.y + 4))

    # Show current brush size
    size_label = font.render(f"{brush_size}px", True, (40,40,40))
    screen.blit(size_label, (SIDEBAR_WIDTH // 2 - size_label.get_width() // 2, 420))

    # Preview of current brush
    screen.blit(font.render("Preview", True, (40,40,40)), (20, 450))
    preview_center = (SIDEBAR_WIDTH // 2, 540)
    pg.draw.circle(screen, current_color, preview_center, brush_size)
    pg.draw.circle(screen, (100,100,100), preview_center, brush_size, 1)

# initial sidebar draw
draw_sidebar()
pg.display.update()

clock = pg.time.Clock()
running = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

        elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos
            # Click inside sidebar?
            if mx < SIDEBAR_WIDTH:
                # pick a swatch if clicked
                for rect_t, col in color_swatches:
                    if pg.Rect(rect_t).collidepoint((mx, my)):
                        current_color = col
                        draw_sidebar()
                        pg.display.update()
                        break
                # size buttons
                if dec_button.collidepoint((mx, my)):
                    brush_size = max(MIN_BRUSH, brush_size - 5)
                    draw_sidebar(); pg.display.update()
                elif inc_button.collidepoint((mx, my)):
                    brush_size = min(MAX_BRUSH, brush_size + 5)
                    draw_sidebar(); pg.display.update()
            else:
                # Draw on canvas only
                if canvas_rect.collidepoint((mx, my)):
                    pg.draw.circle(screen, current_color, (mx, my), brush_size)
                    pg.display.update()

        elif e.type == pg.MOUSEMOTION and e.buttons[0]:
            mx, my = e.pos
            # Draw while dragging, but only if pointer is in canvas area (not sidebar)
            if mx >= SIDEBAR_WIDTH:
                pg.draw.circle(screen, current_color, (mx, my), brush_size)
                pg.display.update()

        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_c:
                # clear canvas
                pg.draw.rect(screen, BG_COLOR, canvas_rect)
                draw_sidebar(); pg.display.update()
            elif e.key == pg.K_UP:
                brush_size = min(MAX_BRUSH, brush_size + 5); draw_sidebar(); pg.display.update()
            elif e.key == pg.K_DOWN:
                brush_size = max(MIN_BRUSH, brush_size - 5); draw_sidebar(); pg.display.update()

    # limit loop to reasonable frame rate
    clock.tick(15)

pg.quit()