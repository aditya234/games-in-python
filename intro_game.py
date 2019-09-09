import pygame

##initialize pygame
pygame.init()

win = pygame.display.set_mode((1000, 500))

pygame.display.set_caption('A demo Game in python')

x = 50
y = 425
width = 40
height = 60
velocity = 5

# creating main loop for the game
run = True

while (run):
    pygame.time.delay(100)
    # event loop
    # checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # getting key press events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 1000 - width - velocity:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
        print('Y = {0} and velocity = {1}'.format(y, velocity))
    if keys[pygame.K_DOWN] and y < 500 - velocity - height:
        y += velocity
        print('Y = {0} and velocity = {1}'.format(y, velocity))

    # filling old canvas to only display the new one
    # We do this so that changes can be visible
    win.fill((0, 0, 0))
    #
    pygame.draw.rect(win, (235, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
