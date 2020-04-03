# 3. Описати рекурсивную функцію PowerN (X, N) дійсного типу, яка знаходить значення N-го ступеня числа X за формулами:
# X0 = 1,
# XN = (XN / 2) 2 при парних N> 0, XN = X • XN-1 при непарних N> 0,
# XN = 1 / X-N при N <0
# (X ≠ 0 - дійсне число, N - ціле; у формулі для парних N повинна використовуватися операція цілочисельного ділення).
# За допомогою цієї функції знайти значення XN для даного X при довільних значеннях N.

def power(x,n):
    if n==0:
        return 1
    if n>0:
        if n%2==1:
            return x*power(x,n-1)
        else:
            return power(x,n/2)*power(x,n/2)
    else:
        return 1/power(x,-1*n)
    #return 0

print(power(2,-3))