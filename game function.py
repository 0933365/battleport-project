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
deadboat = pygame.image.load('deadboat.png')
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
card = pygame.image.load('3032008-four-aces.jpg')
shipstats = pygame.image.load('shipstats.png')
cards = pygame.image.load('cards.png')
bgrect = bg.get_rect()
size = (width, height) = bg.get_size()


class Boat:
    def __init__(self, x, y, hp, select, press, damage):
        self.x = x
        self.y = y
        self.hp = hp
        self.select = False
        self.press = 0
        self.damage = damage


player1_boat = Boat(5, 5, 2, False,0,1)
player1_boat1 = Boat(230, 5, 3, False,0,1)
player1_boat2 = Boat(410, 5, 4, False,0,1)
player1_boat3 = Boat(635, 5, 2, False,0,1)

player2_boat = Boat(5, 635, 2, False,0,1)
player2_boat1 = Boat(230, 635, 3, False,0,1)
player2_boat2 = Boat(410, 635, 4, False,0,1)
player2_boat3 = Boat(635, 635, 2, False,0,1)

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
    step = 45
    draw_card = True


    while start:
        pygame.display.set_mode((width, height))
        screen.blit(grid_bg, (0, 0))
        screen.blit(pauze_button, (1000, 10))
        screen.blit(end_turn, (690, 630))
        screen.blit(card, (700, 10))
        screen.blit(attack_button,(850,10))
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
            if draw_card:
                if 700 + 100 > mouse[0] > 700 and 10 + 98 > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        cards = [1, 2, 3]
                        if random.choice(cards) == 1:
                            step *= 2
                            print('This is card: step * 2 \n All your boats take steps that are twice as big now')
                            print(step)
                            draw_card == False
                        if random.choice(cards) == 2:
                            print('This is card: +1 HP \n All your boats have +1 HP now')
                            draw_card == False
                            if turn:
                                if player1_boat.hp > 0:
                                    player1_boat.hp = player1_boat.hp + 1
                                if player1_boat1.hp > 0:
                                    player1_boat1.hp = player1_boat1.hp + 1
                                if player1_boat2.hp > 0:
                                    player1_boat2.hp = player1_boat2.hp + 1
                                if player1_boat3.hp > 0:
                                    player1_boat3.hp = player1_boat3.hp + 1
                            else:
                                if player2_boat.hp > 0:
                                    player2_boat.hp = player2_boat.hp + 1
                                if player2_boat1.hp > 0:
                                    player2_boat1.hp = player2_boat1.hp + 1
                                if player2_boat2.hp > 0:
                                    player2_boat2.hp = player2_boat2.hp + 1
                                if player2_boat3.hp > 0:
                                    player2_boat3.hp = player2_boat3.hp + 1
                        if random.choice(cards) == 3:
                            print('This is card: +1 Damage \n All your boats deal +1 damage now')
                            draw_card = False
                            if turn:
                                player1_boat.damage = player1_boat.damage + 1
                                player1_boat1.damage = player1_boat1.damage + 1
                                player1_boat2.damage = player1_boat2.damage + 1
                                player1_boat3.damage = player1_boat3.damage + 1
                            else:
                                player2_boat.damage = player2_boat.damage + 1
                                player2_boat1.damage = player2_boat1.damage + 1
                                player2_boat2.damage = player2_boat2.damage + 1
                                player2_boat3.damage = player2_boat3.damage + 1

            if 690 + 126 > mouse[0] > 690 and 630 + 44 > mouse[1] > 630 and turn == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    turn = False
                    print(turn)
                    step = 45
                    player1_boat.damage = 1
                    player1_boat1.damage = 1
                    player1_boat2.damage = 1
                    player1_boat3.damage = 1
                    player1_boat.press = 0
                    player1_boat2.press = 0
                    player1_boat3.press = 0
                    draw_card = True
                    print ('Player2 Boat1 HP:', player2_boat.hp , 'Player2 Boat1 damage:', player2_boat.damage)
                    print('Player2 Boat2 HP:', player2_boat1.hp, 'Player2 Boat2 damage:', player2_boat1.damage)
                    print('Player2 Boat3 HP:', player2_boat2.hp, 'Player2 Boat3 damage:', player2_boat2.damage)
                    print('Player2 Boat4 HP:', player2_boat3.hp, 'Player2 Boat4 damage:', player2_boat3.damage)
            elif 690 + 126 > mouse[0] > 690 and 630 + 44 > mouse[1] > 630 and turn == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    turn = True
                    print(turn)
                    step = 45
                    player2_boat.damage = 1
                    player2_boat1.damage = 1
                    player2_boat2.damage = 1
                    player2_boat3.damage = 1
                    player2_boat.press = 0
                    player2_boat2.press = 0
                    player2_boat3.press = 0
                    draw_card == True
                    print ('Player1 Boat1 HP:', player1_boat.hp , 'Player1 Boat1 damage:', player1_boat.damage)
                    print('Player1 Boat2 HP:', player1_boat1.hp, 'Player1 Boat2 damage:', player1_boat1.damage)
                    print('Player1 Boat3 HP:', player1_boat2.hp, 'Player1 Boat3 damage:', player1_boat2.damage)
                    print('Player1 Boat4 HP:', player1_boat3.hp, 'Player1 Boat4 damage:', player1_boat3.damage)

        if player1_boat.hp <= 0:
            player1_boat.x = 10000
        if player1_boat1.hp <= 0:
            player1_boat1.x = 10000
        if player1_boat2.hp <= 0:
            player1_boat2.x = 10000
        if player1_boat3.hp <= 0:
            player1_boat3.x = 10000
        if player2_boat.hp <= 0:
            player2_boat.x = 10000
        if player2_boat1.hp <= 0:
            player2_boat1.x = 10000
        if player2_boat2.hp <= 0:
            player2_boat2.x = 10000
        if player2_boat3.hp <= 0:
            player2_boat3.x = 10000

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

            if player2_boat.y - player1_boat.y <= 90 or player2_boat.x - player1_boat.x <= 90 and player2_boat.y - player1_boat.y == 0 or player1_boat.x - player2_boat.x <= 90 and player2_boat.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat.hp -= player1_boat.damage
                            print(player2_boat.hp)

            if player2_boat1.y - player1_boat.y <= 90 or player2_boat1.x - player1_boat.x <= 90 and player2_boat1.y - player1_boat.y == 0 or player1_boat.x - player2_boat1.x <= 90 and player2_boat1.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat1.hp -= player1_boat.damage
                            print(player2_boat1.hp)

            if player2_boat2.y - player1_boat.y <= 90 or player2_boat2.x - player1_boat.x <= 90 and player2_boat2.y - player1_boat.y == 0 or player1_boat.x - player2_boat2.x <= 90 and player2_boat2.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat2.hp -= player1_boat.damage
                            print(player2_boat2.hp)

            if player2_boat3.y - player1_boat.y <= 90 or player2_boat3.x - player1_boat.x <= 90 and player2_boat3.y - player1_boat.y == 0 or player1_boat.x - player2_boat3.x <= 90 and player2_boat3.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat3.hp -= player1_boat.damage
                            print(player2_boat3.hp)

            if player2_boat.y - player1_boat1.y <= 135 or player2_boat.x - player1_boat1.x <= 135 and player2_boat.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat.x <= 135 and player2_boat.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat.hp -= player1_boat1.damage
                            print(player2_boat.hp)

            if player2_boat1.y - player1_boat1.y <= 135 or player2_boat1.x - player1_boat1.x <= 135 and player2_boat1.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat1.x <= 135 and player2_boat1.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat1.hp -= player1_boat1.damage
                            print(player2_boat1.hp)

            if player2_boat2.y - player1_boat1.y <= 135 or player2_boat2.x - player1_boat1.x <= 135 and player2_boat2.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat2.x <= 135 and player2_boat2.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat2.hp -= player1_boat1.damage
                            print(player2_boat2.hp)

            if player2_boat3.y - player1_boat1.y <= 135 or player2_boat3.x - player1_boat1.x <= 135 and player2_boat3.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat3.x <= 135 and player2_boat3.y - player1_boat1.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player2_boat3.hp -= player1_boat1.damage
                        print(player2_boat3.hp)

            if player2_boat.y - player1_boat2.y <= 180 or player2_boat.x - player1_boat2.x <= 180 and player2_boat.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat.x <= 180 and player2_boat.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat.hp -= player1_boat2.damage
                            print(player2_boat.hp)

            if player2_boat1.y - player1_boat2.y <= 180 or player2_boat1.x - player1_boat2.x <= 180 and player2_boat1.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat1.x <= 180 and player2_boat1.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat1.hp -= player1_boat2.damage
                            print(player2_boat1.hp)

            if player2_boat2.y - player1_boat2.y <= 180 or player2_boat2.x - player1_boat2.x <= 180 and player2_boat2.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat2.x <= 180 and player2_boat2.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat2.hp -= player1_boat2.damage
                            print(player2_boat2.hp)

            if player2_boat3.y - player1_boat2.y <= 180 or player2_boat3.x - player1_boat2.x <= 180 and player2_boat3.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat3.x <= 180 and player2_boat3.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat3.hp -= player1_boat2.damage
                            print(player2_boat2.hp)

            if player2_boat.y - player1_boat3.y <= 90 or player2_boat.x - player1_boat3.x <= 90 and player2_boat.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat.x <= 90 and player2_boat.y - player1_boat3.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player2_boat.hp -= player1_boat3.damage
                            print(player2_boat.hp)

            if player2_boat1.y - player1_boat3.y <= 90 or player2_boat1.x - player1_boat3.x <= 90 and player2_boat1.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat1.x <= 90 and player2_boat1.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player2_boat1.hp -= player1_boat3.damage
                        print(player2_boat1.hp)

            if player2_boat2.y - player1_boat3.y <= 90 or player2_boat2.x - player1_boat3.x <= 90 and player2_boat2.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat2.x <= 90 and player2_boat2.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player2_boat2.hp -= player1_boat3.damage
                        print(player2_boat2.hp)

            if player2_boat3.y - player1_boat3.y <= 90 or player2_boat3.x - player1_boat3.x <= 90 and player2_boat3.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat3.x <= 90 and player2_boat3.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player2_boat3.hp -= player1_boat3.damage
                        print(player2_boat3.hp)


            if player1_boat1.select:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1_boat1.x -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player1_boat1.x += step
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player1_boat1.y -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player1_boat1.y += step
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
                            player1_boat2.x -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player1_boat2.x += step
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player1_boat2.y -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player1_boat2.y += step
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
                            player1_boat3.x -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player1_boat3.x += step
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player1_boat3.y -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player1_boat3.y += step
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
                        player1_boat.x -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player1_boat.x += step
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player1_boat.y -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player1_boat.y += step
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

            if player2_boat.y - player1_boat.y <= 90 or player2_boat.x - player1_boat.x <= 90 and player2_boat.y - player1_boat.y == 0 or player1_boat.x - player2_boat.x <= 90 and player2_boat.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat.hp -= player2_boat.damage
                            print(player1_boat.hp)

            if player2_boat1.y - player1_boat.y <= 90 or player2_boat1.x - player1_boat.x <= 90 and player2_boat1.y - player1_boat.y == 0 or player1_boat.x - player2_boat1.x <= 90 and player2_boat1.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat.hp -= player2_boat1.damage
                            print(player1_boat1.hp)

            if player2_boat2.y - player1_boat.y <= 90 or player2_boat2.x - player1_boat.x <= 90 and player2_boat2.y - player1_boat.y == 0 or player1_boat.x - player2_boat2.x <= 90 and player2_boat2.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat.hp -= player2_boat2.damage
                            print(player1_boat2.hp)

            if player2_boat3.y - player1_boat.y <= 90 or player2_boat3.x - player1_boat.x <= 90 and player2_boat3.y - player1_boat.y == 0 or player1_boat.x - player2_boat3.x <= 90 and player2_boat3.y - player1_boat.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat.hp -= player2_boat3.damage
                            print(player1_boat3.hp)

            if player2_boat.y - player1_boat1.y <= 135 or player2_boat.x - player1_boat1.x <= 135 and player2_boat.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat.x <= 135 and player2_boat.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat1.hp -= player2_boat.damage
                            print(player1_boat.hp)

            if player2_boat1.y - player1_boat1.y <= 135 or player2_boat1.x - player1_boat1.x <= 135 and player2_boat1.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat1.x <= 135 and player2_boat1.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat1.hp -= player2_boat1.damage
                            print(player1_boat1.hp)

            if player2_boat2.y - player1_boat1.y <= 135 or player2_boat2.x - player1_boat1.x <= 135 and player2_boat2.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat2.x <= 135 and player2_boat2.y - player1_boat1.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat1.hp -= player2_boat2.damage
                            print(player1_boat2.hp)

            if player2_boat3.y - player1_boat1.y <= 135 or player2_boat3.x - player1_boat1.x <= 135 and player2_boat3.y - player1_boat1.y == 0 or player1_boat1.x - player2_boat3.x <= 135 and player2_boat3.y - player1_boat1.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player1_boat1.hp -= player2_boat3.damage
                        print(player1_boat3.hp)

            if player2_boat.y - player1_boat2.y <= 180 or player2_boat.x - player1_boat2.x <= 180 and player2_boat.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat.x <= 180 and player2_boat.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat2.hp -= player2_boat.damage
                            print(player1_boat.hp)

            if player2_boat1.y - player1_boat2.y <= 180 or player2_boat1.x - player1_boat2.x <= 180 and player2_boat1.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat1.x <= 180 and player2_boat1.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat2.hp -= player2_boat1.damage
                            print(player1_boat1.hp)

            if player2_boat2.y - player1_boat2.y <= 180 or player2_boat2.x - player1_boat2.x <= 180 and player2_boat2.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat2.x <= 180 and player2_boat2.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat2.hp -= player2_boat2.damage
                            print(player1_boat2.hp)

            if player2_boat3.y - player1_boat2.y <= 180 or player2_boat3.x - player1_boat2.x <= 180 and player2_boat3.y - player1_boat2.y == 0 or player1_boat2.x - player2_boat3.x <= 180 and player2_boat3.y - player1_boat2.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat2.hp -= player2_boat3.damage
                            print(player1_boat2.hp)

            if player2_boat.y - player1_boat3.y <= 90 or player2_boat.x - player1_boat3.x <= 90 and player2_boat.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat.x <= 90 and player2_boat.y - player1_boat3.y == 0:
                    if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print('nice')
                            player1_boat3.hp -= player2_boat.damage
                            print(player1_boat.hp)

            if player2_boat1.y - player1_boat3.y <= 90 or player2_boat1.x - player1_boat3.x <= 90 and player2_boat1.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat1.x <= 90 and player2_boat1.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player1_boat3.hp -= player2_boat1.damage
                        print(player1_boat1.hp)

            if player2_boat2.y - player1_boat3.y <= 90 or player2_boat2.x - player1_boat3.x <= 90 and player2_boat2.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat2.x <= 90 and player2_boat2.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player1_boat3.hp -= player2_boat2.damage
                        print(player1_boat2.hp)

            if player2_boat3.y - player1_boat3.y <= 90 or player2_boat3.x - player1_boat3.x <= 90 and player2_boat3.y - player1_boat3.y == 0 or player1_boat3.x - player2_boat3.x <= 90 and player2_boat3.y - player1_boat3.y == 0:
                if (850 + 104) > mouse[0] > 850 and (10 + 44) > mouse[1] > 10:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print('nice')
                        player1_boat3.hp -= player2_boat3.damage
                        print(player1_boat3.hp)

            if player2_boat1.select:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player2_boat1.x -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2_boat1.x += step
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player2_boat1.y -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player2_boat1.y += step
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
                            player2_boat2.x -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player2_boat2.x += step
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player2_boat2.y -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player2_boat2.y += step
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
                            player2_boat3.x -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_RIGHT:
                            player2_boat3.x += step
                            #pygame.mixer.music.play(0, 0)
                        if event.key == pygame.K_UP:
                            player2_boat3.y -= step
                            #pygame.mixer.music.play(0, 0)
                        elif event.key == pygame.K_DOWN:
                            player2_boat3.y += step
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
                        player2_boat.x -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2_boat.x += step
                        #pygame.mixer.music.play(0, 0)
                    if event.key == pygame.K_UP:
                        player2_boat.y -= step
                        #pygame.mixer.music.play(0, 0)
                    elif event.key == pygame.K_DOWN:
                        player2_boat.y += step
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
