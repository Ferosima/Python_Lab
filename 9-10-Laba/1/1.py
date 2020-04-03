#2. Дано імена чотирьох файлів. Знайти кількість файлів із зазначеними іменами, які є в поточному каталозі.
import os
import platform
import sys
folders_dir=['dir','dir2']
names_file = ["File1", "File2", "File3", "File4"]
a=input('Need folders \'dir\' and \'dir2\'.Do you want create this folders and files in them? \nIf yes - input 1, else-0\n')
# создание папок
if a=='1':
 try:
    os.mkdir(path='dir', mode=0o777, dir_fd=None)
    os.mkdir(path='dir2', mode=0o777, dir_fd=None)
 except OSError:
    print('This folder(s) exist ')

 folders = []  # перечень папок
 for check_be_folder in os.listdir():
    isFolder = True
    for i in range(len(check_be_folder)):
        if check_be_folder[i] == '.':
            isFolder = False
    if isFolder == True:
        folders.append(check_be_folder)
 print('Find folders:',folders)


 for folder in folders:#создание файлов в папках
    if folder=='dir'or folder=='dir2':
     for file in names_file:
        with open(os.getcwd() + '\\' + folder + '\\' + file + '.txt', 'w') as f:
            s = 'File name:' + file+'\n'
            f.write(s)
            s = 'System:' + platform.system() + platform.version() + '\n' + 'User name:' + os.getlogin()+'\n'
            f.write(s)
            s='File system encoding:'+sys.getfilesystemencoding()
            f.write(s)
print("Files check")
for folder in folders_dir:
    for file in names_file:
     try:
      with open(os.getcwd() + '\\'+folder+'\\' + file + '.txt', 'r') as f:
        pass
     except FileNotFoundError:
       print(file,' not found in ',folder,' folder')
print('You have all files')

