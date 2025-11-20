import pygame

pygame.init()

SCREEN_SIZE = (1000, 1000)
BG = (30, 30, 30)
BTN_BG = (50, 50, 215)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("mine gambling")
clock = pygame.time.Clock()
running = True
h= 100
w=100
x=100
y=100
one_rect=pygame.Rect(x+175*0, y+175*0, h, w)
two_rect=pygame.Rect(x+175*1, y+175*0, h, w)
three_rect=pygame.Rect(x+175*2, y+175*0, h, w)
four_rect=pygame.Rect(x+175*3, y+175*0, h, w)
five_rect=pygame.Rect(x+175*4, y+175*0, h, w)
six_rect=pygame.Rect(x+175*0, y+175*1, h, w)
seven_rect=pygame.Rect(x+175*1, y+175*1, h, w)
eight_rect=pygame.Rect(x+175*2, y+175*1, h, w)
nine_rect=pygame.Rect(x+175*3, y+175*1, h, w)
ten_rect=pygame.Rect(x+175*4, y+175*1, h, w)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # left mouse button pressed
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if one_rect.collidepoint(event.pos):
                print("1")
            elif two_rect.collidepoint(event.pos):
                print("2")
            elif three_rect.collidepoint(event.pos):
                print("3")    
            elif four_rect.collidepoint(event.pos):
                print("4")        
            elif five_rect.collidepoint(event.pos):
                print("5")
            elif six_rect.collidepoint(event.pos):
                print("6")
            elif seven_rect.collidepoint(event.pos):
                print("7")
            elif eight_rect.collidepoint(event.pos):
                print("8")    
            elif nine_rect.collidepoint(event.pos):
                print("9")        
            elif ten_rect.collidepoint(event.pos):
                print("10")    
        
    screen.fill(BG)
    pygame.draw.rect(screen, BTN_BG, one_rect)
    pygame.draw.rect(screen,BTN_BG, two_rect)
    pygame.draw.rect(screen,BTN_BG, three_rect)
    pygame.draw.rect(screen,BTN_BG, four_rect)
    pygame.draw.rect(screen,BTN_BG, five_rect)
    pygame.draw.rect(screen, BTN_BG, six_rect)
    pygame.draw.rect(screen,BTN_BG, seven_rect)
    pygame.draw.rect(screen,BTN_BG, eight_rect)
    pygame.draw.rect(screen,BTN_BG, nine_rect)
    pygame.draw.rect(screen,BTN_BG, ten_rect)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
