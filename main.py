import pygame
from sys import exit

pygame.init

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill("black")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()