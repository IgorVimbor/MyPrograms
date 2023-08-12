# Модуль генерирует задания на сложение/вычитание 2 и/или 3 чисел
# без использования скобок в пределах числа-ограничения.

import random

class Example_12:
    def __init__(self, limit) -> None:
        """limit: число-ограничение (в пределах этого числа будут числа в примерах и результат действий)
        Например, limit=20 -> числа в примерах и результат выполнения действий будет НЕ более 20.
        """
        self.limit = limit     # число-ограничение

    # метод возвращает три рандомных числа в пределах ограничения limit
    def get_nums(self):
        x = random.randint(0, self.limit)
        y = random.randint(0, self.limit)
        z = random.randint(0, self.limit)
        return x, y, z

    # метод генерирует и возвращает задание на сложение ДВУХ чисел
    def add_2_args_12(self):
        while True:
            x, y, z = self.get_nums()
            if x + y <= self.limit:
                result = f'{x} + {y} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на вычитание ДВУХ чисел
    def sub_2_args_12(self):
        while True:
            x, y, z = self.get_nums()
            if x - y <= self.limit and x - y > 0:
                result = f'{x} - {y} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на сложение ТРЕХ чисел
    def add_3_args_12(self):
        while True:
            x, y, z = self.get_nums()
            if x + y + z <= self.limit:
                result = f'{x} + {y} + {z} ='
                return result
            else:
                continue

    # метод генерирует и возвращает задание на вычитание ТРЕХ чисел
    def sub_3_args_12(self):
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

    # метод возвращает пример, сгенерированный методом, который выбирается
    # из словаря по ключу случайным образом выбранным из списка _lst
    def get_example(self, flag_2=0, flag_3=0):
        _dct_example = {
            1: self.add_2_args_12(),
            2: self.sub_2_args_12(),
            3: self.add_3_args_12(),
            4: self.sub_3_args_12()
        }
        mask = flag_2, flag_3
        # если нужны примеры только с 2-мя числами
        if mask == (1, 0):
            _lst_2 = [random.randint(1, 2) for _ in range(10)]
            return _dct_example[random.choice(_lst_2)]
        # если нужны примеры только с 3-мя числами
        if mask == (0, 1):
            _lst_3 = [random.randint(3, 4) for _ in range(10)]
            return _dct_example[random.choice(_lst_3)]
        # если нужны примеры с 2-мя и 3-мя числами
        if mask == (1, 1):
            _lst = [random.randint(1, 4) for _ in range(10)]
            return _dct_example[random.choice(_lst)]


if __name__ == '__main__':
    obj = Example_12(20)     # 20 - число-ограничение

    for _ in range(10):    # печатаем 5 примеров
        print(obj.get_example(1, 1))
