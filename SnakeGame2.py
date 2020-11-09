import pygame
import sys
import random

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# screen - background
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# snake - player
position = [((screen_width/2), (screen_height/2))]


up = (0, -10)
down = (0,10)
left = (-10,0)
right = (10,0)


def random_direction():
    return random.choice([up, down, left, right])


def position_container():
    return position[0]


def new():
    current_position = position_container()
    x,y = random_direction()
    newer = ((current_position[0]+x),(current_position[1]+y))
    position.insert(0, newer)
    if len(position)>2:
        position.pop()
    return position[0]


rectangular = pygame.Rect(new(), (15, 15))

direction = {pygame.K_LEFT: [-10, 0], pygame.K_RIGHT: [10, 0], pygame.K_UP: [0, -10], pygame.K_DOWN: [0, 10]}
screen.blit(surface, (0, 0))
start_position = (screen_width/2, screen_height/2)
# rect = pygame.Rect(start_position, (15, 15))
# snake_head = pygame.draw.rect(surface, RED, rect)
pygame.display.update()


def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key in direction:
        #         v = direction[event.key]
        #         rect.move_ip(v)
        #         pygame.display.update()
        surface.fill(GRAY)
        pygame.draw.rect(surface, RED, rectangular)
        screen.blit(surface, (0, 0))
        pygame.display.flip()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        handle_keys()


main()
