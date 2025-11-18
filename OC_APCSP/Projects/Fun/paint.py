import pygame as pg

# Set up display
pg.init()
screen = pg.display.set_mode((1000, 800)) #800x800 window
running = True 
pg.display.set_caption("paint") 

size = 30
color = (0, 0, 0) 

# fill once so drawings persist
screen.fill((250, 250, 250))
pg.display.update()

while running:
    # Process events first
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            pg.draw.circle(screen, color, (mouseX, mouseY), size)
            pg.display.update()
        elif event.type == pg.MOUSEMOTION and event.buttons[0]:
            # draw while dragging with the left mouse button held
            pg.draw.circle(screen, color, event.pos, size)
            pg.display.update()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                # Clear the screen when 'c' is pressed
                screen.fill((color))
                pg.display.update()
            elif event.key == pg.K_UP:
                size += 5  # Increase brush size
            elif event.key == pg.K_DOWN:
                size = max(5, size - 5)  # Decrease brush size but not below 5
            elif event.key == pg.K_r:
                color = (255, 0, 0)  # Change color to red
            elif event.key == pg.K_g:
                color = (0, 255, 0)  # Change color to green
            elif event.key == pg.K_b:
                color = (0, 0, 255)  # Change color to blue
            elif event.key == pg.K_d:
                color = (0, 0, 0)    # Change color to black
            elif event.key == pg.K_w:
                color = (250, 250, 250)    # Change color to white