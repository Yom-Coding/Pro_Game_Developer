import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/space_background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
spaceship_height = 50
spaceship_width = 50
red_spaceship = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/spaceship_red.png")
red_spaceship = pygame.transform.scale(red_spaceship, (spaceship_height, spaceship_width))
red_spaceship = pygame.transform.rotate(red_spaceship, 90)
yellow_spaceship = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/spaceship_yellow.png")
yellow_spaceship = pygame.transform.scale(yellow_spaceship, (spaceship_height, spaceship_width))
yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 270)
def main():
    run = True
    while run:
        screen.blit(background, (0,0))
        screen.blit(red_spaceship, (200,HEIGHT/2 ))
        screen.blit(yellow_spaceship, (700, HEIGHT/2))
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

main()