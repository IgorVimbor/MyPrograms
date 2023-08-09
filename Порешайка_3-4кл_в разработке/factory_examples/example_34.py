# Модуль генерирует задания:
# - на сложение/вычитание 3 чисел в пределах числа-ограничения с использованием скобок,
# - на умножение/деление 2 чисел в пределах 100,
# - комбинированные варианты сложения/вычитания и умножения/деления с использованием скобок.

import random

class Example_34:
    def __init__(self, limit) -> None:
        """limit: число-ограничение (в пределах этого числа будут числа в примерах и результат действий)
        Например, limit=20 -> числа в примерах и результат выполнения действий будет НЕ более 20.
        """
        self.limit = limit     # число-ограничение

    # метод возвращает три рандомных числа в пределах ограничения limit
    def get_nums(self):
        x = random.randint(1, self.limit)
        y = random.randint(1, self.limit)
        z = random.randint(1, self.limit)
        return x, y, z

    # метод возвращает задание на сложение/вычитание ТРЕХ чисел с использованием скобок
    def add_sub_3_args_34(self):
        while True:
            x, y, z = self.get_nums()
            if y + z <= self.limit and x - (y + z) >= 0:
                result = f'{x} - ({y} + {z}) ='
                return result
            elif y - z >= 0 and x + (y - z) <= self.limit:
                result = f'{x} + ({y} - {z}) ='
                return result
            else:
                continue

    # метод возвращает задание на умножение в пределах таблицы умножения (в пределах 100)
    def mul_2_args_34(self):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return f'{x} * {y} ='

    # метод возвращает задание на умножение в пределах таблицы умножения (в пределах 100)
    def div_2_args_34(self):
        while True:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            if x / y > 0 and x % y == 0:
                result = f'{x} : {y} ='
                return result
            else:
                continue

    # метод возвращает миксовое задание на деление со сложением/вычитанием
    def div_mixt_34(self):
        while True:
            x, y, z = self.get_nums()
            if y + z <= self.limit and x % (y + z) == 0:
                result = f'{x} : ({y} + {z}) ='
                return result
            elif x - y > 0 and (x - y) % z == 0:
                result = f'({x} - {y}) : {z} ='
                return result
            else:
                continue

    # метод возвращает миксовое задание на умножение со сложением/вычитанием
    def mul_mixt_34(self):
        while True:
            x, y, z = self.get_nums()
            if y + z <= self.limit and x * (y + z) <= 100:
                result = f'{x} * ({y} + {z}) ='
                return result
            elif x - y > 0 and (x - y) * z <= 100:
                result = f'({x} - {y}) * {z} ='
                return result
            else:
                continue

    # метод возвращает пример, сгенерированный методом, который выбирается
    # из словаря по ключу случайным образом выбранным из списка _lst
    def get_example(self, flag_add_sub=0, flag_mul_div=0, flag_all=0):
        _dct_example = {
            1: self.add_sub_3_args_34(),
            2: self.mul_2_args_34(),
            3: self.div_2_args_34(),
            4: self.mul_mixt_34(),
            5: self.div_mixt_34()
        }

        mask = flag_add_sub, flag_mul_div, flag_all
        # если нужны примеры только сложение/вычитание ТРЕХ чисел с использованием скобок
        if mask == (1, 0, 0):
            return _dct_example[1]
        # если нужны примеры только на умножение/деление
        if mask == (0, 1, 0):
            _lst_mul_div = [random.randint(2, 3) for _ in range(20)]
            return _dct_example[random.choice(_lst_mul_div)]
        # если нужны примеры на сложение/вычитание и умножение/деление
        if mask == (1, 1, 0):
            _lst_add_div = [random.randint(1, 3) for _ in range(30)]
            return _dct_example[random.choice(_lst_add_div)]
        # если нужны все виды примеров
        if mask in [(1, 1, 1), (1, 0, 1), (0, 1, 1), (0, 0, 1)]:
            _lst_all = [random.randint(1, 5) for _ in range(50)]
            return _dct_example[random.choice(_lst_all)]


if __name__ == '__main__':
    obj = Example_34(30)     # 20 - число-ограничение

    for _ in range(10):    # печатаем 5 примеров
        print(obj.get_example(1, 1, 1))
