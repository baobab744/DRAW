import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH_WIN, HEIGHT_WIN = 800, 600
collide = False
collide1 = False
num = 0
num1 = 0
speed_x, speed_y = 5, 5
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

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.MOUSEMOTION:
            rect1.center = e.pos
    ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
        speed_x = -speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
        speed_y = -speed_y
    screen.fill(BG)

    COLOR = RED if collide or collide1 else BLUE

    def move(speed_x, speed_y)
        if ball_rect.left < 0 or ball_rect.right > WIDTH_WIN:
            speed_x = -speed_x
        if ball_rect.top < 0 or ball_rect.bottom > HEIGHT_WIN:
            speed_y = -speed_y

    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))
    screen.blit(surface, rect1)
    screen.blit(ball, ball_rect)
    screen.blit(font.render(str(num), True, BLACK), (40, 25))
    screen.blit(font.render(str(num1), True, BLACK), (WIDTH_WIN - 40, 25))
    if rect1.colliderect(rect2):
        collide = True
        if COLOR == BLUE:
            num += 1
    else:
        collide = False
    if ball_rect.colliderect(rect2):
        collide1 = True
        if COLOR == BLUE:
            num1 += 1
    else:
        collide1 = False

    pygame.display.update()
    clock.tick(FPS)
