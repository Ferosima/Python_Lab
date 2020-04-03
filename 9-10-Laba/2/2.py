#7. Даний файл довільного типу. Створити його копію з новим ім'ям.
import os
import shutil
#f=open ('2_copy', "w").close ()
for i in range(len(os.listdir()[0])):
        if os.listdir()[0][i] == '.':
            type=os.listdir()[0][i:len(os.listdir()[0])]
shutil.copy(os.listdir()[0],'2_copy'+type)