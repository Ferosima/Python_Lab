list16=["A","B","C","D","E","F"]
def systembody(a,n):
    if a>=2 and a<=16:
        if n>0:
         s=""
         if n%a>=10:
             s=list16[n%a-10]+str(systembody(a,n//a))
         else:
          s=str(n%a)+str(systembody(a,n//a))
         return s
        elif n==0:
            pass
            #return 0
    return ""
def system (a,n):
    return systembody(a,n)[::-1]
print(system(16,31))