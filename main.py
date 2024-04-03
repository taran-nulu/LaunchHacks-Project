import pygame
from pygame.locals import * 

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

transparent = (0, 0, 0, 0)

black = (0, 0, 0)
white = (255, 255, 255)

p1 = ""
p2 = ""

font = pygame.font.SysFont("impact", 40)

again_rect = Rect(screen_width // 2 - 80, screen_height // 2 + 10, 160, 50)

def draw_grid():
    bg = (255, 255, 255)
    grid = (0, 0, 0)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, black, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, black, (x * 100, 0), (x * 100, screen_height), line_width)

for x in range(3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1: 
                pygame.draw.line(screen, black, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, black, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, black, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def check_winner():
    y_pos = 0
    global winner
    global game_over
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][2] + markers[1][1] + markers[0][0] == -3:
        winner = 1
        game_over = True

def draw_winner(winner):
    win_text = 'Player ' + str(winner) + " wins"
    win_img = font.render(win_text, True, black)
    pygame.draw.rect(screen, white, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))
    again_text = "Play again?"
    again_img = font.render(again_text, True, black)
    pygame.draw.rect(screen, white, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))



run = True
while run:
    
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                p1 = "rock"
            if event.key == pygame.K_s:
                p1 = "paper"
            if event.key == pygame.K_d:
                p1 = "scissors"
            if event.key == pygame.K_j:
                p2 = "rock"
            if event.key == pygame.K_k:
                p2 = "paper"
            if event.key == pygame.K_l:
                p2 = "scissors"

            # SET VARS TO FALSE AFTER DISPLAYING IMAGE
            if p1 == "rock" and p2 == "rock":
                print("rock tie")
                p1 = ""
                p2 = ""
            if p1 == "paper" and p2 == "paper":
                print("paper tie")
                p1 = ""
                p2 = ""
            if p1 == "scissors" and p2 == "scissors":
                print("scissors tie")
                p1 = ""
                p2 = ""
            if p1 == "rock" and p2 == "scissors":
                print("p1 rock win")
                p1 = ""
                p2 = ""
            if p1 == "scissors"and p2 == "paper":
                print("p1 scissors win")
                p1 = ""
                p2 = ""
            if p1 == "paper" and p2 == "rock":
                print("p1 paper win")
                p1 = ""
                p2 = ""
            if p2 == "rock" and p1 == "scissors":
                print("p2 rock win")
                p1 = ""
                p2 = ""
            if p2 == "scissors" and p1 == "paper":
                print("p2 scissors win")
                p1 = ""
                p2 = ""
            if p2 == "paper" and p1 == "rock":
                print("p2 paper win")
                p1 = ""
                p2 = ""

    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                line_width = 6
                markers = []
                clicked = False
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0] * 3
                markers.append(row)
    


    pygame.display.update()
pygame.quit()
