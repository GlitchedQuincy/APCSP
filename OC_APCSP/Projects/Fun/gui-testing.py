import pygame as pg
import sys
import random
import os
import numpy as np

# Initialize Pygame
pg.init()

# Set up display
screen = pg.display.set_mode((800, 800)) #800x800 window
runing = True #this lets me create a loop
pg.display.set_caption("tic tac toe") # title 

#start ai 
# load board image once (use script dir to build a reliable path) 
script_dir = os.path.dirname(__file__)
board_path = os.path.join(script_dir, "Board.png")  # file is in the same folder as this script
sprite_image = pg.image.load(board_path).convert_alpha()
sprite_rect = sprite_image.get_rect()
sprite_rect.center = (400, 400)
# load X/O sprites
bx_path = os.path.join(script_dir, "BX.png")
bo_path = os.path.join(script_dir, "BO.png")
try:
    bx_image = pg.image.load(bx_path).convert_alpha()
    bo_image = pg.image.load(bo_path).convert_alpha()
    cell_size = 800 // 3
    target = (int(cell_size * 0.8), int(cell_size * 0.8))
    bx_image = pg.transform.smoothscale(bx_image, target)
    bo_image = pg.transform.smoothscale(bo_image, target)
except Exception as e:
    print("Could not load BX/BO images:", e)
    bx_image = None
    bo_image = None
#end ai (the images were not loading properly)

# set up console board
board = np.zeros((3, 3), dtype=int) # make a 3x3 numpy array filled with zeros
def mark_square(row, col, player): 
    board[row][col] = player #mark the numpy array at row,col with player number (1 or 2)
def available_square(row, col):
    return board[row][col] == 0 #check if the square is available (0 means empty)
def is_board_full(): 
    for row in range(3): 
        for col in range(3):
            if board[row][col] == 0: #goes through whole board 
                return False
    return True

# draw X / O based on the console board
def draw_marks():
    cell = 800 // 3 #
    for r in range(3):
        for c in range(3):
            val = board[r][c]
            cx = int(c * cell + cell / 2)
            cy = int(r * cell + cell / 2)
            if val == 1:
                if bx_image:
                    rect = bx_image.get_rect(center=(cx, cy))
                    screen.blit(bx_image, rect)
                else:
                    off = int(cell * 0.3)
                    pg.draw.line(screen, (200, 30, 30), (cx - off, cy - off), (cx + off, cy + off), 10)
                    pg.draw.line(screen, (200, 30, 30), (cx - off, cy + off), (cx + off, cy - off), 10)
            elif val == 2:
                if bo_image:
                    rect = bo_image.get_rect(center=(cx, cy))
                    screen.blit(bo_image, rect)
                else:
                    radius = int(cell * 0.35)
                    pg.draw.circle(screen, (30, 30, 200), (cx, cy), radius, 10)

def check_winner():
    """
    Return:
      - 1 or 2 : winning player
      - 0       : draw (board full, no winner)
      - None    : no winner yet
    Also returns a list of winning cell coordinates for highlighting.
    """
    # rows
    for r in range(3):
        if board[r,0] != 0 and board[r,0] == board[r,1] == board[r,2]:
            return board[r,0], [(r,0),(r,1),(r,2)]
    # cols
    for c in range(3):
        if board[0,c] != 0 and board[0,c] == board[1,c] == board[2,c]:
            return board[0,c], [(0,c),(1,c),(2,c)]
    # diagonals
    if board[0,0] != 0 and board[0,0] == board[1,1] == board[2,2]:
        return board[0,0], [(0,0),(1,1),(2,2)]
    if board[0,2] != 0 and board[0,2] == board[1,1] == board[2,0]:
        return board[0,2], [(0,2),(1,1),(2,0)]
    # draw
    if np.all(board != 0):
        return 0, []
    return None, []

# track game state
game_over = False
winner = None
winning_cells = []

