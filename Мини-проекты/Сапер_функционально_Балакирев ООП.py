import random

N, M = (5, 10)   # размер игрового поля NxN и число мин M


def getTotalMines(PM, i, j):
    """вспомогательная функция для подсчета количества мин
    """
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            x = i + k
            y = j + l
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM[x * N + y] < 0:
                n += 1
    return n


def createGame(PM):
    """Создание игрового поля: расположение мин
        и подсчет числа мин вокруг клеток без мин
    """
    rng = random.Random()
    n = M
    while n > 0:
        i = rng.randrange(N)  # случайное целое [0; N)
        j = rng.randrange(N)
        if PM[i * N + j] != 0:
            continue
        PM[i * N + j] = -1    # расставляем мины (-1 = мина)
        n -= 1

    # вычисляем количество мин вокруг клетки
    for i in range(N):
        for j in range(N):
            if PM[i * N + j] >= 0:
                PM[i * N + j] = getTotalMines(PM, i, j)


def show(pole):
    """Функция отображения состояния текущего
        игрового поля
    """
    for i in range(N):
        for j in range(N):
            print(str(pole[i * N + j]).rjust(3), end="")
        print()


def goPlayer():
    """Функция для ввода пользователем координат
        закрытой клетки игрового поля
    """
    flLoopInput = True
    while flLoopInput:
        x, y = input("Введите координату через пробел: ").split()
        if not x.isdigit() or not y.isdigit():
            print("Координаты введены неверно")
            continue

        x = int(x)-1
        y = int(y)-1

        if x < 0 or x >= N or y < 0 or y >= N:
            print("Координаты выходят за пределы поля")
            continue

        flLoopInput = False

    return (x, y)


def isFinish(PM, P):
    """Определение текущего состояния игры:
        -2 = выиграли, -1 = проиграли, 1 = игра продолжается
    """
    for i in range(N*N):
        if P[i] != '*' and PM[i] < 0:
            return -1

    for i in range(N * N):
        if P[i] == '*' and PM[i] >= 0:
            return 1
    return -2


def startGame():
    """Функция запуска игры: отображается игровое поле,
        игрок открывает любую закрытую клетку,
        результат проверяется на наличие мины или
        выигрышной ситуации
    """
    P = ['*']*N*N  # игровое поле (все клетки закрыты *)
    PM = [0]*N*N   # поле с минами и числом мин в пустых клетках вокруг мины

    createGame(PM)

    finishState = isFinish(PM, P)
    while finishState > 0:
        show(P)
        x, y = goPlayer()

        P[x*N+y] = PM[x*N+y]
        finishState = isFinish(PM, P)

    if finishState == -1:
        print("\nВы проиграли\nПосмотрите игровое поле")
        show(PM)
    else:
        print("\nВы выиграли! Поздравляем!")


startGame()
