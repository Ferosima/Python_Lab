#7
# s=str(input())
# sNew=s.replace("1","one")
# print(sNew)
#6
s=(str(input()))
i=1
sNew=""
if len(s)>0:
 sNew+=s[0]
 while i<len(s) :
  sNew+="*"+s[i]
  i += 1
 print(sNew)