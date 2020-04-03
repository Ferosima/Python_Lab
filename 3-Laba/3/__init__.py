#11
j=int(input())
n=0
for i in range(j):
    if (j%(i+1))!=0:
        continue
    n+=1
if n==2:
    print("Просте")
print(n)

