#5. Іграшковий лабіринт є прозорою пласкою прямокутною коробкою, всередині якої є перешкоди і переміщається кулька. Лабіринт можна нахиляти вліво, вправо, до себе або від себе, після кожного нахилу кулька переміщається в заданому напрямку до найближчої перешкоди або до стінки лабіринту, після чого зупиняється. Метою гри є загнати кульку в один зі спеціальних отворів - виходів. Шарик провалюється в отвір, якщо він зустрічається на його шляху (кулька не зобов'язана зупинятися в отворі).
# Спочатку кулька знаходиться в лівому верхньому кутку лабіринту. Гарантується, що рішення існує і лівий верхній кут не зайнятий перешкодою або отвором.
#
# Вхідні дані
#
# У першому рядку вхідного файлу записано числа N і M - розміри лабіринту (цілі позитивні числа, що не перевищують 100). Потім йде N рядків по M чисел в кожному - опис лабіринту. Число 0 в описі означає вільне місце, число 1 - перешкода, число 2 - отвір.
#
# Вихідні дані
#
# Виведіть єдине число - мінімальну кількість нахилів, які необхідно зробити, щоб кулька покинула лабіринт через один з отворів.

def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        weight += 1
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == (weight - 1):
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight

                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight
                        return True
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            y -= 1
            result[weight] = 'down'
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'up'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'right'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'left'
            x += 1

    return result[1:]


def main():
    # Выход из лабиринта .Волновой алгоритм
    labirint = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    # Координаты входа [2,0], координаты выхода [7,0]. В которой 1 - это стена, 0 - это путь.
    # координаты входа
    pozIn = (2, 0)
    pozOut = (7, 0)

    path = [[x if x == 0 else -1 for x in y] for y in labirint]
    path[pozIn[0]][pozIn[1]] = 1;

    if not found(path, pozOut):
        print("Путь не найден!")
        return

    result = printPath(path, pozOut)

    for i in path:
        for line in i:
            print("{:^3}".format(line), end=",")
        print("")
    print(result)


if __name__ == '__main__':
    main()
