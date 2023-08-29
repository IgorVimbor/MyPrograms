# Программа генерирует задания на сложение, вычитание и сравнение чисел.
# Выводит на печать или сохраняет в файл список заданий.

import random

class Test_math:
    def __init__(self, count, limit) -> None:
        """count: количество заданий (тестов).
        limit: число-ограничение (в пределах этого числа будут слагаемые и результат действий)
        Например, limit=20 -> слагаемые и результат сложения/вычитания чисел должен быть НЕ более 20.
        """
        self.count = count                             # общее количество заданий
        self.count_sum = self.count // 2               # количество заданий на сложение
        self.count_dif = self.count - self.count_sum   # количество заданий на вычитание
        self.limit = limit                             # число-ограничение
        self.lst_2num = []                             # результирующий список заданий с ДВУМЯ числами
        self.lst_3num = []                             # результирующий список заданий с ТРЕМЯ числами

    # метод возвращает три рандомных числа в пределах ограничения limit
    def get_nums(self):
        x = random.randint(0, self.limit)
        y = random.randint(0, self.limit)
        z = random.randint(0, self.limit)
        return x, y, z

    # метод добавляет в результирующий список задания на сложение ДВУХ чисел
    def sum_2_args(self):
        i = 0
        while i < self.count_sum:
            x, y, z = self.get_nums()
            if x + y <= self.limit:
                result = f'{x} + {y}'
            else:
                continue
            self.lst_2num.append(result)
            i += 1

    # метод добавляет в результирующий список задания на вычитание ДВУХ чисел
    def dif_2_args(self):
        i = 0
        while i < self.count_dif:
            x, y, z = self.get_nums()
            if x - y <= self.limit and x - y > 0:
                result = f'{x} - {y}'
            else:
                continue
            self.lst_2num.append(result)
            i += 1

    # метод добавляет в результирующий список задания на сложение ТРЕХ чисел
    def sum_3_args(self):
        i = 0
        while i < self.count_sum:
            x, y, z = self.get_nums()
            if x + y + z <= self.limit:
                result = f'{x} + {y} + {z}'
            else:
                continue
            self.lst_3num.append(result)
            i += 1

    # метод добавляет в результирующий список задания на вычитание ТРЕХ чисел
    def dif_3_args(self):
        i = 0
        while i < self.count_dif:
            x, y, z = self.get_nums()
            if x - y + z <= self.limit and x - y > 0:
                result = f'{x} - {y} + {z}'
            elif x + y <= self.limit and x + y - z > 0:
                result = f'{x} + {y} - {z}'
            else:
                continue
            self.lst_3num.append(result)
            i += 1

    # метод перемешивает результирующие списки и возвращает их
    def get_lst(self):
        self.sum_2_args()
        self.dif_2_args()
        random.shuffle(self.lst_2num)

        self.sum_3_args()
        self.dif_3_args()
        random.shuffle(self.lst_3num)

        return self.lst_2num, self.lst_3num

    # метод выводит задания в консоль по столбцам
    def show_test(self, d, mark=None):
        """аргумент mark - флаг сохранения в файл (по умолчанию - вывод в консоль).
           d - количество столбцов при выводе на печать
        """
        # делим списки с заданиями на подсписки размерами равными количеству столбцов
        data_2num = [self.get_lst()[0][i:d+i] for i in range(0, self.count, d)]
        data_3num = [self.get_lst()[1][i:d+i] for i in range(0, self.count, d)]

        print('  \n1. Выполни задания на сложение и вычитание двух чисел:\n', file=mark)
        for el in data_2num:
            for value in el:
                print(f"{value + ' =':30}", end='', file=mark)
            print(file=mark)
        print(file=mark)

        print('  \n2. Выполни задания на сложение и вычитание трех чисел:\n', file=mark)
        for el in data_3num:
            for value in el:
                print(f"{value + ' =':30}", end='', file=mark)
            print(file=mark)
        print(file=mark)

        print('  \n3. Выполни задания на сравнение чисел:\n', file=mark)
        for i in range(0, self.count-1, 2):
            print(self.lst_2num[i], self.lst_2num[i+1], sep='   ', file=mark)
        print(file=mark)

        return 'Файл записан.' if mark else None


if __name__ == '__main__':
    # создаем экземпляр класса
    obj = Test_math(15, 20)   # 15 - количество заданий, 20 - число-ограничение

    # obj.show_test(3)        # выводим в консоль в три столбца

    # сохраняем в файл на локальном диске Е (задания печатаются в три столбца)
    with open('E://Задания_по_математике_2класс.txt', 'w') as file_out:
        print(obj.show_test(3, mark=file_out))
