from tkinter import *
from math import *

def SQUARE():
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a=float(Z1.get())
        b=float(Z2.get())
        c=float(Z3.get())
        D=b**2-4*a*c
        vast.configure(text=D)
        
        if D>0:
            k1=round((-b+D**0.5)/(2*a),2)
            k2=round((-b-D**0.5)/(2*a),2)
            geg=f"K1={k1} \n K2={k2}"
            flag=True
            vast.configure(text=f"D={D}\n K1={k1}\n K2={k2}")

        elif D==0:
            x=-b/2*a
            geg=f"X={x}"
            flag=True
            vast.configure(text=f"один корень={D}")

        else:
            vast.configure(text=f"корней нет={D}")
            flag=False
        return flag,D,geg

def graafik():
    flag,D,geg=SQUARE()
    if flag==True:
        a1=int(a.get())
        b1=int(b.get())
        c1=int(c.get())
        x0=(-b1)/(2*a1)
        y0=a1*x0*x0+b1*x0+c1
        x = np.arange(x0-10, x0+10, 0.5)
        y=a1*x*x+b1*x+c1
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    answer.configure(text=f"D={D}\n{t}\n{text}")




aken=Tk()
aken.title("Akna nimetus")
aken.geometry("650x300")
#A=Frame()
#---------------------------------------------------------------------------------------------------------------------------------
lbl=Label(aken,text="Решение квадратного уравнения ",height=2,width=37,font="Arial 15",fg="green",bg="lightblue")
lbl.pack()
vast=Label(aken,text="Решение",height=4,width=27,font="Arial 20",fg="black",bg="yellow")

text1=Label(aken,text="x**2+",height=1,width=4,font="Arial 20",fg="green",bg="white")
text2=Label(aken,text="x+",height=1,width=2,font="Arial 20",fg="green",bg="white")
text3=Label(aken,text="=0",height=1,width=2,font="Arial 20",fg="green",bg="white")

BT=Button(aken,text="Решение",font="Arial 20",height=1,width=8,bg="green",fg="black",command=SQUARE)

btn_g=Button(aken,text="График",font="Calibri 26",bg="white",command=graafik)
btn_g.pack(side=LEFT)


Z1=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
Z2=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
Z3=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)




Z1.place(x=0,y=100)
Z2.place(x=150,y=100)
Z3.place(x=250,y=100)

text1.place(x=68,y=100)
text2.place(x=215,y=100)
text3.place(x=320,y=100)

vast.place(x=70,y=150)
BT.place(x=370,y=90)









aken.mainloop()