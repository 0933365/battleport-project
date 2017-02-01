import pygame
pygame.init()

# ------------Code written by me-------------#

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('sea2.jpg')
back_button = pygame.image.load('backbutton4.png')
battle_port = pygame.image.load('BattlePort.gif')
instructions_image = pygame.image.load('instructions.png')
next_button = pygame.image.load('nextbutton.png')
instructions_text = pygame.image.load('instructions1.png')
instructions_texttwee = pygame.image.load('instructions2.png')
instructions_textdrie = pygame.image.load('instructions3.png')
instructions_textvier = pygame.image.load('instructions4.png')
pauze_button = pygame.image.load('pauzebutton.png')
hqdefault = pygame.image.load('hqdefault.jpg')
red_turn = pygame.image.load('REd-turn.gif')
green_turn = pygame.image.load('green-turn.gif')
GreenBoat1 = pygame.image.load('GreenBoat1.png')
GreenBoat2 = pygame.image.load('GreenBoat2.png')
GreenBoat3 = pygame.image.load('GreenBoat3.png')
RedBoat1 = pygame.image.load('RedBoat1.png')
RedBoat2 = pygame.image.load('RedBoat2.png')
RedBoat3 = pygame.image.load('RedBoat3.png')
continue_button = pygame.image.load('Continue.png')
boat_green1_1 = pygame.image.load("GreenBoat1.png")
boat_green1_2 = pygame.image.load("GreenBoat1.2.png")
boat_green1_3 = pygame.image.load("GreenBoat1.3.png")
boat_green1_4 = pygame.image.load("GreenBoat1.4.png")
boat_green2_1 = pygame.image.load("GreenBoat2.png")
boat_green2_2 = pygame.image.load("GreenBoat2.2.png")
boat_green2_3 = pygame.image.load("GreenBoat2.3.png")
boat_green2_4 = pygame.image.load("GreenBoat2.4.png")
boat_green3_1 = pygame.image.load("GreenBoat3.png")
boat_green3_2 = pygame.image.load("GreenBoat3.2.png")
boat_green3_3 = pygame.image.load("GreenBoat3.3.png")
boat_green3_4 = pygame.image.load("GreenBoat3.4.png")

boat_red1_1 = pygame.image.load("RedBoat1.png")
boat_red1_2 = pygame.image.load("RedBoat1.2.png")
boat_red1_3 = pygame.image.load("RedBoat1.3.png")
boat_red1_4 = pygame.image.load("RedBoat1.4.png")
boat_red2_1 = pygame.image.load("RedBoat2.png")
boat_red2_2 = pygame.image.load("RedBoat2.2.png")
boat_red2_3 = pygame.image.load("RedBoat2.3.png")
boat_red2_4 = pygame.image.load("RedBoat2.4.png")
boat_red3_1 = pygame.image.load("RedBoat3.png")
boat_red3_2 = pygame.image.load("RedBoat3.2.png")
boat_red3_3 = pygame.image.load("RedBoat3.3.png")
boat_red3_4 = pygame.image.load("RedBoat3.4.png")
end_turn = pygame.image.load("end turn.png")
grid_bg = pygame.image.load("gridps.png")

bgrect = bg.get_rect()
size = (width, height) = bg.get_size()

