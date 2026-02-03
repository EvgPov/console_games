from main import choice
import time
import random
def play_game(two_players=True):
    #основная функция

def def_tic_tac_toe():
    # меню
    while True:
        print('\n' + '=' * 45)
        print('КРЕСТИКИ-НОЛИКИ'.center(45))
        print('=' * 45)
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
