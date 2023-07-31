import pygame
from bird import Bird
from floor import Base
from pipe import Pipe
from number import Number
from sys import exit
import random
from pygame.locals import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((450,650))
pygame.display.set_caption("Flappy Bird v2.0")
clock = pygame.time.Clock()
running = True

background_surf = pygame.transform.scale(pygame.image.load("sprites/background-day.png").convert_alpha(), (450,750))
background_base = pygame.transform.scale(pygame.image.load("sprites/base.png").convert_alpha(), (450,100))
base_rect = background_base.get_rect(bottomleft = (0,690))


#-------------- START MENU WITH INSTRUCTIONS ---------
width = 450
height = 750
alpha_value = 128 # 0 (fully transparent) to 255 (fully opqaue)
transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
transparent_surface.fill((0,0,0, alpha_value))
font = pygame.font.Font("flappybirdy-font/FlappybirdyRegular-KaBW.ttf", 36)
text_color = (255,255,255)
text = "Press SPACE BAR to begin"
text_surface = font.render(text, True, text_color)

#|----------- RESET GAME FUNCTION

# def reset_game():
    # global all_birds, all_floors, all_numbers, top_pipes, bottom_pipes, game_started, alive, over_all_score, a_bird

    # all_birds.empty()
    # all_floors.empty()
    # top_pipes.empty()
    # bottom_pipes.empty()

    # a_bird = Bird()
    # all_birds.add(a_bird)

    # #|----------- FLOOR ------------|
    # all_floors = pygame.sprite.Group()
    # a_floor_1 = Base(0,690)
    # a_floor_2 = Base(450, 690)
    # all_floors.add(a_floor_1, a_floor_2) 

    # #|------------ PIPES -----------
    # top_pipe_1 = Pipe(500, 200, 180, 1)
    # top_pipes.add(top_pipe_1)

    # bottom_pipe_1 = Pipe(500, 400, 0, 2)
    # bottom_pipes.add(bottom_pipe_1)

    # game_started = False
    # alive = True

    # over_all_score = 0
    # all_numbers.empty()  # Clear the existing group
    # a_number_1 = Number(225, 100, 0)  # Initialize the number value to 0
    # all_numbers.add(a_number_1)
    # count_by_one = 0
    # count_by_ten = 0
    # count_by_hundred = 0

    # return all_birds, all_floors, all_numbers, top_pipes, bottom_pipes, game_started, count_by_one, count_by_ten, count_by_hundred, count


#|----------- NUMBER --------------|
over_all_score = 0
count = 0
all_numbers = pygame.sprite.Group()
a_number_1 = Number(225,100,count)
all_numbers.add(a_number_1)

count_by_one = 0
count_by_ten = 0
count_by_hundred = 0


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
top_pipe_1 = Pipe(500, 200, 180, 1)
top_pipes.add(top_pipe_1)

bottom_pipes = pygame.sprite.Group()
bottom_pipe_1 = Pipe(500, 400, 0, 2)
bottom_pipes.add(bottom_pipe_1)




#|----------- NUMBER --------------|
over_all_score = 0
count = 0
all_numbers = pygame.sprite.Group()
a_number_1 = Number(225,100,count)
all_numbers.add(a_number_1)

count_by_one = 0
count_by_ten = 0
count_by_hundred = 0

