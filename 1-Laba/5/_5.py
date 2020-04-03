#3
running=True
while running:
 a=int(input("Введіть а\n"))
 b=int(input("Введіть b\n"))
 c=int(input("Введіть c\n"))
 if a==0|b==0|c==0:
     continue
 break
print("сумма={0}".format(a**2+b**2+c**2))
print("різниця={0}".format(a**2-b**2-c**2))
print("добуток={0} ".format(a**2*b**2*c**2))
print("частка={0} ".format(a**2/b**2/c**2))