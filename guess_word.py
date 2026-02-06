import random
import time

from clear_screen import clear_screen

def guess_word():
    # список слов
    words = [
        'массив',
        'программа',
        'приложение',
        'класс',
        'объект',
        'вирус',
        'сервер',
        'цикл',
        'компьютер',
        'монитор',
        'клавиатура',
        'программирование',
        'переменная',
        'константа',
        'интернет',
        'функция',
        'алгоритм',
        'интерфейс',
        'планшет',
        'ноутбук'
    ]
    # выбираем случайное слово (выбор одного слова из последовательности)
    secret_word = random.choice(words)
    # приводим слово к нижнему регистру (на всякий случай)
    secret_word = secret_word.lower()
    #  максимальное количество попыток
    max_attempts = 7
    attempts = max_attempts
    # названные буквы
    guessed_letters = set()
    # текущее отображение слова
    display = ['_']* len(secret_word)

    clear_screen()  # очищаем экран
    print('\nДобро пожаловать в игру "Угадай слово"')
    print('\n' + '═' * 45)
    print('УГАДАЙ СЛОВО'.center(45))
    print('═' * 45)
    print('У Вас есть', max_attempts, 'попыток')
    print('Слово состоит из', len(secret_word), 'букв\n')

    while attempts > 0 and '_' in display:
        # текущее состояние
        print(''.join(display))
        print(f'Осталось попыток: {attempts}')

        if guessed_letters:
            print('Названные буквы:', ', '.join(sorted(guessed_letters)))

        # ввод буквы
        letter = input('\nНазовите букву: ').lower().strip()

        #  проверяем корректность ввода
        if len(letter) != 1 or not letter.isalpha():
            print('Нужно ввести ровно одну букву!')
            continue

        if letter in guessed_letters:
            print('Вы уже называли эту букву')
            continue

        # запонимаем букву
        guessed_letters.add(letter)

        if letter in secret_word:
            print('Эта буква есть в слове!')

            # открываем все вхождения этой буквы
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    display[i] = letter
        else:
            print('Этой буквы нет в слове!')
            attempts -= 1
    print('\n' + '═' * 45)
    if '_' not in display:
        print(f"Победа! Вы угадали слово: {secret_word.upper()}".center(45))
    else:
        print('Попытки закончились'.center(45))
        print(f"Загаданное слово было: {secret_word.upper()}".center(45))
    print('═' * 45)
    time.sleep(1.5)