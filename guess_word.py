import random
def def_guess_word():
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
    # угаданные буквы
    guessed_letters = set()
    # текущее отображение слова
    display = ['_']* len(secret_word)

    print('\nДобро пожаловать в игру "Угадай слово"')
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
            print('Ты уже называл эту букву')
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
    print('\n' + '-' * 45)
    if '_' not in display:
        print('Победа! Вы угадали слово:', secret_word.upper())
    else:
        print('Попытки закончились')
        print('Загаданное слово было: ', secret_word.upper())
    print('\n' + '-' * 45)