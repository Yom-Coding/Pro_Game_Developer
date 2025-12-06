import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))


line = False      
run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position_one = pygame.mouse.get_pos()
            print(position_one)
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
                position_two = pygame.mouse.get_pos()
                print(position_two)
                pygame.draw.line(screen, (255, 255, 255), position_one, position_two)
                drawing = False
                pygame.display.update()
