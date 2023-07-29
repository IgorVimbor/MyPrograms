# Программа генерирует задания на сложение и вычитание чисел.

import random

class Example:
    def __init__(self, limit) -> None:
        """limit: число-ограничение (в пределах этого числа будут слагаемые и результат действий)
        Например, limit=20 -> слагаемые и результат сложения/вычитания чисел должен быть НЕ более 20.
        """
        self.limit = limit     # число-ограничение

    # метод возвращает три рандомных числа в пределах ограничения limit
    def get_nums(self):
        x = random.randint(0, self.limit)
        y = random.randint(0, self.limit)
        z = random.randint(0, self.limit)
        return x, y, z

    # метод генерирует и возвращает задание на сложение ДВУХ чисел
    def sum_2_args(self):
        while True:
            x, y, z = self.get_nums()
            if x + y <= self.limit:
                result = f'{x} + {y} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на вычитание ДВУХ чисел
    def dif_2_args(self):
        while True:
            x, y, z = self.get_nums()
            if x - y <= self.limit and x - y > 0:
                result = f'{x} - {y} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на сложение ТРЕХ чисел
    def sum_3_args(self):
        while True:
            x, y, z = self.get_nums()
            if x + y + z <= self.limit:
                result = f'{x} + {y} + {z} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на вычитание ТРЕХ чисел
    def dif_3_args(self):
        while True:
            x, y, z = self.get_nums()
            if x - y + z <= self.limit and x - y > 0:
                result = f'{x} - {y} + {z} ='
                return result
            elif x + y <= self.limit and x + y - z > 0:
                result = f'{x} + {y} - {z} ='
                return result
            else:
                continue

    # метод возвращает пример, сгенерированный методом,
    # который случайным образом выбран из списка _lst
    def get_example(self):
        _dct_example = {
            1: self.sum_2_args(),
            2: self.dif_2_args(),
            3: self.sum_3_args(),
            4: self.dif_3_args()
        }

        _lst = [random.randint(1, 4) for _ in range(10)]

        return _dct_example[random.choice(_lst)]


if __name__ == '__main__':
    obj = Example(20)     # 20 - число-ограничение

    for _ in range(5):    # печатаем 5 примеров
        print(obj.get_example())
