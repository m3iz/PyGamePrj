import pygame 

pygame.init() 
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
start = True
x = 0
y = 0
her = 50/10
dx = 0
w = 75
h = 120
onGround = False
while start == 1:
    pygame.time.delay(5)
    if onGround:
        if dx < 0:
            dx -= 15
    else:
        if (dx < 100)&(onGround==False):
            dx += her/10
            print(dx)
        y += dx ##gravity


    if y > 850:
        y = 855.1
    if (y >= 855)&(y <= 856):
        onGround=True
##Клавиши
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= her
    if keys[pygame.K_RIGHT]:
        x += her

    if keys[pygame.K_UP]:
        if onGround:
            onGround=False
            dx = -15

    ##Конец управления
    for huy in pygame.event.get():
        if huy.type == pygame.QUIT:
            start = False

    ##DRAW
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 255), (x, y, w, h))

    pygame.display.update()
