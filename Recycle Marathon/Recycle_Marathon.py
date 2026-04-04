import pygame
import random
import time

pygame.init()

WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0
font = pygame.font.SysFont("Calibri", 20)
background = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/recycle_bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
run = True
start_time = 0
time_passed = 0
time_limit = 30
score_limit = 20
score = 0
class Bin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/bin.png")
        self.image = pygame.transform.scale(self.image, (20, 25))
        self.rect = self.image.get_rect()
        
    def update(self, keys):
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x = self.rect.x + 1
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = self.rect.x - 1
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y = self.rect.y - 1
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y = self.rect.y + 1

class Recyable_Trash(pygame.sprite.Sprite):
    objects = ["bag.png", "box1.png", "pencil.png"]
    def __init__(self):
        super().__init__()
        random_image = random.choice(self.objects)
        self.image = pygame.image.load ("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/" + random_image)
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(50, HEIGHT - 50)

class Non_Recyable_Trash(pygame.sprite.Sprite):
    objects1 = ["plastic_bag.png"]
    def __init__(self):
        super().__init__()
        random_image1 = random.choice(self.objects1)
        self.image = pygame.image.load ("/Users/yompatel/Desktop/Jet Learn/Pro Game Developer/Recycle Marathon/Images/" + random_image1)
        self.image = pygame.transform.scale(self.image, (20, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(50, HEIGHT - 50)


bin_group = pygame.sprite.Group()
bin = Bin()
bin_group.add(bin)

recyable_trash_group = pygame.sprite.Group()
for i in range(50):
    recyable_trash = Recyable_Trash()
    recyable_trash_group.add(recyable_trash)

non_recyable_trash_group = pygame.sprite.Group()
for i in range (20):
    non_recyable_trash = Non_Recyable_Trash()
    non_recyable_trash_group.add(non_recyable_trash)

start_time = time.time()





while run:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            pygame.quit()

    time_passed = time.time() - start_time
    if time_passed < time_limit:
        bin_group.draw(screen)
        recyable_trash_group.draw(screen)
        non_recyable_trash_group.draw(screen)
        keys_pressed = pygame.key.get_pressed()
        bin_group.update(keys_pressed)
        recyable_trash_list = pygame.sprite.spritecollide(bin, recyable_trash_group, True)
        non_recyable_trash_list = pygame.sprite.spritecollide(bin, non_recyable_trash_group, True)
        score = score + len(recyable_trash_list) - 3* len(non_recyable_trash_list)
        print(recyable_trash_list)
        score_text = font.render("Your Score is " + str(score), True, (0,0,0))
        screen.blit(score_text, (WIDTH - 150,10))
    else:
        if score >= score_limit:
            game_over_text = font.render("You Have Won", True, (0,0,0))
            screen.blit(game_over_text, (WIDTH/2, HEIGHT/2))
        else:
            lose_text = font.render("You Have Lost", True, (0,0,0))
            screen.blit(lose_text, (WIDTH/2, HEIGHT/2))
    
    pygame.display.update()