#|----------- to check when the player has started playing by pressing the key
game_started = False
alive = True
while running:
    if alive:
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

    #|------------- THIS CHANGES THE SCORE COUNTER ----------------------|
            for pipe in top_pipes:
                if pipe.rect.x == 200:
                    random_number = random.randint(50,300)
                    new_top_pipe = Pipe(500, random_number, 0, 1)
                    new_bottom_pipe = Pipe(500, (random_number + 200), 180, 2)
                    top_pipes.add(new_top_pipe)
                    bottom_pipes.add(new_bottom_pipe)
                if pipe.rect.x == 100:
                    if count_by_ten  == 0 and count_by_one <= 8 and count_by_hundred == 0:
                        count_by_one += 1
                        a_number_1.change_number(count_by_one)
                        over_all_score += 1
                    elif count_by_ten == 0 and count_by_one == 9 and count_by_hundred == 0:
                        count_by_ten += 1
                        count_by_one = 0
                        a_number_1.change_number(count_by_ten)
                        a_number_2 = Number(245,100, count)
                        all_numbers.add(a_number_2)
                        over_all_score += 1
                    elif count_by_ten >= 1 and count_by_one <= 8 and count_by_hundred == 0:
                        count_by_one += 1
                        a_number_2.change_number(count_by_one)
                        over_all_score += 1
                    elif count_by_ten >= 1 and count_by_ten <= 8 and count_by_one == 9 and count_by_hundred == 0:
                        count_by_ten += 1
                        count_by_one = 0
                        a_number_1.change_number(count_by_ten)
                        a_number_2.change_number(count_by_one)
                        over_all_score += 1
                    #|----------------------- attempt at adding triple digits
                    elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred == 0:
                        a_number_3 = Number(265,100, count)
                        all_numbers.add(a_number_3)
                        count_by_one = 0
                        count_by_ten = 0
                        count_by_hundred += 1
                        a_number_1.change_number(count_by_hundred)
                        a_number_2.change_number(count_by_ten)
                        over_all_score += 1
                    elif count_by_ten <= 8 and count_by_one <= 8 and count_by_hundred >= 1 and count_by_hundred <= 8:
                        count_by_one += 1
                        a_number_3.change_number(count_by_one)
                        over_all_score += 1
                    elif count_by_ten <= 8 and count_by_one == 9 and count_by_hundred >= 1 and count_by_hundred <= 8:
                        count_by_ten += 1
                        count_by_one = 0
                        a_number_2.change_number(count_by_ten)
                        a_number_3.change_number(count_by_one)
                        over_all_score += 1
                    elif count_by_ten == 9 and count_by_one <= 8 and count_by_hundred >= 1 and count_by_hundred <= 8:
                        count_by_one += 1
                        a_number_3.change_number(count_by_one)
                        over_all_score += 1
                    elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred >= 1 and count_by_hundred <= 8:
                        count_by_one = 0
                        count_by_ten = 0
                        count_by_hundred += 1
                        a_number_1.change_number(count_by_hundred)
                        a_number_2.change_number(count_by_ten)
                        a_number_3.change_number(count_by_one)   
                        over_all_score += 1 
                    elif count_by_ten == 9 and count_by_one == 9 and count_by_hundred == 9:
                        count_by_ten = 0
                        count_by_one = 0
                        count_by_hundred = 0
                        a_number_1.change_number(count_by_hundred)
                        a_number_2.change_number(count_by_ten)
                        a_number_3.change_number(count_by_one)
                        over_all_score += 1
    #|-------------------------- END OF SCORE COUNTER---------------------------
            
        all_floors.draw(screen)
        all_floors.update()

        for pipe in top_pipes:
            if a_bird.rect.colliderect(pipe.rect):
                alive = False
        for pipe in bottom_pipes:
            if a_bird.rect.colliderect(pipe.rect):
                alive = False

        time = clock.get_time()


        
        all_numbers.draw(screen)
        all_numbers.update()
        if not game_started:
            screen.blit(transparent_surface, (0,0))
            screen.blit(text_surface, (110, 200))
    
    
        pygame.display.flip()
        clock.tick(60)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         reset_game()
        screen.blit(background_surf, (0,0))
        all_floors.draw(screen)
        all_floors.update()
        text_surface1 = font.render(f"Your final score is {over_all_score}", True, text_color)
        # text_surface2 = font.render(f"Press SPACEBAR to play again", True, text_color)
        screen.blit(text_surface1, (110, 200))
        # screen.blit(text_surface2, (80, 230))
        
        pygame.display.flip()
        clock.tick(60)

pygame.quit()