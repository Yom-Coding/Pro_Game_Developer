import pygame
pygame.init()
WIDTH = 600
HEIGHT = 500


direction = {"up":False, "left":False, "right":False}



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
            # This code is used for single button pressing as it just says if the the key is pressed then do this,
            # While if you want to hold it you have to write that once you press down it will do the action until let go
            # if event.key == pygame.K_UP:
            #     rocket.y = rocket.y - 5
            # if event.key == pygame.K_LEFT:
            #     rocket.x = rocket.x - 5
            # elif event.key == pygame.K_RIGHT:
            #     rocket.x = rocket.x + 5

            # For continous character movement:
            if event.key == pygame.K_UP:
                direction["up"] = True
            elif event.key == pygame.K_LEFT:
                direction["left"] = True
            # elif event.key == pygame.K_RIGHT:
            #     direction["right"] = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction["up"] = False
            elif event.key == pygame.K_LEFT:
                direction["left"] = False
            # elif event.key == pygame.K_RIGHT:
            #     direction["right"] = False
            


    if direction["up"]:
        rocket.y = rocket.y - 5
    if direction["left"]:
        rocket.x = rocket.x - 5
    # if direction["right"]:
    #     rocket.x = rocket.x + 5


    #direct method
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rocket.x = rocket.x + 5



    
