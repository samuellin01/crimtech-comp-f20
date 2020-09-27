import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        if dir == 'u':
            self.direction = 'u'
        if dir == 'd':
            self.direction = 'd'
        if dir == 'l':
            self.direction = 'l'
        if dir == 'r':
            self.direction = 'r'

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        head = (x, y)
        if (x < 0 or x > 23 or y < 0 or y > 23):
            return True
        if head in self.body[1:]:
            return True
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times
        head = self.body[0]
        new_head = (head[0] + DIR[self.direction][0], head[1] + DIR[self.direction][1])
        self.body = [new_head] + self.body[:-1]
        #self.body = [new_head]
        #self.body.extend(self.body[:-1])
        if self.collision(new_head[0], new_head[1]) == True:
            self.kill()

    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i % 2), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        if snake != []:
            while True:
                x = random.randint(0, 23)
                y = random.randint(0, 23)
                food_position = (x, y)
                if food_position not in snake.body:
                    self.position = (x, y)
                    return

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    font = pygame.font.SysFont('comic_sans_ms', 15)
    text = font.render((str)(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (25, 20)

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(10)
        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if snake.body[0] == apple.position:
            score = score + 1
            snake.body.append(snake.body[-1])
            apple.place(snake)
            
        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        text = font.render("Score: " + (str)(score), True, (0, 0, 0))
        screen.blit(text, textRect)

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()