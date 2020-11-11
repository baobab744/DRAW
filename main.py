import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 800, 600
collide = False
collide1 = False
num = 0
num1 = 0
speed = [5, 5]
FPS = 120
clock = pygame.time.Clock()

# Квадрат
rect_size = w, h = 70, 70
rect_pos = ((WIDTH_WIN - w) // 2, (HEIGHT_WIN - h) // 2)

# Круг
circle_radius = 35
circle_pos = (0, 0)

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BG = (128, 128, 128)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((WIDTH_WIN, HEIGHT_WIN))
font = pygame.font.Font(None, 32)

surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
rect1 = surface.get_rect()

ball = pygame.image.load('img/ball.png')
ball_rect = ball.get_rect(topleft=(0, 0))
print(ball_rect)

def abc(x, y)
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        speed[0] = -x
    elif ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed[1] = -y
    return ball_rect.move(speed)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos
    ball_rect = ball_rect.move(speed_x, speed_y)

    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))
    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(num), True, BLACK), (40, 25))
    screen.blit(font.render(str(num1), True, BLACK), (WIDTH_WIN - 40, 25))
    if rect1.colliderect(rect2):
        if not collide:
            num += 1
            collide = True
    else:
        collide = False
    if ball_rect.colliderect(rect2):
        if not collide1:
            num1 += 1
            collide1 = True
    else:
        collide1 = False
    ball_rect = abc(speed[0], speed[1])
    pygame.display.update()
    clock.tick(FPS)
