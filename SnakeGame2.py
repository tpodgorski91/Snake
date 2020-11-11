import pygame
import sys
import random

# create Snake, App or/and Food classes


class Snake:
    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        # self.size = size

    def position_container(self):
        return self.position[0]

    # moving is already covered by bult-in function 'move_ip'
    def way(self, point):
        self.direction = point

    def move(self):
        current_position = self.position_container()
        x, y = self.direction
        newer = ((current_position[0] + x), (current_position[1] + y))
        self.position.insert(0, newer)
        if len(self.position) > self.length:
            self.position.pop()
        return self.position[0]

    def draw(self):
        for p in self.position:
            # print(self.position)
            rectangular = pygame.Rect((p[0], p[1]), (15, 15))
            pygame.draw.rect(surface, RED, rectangular)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in direction:
                    if event.key == pygame.K_UP:
                        self.way(up)
                    elif event.key == pygame.K_DOWN:
                        self.way(down)
                    elif event.key == pygame.K_LEFT:
                        self.way(left)
                    elif event.key == pygame.K_RIGHT:
                        self.way(right)
            # surface.fill(GRAY)
            # screen.blit(surface, (0, 0))
            # pygame.display.flip()


class Food:
    def __init__(self):
        self.position = position
        # self.size = size

    @staticmethod
    def positions():
        x = random.randrange(0, screen_width, rect_size)
        y = random.randrange(0, screen_height, rect_size)
        return [x, y]
# snake is moving in some direction following keydown click by gamer
# there is one food at once on the screen
# when snake eats food it is growing by 1
# when snakes eats itself game is over


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# screen - background
screen_width = 1200
screen_height = 800
rect_size = 15

# import random
#
# ekran = [((1200),(800))]
# for i in range(10):
#
#     print([x, y])
screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# snake - player
position = [((screen_width/2), (screen_height/2))]


up = (0, -10)
down = (0,10)
left = (-10,0)
right = (10,0)

# rectangular = pygame.Rect(new(), (15, 15))

direction = {pygame.K_LEFT: [-10, 0], pygame.K_RIGHT: [10, 0], pygame.K_UP: [0, -10], pygame.K_DOWN: [0, 10]}

start_position = (screen_width/2, screen_height/2)
# rect = pygame.Rect(start_position, (15, 15))
# snake_head = pygame.draw.rect(surface, RED, rect)
pygame.display.update()
# rectangular = pygame.Rect(new(), (15, 15))

def main():
    pygame.init()
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    print(food.positions())
    print("")
    while True:
        clock.tick(10)
        snake.handle_keys()
        surface.fill(GRAY)
        pygame.display.flip()
        snake.move()
        snake.draw()
        screen.blit(surface, (0, 0))

main()
