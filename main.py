import pygame
from bird import Bird
from floor import Base
from sys import exit


pygame.init()

screen = pygame.display.set_mode((450,650))
clock = pygame.time.Clock()
running = True

background_surf = pygame.transform.scale(pygame.image.load("sprites/background-day.png").convert_alpha(), (450,750))
background_base = pygame.transform.scale(pygame.image.load("sprites/base.png").convert_alpha(), (450,100))
base_rect = background_base.get_rect(bottomleft = (0,690))

# | ---------- BIRD------------|
all_birds = pygame.sprite.GroupSingle()
a_bird = Bird()
all_birds.add(a_bird)

#|----------- FLOOR ------------|
all_floors = pygame.sprite.Group()
a_floor_1 = Base(0,690)
a_floor_2 = Base(450, 690)
all_floors.add(a_floor_1, a_floor_2) 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and a_bird.start == False:
                a_bird.start = True
                a_bird.falling = True
            if event.key == pygame.K_SPACE and a_bird.falling == True:
                a_bird.fly_speed = 0
                a_bird.falling = False
    


    screen.fill("black")
    screen.blit(background_surf, (0,0))
    # screen.blit(background_base, base_rect)

    all_birds.draw(screen)
    all_birds.update()

    all_floors.draw(screen)
    all_floors.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()