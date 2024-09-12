import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1250,690))

spaceship = pygame.image.load("lesson 5/photo/spaceship.png")
space = pygame.image.load("lesson 5/photo/space bg.png")
space = pygame.transform.scale(space,(1250,690))

shipx = 625
shipy = 345

font = pygame.font.SysFont("Times New Roman",36)

while shipy<600:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                shipy -= 20
             if event.key == pygame.K_s:
                shipy += 5
             if event.key == pygame.K_a:
                shipx -= 5
             if event.key == pygame.K_d:
                shipx += 5
    screen.fill("black")
    screen.blit(space,(0,0))
    screen.blit(spaceship,(shipx,shipy))
    shipy += 0.2
    pygame.display.update()
else:
    text = font.render("you lose.",True,"white")
    screen.blit(space,(0,0))
    screen.blit(text,(650,200))
    pygame.display.update()
    time.sleep(5)