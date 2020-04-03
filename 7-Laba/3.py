#12. У вхідному файлі записано текст. Словом вважається послідовність непробельний символів,
#що йдуть підряд, слова розділені одним або більшим числом прогалин або символами кінця рядка.
# Визначте, скільки різних слів міститься в цьому тексті.
import re

def get_file_content():
  f = open('3.txt', 'r')
  file_content = f.read()
  f.close()
  words_arr = []
  for word in re.split(r'\s+', file_content):
    words_arr.append(word.lower())
  print(words_arr)
  return words_arr
array=get_file_content()
#array = input("Введите список через пробел").split()
count = 0
unique_array = []
for x in array:
    if x not in unique_array:
        count += 1
        unique_array.append(x)
print(len(unique_array))