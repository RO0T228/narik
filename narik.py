import pygame
import time

pygame.init()
pygame.mixer.music.load("image/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)
wins = pygame.mixer.Sound("image/win_sound1.mp3")
loses = pygame.mixer.Sound('image/lose_sound1.mp3')
pygame.display.set_caption("нарик")

screen = pygame.display.set_mode((500, 700))
icon = pygame.image.load("image/рей.ico")
pygame.display.set_icon(icon)
hand = pygame.image.load('image/hand.png')
win = pygame.image.load('image/win1.png')
lose = pygame.image.load('image/lose.png')
syringe = pygame.image.load(f'image/syringe0.png')

syringe_rect = syringe.get_rect()
clock = pygame.time.Clock()
FPS = 100
running = True
x, y = 0, 10
speed = 2
flag = True

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(hand, (0, 0))
    screen.blit(syringe, (x, y))
    keys = pygame.key.get_pressed()
    x += speed

    if x <= 0 or x >= screen.get_width() - syringe.get_width():
        speed = -speed
    if keys[pygame.K_q]:
        y, x, speed = 0, 10, 2
    if keys[pygame.K_SPACE]:
        speed = 0
        y += 3
    if keys[pygame.K_ESCAPE]:
        break

    syringe_rect.x = x
    syringe_rect.y = y

    if syringe_rect.y + 236 >= 567:
        if 195 <= syringe_rect.x + 22 <= 198 or 215 <= syringe_rect.x + 22 <= 219 or 233 <= syringe_rect.x + 22 <= 240 or 266 <= syringe_rect.x + 22 <= 271 or 280 <= syringe_rect.x + 22 <= 285:
            pygame.mixer.music.set_volume(0.5)
            wins.play()
            time.sleep(0.3)
            screen.blit(win, (0, 0))
            pygame.display.flip()
            time.sleep(2)
            pygame.mixer.music.set_volume(1.0)
            x, y, speed = 0, 10, 2
        else:
            pygame.mixer.music.set_volume(0.5)
            loses.play()
            time.sleep(0.3)
            screen.blit(lose, (0, 0))
            pygame.display.flip()
            time.sleep(2.5)
            pygame.mixer.music.set_volume(1.0)
            x, y, speed = 0, 10, 2

    pygame.display.flip()
    clock.tick(FPS)

my_telegram = "https://t.me/mtvgrshn"
