from tkinter import *

r = int(input("Radius: "))
root=Tk()
root.title("CIRCLE")
height=500
width=500
canvas=Canvas(root,height=height,width=width)
canvas.pack()
xc=int(height/2)
yc=int(width/2)
x=0
y=r
p=1-r
while(x<y):
    if(p<0):
        x=x+1
        p=p+2*(x+1)+1
    else:
        x=x+1
        y=y-1
        p=p+2*(x-y)+1

        canvas.create_text(xc+x,yc+y,text=".")
        canvas.create_text(xc-x,yc+y,text=".")
        canvas.create_text(xc+x,yc-y,text=".")
        canvas.create_text(xc-x,yc-y,text=".")
        canvas.create_text(xc+y,yc+x,text=".")
        canvas.create_text(xc-y,yc+x,text=".")
        canvas.create_text(xc+y,yc-x,text=".")
        canvas.create_text(xc-y,yc-x,text=".")

root.mainloop()
