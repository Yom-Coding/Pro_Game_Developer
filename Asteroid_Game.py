import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Asteroids(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Space Invaders/images_and_assets/image.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = 0





background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/space.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/image/rocket.jpg")
rocket = pygame.transform.scale(rocket, (100, 100))
clock = pygame.time.Clock()


rocket_x = WIDTH//2
rocket_y = 100
rocket_width = 100
rocket_height = 100

asteroid_x = HEIGHT
asteroid_y = 100

rocket_rect = pygame.Rect(rocket_x, rocket_y, rocket_width, rocket_height)
score = 0
font = pygame.font.SysFont(None, 36)

asteroids = []
asteroid_radius = 20
asteroid_speed = 3

last_spawn = pygame.time.get_ticks()
spawn_delay = 2000

start_time = time.time()

asteroid_group = pygame.sprite.Group()
for i in range(5):
    asteroid1 = Asteroids()
    asteroid_group.add(asteroid1)










run = True
while run:
    screen.blit(background, (0, 0))
    screen.blit(rocket, (rocket_rect.x, rocket_rect.y))
    asteroid_group.draw(screen)

  
    mouse_x, mouse_y = pygame.mouse.get_pos()

    rocket_rect.x = mouse_x - rocket_width // 2
    rocket_rect.y = mouse_y - rocket_height // 2








    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()




     
    

pygame.quit()