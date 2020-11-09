import pygame
import time
import random


class Snake:
    def __init__(self):
        self.length = 1
        self.start_position = [((screen_height/2), (screen_width/2))]
        self.color = white


class Food:
    pass


class Window:
    pass


pygame.init()

#colors RGB
white = (255,255,255)
black = (0,0,0)
yellow =(255,255,0)
red = (255,0,0)
green = (0, 255, 0)
blue = (50, 153, 213)

screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game by Maszt071')

#tworzy obiekt do śledzenia czasu
clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont("comicsansms",20)

def Your_score(score):
    # render tworzy nową powierzchnię z podanym tekstem, parametry: tekst, antyalias, kolor, tło
    value = score_font.render("Your Score: " + str(score), True, green)
    #blit rysuje jeden obrazek na drugim, parametry: źródło, cel.
    screen.blit(value, [0, 0])

def my_snake(snake_block, snake_list):
    for x in snake_list:
        # draw.rect parametry: powierzchnia, kolor, obiekt Rect, grubość obramowania.
        pygame.draw.rect(screen, yellow, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    #food location

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True: #when lose
            screen.fill(red) #wypełnia obrazek kolorem
            message("You lost! Press Q-Quit or P-Play again", white)
            pygame.display.update()
            for event in pygame.event.get(): #event zapis zajścia w systemie komputerowym określonej sytuacji, np. poruszenie myszką, kliknięcie, pygame.event.get() pobiera zdarzenia z kolejki zdarzeń
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key ==pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key ==pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key ==pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1>=screen_width or x1 <0 or y1>=screen_height or y1 <0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        #snake head location
        snake_Head =[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close= True

        my_snake(snake_block,snake_List)
        Your_score(Length_of_snake - 1)

        #pygame.draw.rect(dis,yellow,[x1,y1,snake_block,snake_block])
        pygame.display.update()
        #if snake head meets food than snake length is longer 1
        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake +=1
        #tick kontroluje ile milisekund upłynęło od poprzedniego wywołania
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