# Retry button setup
font = pg.font.SysFont(None, 40)
retry_text_surf = font.render("Retry", True, (255, 255, 255))
retry_padding = 20
retry_w = retry_text_surf.get_width() + retry_padding
retry_h = retry_text_surf.get_height() + retry_padding
retry_rect = pg.Rect(0, 0, retry_w, retry_h)
retry_rect.center = (800 // 2, 800 - 60)

def reset_game():
    global board, game_over, winner, winning_cells, current_player
    board[:, :] = 0
    game_over = False
    winner = None
    winning_cells = []
    current_player = 1

# add a persistent player variable (1 or 2)
current_player = 1

# Main loop
while runing:
    # Fill the screen with a color (optional)
    screen.fill((250, 250, 250))

    # Process events first
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runing = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            # use float division and clamp to [0,2] to avoid index 3
            cell_size = 800 / 3
            clicked_row = min(int(mouseY / cell_size), 2)
            clicked_col = min(int(mouseX / cell_size), 2)

            if available_square(clicked_row, clicked_col) and not game_over:
                # mark with the current player
                mark_square(clicked_row, clicked_col, current_player)

                # check winner immediately after the move
                w, cells = check_winner()
                if w is not None:
                    game_over = True
                    winner = w
                    winning_cells = cells
                    if w == 0:
                        print("Draw")
                    else:
                        print(f"Player {w} wins! winning cells: {cells}")
                else:
                    # toggle player only if game continues
                    current_player = 2 if current_player == 1 else 1
                    print("player now:", current_player)
                print(board)
            # Retry button logic
            elif event.button == 1 and game_over and retry_rect.collidepoint(event.pos):
                reset_game()

    # draw the board background
    screen.blit(sprite_image, sprite_rect)

    # draw X/O based on the console board
    draw_marks()

    # highlight winning cells if game over and we have a winner (not a draw)
    if game_over and winner in (1,2) and winning_cells:
        cell = 800 // 3
        highlight_color = (255, 215, 0, 140)  # semi-transparent gold
        s = pg.Surface((cell, cell), pg.SRCALPHA)
        s.fill(highlight_color)
        for (r,c) in winning_cells:
            screen.blit(s, s.get_rect(topleft=(c*cell, r*cell)))

    # --- Hover ghost (new) ---
    # compute cell size and mouse cell
    cell_size = 800 / 3
    mx, my = pg.mouse.get_pos()
    hovered_row = max(0, min(int(my / cell_size), 2))
    hovered_col = max(0, min(int(mx / cell_size), 2))

    if available_square(hovered_row, hovered_col):
        # center of the hovered cell
        cx = int(hovered_col * (800 // 3) + (800 // 3) / 2)
        cy = int(hovered_row * (800 // 3) + (800 // 3) / 2)

        # show ghost using loaded sprites if available
        if current_player == 1:
            if bx_image:
                ghost = bx_image.copy()
                ghost.set_alpha(120)
                rect = ghost.get_rect(center=(cx, cy))
                screen.blit(ghost, rect)
            else:
                # draw semi-transparent X on a temporary surface
                s = pg.Surface((800 // 3, 800 // 3), pg.SRCALPHA)
                off = int((800 // 3) * 0.3)
                color = (200, 30, 30, 120)
                pg.draw.line(s, color, (off, off), (s.get_width() - off, s.get_height() - off), 10)
                pg.draw.line(s, color, (off, s.get_height() - off), (s.get_width() - off, off), 10)
                screen.blit(s, s.get_rect(center=(cx, cy)))
        else:
            if bo_image:
                ghost = bo_image.copy()
                ghost.set_alpha(120)
                rect = ghost.get_rect(center=(cx, cy))
                screen.blit(ghost, rect)
            else:
                s = pg.Surface((800 // 3, 800 // 3), pg.SRCALPHA)
                radius = int((800 // 3) * 0.35)
                color = (30, 30, 200, 120)
                pg.draw.circle(s, color, (s.get_width() // 2, s.get_height() // 2), radius, 10)
                screen.blit(s, s.get_rect(center=(cx, cy)))
    # --- end hover ghost ---

    # draw retry button if game over
    if game_over:
        pg.draw.rect(screen, (0, 0, 0), retry_rect)
        screen.blit(retry_text_surf, retry_text_surf.get_rect(center=retry_rect.center))

    # Update the display
    pg.display.flip()

# Clean up
pg.quit()
sys.exit()

