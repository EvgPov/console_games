import time
import random
from clear_screen import clear_screen

NUMBERS = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]

def print_board(board):
# вывод игрового поля
    print('\n' + '=' * 13)
    print(' ИГРОВОЕ ПОЛЕ')
    print('=' * 13)
    for i in range(2, -1, -1):
        print(' | '.join(board[i]), end=' |')
        print()
        if i > 0:
            print('---+---+---')
    print('=' * 13)
    print('НОМЕРА ДЛЯ ВВОДА:')
    print(' 7 | 8 | 9 ')
    print('---+---+---')
    print(' 4 | 5 | 6 ')
    print('---+---+---')
    print(' 1 | 2 | 3 ')
    print('=' * 13 + '\n')

def make_move(board, position, symbol):
# ставит символ в указанную позицию
    row, col = divmod(position - 1, 3)
    if board[row][col].isdigit():
        board[row][col] = symbol
        return True
    return False

def check_winner(board, symbol):
    # проверка победы
    # горизонтали
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # вертикали
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # диагонали
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False

def is_board_full(board):
    # проверка ничьи
    for row in range(3):
        for col in range(3):
            cell = board[row][col]
            if cell in '123456789':
                return False
    return True

def get_computer_move(board):
    # компьютер ищет выигрыш/блокировку

    # проверка выигрышных ходов
    for pos in range(1, 10):
        temp_board =[row[:] for row in board]
        if make_move(temp_board, pos, 'X'):
            if check_winner(temp_board, 'X'):
                return pos
    # блокируем выигрыш игрока
    for pos in range(1, 10):
        temp_board = [row[:] for row in board]
        if make_move(temp_board, pos, 'O'):
            if check_winner(temp_board, 'O'):
                return pos

    # центр
    if make_move(board, 5, 'X'):
        return 5
    # углы
    corners = [1, 3, 7, 9]
    random.shuffle(corners)
    for corner in corners:
        if make_move(board, corner, 'X'):
            return corner
    # любая свободная клетка
    for pos in range(1, 10):
        if make_move(board, pos, 'X'):
            return pos

def play_game(two_players=True):
    #основная функция
    board = [row[:] for row in NUMBERS] # копируем поле с номерами

    current_player = 'O' # первый ход - нолик
    clear_screen()  # очищаем экран
    print('КРЕСТИКИ-НОЛИКИ')
    print('Игрок 1: 0 (нолик) - ходит первым')
    print('Игрок 2: X (крестик)' if two_players else 'Компьютер: X (крестик)')
    print()

    while True:
        print_board(board)
    # ход игрока
        if current_player == 'O' or two_players:
            while True:
                try:
                    pos = int(input(f'Ход {current_player} (1-9): '))
                    if 1 <= pos <= 9 and make_move(board, pos, current_player):
                        break
                    else:
                        print ('Неверная позиция! Выберите свободную клетку (1-9)')
                except ValueError:
                    print('Введите число от 1 до 9!')
        else:
            print('Компьютер думает')
            pos = get_computer_move(board)
            make_move(board, pos, 'X')
            print(f'Компьютер выбрал: {pos}')
    # проверка победы
        if check_winner(board, current_player):
            clear_screen()  # очищаем экран
            print_board(board)
            print(f" {'Игрок 1' if current_player == 'O' else 'Игрок 2' if two_players else 'Компьютер'} Победил!")
            time.sleep(1)
            return
    # проверка ничьи
        if is_board_full(board):
            clear_screen()  # очищаем экран
            print_board(board)
            print('НИЧЬЯ!')
            time.sleep(1)
            return
    #  смена игрока
        current_player = 'X' if current_player == 'O' else 'O'
        clear_screen()  # очищаем экран

def tic_tac_toe():
    # меню
    while True:
        clear_screen()  # очищаем экран
        print('\nДобро пожаловать в игру "КРЕСТИКИ-НОЛИКИ"')
        print('\n' + '═' * 45)
        print('КРЕСТИКИ-НОЛИКИ'.center(45))
        print('═' * 45)
        print('1. Игра вдвоем')
        print('2. Игра против компьютера')
        print('0. Выход')
        print('=' * 45)

        choice = input('Выберите режим игры: ').strip()

        if choice == '1':
            play_game(two_players=True)
            input('\nНажмите Enter для продолжения')
        elif choice == '2':
            play_game(two_players=False)
            input('\nНажмите Enter для продолжения')
        elif choice == '0':
            print('Спаcибо за игру! До встречи!')
            time.sleep(1)
            break
        else:
            print('Такого пункта нет')
            input('\nНажмите Enter для продолжения')
            time.sleep(1)
