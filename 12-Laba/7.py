# 7. Змій Горинич опинився в лабіринті і хоче вибратися з нього якомога швидше.
# На жаль, після вчорашнього вживання кефіру, ліва голова Змія розуміє погано. Тому Змій Горинич може повертати праворуч і йти прямо, але не може повертати ліворуч і розвертатися на місці. Допоможіть Змію Гориничу визначити довжину найкоротшого шляху до виходу з лабіринту.
#
# Вхідні дані
#
# У першому рядку через пропуск записані числа r і c (4 ≤ r, c ≤ 20) - кількість рядків і стовпців в карті лабіринту.
# У кожному з наступних r рядків записано по c символів, які задають цю карту. Символ S позначає положення Змія Горинича,
# символ F - точку виходу з лабіринту, символ X - стінку. Пробілами позначені прохідні клітини. Гарантується,
# що лабіринт оточений стінами. Перед початком руху Змій Горинич може зорієнтуватися за допомогою одного з 4 напрямків
# (вгору, вниз, ліворуч або праворуч).
#
# Вихідні дані
#
# Виведіть єдине число - відстань , яку доведеться пройти Змію Гориничу. Гарантується, що він завжди зможе вийти з лабіринту.
BOTTOM, TOP, LEFT, RIGHT = (4, -1, -1, 17)
START_X, START_Y = (0, 0)

matrix = []

mazeMap = open('map.txt')
row_index = 0

# Парсим файл с картой и делаем из него матрицу
for row in mazeMap:
  column_index = 0
  matrix.append([])
  for column in row:
    if (column == 'S'):
        start_x = row_index;
        start_y = column_index
        matrix[row_index].append({ 'isVisited': True, 'canVisit': False, 'destination': False })
    elif (column == 'F'):
        matrix[row_index].append({ 'canVisit': True, 'isVisited': False, 'destination': True })
    elif (column == ' '):
      matrix[row_index].append({ 'canVisit': True, 'isVisited': False, 'destination': False })
    else:
      matrix[row_index].append({ 'canVisit': False, 'isVisited': False, 'destination': False })
    column_index += 1
  row_index += 1

def move(coordX = START_X, coordY = START_Y, pathLength = 1):
  nextX = coordX + 1
  nextY = coordY + 1

  if nextX < RIGHT and nextX > LEFT and matrix[coordY][nextX]['canVisit']:
    if matrix[coordY][nextX]['destination']:
      return pathLength
    else:
      shortesPath = move(nextX, coordY, pathLength + 1)
      if (shortesPath != False):
        return shortesPath

  if nextY > TOP and nextY < BOTTOM and matrix[nextY][nextX]['canVisit']:
    if matrix[nextY][coordX]['destination']:
      return pathLength
    else:
      shortesPath = move(coordX, nextY, pathLength + 1)
      if (shortesPath != False):
        return shortesPath

  else:
    return False

print(move())
