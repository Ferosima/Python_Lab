#4
def function(a=str()):
    if len(a)!=0:
     return a[len(a)-1]+function(a[0:len(a)-1])
    return ""
a="12345"
print(function(a))
