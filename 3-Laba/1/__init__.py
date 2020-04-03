#2
import random
import math
listDay=["Понеділок","Вівторок","Середа","Четверг","П'ятниця","Субота","Неділя"]
def function(n,k):
    a=random.randrange(n,k,1)
    print("a={0}".format(a))
    b=random.randrange(n,k,1)
    print("b={0}".format(b))
    x=random.randrange(n,k,1)
    print("x={0}".format(x))
    y=int(math.log(x**2+a*b)/7)
    return y
n=int(input())
k=int(input())
print(listDay[function(n,k)])
