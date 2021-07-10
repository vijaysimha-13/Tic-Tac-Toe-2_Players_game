import time


# table is the list that contains 3 elements which stand for each row in the Tic-Tac-Toe board.
# And each of these 3 elements is also a list consisting of three sub-elements that represent
# each column in the Tic-Tac-Toe board.
#                                 table[0][0] | table[0][1] | table[0][2]
#                                 ---------------------------------------
#                                 table[1][0] | table[1][1] | table[1][2]
#                                 ---------------------------------------
#                                 table[2][0] | table[2][1] | table[2][2]


def display_board(table):       # Function for printing out the Tic-Tac-Toe board.

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(table[0][0], table[0][1], table[0][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(table[1][0], table[1][1], table[1][2]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(table[2][0], table[2][1], table[2][2]))
    print("\t     |     |")


def result(table, n, signs):
    # signs is a list that consists of 2 elements, 1st element represents Player 1 marker and 2nd element is Player 2's
    # n stands for total number of moves made till that time

    game_status = 'Playing'
    for k in range(3):
        # conditions for row or column win cases
        if ((table[0][k], table[1][k], table[2][k]).count(signs[0]) == 3) or (table[k].count(signs[0]) == 3):
            game_status = 'Player-1 Won'
            return 'Yay!, Great Player 1, You have won'
            break
        if ((table[0][k], table[1][k], table[2][k]).count(signs[1]) == 3) or (table[k].count(signs[1]) == 3):
            game_status = 'Player-2 Won'
            return 'Yay!, Great Player 2, You have won!!'
            break

    # conditions for case where a player wins in a diagonal manner
    if (table[0][0] == table[1][1] == table[2][2]) or (table[0][2] == table[1][1] == table[2][0]):
        # checking which player has won
        if table[1][1] == signs[0]:
            game_status = 'Player-1 Won'
            return 'Yay!, Great Player 1, You have won!'
        elif table[1][1] == signs[1]:
            game_status = 'Player-2 Won'
            return 'Yay!, Great Player 2, You have won'

    if (game_status == 'Playing') and (n == 9):
        return "Oops!, It's a Draw ^_^"


def game(table):

    # INTRO TEXTS
    print('Welcome to Tic-Tac-Toe')
    symbols = input("Enter your game marker signs in the order, Player-1 Player-2:")     # Asking for Players game signs
    marker = [symbols[0], symbols[2]]
    print('Be ready players, It is time to have some fun!!!')
    time.sleep(2)
    display_board(table)
    print(f"Player 1 start the game with your first move, Enter the position where you want to make your move "
          f"in this way:(row-number column-number)")
    # INTRO TEXTS ENDS

    m = 0                         # m equals number of moves made

    # res stands for game status, if 'res' exists, that means the game has been ended.
    res = result(table, 0, marker)
    while not res:
        # input is in the order of "row-number column-number",this is the position where the player wants to make a move
        input_position = input()

        # 'x' denotes row number and 'y' denotes column number
        x, y = (int(input_position[0]), int(input_position[2]))

        # 'z' stands for game marker of the player who is making a move, if it's Nth move, m stands for N-1 value
        z = marker[0] if m % 2 == 0 else marker[1]

        if table[x-1][y-1] == ' ':            # checking whether the mentioned position is empty or not
            table[x-1][y-1] = z
            display_board(table)
            m += 1
            res = result(table, m, marker)
            if not res:
                print(f"make a move")
        else:
            print(f"That position is already filled, please re-enter {z} position correctly")
    return res


# Each element in this list stands for each row in the Tic-Tac-Toe board
empty_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]             # Game starts with empty board
print(game(empty_grid))
