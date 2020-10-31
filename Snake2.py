import pygame
import sys

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_width = 1200
screen_height = 800


direction = {pygame.K_LEFT: [-10, 0], pygame.K_RIGHT: [10, 0], pygame.K_UP: [0, -10], pygame.K_DOWN: [0, 10]}
start_position = (screen_width/2, screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
rect = pygame.Rect(start_position, (15, 15))


def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in direction:
                v = direction[event.key]
                rect.move_ip(v)
    surface.fill(GRAY)
    pygame.draw.rect(surface, RED, rect)
    pygame.display.flip()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        handle_keys()
        screen.blit(surface, (0, 0))
        pygame.display.update()


main()
