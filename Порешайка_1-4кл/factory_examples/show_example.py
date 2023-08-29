# Модуль возвращает одно задание из перечня методов модуля examples.py,
# которое затем будет показано в окне приложения Порешайка

import random
from factory_examples.examples import Addsub, Muldiv, Mix


class Show_test():
    def __init__(self, limit) -> None:
        self.limit = limit

    # метод возвращает задание, сгенерированное одним из методов, который выбирается
    # из словаря по ключу случайным образом выбранным из списка _lst
    def get_example(self, f_1=0, f_2=0, f_3=0, f_4=0, f_5=0, f_6=0):
        obj_1 = Addsub(self.limit)   # число-ограничение
        obj_2 = Muldiv()             # в заданиях на умножение/деление 2-х чисел ограничение = 100
        obj_3 = Mix(self.limit)      # число-ограничение

        _dct_example = {
            1: obj_1.add_2args_wb(),
            2: obj_1.sub_2args_wb(),
            3: obj_1.add_3args_wb(),
            4: obj_1.sub_3args_wb(),
            5: obj_1.addsub_3args_wb(),
            6: obj_1.addsub_3args(),
            7: obj_2.mul_2args_wb(),
            8: obj_2.div_2args_wb(),
            9: obj_3.mul_mix_wb(),
            10: obj_3.div_mix_wb(),
            11: obj_3.mul_mix(),
            12: obj_3.div_mix()
        }

        mask = f_1, f_2, f_3, f_4, f_5, f_6

        # только сложение/вычитание с 2-мя числами
        if mask == (1, 0, 0, 0, 0, 0):
            _lst = [random.randint(1, 2) for _ in range(10)]

        # только сложение/вычитание с 3-мя числами без скобок
        if mask == (0, 1, 0, 0, 0, 0):
            _lst = [random.randint(3, 5) for _ in range(20)]

        # сложение/вычитание с 2-мя + 3-мя числами без скобок
        if mask == (1, 1, 0, 0, 0, 0):
            _lst = [random.randint(1, 5) for _ in range(30)]

        # только сложение/вычитание с 3-мя числами со скобками
        if mask == (0, 0, 1, 0, 0, 0):
            return _dct_example[6]

        # сложение/вычитание с 2-мя числами + 3-мя числами со скобками
        if mask == (1, 0, 1, 0, 0, 0):
            _lst = [random.choice([1, 2, 6]) for _ in range(20)]

        # сложение/вычитание с 3-мя числами без скобок + со скобками
        if mask == (0, 1, 1, 0, 0, 0):
            _lst = [random.randint(3, 6) for _ in range(25)]

        # сложение/вычитание с 2-мя числами +
        # 3-мя числами без скобок + со скобками
        if mask == (1, 1, 1, 0, 0, 0):
            _lst = [random.randint(1, 6) for _ in range(30)]

        # только умножение/деление 2-х чисел
        if mask == (0, 0, 0, 1, 0, 0):
            _lst = [random.randint(7, 8) for _ in range(20)]

        # сложение/вычитание с 2-мя числами +
        # умножение/деление 2-х чисел
        if mask == (1, 0, 0, 1, 0, 0):
            _lst = [random.choice([1, 2, 7, 8]) for _ in range(25)]

        # сложение/вычитание с 3-мя числами без скобок +
        # умножение/деление 2-х чисел
        if mask == (0, 1, 0, 1, 0, 0):
            _lst = [random.choice([3, 4, 5, 7, 8]) for _ in range(30)]

        # сложение/вычитание с 2-мя числами + 3-мя числами без скобок +
        # умножение/деление 2-х чисел
        if mask == (1, 1, 0, 1, 0, 0):
            _lst = [random.choice([1, 2, 3, 4, 5, 7, 8]) for _ in range(40)]

        # сложение/вычитание с 3-мя числами со скобками +
        # умножение/деление 2-х чисел
        if mask == (0, 0, 1, 1, 0, 0):
            _lst = [random.randint(6, 8) for _ in range(30)]

        # сложение/вычитание с 2-мя числами +
        # сложение/вычитание с 3-мя числами со скобками + умножение/деление 2-х чисел
        if mask == (1, 0, 1, 1, 0, 0):
            _lst = [random.choice([1, 2, 6, 7, 8]) for _ in range(40)]

        # сложение/вычитание с 3-мя числами без скобок +
        # со скобками + умножение/деление 2-х чисел
        if mask == (0, 1, 1, 1, 0, 0):
            _lst = [random.randint(3, 8) for _ in range(50)]

        # сложение/вычитание с 2-мя + 3-мя числами без скобок +
        # со скобками + умножение/деление 2-х чисел
        if mask == (1, 1, 1, 1, 0, 0):
            _lst = [random.randint(1, 8) for _ in range(50)]

        # только сложение/вычитание с умножением/делением без скобок
        if mask == (0, 0, 0, 0, 1, 0):
            _lst = [random.randint(9, 10) for _ in range(40)]

        # сложение/вычитание с 2-мя числами +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (1, 0, 0, 0, 1, 0):
            _lst = [random.choice([1, 2, 9, 10]) for _ in range(40)]

        # сложение/вычитание с 3-мя числами без скобок +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (0, 1, 0, 0, 1, 0):
            _lst = [random.choice([3, 4, 5, 9, 10]) for _ in range(50)]

        # сложение/вычитание с 3-мя числами со скобками +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (0, 0, 1, 0, 1, 0):
            _lst = [random.choice([6, 9, 10]) for _ in range(30)]

        # умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (0, 0, 0, 1, 1, 0):
            _lst = [random.randint(7, 10) for _ in range(40)]

        # сложение/вычитание с 2-мя числами + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (1, 0, 0, 1, 1, 0):
            _lst = [random.choice([1, 2, 7, 8, 9, 10]) for _ in range(60)]

        # сложение/вычитание с 3-мя числами без скобок + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (0, 1, 0, 1, 1, 0):
            _lst = [random.choice([3, 4, 5, 7, 8, 9, 10]) for _ in range(70)]

        # сложение/вычитание с 3-мя числами со скобками + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (0, 0, 1, 1, 1, 0):
            _lst = [random.randint(6, 10) for _ in range(50)]

        # сложение/вычитание с 2-мя числами + сложение/вычитание с 3-мя числами со скобками +
        # умножение/деление 2-х чисел + сложение/вычитание с умножением/делением без скобок
        if mask == (1, 0, 1, 1, 1, 0):
            _lst = [random.choice([1, 2, 6, 7, 8, 9, 10]) for _ in range(70)]

        # сложение/вычитание с 3-мя числами без скобок + со скобками +
        # умножение/деление 2-х чисел + сложение/вычитание с умножением/делением без скобок
        if mask == (0, 1, 1, 1, 1, 0):
            _lst = [random.randint(3, 10) for _ in range(80)]

        # сложение/вычитание с 2-мя числами + сложение/вычитание с 3-мя числами без скобок +
        # сложение/вычитание с 3-мя числами со скобками + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок
        if mask == (1, 1, 1, 1, 1, 0):
            _lst = [random.randint(1, 10) for _ in range(100)]

        # только сложение/вычитание с умножением/делением со скобками
        if mask == (0, 0, 0, 0, 0, 1):
            _lst = [random.randint(11, 12) for _ in range(40)]

        # сложение/вычитание с 2-мя числами +
        # сложение/вычитание с умножением/делением со скобками
        if mask == (1, 0, 0, 0, 0, 1):
            _lst = [random.choice([1, 2, 11, 12]) for _ in range(40)]

        # сложение/вычитание с 3-мя числами без скобок +
        # сложение/вычитание с умножением/делением со скобками
        if mask == (0, 1, 0, 0, 0, 1):
            _lst = [random.choice([3, 4, 5, 11, 12]) for _ in range(50)]

        # сложение/вычитание с 3-мя числами со скобками +
        # сложение/вычитание с умножением/делением со скобками
        if mask == (0, 0, 1, 0, 0, 1):
            _lst = [random.choice([6, 11, 12]) for _ in range(40)]

        # умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением со скобками
        if mask == (0, 0, 0, 1, 0, 1):
            _lst = [random.choice([7, 8, 11, 12]) for _ in range(40)]

        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 0, 0, 0, 1, 1):
            _lst = [random.randint(9, 12) for _ in range(40)]

        # сложение/вычитание с 2-мя числами +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (1, 0, 0, 0, 1, 1):
            _lst = [random.choice([1, 2, 9, 10, 11, 12]) for _ in range(60)]

        # сложение/вычитание с 3-мя числами без скобок +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 1, 0, 0, 1, 1):
            _lst = [random.choice([3, 4, 5, 9, 10, 11, 12]) for _ in range(70)]

        # сложение/вычитание с 3-мя числами без скобок +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 0, 1, 0, 1, 1):
            _lst = [random.choice([6, 9, 10, 11, 12]) for _ in range(50)]

        # умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 0, 0, 1, 1, 1):
            _lst = [random.randint(7, 12) for _ in range(60)]

        # сложение/вычитание с 3-мя числами без скобок + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 1, 0, 1, 1, 1):
            _lst = [random.choice([3, 4, 5, 7, 8, 9, 10, 11, 12]) for _ in range(90)]

        # сложение/вычитание с 3-мя числами без скобок + умножение/деление 2-х чисел +
        # сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 0, 1, 1, 1, 1):
            _lst = [random.randint(6, 12) for _ in range(70)]

        # сложение/вычитание с 2-мя числами + сложение/вычитание с 3-мя числами без скобок +
        # умножение/деление 2-х чисел + сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (1, 0, 1, 1, 1, 1):
            _lst = [random.choice([1, 2, 6, 7, 8, 9, 10, 11, 12]) for _ in range(90)]

        # сложение/вычитание с 3-мя числами без скобок + сложение/вычитание с 3-мя числами без скобок +
        # умножение/деление 2-х чисел + сложение/вычитание с умножением/делением без скобок + со скобками
        if mask == (0, 1, 1, 1, 1, 1):
            _lst = [random.randint(3, 12) for _ in range(100)]

        # все действия
        if mask == (1, 1, 1, 1, 1, 1):
            _lst = [random.randint(1, 12) for _ in range(120)]

        return _dct_example[random.choice(_lst)]


if __name__ == '__main__':
    ex = Show_test(25)     # 25 - число-ограничение

    for _ in range(10):    # печатаем 10 примеров
        print(ex.get_example(0, 0, 0, 0, 0, 1))
