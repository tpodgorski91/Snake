import pygame
import sys
import random


class Snake:
    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        # self.size = size

    def head_position(self):
        return self.position[0]

    def way(self, point):
        self.direction = point

    def move(self):
        current_position = self.head_position()
        x, y = self.direction
        newer = ((current_position[0] + x), (current_position[1] + y))
        self.position.insert(0, newer)
        if len(self.position) > self.length:
            self.position.pop()
        return self.position[0]

    def draw(self):
        for p in self.position:
            # print("dupa")
            # print(self.position)
            rectangular = pygame.Rect((p[0], p[1]), (rect_size, rect_size))
            pygame.draw.rect(surface, GREEN, rectangular)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.way(up)
                elif event.key == pygame.K_DOWN:
                    self.way(down)
                elif event.key == pygame.K_LEFT:
                    self.way(left)
                elif event.key == pygame.K_RIGHT:
                    self.way(right)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
        # self.size = size

    # @staticmethod
    def randomize_position(self):
        self.position = ((random.randrange(0, screen_width, rect_size)), (random.randrange(0, screen_height, rect_size)))

    def draw(self):
        # print("plecy")
        # print(self.position)
        rectangular = pygame.Rect((self.position[0], self.position[1]), (rect_size, rect_size))
        pygame.draw.rect(surface, RED, rectangular)

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
screen_width = 600
screen_height = 480
rect_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

# snake - player
up = (0, -20)
down = (0,20)
left = (-20,0)
right = (20,0)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    surface.fill(GRAY)
    # pygame.display.flip()
    snake = Snake()
    food = Food()
    food.draw()
    while True:
        clock.tick(10)
        snake.handle_keys()
        surface.fill(GRAY)
        # pygame.display.flip()
        snake.move()
        if snake.head_position() == food.position:
            snake.length += 1
            food.randomize_position()
        snake.draw()
        food.draw()
        screen.blit(surface, (0, 0))
        pygame.display.update()



main()
