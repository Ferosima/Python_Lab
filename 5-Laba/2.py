# 7. Описати рекурсивную функцію GCD (A, B) цілого типу, яка знаходить найбільший спільний дільник (НСД, greatest common divisor)
# двох цілих позитивних чисел A і B, використовуючи алгоритм Евкліда:
# НСД (A, B) = НСД (B, A mod B), B ≠ 0; НСД (A, 0) = A,
# де «mod» позначає операцію взяття залишку від ділення. За допомогою цієї функції знайти НСД (A, B), НСД (A, C), НСД (A, D),
# якщо дано числа A, B, C, D.\
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
print(GCD(1071, 462))