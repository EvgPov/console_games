import random
import sys
import time

from clear_screen import clear_screen

# размер игрового поля
SIZE = 15

# генерирует новую еду в местах, где нет змейки
def get_food(snake):
    while True:
        r = random.randint(0, SIZE - 1)
        c = random.randint(0, SIZE - 1)
        if (r, c) not in snake:
            return (r, c)

def draw(snake, food, score):
    board = [['⬛'] * SIZE for _ in range(SIZE)]

    # тело змейки
    for r, c in snake:
        board[r][c] = '⬜'
    # голова змейки
    hr, hc = snake[-1]
    board[hr][hc] = '👀'
    # еда
    fr, fc = food
    board[fr][fc] = '🍎'
    # рамка и поле
    print('┌' + '─' * (SIZE * 2) + '┐')
    for row in board:
        print('│ ' + ' '.join(row) + '│')
    print('└'+ '─' * (SIZE * 2) + '┘')
    print(f" Счет: {score}  w (вверх), a (влево), s (вниз), d (право) - движение, q - выход)")

def is_valid_position(pos):
    r, c = pos
    return 0 <= r < SIZE and 0 <= c < SIZE

def snake():
    clear_screen()  # очищаем экран
    # змейка размером 1 в центре поля
    snake = [(SIZE // 2, SIZE // 2)] # координаты [7, 7]
    direction = (0, 1) # начальное направление вправо
    food = get_food(snake) # генерируется первая еда
    score = 0

    directions = {
        'w': (-1, 0), # up
        'a': (0, -1), # left
        's': (1, 0), # down
        'd': (0, 1) # right
    }
    print('\nДобро пожаловать в игру "Змейка" (15 X 15)')
    # print ('Управление: w (вверх), a (влево), s (вниз), d (право)')
    # print('q - выход из игры')
    print('Нажмите Enter для начала')
    input()

    while True:
        clear_screen() # очищаем экран
        draw(snake, food, score) # рисуем текущее состояние поля
        try:
            key = input().lower().strip() # ждем нажатия клавиши
        except KeyboardInterrupt:
            print('\nИгра прервана')
            sys.exit(0)
        if key == 'q':
            print("Игра окончена")
            print(f"Финальный счет: {score}")
            time.sleep(1)
            break
        if key in directions: # если нажата w/a/s/d, то пытаемся изменить напрвление
            new_direction = directions[key]
            # запрещаем разворот на 180 градусов
            if new_direction != (-direction[0], -direction[1]):
                direction = new_direction
        # новая позиция головы
        head_r, head_c = snake[-1]
        new_head = (head_r + direction[0], head_c + direction[1])
        # проверка на стлкновение со стеной
        if not is_valid_position(new_head):
            print('\nВврезался в стену')
            print(f'Финальный счет: {score}')
            time.sleep(1)
            break
        # проверка на столкновение с собой
        if new_head in snake:
            print('\nВрезался в себя!')
            print(f'Финальный счет: {score}')
            time.sleep(1)
            break
        # добавляем новую голову
        snake.append(new_head)
        # если съела еду
        if new_head == food:
            score += 1
            food = get_food(snake)
        else:
            # убираем хвост, если не съели
            snake.pop(0)