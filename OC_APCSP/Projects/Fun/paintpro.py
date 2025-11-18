import pygame as pg

# Set up display
pg.init()
WIDTH, HEIGHT = 1000, 800
SIDEBAR_W = 200

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("paint")

bg_color = (250, 250, 250)
canvas_rect = pg.Rect(SIDEBAR_W, 0, WIDTH - SIDEBAR_W, HEIGHT)

size = 30
min_size, max_size = 5, 100
color = (0, 0, 0)

# color swatches (placed in sidebar)
swatches = [
    ( (20, 20, 40, 40), (0, 0, 0) ),       # black
    ( (20, 70, 40, 40), (255, 0, 0) ),     # red
    ( (20, 120, 40, 40), (0, 255, 0) ),    # green
    ( (20, 170, 40, 40), (0, 0, 255) ),    # blue
    ( (20, 220, 40, 40), (255, 255, 255) ),# white
    ( (20, 270, 40, 40), (255, 255, 0) ),  # yellow
    ( (20, 320, 40, 40), (128, 0, 128) ),  # purple
]

# size slider
slider_rect = pg.Rect(20, 380, SIDEBAR_W - 40, 24)
slider_handle_w = 12
dragging_size = False

# initial draw
screen.fill(bg_color)
pg.draw.rect(screen, (230, 230, 230), (0, 0, SIDEBAR_W, HEIGHT))  # sidebar background
pg.display.update()

running = True
clock = pg.time.Clock()

def draw_sidebar():
    # sidebar background
    pg.draw.rect(screen, (230, 230, 230), (0, 0, SIDEBAR_W, HEIGHT))
    # title
    font = pg.font.SysFont(None, 22)
    screen.blit(font.render("Colors", True, (40,40,40)), (20, 0))
    # swatches
    for rect_t, col in swatches:
        r = pg.Rect(rect_t)
        pg.draw.rect(screen, col, r)
        pg.draw.rect(screen, (100,100,100), r, 2)
        if col == color:
            pg.draw.rect(screen, (255,255,255), r.inflate(6,6), 3)
    # size slider label
    screen.blit(font.render("Brush size", True, (40,40,40)), (20, 360))
    # slider track
    pg.draw.rect(screen, (200,200,200), slider_rect)
    # handle position mapped from size
    t = (size - min_size) / (max_size - min_size)
    handle_x = slider_rect.x + int(t * (slider_rect.w - slider_handle_w))
    handle_rect = pg.Rect(handle_x, slider_rect.y - 4, slider_handle_w, slider_rect.h + 8)
    pg.draw.rect(screen, (120,120,120), handle_rect)
    # preview
    screen.blit(font.render("Preview", True, (40,40,40)), (20, 430))
    preview_center = (SIDEBAR_W // 2, 500)
    pg.draw.circle(screen, color, preview_center, size)
    pg.draw.circle(screen, (100,100,100), preview_center, size, 1)

# draw initial sidebar
draw_sidebar()
pg.display.update()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if event.button == 1:
                # clicked inside sidebar?
                if mx < SIDEBAR_W:
                    # check swatches
                    for rect_t, col in swatches:
                        if pg.Rect(rect_t).collidepoint((mx, my)):
                            color = col
                            draw_sidebar()
                            pg.display.update()
                            break
                    # check slider
                    if slider_rect.collidepoint((mx, my)):
                        dragging_size = True
                else:
                    # draw on canvas
                    if canvas_rect.collidepoint((mx, my)):
                        pg.draw.circle(screen, color, (mx, my), size)
                        pg.display.update()
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                dragging_size = False

        elif event.type == pg.MOUSEMOTION:
            mx, my = event.pos
            if event.buttons[0]:
                if dragging_size:
                    # map mouse x within slider to size
                    rel_x = max(0, min(mx - slider_rect.x, slider_rect.w))
                    t = rel_x / slider_rect.w
                    size = int(min_size + t * (max_size - min_size))
                    draw_sidebar()
                    pg.display.update()
                else:
                    # drawing while dragging on canvas only
                    if mx >= SIDEBAR_W:
                        pg.draw.circle(screen, color, (mx, my), size)
                        pg.display.update()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                # clear canvas only
                pg.draw.rect(screen, bg_color, canvas_rect)
                draw_sidebar()
                pg.display.update()
            elif event.key == pg.K_UP:
                size = min(max_size, size + 5)
                draw_sidebar()
                pg.display.update()
            elif event.key == pg.K_DOWN:
                size = max(min_size, size - 5)
                draw_sidebar()
                pg.display.update()
            # optional quick color keys
            elif event.key == pg.K_r:
                color = (255,0,0); draw_sidebar(); pg.display.update()
            elif event.key == pg.K_g:
                color = (0,255,0); draw_sidebar(); pg.display.update()
            elif event.key == pg.K_b:
                color = (0,0,255); draw_sidebar(); pg.display.update()
            elif event.key == pg.K_d:
                color = (0,0,0); draw_sidebar(); pg.display.update()
            elif event.key == pg.K_w:
                color = bg_color; draw_sidebar(); pg.display.update()

    clock.tick(120)

pg.quit()