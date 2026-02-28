import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0

background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/recycle_bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
run = True

class Bin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/bin.png")
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()


bin = Bin()

bin_group = pygame.sprite.Group()
bin_group.add(bin)

while run:
    screen.blit(background, (0, 0))
    
    bin_group.draw(screen)

    pygame.display.update()







    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            pygame.quit()