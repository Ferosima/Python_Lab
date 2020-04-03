def function (k=0):
    if k == 2:
     return 0
    b=int(input())
    if k<=1:
       if b==0:
        k+=1
        print("k=", k)
        return function(k)
       elif b==1:
        k=0
        return (1+function(k))
       else:
        function(k)

print(function())