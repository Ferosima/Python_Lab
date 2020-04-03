#12. Даний рядковий файл. Створити новий рядковий файл, який містить всі рядки вихідного файлу найменшої довжини (в тому ж порядку).
try:
    f = open('file.txt', 'r')
except FileNotFoundError:
    print('File not found. Do you want create new file?')
    a=int(input('1-yes, 0- no\n'))
    if a==1:
        f = open('file.txt', 'w')
        print('File created \nInput data in file')
        stop=False
        print('if you want stop input input 0')
        str=""
        while True!=stop:
          a=input()
          if a!='0':
              str=str+a+'\n'
          else:
             str=str[0:len(str)-1]
             print(str)
             stop=True
        f.write(str)
f = open('file.txt', 'r')
lines=f.read().split('\n')
len=len(lines[0])
for line in lines:
    if len>=line.__len__():
        len=line.__len__()
f_copy=open('file_min_len.txt','w')
for line in lines:
    if len==line.__len__():
        str=line+'\n'
        f_copy.write(str)
print("Done!")