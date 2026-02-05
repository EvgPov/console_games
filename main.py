from guess_word import guess_word
from tic_tac_toe import tic_tac_toe
from snake import snake

import time
while True:
    print("\n" + "═" * 45)
    print("КОНСОЛЬНЫЕ ИГРЫ".center(45))
    print("═" * 45)
    print()
    print("  1  →  Угадай слово")
    print("  2  →  Крестики-нолики")
    print("  3  →  Змейка")
    print()
    print("  0  →  Выход")
    print("═" * 45)
    print()

    choice = input('Выберите игру(1-3): ').strip()
    if choice == '1':
        guess_word()
    elif choice == '2':
        tic_tac_toe()
    elif choice == '3':
        snake()
    elif choice == '0':
        print('Спаcибо за игру! До встречи!')
        time.sleep(1)
        break
    else:
        print('\nТакого пункта нет')
        time.sleep(1)

