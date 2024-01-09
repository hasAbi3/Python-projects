import pygame
import random

#pygame initialization
pygame.init()

#colors
GREEN = (0,120,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

#dimensions
WIDTH = 640
HEIGHT = 480

CELL_SIZE = 20

# set up the screen variable
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0]* CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE ))
    pass

def draw_food(food):
    pygame.draw.rect(screen, RED, pygame.Rect(food[0]* CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_score(score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True,WHITE )

    screen.blit(score_text, (10,10))#blit also allows images

def game_over(score):
    font = pygame.font.SysFont(None, 70)
    game_over_text = font.render("Game Over", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - 50, HEIGHT // 2 + 20))
    pygame.display.flip()
    pygame.time.delay(20000) 

#main functionality
def main():

    running =True

    #default direction is right
    direction = (1,0) #RIGHT

    #body of snake
    snake = [(1,1), (0,1)]

    #food
    food = ((random.randint(0, (WIDTH//CELL_SIZE)-1)), (random.randint(0, (HEIGHT//CELL_SIZE)-1)))

    score = 0
    while running:
        screen.fill(BLACK)

        #user ko input aauda samma chalxa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #movement of snake
            elif event.type == pygame.KEYDOWN:  #event when any key is pressed
                if event.key == pygame.K_UP:
                    direction = (0,-1)
                elif event.key == pygame.K_DOWN:
                    direction = (0,1)
                elif event.key == pygame.K_LEFT:
                    direction = (-1,0)
                elif event.key == pygame.K_RIGHT:
                    direction = (1,0)

        #head of snake
        head = snake[0]
        new_head = ((head[0] + direction[0]) % (WIDTH//CELL_SIZE),(head[1]+ direction[1]) % (HEIGHT//CELL_SIZE))  #???

        snake.insert(0, new_head)

        #when food is found, 
        if new_head == food:
            food = ((random.randint(0, (WIDTH//CELL_SIZE)-1)), (random.randint(0, (HEIGHT//CELL_SIZE)-1)))
            score = score + 1

        else:
        #as we add new head, we are popping the previous one
            snake.pop()

        if new_head in snake[1:]:
            running = False
            game_over(score)
    


        draw_snake(snake)
        draw_food(food)
        draw_score(score)
        
        pygame.display.flip()
        clock.tick(6)
    pygame.quit()

main()