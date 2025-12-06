import pygame
pygame.init()
WIDTH = 600
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

image2 = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")
rocket = pygame.Rect(WIDTH/2, HEIGHT/2, 150,219)
run = True 

while run:
    screen.blit(image, (0,0))
    screen.blit(image2, (rocket.x, rocket.y))
    pygame.display.update()










    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.y = rocket.y - 5
            if event.key == pygame.K_LEFT:
                rocket.x = rocket.x - 5
            elif event.key == pygame.K_RIGHT:
                rocket.x = rocket.x + 5

