import pygame
import random
import time
pygame.font.init()
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
FPS = 10
pygame.display.set_caption("Snake Game")
WIN = pygame.display.set_mode((WIDTH , HEIGHT))

snake_pos = [260 , 260]
snake_body = [[260 , 260] , [240 , 260] , [220 , 260]]

BG = (0 , 193 , 212)
WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
RED = (255 , 10 , 0)

my_font = pygame.font.SysFont('Avenir' , 20)
end_font = pygame.font.SysFont('Avenir' , 50)

def draw():
    WIN.fill(BG)
    for pos in snake_body:
        pygame.draw.rect(WIN, BLACK , pygame.Rect(pos[0] , pos[1] , CELL_SIZE , CELL_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(WIN , RED , pygame.Rect(food_pos[0] , food_pos[1] , CELL_SIZE  , CELL_SIZE))

def draw_score(score):
    score_text = my_font.render("Score : " + str(score) , 1 , WHITE)
    WIN.blit(score_text , (10 , 10))

def game_over(score):
    end_text = end_font.render("Game Over" , 1 , WHITE)
    WIN.blit(end_text , (WIDTH/2 - end_text.get_width() / 2 , HEIGHT/2 - end_text.get_height()/2))
    draw_score(score)
    pygame.display.update()
    time.sleep(5)

def get_coords():
    x = random.randint(0  , 24)
    y = random.randint(0  , 24)
    
    return [x * 20 , y * 20]

def main():
    run = True 
    direction = 'R'
    change_to = direction
    food_pos = get_coords()
    score = 0
    food = False
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP):
                    change_to = 'U'
                if(event.key == pygame.K_DOWN):
                    change_to = 'D' 
                if(event.key == pygame.K_RIGHT):
                    change_to = 'R'
                if(event.key == pygame.K_LEFT):
                    change_to = 'L'    
                if(event.key == pygame.K_ESCAPE):
                    run = False

        if(change_to == 'U' and direction != 'D'):
            direction = 'U'   
        if(change_to == 'D' and direction != 'U'):
            direction = 'D'
        if(change_to == 'R' and direction != 'L'):
            direction = 'R'
        if(change_to == 'L' and direction != 'R'):
            direction = 'L'                     

        if direction == 'U':
            snake_pos[1] -= 20
        if direction == 'D':
            snake_pos[1] += 20
        if direction == 'R':
            snake_pos[0] += 20
        if direction == 'L':
            snake_pos[0] -= 20

        snake_body.insert(0 , list(snake_pos))
        if(snake_pos == food_pos):
            score += 1
            food = False
        else:
            snake_body.pop()

        if not food:
            food = True
            food_pos = get_coords()        
        
        draw()
        draw_food(food_pos)

        #check if valid
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= WIDTH:
            print("Game Over" , " Score : " , score)
            game_over(score)
            run = False

        for block in snake_body[1:]:
            if(snake_pos[0] == block[0] and snake_pos[1] == block[1]):
                print("Game Over" , " Score : " , score)
                game_over(score)
                run = False

        draw_score(score)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

