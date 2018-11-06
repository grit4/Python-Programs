#Program to print nested rectangles
import tkinter
root=tkinter.Tk()
c=tkinter.Canvas(root,height=400,width=500)
c.pack()
p,q,r,s=10,10,490,390
f=False
for i in range(10):
    if f:
        c.create_rectangle(p,q,r,s,fill="red")
        f=not f
    else:
        c.create_rectangle(p,q,r,s,fill="yellow")
        f=not f
    p,q,r,s=p+20,q+20,r-20,s-20
root.mainloop()
