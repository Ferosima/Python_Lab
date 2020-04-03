from tkinter import *

root = Tk()
w, h = 800, 800
canv = Canvas(root, width=w, height=h, bg='white')

def squarePifagor(x0, y0, L, N):
    k = 0.4
    if (N > 0):
        x1 = x0 - L / 2
        y1 = y0 + L / 2
        x2 = x1 + L
        y2 = y1 - L
        line = canv.create_line(int(x1), int(y1), int(x2), int(y1), fill='black')
        line = canv.create_line(int(x2), int(y1), int(x2), int(y2), fill='black')
        line = canv.create_line(int(x1), int(y2), int(x2), int(y2), fill='black')
        line = canv.create_line(int(x1), int(y2), int(x1), int(y1), fill='black')
        squarePifagor(x1, y1, L * k, N - 1)
        squarePifagor(x2, y2, L * k, N - 1)
        squarePifagor(x1, y2, L * k, N - 1)
        squarePifagor(x2, y1, L * k, N - 1)


squarePifagor(400, 400, 400, 7)
canv.pack()
root.mainloop()
