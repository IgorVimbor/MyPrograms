from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y    # координаты начала расположения корабля (целые числа)
        self._length = length      # длина корабля (число палуб: целое значение: 1, 2, 3 или 4)
        self._tp = tp              # ориентация корабля (1 - горизонтальная; 2 - вертикальная)
        self._is_move = True       # возможно ли перемещение корабля (изначально равно True)
        self._cells = [1] * self._length   # изначально список длиной length, состоящий из 1

    def set_start_coords(self, x, y):
        # установка начальных координат x, y
        self._x = x
        self._y = y

    def get_start_coords(self):
        # получение начальных координат корабля в виде кортежа x, y
        return self._x, self._y

    def move(self, go):
        # перемещение корабля по его ориентации на go клеток
        # (go = 1 - движение в одну сторону на клетку; go = -1 - в другую сторону на одну клетку)
        # движение возможно только если флаг _is_move = True
        if self._is_move:
            if self._tp == 1:
                self._x += go
            if self._tp == 2:
                self._y += go

    def add_array_ship(self, ship):
        # метод создает список кортежей координат точек вокруг корабля, включая координаты точек корабля
        array_ship = [(x, y) for x in range(ship._x - 1, ship._x + ship._length + 1)
                      for y in range(ship._y - 1, ship._y + 2)] \
            if self._tp == 1 else [(x, y) for x in range(ship._x - 1, ship._x + 2)
                                   for y in range(ship._y - 1, ship._y + ship._length + 1)]
        return array_ship

    def is_collide(self, array_ships):
        # проверка на столкновение с другим кораблем ship
        # (если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали)
        # метод возвращает True, если столкновение есть и False - в противном случае

        x_new, y_new = self.get_start_coords()
        # создаем список кортежей координат точек нового корабля
        array_new_ship = [(x, y_new) for x in range(x_new, x_new + self._length)] \
            if self._tp == 1 else [(x_new, y) for y in range(y_new, y_new + self._length)]
        # список кортежей координат точек пересечения или соприкосновения
        intersection = [point for array in array_ships
                        for point in array_new_ship if point in array]
        # если список intersection пустой, то вредного контакта нет
        return [True, False][len(intersection) == 0]

    def is_out_pole(self, size):
        # проверка на выход корабля за пределы поля (True если вышел и False - в противном случае)
        if self._tp == 1:
            return False if (self._x + self._length) <= size else True
        if self._tp == 2:
            return False if (self._y + self._length) <= size else True

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size   # размер игрового поля (целое положительное число)
        self._ships = []    # список из кораблей (объектов класса Ship); изначально пустой список
        self.array_ships = [[]]  # общий список списков кортежей координат точек всех кораблей
        self.pole = [[0 for _ in range(self._size)] for _ in range(self._size)]  # игровое поле

    def init(self):
        self._lst = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                     Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                     Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                     Ship(1, tp=randint(1, 2))
                     ]

        while len(self._ships) < 10:
            for ship in self._lst:
                ship.set_start_coords(x=randint(0, 9), y=randint(0, 9))
                if ship.is_out_pole(self._size) or ship.is_collide(self.array_ships):
                    continue
                self._ships.append(ship)
                self.array_ships.append(ship.add_array_ship(ship))
                self._lst.remove(ship)

    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        for ship in self._ships:
            x_now, y_now = ship.get_start_coords()
            for i in range(len(ship._cells)):
                if ship._tp == 1:
                    self.pole[x_now+i][y_now] = ship._cells[i]
                if ship._tp == 2:
                    self.pole[x_now][y_now+i] = ship._cells[i]
        self.pole = [[self.pole[i][j] for i in range(self._size)] for j in range(self._size)]
        [print(*row) for row in self.pole]

    def get_pole(self):
        return [row for row in self.pole]


SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
[print(i.__dict__) for i in pole.get_ships()]
print(len(pole.array_ships))
pole.show()