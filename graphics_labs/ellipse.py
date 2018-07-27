from tkinter import *

def PlotEllipse(xc, yc, x, y):
    canvas.create_text(xc+x,yc+y,text=".")
    canvas.create_text(xc+x,yc-y,text=".")
    canvas.create_text(xc-x,yc+y,text=".")
    canvas.create_text(xc-x,yc-y,text=".")

xc = int(input("Xc: "))
yc = int(input("Yc: "))
a = int(input("a: "))
b = int(input("b: "))

root=Tk()
root.title("Ellipse")
height=700
width=700
canvas=Canvas(root,height=height,width=width)
canvas.pack()


x = 0
y = 0
p = 0
pe = 0
ps = 0
pse = 0
pe2 = 0
ps2 = 0
pse2 = 0
x = 0
y = b
p = b*b + ((a*a)*(1-4*b))/4
pe = 3*b*b
pe2 = 2*b*b
pse - pe - ((2*a*a)*(b-1))
pse2 = pe2 + (2*a*a)
PlotEllipse(xc, yc, x, y)
while (pse < ((2*a*a)+(3*b*b))):
    if (p < 0):
        p = p + pe
        pe = pe + pe2
        pse = pse + pe2
    else:
        p = p + pse
        pe = pe + pe2
        pse = pse + pse2
        y = y - 1
    x = x + 1
    PlotEllipse(xc, yc, x, y)
p = p - ((((a*a)-(4*y-3)) + (b*b)*((4*x+3))+2))/4
ps = (a*a)*(3-2*y)
pse = (2*b*b) + (3*a*a)
ps2 = 2*a*a
while (y > 0):
    if (p > 0):
        p = p + pe
        pe = pe + ps2
        pse = pse + ps2
    else:
        p = p + pse
        pe = pe + ps2
        pse = pse + pse2
        x = x + 1
    y = y - 1
    PlotEllipse(xc, yc, x, y)
root.mainloop()
