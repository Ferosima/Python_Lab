#2. Дано перший член і знаменник геометричної прогресії. Написати рекурсивну функцію знаходження n-го члена прогресії і знаходження суми n перших членів прогресії.
def geometryRecursion(b,q,n):
 if n>0:
     return (b * q*geometryRecursion(1,q,n-1))
 return 1

a=geometryRecursion(2,2,4)
print (a)