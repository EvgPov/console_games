import os

def clear_screen():
    # очищает консоль
    os.system('cls' if os.name == 'nt' else 'clear')
