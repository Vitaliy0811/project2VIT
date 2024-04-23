import random
import sqlite3

conn = sqlite3.connect('game.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS numbers (number INTEGER, result TEXT)''')
conn.commit()

class Game:
    def __init__(self):
        self.number = 0
        self.result = ''
        self.number = random.randint(1, 100)

    def create_number(self):  # zagadannoe chislo
        self.number = random.randint(1, 100)

    def check_guess(self, guess):
        if guess == self.number:
            self.result = 'Вы угадали!'
        elif guess < self.number:
            self.result = 'Не верно, подсказка: число больше'
        else:
            self.result = 'Не верно, подсказка: число меньше'

    def save_result(self):
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO numbers VALUES (?, ?)", (self.number, self.result))
        conn.commit()

    def get_results(self):
        conn = sqlite3.connect('game.db')
        cursor = conn.cursor()
        cursor.execute("SELECT number, result FROM numbers")
        results = cursor.fetchall()
        for result in results:
            print(f"Загаданное число: {result[0]}, Результат: {result[1]}")

game = Game()

while True:
    guess = input('Введите число от 1 до 100:')
    if guess.isdigit():
        guess = int(guess)
        game.check_guess(guess)
        print(game.result)
        if game.result == 'Вы угадали!':
            game.save_result()
            break
    else:
        print('Вы ввели некорректное число!')

game.get_results()