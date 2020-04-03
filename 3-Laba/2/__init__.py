#6
import random
def function(j,n=0,k=10):
    a=[]
    for i in range(j):
     a.append(random.randrange(n,k,1))
    return a
j=int(input())
list=function(j)
for i in range(10):
    print("{0}={1}".format(i,list.count(i)))