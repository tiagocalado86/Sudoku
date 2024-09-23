import pygame

#setup
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

def row(top: int):
    left = 50 #max 450
    while left < 450:
        pygame.draw.rect(screen, "black", pygame.Rect(left, top, 100, 100), 1)
        left += 50


def drawGrid():
    top = 50 #max 450
    for i in range(8):
        row(top)
        top += 50
    #red lines
    pygame.draw.lines(screen, "red", False, [(200, 50), (200, 500)], 3)
    pygame.draw.lines(screen, "red", False, [(350, 50), (350, 500)], 3)
    pygame.draw.lines(screen, "red", False, [(50, 200), (500, 200)], 3)
    pygame.draw.lines(screen, "red", False, [(50, 350), (500, 350)], 3)

def drawButton(text: str):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text, True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (110, 650)
    screen.blit(text, textRect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    #ui
    screen.fill("white")
    drawGrid()
    drawButton("Finish")

    buttonFinish = pygame.draw.rect(screen, "black", pygame.Rect(50, 625, 125, 50), 2)

    #check for the mouse button down event
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if buttonFinish.collidepoint(event.pos):
            print("Button clicked!")


    #verify


    #resolve


    #render
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
