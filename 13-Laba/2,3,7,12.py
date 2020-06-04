#2. Даний об'єкт A1 типу Node - корінь дерева. Цей об'єкт пов'язаний властивостями Left і Right з іншими об'єктами того ж типу
# (дочірніми вершинами), вони, в свою чергу, - зі своїми дочірніми вершинами, і так далі до об'єктів, властивості Left і Right
# яких рівні null (у деяких вершин може дорівнювати null одна з властивостей - Left або Right).
# Вивести кількість вершин дерева.

#3. Даний корінь A1 непорожнього дерева і число K. Вивести кількість вершин дерева, значення яких дорівнює K.

#7. Даний корінь A1 непорожнього дерева. Вивести максимальне з значень його вершин і
# кількість вершин, що мають це максимальне значення.

#12. Даниц корінь A1 непорожнього дерева. Створити копію даного дерева і вивести посилання A2 на корінь створеної копії
from tkinter import *

root = Tk()
w, h = 800, 800
canv = Canvas(root, width=w, height=h, bg='white')
list_symbol_one = ['*', '/']
list_symbol_two = ['+', '-', ]
list_all_symbol = ['+', '-', '*', '/', ]
global max
max=0
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

    def number_of_node(self):
        if isinstance(self.right, TreeNode):
          a=self.right.number_of_node()+1
        else:
            a= 1
        if isinstance(self.left, TreeNode):
            b= self.left.number_of_node()+1
        else:
            b= 1
        return a+b


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

m=0
def max(self:TreeNode):
    global m
    if isinstance(self.right, TreeNode):
        max(self.right)
    else:
        if m < int(self.right):
            m = int(self.right)
    if isinstance(self.left, TreeNode):
        max(self.left)
    else:
        if m< int(self.left):
            m = int(self.left)

number_m=0
def number_max(self:TreeNode):
    global number_m
    if isinstance(self.right, TreeNode):
        number_max(self.right)
    else:
        if m == int(self.right):
            number_m+=1
    if isinstance(self.left, TreeNode):
        number_max(self.left)
    else:
        if m== int(self.left):
            number_m+=1

num_k=0
def number_k(self: TreeNode,k):
        global num_k
        if isinstance(self.right, TreeNode):
            number_k(self.right,k)
        else:
            if k == int(self.right):
                num_k += 1
        if isinstance(self.left, TreeNode):
            number_k(self.left,k)
        else:
            if k == int(self.left):
                num_k += 1
#12
def copy_Tree(tree:TreeNode):
 tree_two=TreeNode()
 tree_two.data=tree.data
 if isinstance(tree.right,TreeNode):
     tree_two.right=copy_Tree(tree.right)
 else:
     tree_two.right=tree.right
 if isinstance(tree.left,TreeNode):
     tree_two.left=copy_Tree(tree.left)
 else:
     tree_two.left=tree.left
 return tree_two

#a = "(1+-1)*(1*1)"
a=input("Вводите, пожайлуста, без лишних скобокб и не забывайте их закрывать,\nотрицательные числа берите в скобки(так должно работать лучше)\n")
#a="1+2*(3-4)"
c = str_to_TreeNode(a, 400, 300)
if isinstance(c, TreeNode):
    print("2.Количество узлов: ",c.number_of_node()+1)
    k=int(input("3.Введите k:"))
    number_k(c,k)
    print("3.Количество k элементов: ",num_k)
    max(c)
    number_max(c)
    print("7.Максимальный элемент дерева: ",m)
    print("7.Кількість максимальних елементів: ",number_m)
    #12
    c_2=copy_Tree(c)
    print("Відповідь: ",c.call())
    print("я там даже дерево построил), откройте tk")
else:
    print(c)

canv.pack()
root.mainloop()
