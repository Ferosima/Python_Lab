#10
# list_Units=["Один","Два","Три","Чотири","П'ять","Шість","Сім","Вісім","Дев'ять"]
# list_Ten=["Десять","Одинадцять","Дванадцять","Тринадцять","Чотирнадцять","Пятнадцять","Шістнадцять","Сімнадцять"
#     ,"Вісімнадцять","Девятнадьцть"]
# list_Dozens=["Десять","Двадцять","Тридцять","Сорок","П'ядесят","Шістдесяд","Сімдесят","Вісімдесят","Дев'яносто"]
# list_Hundred=["Сто","Двісті","Триста","Чотириста","П'ятьсот","Шістьсот","Сімсот","Вісімсот","Дев'ятсот"]
# a=int(input())
# hundred=a//100
# dozens=a//10%10
# units=a%10
# if hundred>0:
#  print(list_Hundred[hundred-1])
# if dozens>1:
#  print(list_Dozens[dozens-1])
# elif dozens ==1:
#  print(list_Ten[units])
# if units>0 and dozens>1:
#  print(list_Units[units - 1])
#  def func(a):
#      if a==1:
#        return  1
#      else:
#       return  func(a-1)*a
# print (func(hundred))
#2
a=int(input("First number="))
b=int(input("Second number="))
c=int(input("Third number="))
list=[a,b,c]
i=0
n=0
while i<len(list):
  if list[i]>0 :
   n+=1
  i+=1
print(n)