import pygame
import random
import os

pygame.mixer.init()
pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
s_width = 900
s_height = 600
gameWindow = pygame.display.set_mode((s_width, s_height))
#background image

bgimg = pygame.image.load("garry.jpg")
bgimg = pygame.transform.scale(bgimg, (s_width, s_height)).convert_alpha()
bgimg1 = pygame.image.load("snake99.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (s_width, s_height)).convert_alpha()
bgimg2 = pygame.image.load("dead.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (s_width, s_height)).convert_alpha()
pygame.display.set_caption("Snakegame")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
#
# with open("high score.txt", "r") as f:
#     high score = f.read()

def text_screen(text, color, x, y):
    s_text = font.render(text, True, color)
    gameWindow.blit(s_text, [x,y])

# gameloop

def welcome():
    exit_game = False
    while not exit_game:
        pygame.mixer.music.load('background.mp3')
        pygame.mixer.music.play()
        gameWindow.fill(white)
        gameWindow.blit(bgimg1, (0, 0))
        text_screen("Welcome to SNAKE GAME ",black, 260, 250)
        text_screen("Press space bar to play ",black, 230, 290)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('alcoholic.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():


    snake_length = 1
    snake_list = []
    exit_game = False
    game_over = False
    init_velocity = 5
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, s_width / 2)
    food_y = random.randint(20, s_height / 2)
    snake_size = 15
    fps = 30
    score = 0
    snake_length = 1
    snake_list = []
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")


    with open("highscore.txt", "r") as f:
        highscore = f.read()


    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg2, (0, 0))
            text_screen("Press Enter to Continue", red, 200, 200)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_j:
                        score = score + 10


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y )<10:
                score = score + 10
                food_x = random.randint(20, s_width / 2)
                food_y = random.randint(20, s_height / 2)
                snake_length = snake_length+5
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))


            text_screen("score: "+str(score) + "  High-score: "+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>s_width or snake_y<0 or snake_y>s_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
gameloop()