import pygame
import time 
pygame.init()
WIDTH = 500
HEIGHT = 500


screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("cake image.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

image2 = pygame.image.load("card image.jpg")
image2 = pygame.transform.scale(image2, (WIDTH, HEIGHT))

image3 = pygame.image.load("gift image.jpg")
image3 = pygame.transform.scale(image3, (WIDTH, HEIGHT))


run = True

f = pygame.font.SysFont("Calibri",16)
text = f.render("Happy Birthday!", True, (0,0,0))
text2 = f.render("Hope You Have a Good Day", True, (0,0,0))
text2rect = text2.get_rect()
text2rect.center = WIDTH/2, HEIGHT/2
text3 = f.render("Wishes from Yom!", True, (0,0,0))


while run:
    screen.fill((255,0,0))
    screen.blit(image, (0, 0))
    screen.blit(text, (200,430))
    pygame.display.update()
    time.sleep(3)
    screen.blit(image2, (0,0))
    screen.blit(text2, text2rect)
    pygame.display.update()
    time.sleep(3)
    screen.blit(image3, (0,0))
    screen.blit(text3, (50,50))
    pygame.display.update()
    time.sleep(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
