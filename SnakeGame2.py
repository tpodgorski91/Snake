import pygame
import sys
import random


class Snake:

    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
        self.empty_list = []

    def head_position(self):
        return self.position[0]

    def way(self, point):
        self.direction = point

    def move(self):
        current_position = self.head_position()
        x, y = self.direction
        self.empty_list.append(current_position)
        newer = ((current_position[0] + x), (current_position[1] + y))
        if self.length > 2:
            for i in range(1, self.length):
                self.empty_list = self.empty_list[-self.length:]
                if newer == self.empty_list[i]:
                    pygame.quit()
                    sys.exit()
        self.position.insert(0, newer)
        if len(self.position) > self.length:
            self.position.pop()
        return self.position[0]

    def draw(self):
        for p in self.position:
            if screen_width < p[0] or p[0] < 0:
                pygame.quit()
                sys.exit()
            elif screen_height < p[1] or p[1] < 0:
                pygame.quit()
                sys.exit()
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

    def randomize_position(self):
        self.position = ((random.randrange(0, screen_width, rect_size)), (random.randrange(0, screen_height, rect_size)))

    def draw(self):
        rectangular = pygame.Rect((self.position[0], self.position[1]), (rect_size, rect_size))
        pygame.draw.rect(surface, RED, rectangular)


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_width = 600
screen_height = 480
rect_size = 20

screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

up = (0, -20)
down = (0,20)
left = (-20,0)
right = (20,0)


def main():
    pygame.init()
    font = pygame.font.SysFont("bahnschrift", 25)
    clock = pygame.time.Clock()
    surface.fill(GRAY)
    snake = Snake()
    food = Food()
    food.draw()
    while True:
        clock.tick(10)
        snake.handle_keys()
        surface.fill(GRAY)
        snake.move()
        if snake.head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        text = font.render(f"Score: {snake.score}", True, BLUE)
        snake.draw()
        food.draw()
        screen.blit(surface, (0, 0))
        screen.blit(text, [0, 0])
        pygame.display.update()


main()

