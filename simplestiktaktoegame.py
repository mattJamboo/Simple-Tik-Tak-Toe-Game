# Start screen/welcome func
def start_screen():
    want_to_play = ''

    wanna_play = ['Y','N']

    print('Hey, this a Tic Tac Toe game! ')

    while want_to_play not in wanna_play:
        want_to_play = input('Do you want to play? Y or N ').upper()

        if want_to_play not in wanna_play:
            print('Insert a valid option')

    return want_to_play

def player_signpick():
    sign1 = ''
    sign2 = ''
    player1_turn = True
#
    signs = ['X','O']

    while sign1 not in signs:
        sign1 = input('Player 1 will choose. Are you X or O? ').upper()


        if sign1 not in signs:
            print('Pick a valid sign. ')

    if sign1 == 'X':
        sign2 = 'O'
    elif sign1 == 'O':
        sign2 = 'X'

    return sign1,sign2,player1_turn

def game_display(game_line1,game_line2,game_line3):

    print('\n'*100)
    print(game_line1)
    print(game_line2)
    print(game_line3)

def player_pick():

        position = ''
        position_possibility = [1,2,3,4,5,6,7,8,9]

        while position not in position_possibility:
            position = int(input('Where do you want to place your sign? (1-9) '))

            return position

def empty_check(game_line1,game_line2,game_line3,position):


    if position <= 3:
        if game_line1[position-1] == ' ':

            return True

    if position > 3 and position <= 6:
        if game_line2[position-4] == ' ':
            return True


    if position > 6 and position <= 9:
        if game_line3[position-7] == ' ':
            return True

    else:
        return False

def pick_aloccation(player1_turn, game_line1, game_line2, game_line3, position, sign1, sign2,empty ):

        if empty == True:
            if player1_turn == True:
                if position <= 3:
                    game_line1[position - 1] = sign1
                    player1_turn = False

                if position > 3 and position <= 6:
                    game_line2[position - 4] = sign1
                    player1_turn = False

                if position > 6 and position <= 9:
                    game_line3[position - 7] = sign1
                    player1_turn = False

            elif player1_turn == False:
                if position <= 3:
                    game_line1[position - 1] = sign2
                    player1_turn = True

                if position > 3 and position <= 6:
                    game_line2[position - 4] = sign2
                    player1_turn = True

                if position > 6 and position <= 9:
                    game_line3[position - 7] = sign2
                    player1_turn = True
        else:
            print('That spot is already taken! ')

        return game_line1, game_line2, game_line3, player1_turn

def win_draw_check(game_line1,game_line2,game_line3,player1_turn):
    win = False
    draw_cond = ''

    if player1_turn == True:
        player = 'Player 2'
    elif player1_turn == False:
        player = 'Player 1'

    # Win on lines 1,2 and 3
    if game_line1[0] == game_line1[1] == game_line1[2] == 'X' or game_line1[0] == game_line1[1] == game_line1[2] == 'O':

        win = True
    elif game_line2[0] == game_line2[1] == game_line2[2] == 'X' or game_line2[0] == game_line2[1] == game_line2[2] == 'O':

        win = True
    elif game_line3[0] == game_line3[1] == game_line3[2] == 'X' or game_line3[0] == game_line3[1] == game_line3[2] == 'O':

        win = True

    # Win on diagonals
    elif game_line1[0] == game_line2[1] == game_line3[2] == 'X' or game_line1[0] == game_line2[1] == game_line3[2] == 'O':

        win = True
    elif game_line1[2] == game_line2[1] == game_line3[0] == 'X' or game_line1[2] == game_line2[1] == game_line3[0] == 'O':

        win = True

    # Win on columns
    elif game_line1[0] == game_line2[0] == game_line3[0] == 'X' or game_line1[0] == game_line2[0] == game_line3[0] == 'O':

        win = True
    elif game_line1[1] == game_line2[1] == game_line3[1] == 'X' or game_line1[1] == game_line2[1] == game_line3[1] == 'O':

        win = True
    elif game_line1[2] == game_line2[2] == game_line3[2] == 'X' or game_line1[2] == game_line2[2] == game_line3[2] == 'O':

        win = True

    # Check if board is full.

    if game_line1[0] == ' ' or game_line1[1] == ' ' or game_line1[2] == ' ':
        draw_cond = False

    elif game_line2[0] == ' ' or game_line2[1] == ' ' or game_line2[2] == ' ':
        draw_cond = False

    elif game_line3[0] == ' 'or  game_line3[1] == ' ' or  game_line3[2] == ' ':
        draw_cond = False

    else:
         draw_cond = True






    return win,player,draw_cond

def game_on():

    want_to_play = input('Do you want to keep playing? Y or N ').upper()

    return want_to_play

def clear_board():

    game_line1 = [' ', ' ', ' ']
    game_line2 = [' ', ' ', ' ']
    game_line3 = [' ', ' ', ' ']

    return game_line1,game_line2,game_line3

# Game code

game_line1 = [' ',' ',' ']
game_line2 = [' ',' ',' ']
game_line3 = [' ',' ',' ']


want_to_play = start_screen()

sign1,sign2,player1_turn = player_signpick()

while want_to_play == 'Y':

    game_display(game_line1,game_line2,game_line3)

    position = player_pick()

    empty = empty_check(game_line1,game_line2,game_line3,position)

    if empty == False:
        print('That spot is already taken! ')
        continue
    else:
        pass

    game_line1,game_line2,game_line3,player1_turn = pick_aloccation(player1_turn,game_line1,game_line2,game_line3,position,sign1,sign2,empty)

    win,player,draw_cond = win_draw_check(game_line1, game_line2, game_line3, player1_turn)

    if win == True:


        game_display(game_line1, game_line2, game_line3)
        print(f'{player} is the winner! ')
        want_to_play = game_on()

        if want_to_play == 'Y':
            game_line1, game_line2, game_line3 = clear_board()

            sign1, sign2, player1_turn = player_signpick()

        else:
             pass

    elif win == False:

        if draw_cond == True:

            game_display(game_line1, game_line2, game_line3)
            print("It's a draw! ")
            want_to_play = game_on()

            if want_to_play == 'Y':
                game_line1, game_line2, game_line3 = clear_board()

                sign1, sign2, player1_turn = player_signpick()

            else:
                pass



print('Game ended ')




















