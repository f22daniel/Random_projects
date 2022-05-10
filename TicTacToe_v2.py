# Tic Tac Toe with changeable board size and for 2 human players

import os

winner = None
blank = '-'
spacer = '|'
boardDict = {}
boardList = []
Player = 'X'
game_won = False

size = int(input('Enter a size: '))

def display_board():
    position = 0
    alphabet = ''
    for x in range(65, (size + 65)):
        alphabet = alphabet + spacer + chr(x)
    print(alphabet + spacer)
    for n in range(0, size):
        row = ''
        for i in range(0, size):
            boardDict.update({f'{chr(65+i)}{n+1}': f'{blank}'})
            boardList.append(blank)
            row = row + spacer + boardDict.get(f'{chr(65+i)}{n+1}')
            position = position + 1
        row = row + spacer
        print(f'{row} {str(n+1)}')
    print(boardList)

def update_board():
    global boardList
    print(f"It is {Player}'s turn.")
    while True:
        PlayerInput = input('Enter position: ')
        if boardDict[f'{PlayerInput}'] != '-':
            print('Spot already taken, go again.')
        else:
            break
    os.system('cls')
    boardDict.update({PlayerInput: Player})
    position = 0
    alphabet = ''
    for x in range(65, (size + 65)):
        alphabet = alphabet + spacer + chr(x)
    print('')
    print(alphabet + spacer)
    boardList.clear()
    for n in range(0, size):
        row = ''
        for i in range(0, size):
            row = row + spacer + boardDict.get(f'{chr(65 + i)}{n + 1}')
            boardList.append(boardDict.get(f'{chr(65 + i)}{n + 1}'))
            position = position + 1
        row = row + spacer
        print(f'{row} {str(n + 1)}')
    check_for_winner()
    check_for_tie()
    switch_player()

def switch_player():
    global Player
    if Player == 'X':
        Player = 'O'
    elif Player == 'O':
        Player = 'X'

def check_for_tie():
    global game_won, boardList
    if '-' not in boardList:
        game_won = True
        print('Tie!!')

def check_for_winner():
    check_for_column_X()
    check_for_column_O()
    check_for_row_X()
    check_for_row_O()
    check_for_diagonal_X()
    check_for_diagonal_O()

def check_for_column_X():
    global game_won
    mark = 0
    for column in range(1, size+1):
        for row in range(1, size+1):
            if boardDict.get(f'{chr(65 + column)}{row}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0

def check_for_column_O():
    global game_won
    mark = 0
    for column in range(1, size+1):
        for row in range(1, size+1):
            if boardDict.get(f'{chr(65 + column)}{row}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark = 0

def check_for_row_X():
    global game_won
    mark = 0
    for row in range(1, size+1):
        for column in range(1, size+1):
            if boardDict.get(f'{chr(65 + column)}{row}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0

def check_for_row_O():
    global game_won
    mark = 0
    for row in range(1, size+1):
        for column in range(1, size+1):
            if boardDict.get(f'{chr(65 + column)}{row}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark = 0

def check_for_diagonal_X():
    global game_won
    mark = 0
    ''''''
    for i in range(1, size+1):
        for diagonal in range(1, size+1):
            if boardDict.get(f'{chr(63 + diagonal + i)}{diagonal}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0
    for i in range(1, size + 1):
        for diagonal in range(1, size + 1):
            if boardDict.get(f'{chr(64 + diagonal)}{diagonal + i}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0
    for i in range(1, size+1):
        for diagonal in range(1, size+1):
            if boardDict.get(f'{chr(64 + diagonal)}{(size+1) - diagonal - (i-1)}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0
    for i in range(1, size + 1):
        for diagonal in range(size+1, 0, -1):
            if boardDict.get(f'{chr(65 + diagonal)}{(size + 1) - diagonal + (i - 1)}') == 'X':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is X')
                    game_won = True
                    break
            else:
                mark = 0
def check_for_diagonal_O():
    global game_won
    mark = 0
    ''''''
    for i in range(1, size+1):
        for diagonal in range(1, size+1):
            if boardDict.get(f'{chr(63 + diagonal + i)}{diagonal}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark=0
    for i in range(1, size + 1):
        for diagonal in range(1, size + 1):
            if boardDict.get(f'{chr(64 + diagonal)}{diagonal + i}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark = 0
    for i in range(1, size+1):
        for diagonal in range(1, size+1):
            if boardDict.get(f'{chr(64 + diagonal)}{(size+1) - diagonal - (i-1)}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark = 0
    for i in range(1, size + 1):
        for diagonal in range(size+1, 0, -1):
            if boardDict.get(f'{chr(65 + diagonal)}{(size + 1) - diagonal + (i - 1)}') == 'O':
                mark = mark + 1
                if mark == 5:
                    print(f'\nWinner is O')
                    game_won = True
                    break
            else:
                mark = 0

display_board()
while not game_won:
    update_board()
