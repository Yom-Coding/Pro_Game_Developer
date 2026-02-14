import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
run = True
class Rectangle:

    def __init__(self, dimensions, color):
        self.dimensions = dimensions
        self.color = color


    def draw_rectangle(self):
        pygame.draw.rect(screen, self.color, self.dimensions)



rectangle1 = Rectangle((WIDTH//2, HEIGHT//2, 40, 60), (255,0,0))
rectangle1.draw_rectangle()

rectangle2 = Rectangle((WIDTH - 200, HEIGHT- 200, 60, 20), (0,255,0))
rectangle2.draw_rectangle()

rectangle3 = Rectangle((WIDTH- 400, HEIGHT-400, 100, 20), (0,0,255))
rectangle3.draw_rectangle()




pygame.display.update()

while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                pygame.quit()

    