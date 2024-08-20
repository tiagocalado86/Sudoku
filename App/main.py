import pygame

#setup
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

def row(top: int):
    left = 50 #max 450
    while left < 450:
        pygame.draw.rect(screen, "black", pygame.Rect(left, top, 100, 100), width=2)
        left += 50


def drawGrid():
    top = 50 #max 450
    for i in range(9):
        row(top)
        top += 50


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    screen.fill("white")
    #ui
    drawGrid()


    #verify


    #resolve


    #render
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
