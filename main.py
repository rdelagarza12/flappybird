import pygame
from bird import Bird
from sys import exit

pygame.init

screen = pygame.display.set_mode((450,650))
clock = pygame.time.Clock()
running = True

background_surf = pygame.transform.scale(pygame.image.load("sprites/background-day.png").convert_alpha(), (450,750))
background_base = pygame.transform.scale(pygame.image.load("sprites/base.png").convert_alpha(), (450,100))
base_rect = background_base.get_rect(bottomleft = (0,690))


all_birds = pygame.sprite.GroupSingle()
a_bird = Bird()
all_birds.add(a_bird)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    screen.blit(background_surf, (0,0))
    screen.blit(background_base, base_rect)
    all_birds.draw(screen)
    all_birds.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()