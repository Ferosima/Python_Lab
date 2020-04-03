#6
listDay=["Понеділок","Вівторок","Середа","Четверг","П'ятниця","Субота","Неділя"]
i=1
while True:
 i=int(input("Введіть номер дня\n"))
 if i>0 and i<8:
  print(listDay[i-1])
  break