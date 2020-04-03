#16. Створити гру «камінь-ножиці-папір» між двома умовними гравцями.
print("1 - Rock / Камень\n2 - Scissors / Ножницы\n3 - Paper / Бумага")
x=int(input())
y=int(input())

"""
1 - Rock / Камень
2 - Scissors / Ножницы
3 - Paper / Бумага
"""

#lose
if x == 1 and y == 2:
    print("Scissors vs Rock! You lose!")
elif x == 2 and y == 3:
    print("Paper vs Scissors! You lose!")
elif x == 3 and y == 1:
    print("Rock vs Paper! You lose!")

#won
elif x == 2 and y == 1:
    print("Rock vs Scissors! You won!")
elif x == 3 and y == 2:
    print("Scissors vs Paper! You won!")
elif x == 1 and y == 3:
    print("Paper vs Rock! You won!")

#draw
elif x == 1 and y == 1:
    print("Rock vs Rock! Draw!")
elif x == 2 and y == 2:
    print("Scissors vs Scissors! Draw!")
elif x == 3 and y == 3:
    print("Paper vs Paper! Draw!")