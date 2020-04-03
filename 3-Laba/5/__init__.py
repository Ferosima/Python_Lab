# 1. У квадратній матриці відняти останній рядок з усіх рядків. Матрицю заповнити випадковими числами.
from __future__ import print_function
import random
global LineList
LineList = []
n = int(input())
for i in range(n):
    ColumsList = []
    for j in range(n):
        ColumsList.append(random.randrange(-10, 10, 1))
    LineList.append(ColumsList)


def min(LineList=LineList):
    x = len(LineList)-1
    for i in range(n):
        for j in range(n):
            LineList[i][j] -= LineList[x][j]

def out(LineList=LineList):
    for i in  range(n):
        for j in range(n):
            print(LineList[i][j],end='|')
        print("")
out(LineList)
min(LineList)
print("result")
out(LineList)
# a.append(random.randrange(n,k,1))
