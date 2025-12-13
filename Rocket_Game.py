import pygame

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket_img = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")

run = True


rocket_x = WIDTH // 2
rocket_y = HEIGHT // 2

while run:
    screen.blit(background, (0, 0))
    screen.blit(rocket_img, (rocket_x, rocket_y))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    rocket_x = mouse_x
    rocket_y = mouse_y








    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()




    pygame.display.update()

