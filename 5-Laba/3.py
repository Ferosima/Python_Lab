# 12. Вивести значення цілочисельного виразу, заданого у вигляді рядка S. Вираз визначається наступним чином:
# <Вираз> :: = <цифра> | <Вираз> + <цифра> | <Вираз> - <цифра>
# получился прикольный калькулятор, который может строить деревья
from tkinter import *

root = Tk()
w, h = 800, 800
canv = Canvas(root, width=w, height=h, bg='white')
list_symbol_one = ['*', '/']
list_symbol_two = ['+', '-', ]
list_all_symbol = ['+', '-', '*', '/', ]


def operation(a, b, c=int):
    b = int(b)
    c = int(c)
    if a == '+':
        return b + c
    elif a == '-':
        return b - c
    elif a == '*':
        return b * c
    elif a == '/':
        return b / c


class TreeNode:
    def __init__(self):
        self.data = ""
        self.left = None
        self.right = None

    # ініціалізуються зв’язки вузла,
    # так як дерево бінарне, то
    # можливі тільки 2 дочірні вузла
    def initNode(self, left, right):
        self.left = left
        self.right = right

    # встановлюються деякі дані вузла
    def set_data(self, data):
        self.data = data

    def leftNode(self, n):
        if isinstance(self.left, TreeNode):
            print(n)
            return self.left.leftNode(n + 1)
        else:
            return self.data

    def Cal(self):
        if isinstance(self.left, TreeNode) and isinstance(self.right, TreeNode):
            print("Call r")
            self.right = self.right.Cal()
            print(self.right, "r")
            print("Call l")
            self.left = self.left.Cal()
            print(self.left, "l")
            return operation(self.data, self.left, self.right)
        elif isinstance(self.left, TreeNode):
            self.left = self.left.Cal()
            return operation(self.data, self.left, self.right)
        elif isinstance(self.right, TreeNode):
            self.right = self.right.Cal()
            print(self.right, "ri")
            return self.right
        elif self.left == None:
            self.left = 0
        elif self.right == None:
            self.right == 0
        else:
            print(operation(self.data, self.left, self.right))
            return operation(self.data, self.left, self.right)

    # return operation(self.data, self.left, self.right)

    def call(self):
        if isinstance(self.left, TreeNode):
            if self.data == "":
                self.data = self.left.data
            self.left = self.left.call()
            # print(self.data, 'data')
            # print(self.left, 'left')  # need stop
        if isinstance(self.right, TreeNode):
            # print(self.right.left)
            if self.data == "":
                self.data = self.right.data
            self.right = self.right.call()
            # print(self.data, 'data')
            # print(self.right, "right")
        if self.left == None:
            # if list_symbol_one.count(self.data)==1:
            #     self.left=1
            # else:
            self.left = 0
        if self.right == None:
            # if list_symbol_one.count(self.data)==1:
            #     self.right=1
            # else:
            self.right = 0
        if self.data == "":
            self.data = "+"
        # print(self.right, 'r.e')
        # print(self.left, 'l.e')
        # print(self.data, 'd.e')
        # print(operation(self.data, self.left,self.right))
        # need stop
        return operation(self.data, self.left,self.right)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def str_to_TreeNode(a, x, y):
    b = TreeNode()
    start = 0
    end = 0
    check = 0
    brackets1 = []
    brackets2 = []
    true = 0
    ####delete ()###########################################################################################################
    for i in range(len(a)):
        if a[i] == '(':
            brackets1.append(i)
        if a[i] == ')':
            brackets2.append(i)
    for n in range(len(brackets1)):
        if n != len(brackets1) - 1:
            if brackets1[n + 1] < brackets2[n]:
                true += 1
        if len(brackets1) == len(brackets2) and len(brackets1) == 1:
            true = 1
    if true == len(brackets1) and a[0] == '(' and a[len(a) - 1] == ')':
        a = a[1:len(a) - 1]
        # print(a)
    #####check is it number?################################################################################################
    if is_number(a):
        canv.create_text(x, y, font=("Purisa", 20), text=a)
        return a
    #####check operation + or -#############################################################################################
    for i in range(len(a)):  # check +-
        if a[i] == '(':
            if check == 0:
                start = i + 1
            check += 1
            continue
        if check == 0:
            if list_symbol_two.count(a[i]) == 1:
                end = i
                b.data = a[i]
                # print(b.data, 'data')
                canv.create_text(x, y, font=("Purisa", 20), text=b.data)
                if i > 0 and a[i - 1] != ')':
                    b.left = a[start:end]
                    # print(b.left, 'left+-')
                    canv.create_line(int(x), int(y), int(x - 25), int(y + 25), fill='black')
                    canv.create_text(x - 25, y + 25, font=("Purisa", 20), text=b.left)
                    # print(b.left,"left")
                    # if i + 1 <= len(a) - 1 and a[i + 1] == '(':
                    #     b.right = srt_to_TreeNode(a[end:len(a) - 1], x + 50, y + 50)
                    # else:
                    if a[i + 1] != '(':
                        n = 0
                        for n in range(i + 1, len(a)):
                            if list_all_symbol.count(a[n]) == 1:
                                n += 1
                        if n > 0:
                            canv.create_line(int(x), int(y), int(x + 25), int(y + 25), fill='black')
                            # print(a[end + 1:len(a)], 'right+-')
                            b.right = str_to_TreeNode(a[end + 1:len(a)], x + 25, y + 25)
                            canv.create_text(x, y, font=("Purisa", 20), text=a[i])
                        # canv.create_text(x + 25, y + 25, font=("Purisa", 20), text=a[end + 1:len(a)])
                        else:
                            b.right = a[end + 1:len(a)]
                            canv.create_line(int(x), int(y), int(x + 25), int(y + 25), fill='black')
                            canv.create_text(x + 25, y + 25, font=("Purisa", 20), text=b.right)
                        return b
                    # print(b.right,"right")
                    else:
                        # print(a[end + 1:len(a)], 'right+-')
                        b.right = str_to_TreeNode(a[end + 1:len(a)], x + 25, y + 25)
                        canv.create_line(int(x), int(y), int(x + 25), int(y + 25), fill='black')
                    return b
        if a[i] == ')':  # новая ветка
            check -= 1
            # print(a[start:end],"check")
            end = i
            if check == 0:
                if i < len(a) - 1 and list_all_symbol.count(a[i + 1]) == 1:
                    # print(a[start:end], "left()")
                    b.left = str_to_TreeNode(a[start:end], x - 50, y + 50)
                    canv.create_line(int(x), int(y), int(x - 50), int(y + 50), fill='black')
                    b.data = a[i + 1]
                    canv.create_text(x, y, font=("Purisa", 20), text=b.data)
                    # print(a[end + 2:len(a)], "right.etc")
                    b.right = str_to_TreeNode(a[end + 2:len(a)], x + 50, y + 50)
                    canv.create_line(int(x), int(y), int(x + 50), int(y + 50), fill='black')
                    return b
            # else:
            # print(a[start:end], "right")
            # b.right = str_to_TreeNode(a[start:end], x, y)
            # print(a[start:end])
            #  print(b.right.right,"rr",b.right)
            # return b
            # if b.right == None and a[i] != ')':
            #     b.right = a[start:len(a)]
            #     canv.create_text(x, y, font=("Purisa", 20), text=b.right)
            #     return b
    #############check operation * or /#####################################################################################
    start = 0
    check = 0
    for n in range(len(a)):
        if a[n] == '(':
            if check == 0:
                start = n + 1
            check += 1
            continue
        if a[n] == ')':  # новая ветка
            check -= 1
            # print(a[start:end], "check",n)
            end = n
        if check == 0:
            if list_symbol_one.count(a[n]) == 1:
                end = n
                # print(a[start:end])
                for i in range(n + 1, len(a)):
                    if a[i] == '(':
                        if check == 0:
                            pass
                            # start = n + 1
                        check += 1
                        # print(check, "check+")
                        # print(start, 'start')
                        continue
                    if a[i] == ')':  # новая ветка
                        check -= 1
                        # end = i
                        # print(a[0:end], "check1", n)
                    if check == 0:
                        if list_symbol_two.count(a[i]) == 1 or list_symbol_one.count(a[i]) == 1:
                            # end=i
                            # print(a[start:i], "lF.w")
                            # print(a[i + 1:len(a)], "rF.w")
                            # print(a[i], 'dF.w')
                            b.left = str_to_TreeNode(a[start:i], x - 50, y + 50)
                            #  canv.create_text(x - 25, y + 25, font=("Purisa", 20), text=a[start:i])
                            canv.create_line(int(x), int(y), int(x - 50), int(y + 50), fill='black')
                            b.right = str_to_TreeNode(a[i + 1:len(a)], x + 50, y + 50)
                            # canv.create_text(x + 25, y + 25, font=("Purisa", 20), text=a[i+1:len(a)])
                            canv.create_line(int(x), int(y), int(x + 50), int(y + 50), fill='black')
                            b.data = a[i]
                            canv.create_text(x, y, font=("Purisa", 20), text=b.data)
                            return b

                # print(a[n + 1:len(a)], "rF")
                # print(a[n], 'dF')
                if a[n - 1] == ')':
                    # print(a[start:n - 1], "lF")
                    b.left = str_to_TreeNode(a[start:n - 1], x - 25, y + 25)
                    # canv.create_text(x - 25, y + 25, font=("Purisa", 20), text=a[start:n-1])
                else:
                    # print(a[start:n], "lF", len(a[start - 1:n]))
                    b.left = str_to_TreeNode(a[start:n], x - 25, y + 25)
                    canv.create_text(x - 25, y + 25, font=("Purisa", 20), text=a[start:n])
                canv.create_line(int(x), int(y), int(x - 25), int(y + 25), fill='black')
                # print(a[start:n], "lF")
                b.right = str_to_TreeNode(a[n + 1:len(a)], x + 25, y + 25)
                # canv.create_text(x + 25, y + 25, font=("Purisa", 20), text=a[n + 1:len(a)])
                canv.create_line(int(x), int(y), int(x + 25), int(y + 25), fill='black')
                # print(a[n + 1:len(a)], "rF")
                b.data = a[n]
                canv.create_text(x, y, font=("Purisa", 20), text=b.data)
                return b
    return b

#a = "(1+-1)*(1*1)"
a=input("Вводите, пожайлуста, без лишних скобокб и не забывайте их закрывать,\nотрицательные числа берите в скобки(так должно работать лучше)\n")
#a="1+2*(3-4)"
c = str_to_TreeNode(a, 400, 300)
if isinstance(c, TreeNode):
    print(c.call())
    print("я там даже дерево построил), откройте tk")
else:
    print(c)
canv.pack()
root.mainloop()
