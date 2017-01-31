import pygame
pygame.init()

# ------------Code written by me-------------#

GreenBoat1 = pygame.image.load('GreenBoat1.png')
GreenBoat2 = pygame.image.load('GreenBoat2.png')
GreenBoat3 = pygame.image.load('GreenBoat3.png')
RedBoat1 = pygame.image.load('RedBoat1.png')
RedBoat2 = pygame.image.load('RedBoat2.png')
RedBoat3 = pygame.image.load('RedBoat3.png')
instructions_image = pygame.image.load('instructions.png')
next_button = pygame.image.load('nextbutton.png')
instructions_text = pygame.image.load('instructions1.png')
instructions_texttwee = pygame.image.load('instructions2.png')
instructions_textdrie = pygame.image.load('instructions3.png')
instructions_textvier = pygame.image.load('instructions4.png')
pauze_button = pygame.image.load('pauzebutton.png')
back_button = pygame.image.load('backbutton4.png')

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

def draw_game():
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