import pygame
from bird import Bird
from floor import Base
from pipe import Pipe
from number import Number
from sys import exit
import random


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

#|------------ PIPES -----------
top_pipes = pygame.sprite.Group()
top_pipe_1 = Pipe(408, -700, 180)
top_pipes.add(top_pipe_1)

bottom_pipes = pygame.sprite.Group()
bottom_pipe_1 = Pipe(500, 400, 0)
bottom_pipes.add(bottom_pipe_1)




#|----------- NUMBER --------------|
count = 0
all_numbers = pygame.sprite.Group()
a_number_1 = Number(225,100,count)
all_numbers.add(a_number_1)

count_by_one = 0
count_by_ten = 0
count_by_hundred = 0

#|----------- to check when the player has started playing
game_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            game_started = True
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

    if game_started:
        top_pipes.draw(screen)
        top_pipes.update()
        
        bottom_pipes.draw(screen)
        bottom_pipes.update()
        
        for pipe in top_pipes:
            if pipe.rect.x == 200:
                random_number = random.randint(200,500)
                new_top_pipe = Pipe(500, random_number, 0)
                new_bottom_pipe = Pipe(408, (random_number - 1100), 180)
                top_pipes.add(new_top_pipe)
                bottom_pipes.add(new_bottom_pipe)
            if pipe.rect.x == 100:
                if count_by_ten  == 0 and count_by_one <= 8 and count_by_hundred == 0:
                    count_by_one += 1
                    a_number_1.change_number(count_by_one)
                elif count_by_ten == 0 and count_by_one == 9 and count_by_hundred == 0:
                    count_by_ten += 1
                    count_by_one = 0
                    a_number_1.change_number(count_by_ten)
                    a_number_2 = Number(245,100, count)
                    all_numbers.add(a_number_2)
                elif count_by_ten >= 1 and count_by_one <= 8 and count_by_hundred == 0:
                    count_by_one += 1
                    a_number_2.change_number(count_by_one)
                elif count_by_ten >= 1 and count_by_ten <= 8 and count_by_one == 9 and count_by_hundred == 0:
                    count_by_ten += 1
                    count_by_one = 0
                    a_number_1.change_number(count_by_ten)
                    a_number_2.change_number(count_by_one)
                #|----------------------- attempt at adding triple digits
                elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred == 0:
                    a_number_3 = Number(265,100, count)
                    all_numbers.add(a_number_3)
                    count_by_one = 0
                    count_by_ten = 0
                    count_by_hundred += 1
                    a_number_1.change_number(count_by_hundred)
                    a_number_2.change_number(count_by_ten)
                elif count_by_ten <= 8 and count_by_one <= 8 and count_by_hundred >= 1 and count_by_hundred <= 8:
                    count_by_one += 1
                    a_number_3.change_number(count_by_one)
                elif count_by_ten <= 8 and count_by_one == 9 and count_by_hundred >= 1 and count_by_hundred <= 8:
                    count_by_ten += 1
                    count_by_one = 0
                    a_number_2.change_number(count_by_ten)
                    a_number_3.change_number(count_by_one)
                elif count_by_ten == 9 and count_by_one <= 8 and count_by_hundred >= 1 and count_by_hundred <= 8:
                    count_by_one += 1
                    a_number_3.change_number(count_by_one)
                elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred >= 1 and count_by_hundred <= 8:
                    count_by_one = 0
                    count_by_ten = 0
                    count_by_hundred += 1
                    a_number_1.change_number(count_by_hundred)
                    a_number_2.change_number(count_by_ten)
                    a_number_3.change_number(count_by_one)    
                elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred == 9:
                    count_by_ten = 0
                    count_by_one = 0
                    count_by_hundred = 0
                    a_number_1.change_number(count_by_hundred)
                    a_number_2.change_number(count_by_ten)
                    a_number_3.change_number(count_by_one)


    all_floors.draw(screen)
    all_floors.update()
    time = clock.get_time()


    
    all_numbers.draw(screen)
    all_numbers.update()



    print(top_pipes, bottom_pipes)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()