def pauze_menu():
    pauze = True
    music = 0
    while pauze:
        pygame.display.set_mode((width, height))
        screen.blit(bg, (0,0))
        screen.blit(hqdefault, (300,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pauze == False
                quit()
        mouse = pygame.mouse.get_pos()
        print (mouse)
        if (478 + 120) > mouse[0] > 0 and (245 + 27) > mouse[1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                break
        if (478 + 120 > mouse[0]>0 and (302 + 28)) > mouse [1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_game()
        if (478 + 120 > mouse[0]>0 and (360 + 25)) > mouse [1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_menu()
        if (332 + 38 > mouse[0]>0 and (383 + 34)) > mouse [1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music == 0:
                    music = music + 1
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                    music = music - 1

        pygame.display.flip()

def draw_instructions():
    instructions = True

    while instructions:
        pygame.display.set_mode((width, height))
        screen.blit(bg, (0, 0))
        screen.blit(back_button, (10, 10))
        screen.blit(instructions_image, (410, 20))
        screen.blit(next_button, (1000, 10))
        screen.blit(instructions_text, (50, 150))
        screen.blit(instructions_texttwee, (570, 150))

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if back_button.get_rect().collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                draw_menu()
            if (1000 + 49) > mouse[0] > 1000 and (10 + 43) > mouse[1] > 10:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    instructions_twee()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False

        pygame.display.flip()

def instructions_twee():
    instructions = True
    while instructions:
        pygame.display.set_mode((width, height))
        screen.blit(bg, (0, 0))
        screen.blit(back_button, (10, 10))
        screen.blit(instructions_image, (410, 20))
        screen.blit(instructions_textdrie, (50, 150))
        screen.blit(instructions_textvier, (570, 150))
        pygame.display.flip()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if back_button.get_rect().collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                draw_instructions()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = False

# ----------Code edited by me------------#

def draw_game(): #DELETED
    start = True
    click_count = 0
    turn = True
    #BLACK = (0, 0, 0)
    #WHITE = (255, 255, 255)
    #GREEN = (0, 255, 0)
    #RED = (255, 0, 0)
    #WIDTH = 40
    #HEIGHT = 40
    #MARGIN = 5

    grid = []
    for row in range(25):
        grid.append([])
        for column in range(25):
     #       grid[row].append(0)  # Append a cell

    #pygame.display.set_caption("Array Backed Grid")

    while start:
        pygame.display.set_mode((1100, 680))
        screen.blit(pauze_button,(1000,10))
        mouse = pygame.mouse.get_pos()
        if click_count < 4:
            screen.blit(red_turn, (1000, 555))
        else:
            screen.blit(green_turn, (1000, 555))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn:
                    if click_count < 5:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        grid[row][column] = 1
                        click_count += 1
                        print("Click ", pos, "Grid coordinates: ", row, column)
                    if click_count > 4:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        grid[row][column] = 2
                        click_count += 1
                        print("Click ", pos, "Grid coordinates: ", row, column)
                        if click_count == 9:
                            turn = False

        grid_coordinates = (row, column)
        for row in range(15):
            for column in range(15):
                color = WHITE
                if grid[row][column] == 1:
                    color = RED
                if grid[row][column] == 2:
                    for event in pygame.event.get():
                        if (5 + 40) > mouse[0] > 5 and (5 + 40) > mouse[1] > 5 and event.type == pygame.MOUSEBUTTONDOWN:
                            screen.blit(GreenBoat1,(5,5))

                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        if (1000 + 83) > mouse[0] > 1000 and (10 + 43) > mouse[1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pauze_menu()

        pygame.display.flip()

#---------Code written by me/I have worked on-----------#

class Boat:
    def __init__(self, x, y, hp, select, press):
        self.x = x
        self.y = y
        self.hp = hp
        self.select = False
        self.press = 0


player1_boat = Boat(5, 5, 2, False,0)
player1_boat1 = Boat(230, 5, 3, False,0)
player1_boat2 = Boat(410, 5, 4, False,0)
player1_boat3 = Boat(635, 5, 2, False,0)

player2_boat = Boat(5, 635, 2, False,0)
player2_boat1 = Boat(230, 635, 3, False,0)
player2_boat2 = Boat(410, 635, 4, False,0)
player2_boat3 = Boat(635, 635, 2, False,0)

def draw_game():
    #pygame.mixer.music.load('nautical008.mp3')
    width = 1100
    height = 680
    light_blue = (82, 200, 220)
    red = (255, 0, 0)
    screen = pygame.display.set_mode((width, height))
    press_cnt = 0
    start = True
    turn = True


    while start:
        pygame.display.set_mode((width, height))
        screen.blit(grid_bg, (0, 0))
        screen.blit(pauze_button, (1000, 10))
        screen.blit(end_turn, (690, 630))
        screen.blit(boat_red3_3,(player1_boat.x, player1_boat.y))
        screen.blit(boat_red1_3, (player1_boat1.x, player1_boat1.y))
        screen.blit(boat_red2_3, (player1_boat2.x, player1_boat2.y))
        screen.blit(boat_red3_3, (player1_boat3.x, player1_boat3.y))

        screen.blit(boat_green3_1, (player2_boat.x, player2_boat.y))
        screen.blit(boat_green1_1, (player2_boat1.x , player2_boat1.y))
        screen.blit(boat_green2_1, (player2_boat2.x, player2_boat2.y))
        screen.blit(boat_green3_1, (player2_boat3.x, player2_boat3.y))

        if turn == True:
            screen.blit(red_turn, (1000, 600))
        else:
            screen.blit(green_turn, (1000, 600))
        key_count = 0

        pygame.display.flip()

        mouse = pygame.mouse.get_pos()

        if (1000 + 83) > mouse[0] > 1000 and (10 + 43) > mouse[1] > 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pauze_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            if 690 + 126 > mouse[0] > 690 and 630 + 44 > mouse[1] > 630:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    turn = False
        if turn:
            if (player1_boat.x) +45 > mouse[0] > player1_boat.x and player1_boat.y + 45 > mouse[1] > player1_boat.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player1_boat.select = True
            elif (player1_boat1.x) +45 > mouse[0] > player1_boat1.x and player1_boat1.y + 45 > mouse[1] > player1_boat1.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player1_boat1.select = True
            elif (player1_boat2.x) +45 > mouse[0] > player1_boat2.x and player1_boat2.y + 45 > mouse[1] > player1_boat2.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player1_boat2.select = True
            elif (player1_boat3.x) +45 > mouse[0] > player1_boat3.x and player1_boat3.y + 45 > mouse[1] > player1_boat3.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player1_boat3.select = True


            if player1_boat1.select:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1_boat1.x -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player1_boat1.x += 45
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player1_boat1.y -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player1_boat1.y += 45
                        #pygame.mixer.music.play(0, 0)
                    if player1_boat1.x + 45 > 720:
                        player1_boat1.x -= 45
                    if player1_boat1.x - 45 < -40:
                        player1_boat1.x += 45
                    if player1_boat1.y + 45 > 720:
                        player1_boat1.y -= 45
                    if player1_boat1.y - 45 < -40:
                        player1_boat1.y += 45

                    player1_boat1.select = False

            if player1_boat2.select:
                    if event.type == pygame.KEYDOWN:
                        player1_boat2.press += 1
                        if event.key == pygame.K_LEFT:
                            player1_boat2.x -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player1_boat2.x += 45
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player1_boat2.y -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player1_boat2.y += 45
                            #pygame.mixer.music.play(0, 0)
                        if player1_boat2.x + 45 > 720:
                            player1_boat2.x -= 45
                        if player1_boat2.x - 45 < -40:
                            player1_boat2.x += 45
                        if player1_boat2.y + 45 > 720:
                            player1_boat2.y -= 45
                        if player1_boat2.y - 45 < -40:
                            player1_boat2.y += 45
                    if player1_boat2.press == 2:
                        player1_boat2.select = False

            if player1_boat3.select:
                    if event.type == pygame.KEYDOWN:
                        player1_boat3.press += 1
                        if event.key == pygame.K_LEFT:
                            player1_boat3.x -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player1_boat3.x += 45
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player1_boat3.y -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player1_boat3.y += 45
                            #pygame.mixer.music.play(0, 0)
                        if player1_boat3.x + 45 > 720:
                            player1_boat3.x -= 45
                        if player1_boat3.x - 45 < -40:
                            player1_boat3.x += 45
                        if player1_boat3.y + 45 > 720:
                            player1_boat3.y -= 45
                        if player1_boat3.y - 45 < -40:
                            player1_boat3.y += 45
                    if player1_boat3.press == 3:
                        player1_boat3.select = False


            if player1_boat.select:
                if event.type == pygame.KEYDOWN:
                    player1_boat.press += 1
                    if event.key == pygame.K_LEFT:
                        player1_boat.x -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player1_boat.x += 45
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player1_boat.y -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player1_boat.y += 45
                        #pygame.mixer.music.play(0, 0)
                    if player1_boat.x + 45 > 720:
                        player1_boat.x -= 45
                    if player1_boat.x - 45 < -40:
                        player1_boat.x += 45
                    if player1_boat.y + 45 > 720:
                        player1_boat.y -= 45
                    if player1_boat.y - 45 < -40:
                        player1_boat.y += 45
                if player1_boat.press == 3:
                    player1_boat.select = False


        if turn == False:

            if (player2_boat.x) + 45 > mouse[0] > player2_boat.x and player2_boat.y + 45 > mouse[1] > player2_boat.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player2_boat.select = True
            elif (player2_boat1.x) + 45 > mouse[0] > player2_boat1.x and player2_boat1.y + 45 > mouse[1] > player2_boat1.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player2_boat1.select = True
            elif (player2_boat2.x) + 45 > mouse[0] > player2_boat2.x and player2_boat2.y + 45 > mouse[1] > player2_boat2.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player2_boat2.select = True
            elif (player2_boat3.x) + 45 > mouse[0] > player2_boat3.x and player2_boat3.y + 45 > mouse[1] > player2_boat3.y:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player2_boat3.select = True


            if player2_boat1.select:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player2_boat1.x -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2_boat1.x += 45
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player2_boat1.y -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player2_boat1.y += 45
                        #pygame.mixer.music.play(0, 0)
                    if player2_boat1.x + 45 > 720:
                        player2_boat1.x -= 45
                    if player2_boat1.x - 45 < -40:
                        player2_boat1.x += 45
                    if player2_boat1.y + 45 > 720:
                        player2_boat1.y -= 45
                    if player2_boat1.y - 45 < -40:
                        player2_boat1.y += 45
                    player2_boat1.select = False

            if player2_boat2.select:
                    if event.type == pygame.KEYDOWN:
                        player2_boat2.press += 1
                        if event.key == pygame.K_LEFT:
                            player2_boat2.x -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player2_boat2.x += 45
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player2_boat2.y -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player2_boat2.y += 45
                            #pygame.mixer.music.play(0, 0)
                        if player2_boat2.x + 45 > 720:
                            player2_boat2.x -= 45
                        if player2_boat2.x - 45 < -40:
                            player2_boat2.x += 45
                        if player2_boat2.y + 45 > 720:
                            player2_boat2.y -= 45
                        if player2_boat2.y - 45 < -40:
                            player2_boat2.y += 45
                    if player2_boat2.press == 2:
                        player2_boat2.select = False

            if player2_boat3.select:
                    if event.type == pygame.KEYDOWN:
                        player2_boat3.press += 1
                        if event.key == pygame.K_LEFT:
                            player2_boat3.x -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player2_boat3.x += 45
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player2_boat3.y -= 45
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player2_boat3.y += 45
                            #pygame.mixer.music.play(0, 0)
                        if player2_boat3.x + 45 > 720:
                            player2_boat3.x -= 45
                        if player2_boat3.x - 45 < -40:
                            player2_boat3.x += 45
                        if player2_boat3.y + 45 > 720:
                            player2_boat3.y -= 45
                        if player2_boat3.y - 45 < -40:
                            player2_boat3.y += 45
                    if player2_boat3.press == 3:
                        player2_boat3.select = False

            if player2_boat.select:
                if event.type == pygame.KEYDOWN:
                    player2_boat.press += 1
                    if event.key == pygame.K_LEFT:
                        player2_boat.x -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2_boat.x += 45
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player2_boat.y -= 45
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player2_boat.y += 45
                        #pygame.mixer.music.play(0, 0)
                        if player2_boat.x + 45 > 720:
                            player2_boat.x -= 45
                        if player2_boat.x - 45 < -40:
                            player2_boat.x += 45
                        if player2_boat.y + 45 > 720:
                            player2_boat.y -= 45
                        if player2_boat.y - 45 < -40:
                            player2_boat.y += 45
                if player2_boat.press == 3:
                    player2_boat.select = False

    pygame.display.flip()