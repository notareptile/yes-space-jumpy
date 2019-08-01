import pygame, sys, random
from awesome import Ground
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

player = Player((48, 57, 97))
grounds = []

pygame.time.set_timer(pygame.USEREVENT+1, 3000)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("Thanks for playing!")
    pygame.display.flip()
    screen.fill((48, 21, 61))