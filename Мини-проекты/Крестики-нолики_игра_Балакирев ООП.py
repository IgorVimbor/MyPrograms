# Реализация игры "Крестики-нолики"
import random


class Cell:
    # класс представляющий клетку игрового поля
    def __init__(self):
        self.value = 0    # текущее значение в ячейке:
        # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    def __bool__(self):
        return self.value == 0


class TicTacToe:    # класс для управления игровым процессом
    FREE_CELL = 0   # свободная клетка
    HUMAN_X = 'X'     # крестик (игрок - человек)
    COMPUTER_O = 'O'  # нолик (игрок - компьютер)

    def __init__(self):
        self._n = 3   # размер игрового поля
        # создание игрового поля 3x3, где клетки - это объекты класса Cell
        self.pole = tuple(tuple(Cell() for _ in range(self._n)) for _ in range(self._n))
        self._victory = 0   # 1 - победил человек, 2 - компьютер, 3 - ничья

    def verify(self, indx):  # метод проверки вводимых цифр (индексов)
        i, j = indx
        if type(i) is not int or i not in range(self._n) \
                or type(j) is not int or j not in range(self._n):
            raise IndexError('некорректно указанные индексы')

    def __check_game(self):  # метод проверки кто выиграл
        # проверка строк и столбцов
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._victory = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._victory = 2
                return

        # проверка столбцов (строк в транспонированной матрице)
        tr_pole = tuple(zip(*self.pole))  # транспонированная матрица
        for row in tr_pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._victory = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._victory = 2
                return

        # проверка главной и побочной диагоналей игрового поля
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._n)) or \
                all(self.pole[i][self._n - i - 1].value == self.HUMAN_X for i in range(self._n)):
            self._victory = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._n)) or \
                all(self.pole[i][self._n - i - 1].value == self.COMPUTER_O for i in range(self._n)):
            self._victory = 2
            return

        # проверка на ничью
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._victory = 3

    def __getitem__(self, item):
        self.verify(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.verify(key)
        i, j = key
        self.pole[i][j].value = value
        self.__check_game()

    def init(self):
        # метод инициализации игрового поля (все клетки заполняются нулями)
        for i in range(self._n):
            for j in range(self._n):
                self.pole[i][j].value = 0
        self._victory = 0

    def show(self):
        for row in self.pole:
            for x in row:
                print(x.value if x.value else '*', end=' ')
            print()
        print()

    def human_go(self):
        print('Введите через пробел две цифры от 0 до 2 (включительно)')
        i, j = map(int, input().split())
        if self[i, j] == self.FREE_CELL:
            self[i, j] = self.HUMAN_X

    def computer_go(self):
        while True:
            i = random.randint(0, self._n - 1)
            j = random.randint(0, self._n - 1)
            if self[i, j] != self.FREE_CELL:
                continue
            self[i, j] = self.COMPUTER_O
            break

    @property
    def is_human_win(self):
        return self._victory == 1

    @property
    def is_computer_win(self):
        return self._victory == 2

    @property
    def is_draw(self):
        return self._victory == 3

    def __bool__(self):
        return self._victory == 0 and self._victory not in (1, 2, 3)


game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()
if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
