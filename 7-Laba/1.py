#22. Даний рядок, що містить повне ім'я файлу (наприклад,
# 'C:\WebServers\home\testsite\www\myfile.txt'). Виділіть з цього рядка ім'я файлу без розширення.
s="C:\WebServers\home\\testsite\www\myfile.txt'"
a = s.split("\\")
b=a[len(a)-1].split('.')
name=b[0]
print(name)