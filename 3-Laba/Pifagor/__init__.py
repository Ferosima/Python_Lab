from math import *
from tkinter import *
root=Tk()
w,h=500,500
canv=Canvas(root,width=w,height=h,bg='white')
pi=3.14
def Pifagor(x0,y0,a,L,N):
    k=0.7
    if(N>0):
        x1=x0+L*cos(a)
        y1=y0-L*sin(a)
        line=canv.create_line(int(x0),int(y0),int(x1),int(y1),fill='black')
        Pifagor(x1, y1, a + pi / 4, L * k, N - 1)
        Pifagor(x1, y1, a - pi / 4, L * k, N - 1)
        Pifagor(x1, y1, a - pi / 8, L * k, N - 1)
        Pifagor(x1, y1, a + pi / 8, L * k, N - 1)
Pifagor(250,400,pi/2,150,9)
canv.pack()
root.mainloop()