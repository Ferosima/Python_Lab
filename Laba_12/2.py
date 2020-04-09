#2. На шахівниці NxN в клітинці (x1, y1) стоїть голодний шаховий кінь. Він хоче потрапити в клітинку (x2, y2),
# де росте смачна шахова трава. Яку найменшу кількість ходів він повинен для цього зробити?
# Вхідні дані

# На вхід програми поступає п'ять чисел: N, x1, y1, x2, y2 (5 ≤ N ≤ 20, 1 ≤ x1, y1, x2, y2 ≤ N).
# Ліва верхня клітинка дошки має координати (1, 1), права нижня - (N, N).
# Вихідні дані

# У першому рядку виведіть єдине число K - найменшу необхідну кількість ходів коня. У кожному з наступних K + 1
# рядків має бути записано 2 числа - координати чергової клітинки в шляху коня.
# пришлось почитать про алгоритм трассировки (Алгоритм Ли)
n = int(input('Введіть розмір дошки\n'))
wave_one = 1
wave_two = 2
x1 = int(input('Введіть координату х початкової точки\n'))
y1 = int(input('Введіть координату y початкової точки\n'))
x2 = int(input('Введіть координату х кінцевої точки\n'))
y2 = int(input('Введіть координату х кінцевої точки\n'))
way = []
number_way=0
global number_of_wave
number_of_wave = 0
global matrix
matrix = [[' '] * n for i in range(n)]


def check_matrix(matrix: list):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == ' ':
                return True
    return False


def check_coord(a, b, var):
    if a <= n and b <= n and a >= 0 and b >= 0:
        matrix[b][a] = var
    else:
        print('Ці координати не підходять')


def print_waves(matrix):
    print('   ', end='')
    for i in range(n):
        print(i, '|', end='')
    print('\n')
    print('   ', end='')
    for i in range(n):
        print('=', ' ', end='')
    print('\n')
    for i in range(n):
        for j in range(n + 2):
            if j == 0:
                print(i, end='')
                continue
            if j == 1:
                print('||', end='')
                continue
            if j > 1:
                print(matrix[i][j - 2], "|", end='')
        print('\n')


def wave(x0, y0):
    theEnd = True

    def step(x0, y0, wave_one, wave_two):
        x1 = x0 + wave_one
        y1 = y0 + wave_two
        x2 = x0 + wave_two
        y2 = y0 + wave_one

        def check(a, b):
            def check(a):
                if a <= n - 1 and a >= 0:
                    return True

            if check(a):
                if check(b):
                    # print('x=', a, 'y=', b)
                    if matrix[a][b] != 'end':
                        if matrix[a][b] == ' ':
                            global number_of_wave
                            matrix[a][b] = number_of_wave + 1

                            # wave(a, b, i + 1)
                    else:

                        nonlocal theEnd
                        theEnd = False

        check(x1, y1)
        check(x2, y2)

    step(x0, y0, wave_one, wave_two)
    step(x0, y0, -wave_one, wave_two)
    step(x0, y0, wave_one, -wave_two)
    step(x0, y0, -wave_one, -wave_two)
    return theEnd


#постройка волн
def algorithm_build_waves():
    theEnd = True
    while theEnd:
        for i in range(n):
            for j in range(n):
                global number_of_wave
                if matrix[i][j] == number_of_wave:
                    theEnd = wave(i, j)
                    theEnd = (theEnd == check_matrix(matrix))
                    if theEnd != True:
                        break
            if theEnd != True:
                break
        number_of_wave += 1

def algorithm_li(x0, y0, number):
    def step(x0, y0, wave_one, wave_two):
        x1 = x0 + wave_one
        y1 = y0 + wave_two
        x2 = x0 + wave_two
        y2 = y0 + wave_one

        def check(a, b):
            def check(a):
                if a <= n - 1 and a >= 0:
                    return True

            if check(a):
                if check(b):
                    return True
            return False

        global number_way
        if check(x1, y1):
            if matrix[x1][y1] == 0:
                way.append([x1, y1])
                number_way += 1
                # way.append([x0, y0, number + 1])
                return True
            if matrix[x1][y1] == number:
                if algorithm_li(x1, y1, number - 1):
                    number_way += 1
                    way.append([x1, y1, number])
                    return True
        if check(x2, y2):
            if matrix[x2][y2] == 0:
                number_way += 1
                way.append([x2, y2, number])
                # way.append([x0, y0, number + 1,'ss'])
                return True
            if matrix[x2][y2] == number:
                if algorithm_li(x2, y2, number - 1):
                    number_way += 1
                    way.append([x2, y2, number])
                    return True
        return False

    if step(x0, y0, wave_one, wave_two):
        return True
    if step(x0, y0, -wave_one, wave_two):
        return True
    if step(x0, y0, wave_one, -wave_two):
        return True
    if step(x0, y0, -wave_one, -wave_two):
        return True
    return False


check_coord(x1, y1, 0)
check_coord(x2, y2, 'e')
algorithm_build_waves()
print_waves(matrix)
algorithm_li(x2, y2, number_of_wave - 1)
way.append([x2, y2])
print('Кількість ходів:',number_way)
print('Перші координати-це початок, останні-це кінець')
print(way)

