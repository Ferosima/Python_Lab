#17. Дано два цілих числа I, J і файл дійсних чисел, що містить елементи квадратної матриці (по рядках).
# Вивести елемент матриці, розташований в I-му рядку і J-м стовпці (рядки і стовпці нумеруються від 1).
# Якщо необхідний елемент відсутній, то вивести 0.
f=open('matrix.txt','r')
lines=f.read().split('\n')
matrix=[]
for line in lines:
    print(line)
    matrix.append(line.split('|'))
i = int(input('Input i (0 :{0})\n'.format(len(matrix)-1)))
j = int(input('Input j (0 :{0})\n'.format(len(matrix[0])-1)))
try:
    print(matrix[i][j])
except IndexError:
    print("You are out of range")