import pygame, sys, random
from awesome import Ground
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()

player = Player((48, 57, 97))
grounds = []

pygame.time.set_timer(pygame.USEREVENT+1, 1200)

def addground(xleft, yup, yvelocity, width):
    global grounds
    grounds.append(Ground(xleft, yup, yvelocity, width, (0, 0, 0)))

def touchingground():
    global grounds
    for awesome in grounds:
        if player.yup + player.size < awesome.yup + 21 and player.xleft + player.size > awesome.xleft and player.xleft < awesome.xleft + awesome.width and player.yup > awesome.yup - 20:
            return True
    return False

def init():
    addground(300, 50, 2, 200)

init()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("Thanks for playing!")
        if event.type == pygame.USEREVENT+1:
            addground(random.randint(0, 700), -30, 2, random.randint(50, 300))
            addground(random.randint(0, 700), -30, 2, random.randint(50, 300))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and touchingground():
                player.jump(17)
            if event.key == pygame.K_LEFT:
                player.xvelocity -= 10
            if event.key == pygame.K_RIGHT:
                player.xvelocity += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.xvelocity = 0
            if event.key == pygame.K_RIGHT:
                player.xvelocity = 0
    for awesome in grounds:
        pygame.draw.rect(screen, awesome.color, pygame.Rect(awesome.xleft, awesome.yup, awesome.width, awesome.height), 0)
        awesome.move()
        if awesome.checkdestroy():
            grounds.remove(awesome)
    pygame.draw.rect(screen, player.color, pygame.Rect(player.xleft, player.yup, player.width, player.height), 0)
    if not touchingground():
        player.applygravity(0.5)
    else:
        player.yvelocity = 2
    player.checkdestory()
    if player.shoulddestroy:
        sys.exit("GG")
    player.move()
    pygame.display.flip()
    screen.fill((48, 21, 61))