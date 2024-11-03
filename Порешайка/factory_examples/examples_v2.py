# Модуль генерирует задания на:
# - сложение/вычитание 2 и/или 3 чисел без скобок и со скобками,
# - умножение/деление 2-х чисел,
# - сложение/вычитание с умножением/делением без скобок и со скобками

import random


class Example:
    """родительский класс для дочерних классов, генерирующих задания"""

    def __init__(self, limit) -> None:
        """limit: число-ограничение (в пределах этого числа будут числа в примерах)
        Например, limit=20 -> числа в примерах будут НЕ более 20.
        Результаты вычисления примеров - в пределах 100.
        """
        self.limit = limit  # число-ограничение

    # метод возвращает три рандомных числа в пределах ограничения limit
    def get_nums(self):
        x = random.randint(1, self.limit)
        y = random.randint(1, self.limit)
        z = random.randint(1, self.limit)
        return x, y, z


class Addsub(Example):
    """дочерний класс для генерации заданий на сложение/вычитание двух/трех чисел без/с скобок/скобками"""

    def __init__(self, limit) -> None:
        super().__init__(limit)

    # метод возвращает задание на сложение ДВУХ чисел с результатом в пределах 100
    def add_2args_wb(self):
        while True:
            x, y, z = self.get_nums()
            if x + y > 100:
                continue
            return f"{x} + {y} ="

    # метод возвращает задание на вычитание ДВУХ чисел с результатом больше нуля
    def sub_2args_wb(self):
        while True:
            x, y, z = self.get_nums()
            if x - y < 0:
                continue
            return f"{x} - {y} ="

    # метод возвращает задание на сложение ТРЕХ чисел с результатом в пределах 100
    def add_3args_wb(self):
        while True:
            x, y, z = self.get_nums()
            if x + y + z > 100:
                continue
            return f"{x} + {y} + {z} ="

    # метод возвращает задание на вычитание ТРЕХ чисел с результатом больше нуля
    def sub_3args_wb(self):
        while True:
            x, y, z = self.get_nums()
            if x - y - z < 0:
                continue
            return f"{x} - {y} - {z} ="

    # метод возвращает задание на сложение/вычитание ТРЕХ чисел без использования скобок
    def addsub_3args_wb(self):
        while True:
            x, y, z = self.get_nums()
            if x - y >= 0 and x - y + z <= 100:
                return f"{x} - {y} + {z} ="
            elif x + y > 100 or x + y - z < 0:
                continue
            return f"{x} + {y} - {z} ="

    # метод возвращает задание на сложение/вычитание ТРЕХ чисел с использованием скобок
    def addsub_3args(self):
        while True:
            x, y, z = self.get_nums()
            if 0 <= x - (y + z) <= 100:
                return f"{x} - ({y} + {z}) ="
            if y - z > 0 and x - (y - z) > 0:
                return f"{x} - ({y} - {z}) ="
            elif y - z < 0 or x + (y - z) > 100:
                continue
            return f"{x} + ({y} - {z}) ="


class Muldiv:
    """класс заданий на умножение/деление в пределах 100"""

    # метод возвращает задание на умножение в пределах таблицы умножения (в пределах 100)
    def mul_2args_wb(self):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return f"{x} · {y} ="

    # метод возвращает задание на деление в пределах 100
    def div_2args_wb(self):
        while True:
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            if x % y != 0:
                continue
            return f"{x} ∶ {y} ="


class Mix(Example):
    """дочерний класс для генерации заданий на умножение/деление со сложением/вычитанием без/с скобок/скобками"""

    def __init__(self, limit) -> None:
        super().__init__(limit)

    # метод возвращает миксовое задание на умножение со сложением/вычитанием без использования скобок
    def mul_mix_wb(self):
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a * y + z <= 100:
                return f"{a} · {y} + {z} ="
            elif y - z * a < 0:
                continue
            return f"{y} - {z} · {a} ="

    # метод возвращает миксовое задание на деление со сложением/вычитанием без использования скобок
    def div_mix_wb(self):
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if y % a != 0:
                continue
            if x + int(y / a) <= 100:
                return f"{x} + {y} ∶ {a} ="
            elif x - int(y / a) < 0:
                continue
            return f"{x} - {y} ∶ {a} ="

    # метод возвращает миксовое задание на умножение со сложением/вычитанием с использованием скобок
    def mul_mix(self):
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a * (y + z) <= 100:
                return f"{a} · ({y} + {z}) ="
            elif y - z < 0 or (y - z) * a > 100:
                continue
            return f"({y} - {z}) · {a} ="

    # метод возвращает миксовое задание на деление со сложением/вычитанием с использованием скобок
    def div_mix(self):
        while True:
            a = random.randint(1, 10)
            x, y, z = self.get_nums()
            if a % (y + z) == 0:
                return f"{a} ∶ ({y} + {z}) ="
            elif y - z < 0 or (y - z) % a != 0:
                continue
            return f"({y} - {z}) ∶ {a} ="
