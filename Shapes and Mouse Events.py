import pygame
pygame.init()
WIDTH = 500
HEIGHT = 500


screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

screen.fill((255,255,255))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), position, 5)
            pygame.display.update()
    


