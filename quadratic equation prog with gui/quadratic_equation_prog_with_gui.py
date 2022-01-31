from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def SQUARE():
    """
    функция решает квадратное уравнение следуя от введёных данных в интерактивный графический интерфейс(высшего класса xD)
    """
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a1=float(a.get())
        b1=float(b.get())
        c1=float(c.get())
        D=b1**2-4*a1*c1
        vast.configure(text=D)
        
        if D>0:
            k1=round((-b1+D**0.5)/(2*a1),2)
            k2=round((-b1-D**0.5)/(2*a1),2)
            geg=f"K1={k1} \n K2={k2}"
            flag=True
            vast.configure(text=f"D={D}\n K1={k1}\n K2={k2}")

        elif D==0:
            x=-b1/2*a1
            geg=f"X={x}"
            flag=True
            vast.configure(text=f"один корень={D}")

        else:
            vast.configure(text=f"корней нет={D}")
            flag=False
        return flag,D,geg

#--------------------------------------------------------------------------
def graafik():
    """
    функция строит график исходя из данных полученых в процессе работы функции "SQUARE"
    """
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
    vast.configure(text=f"D={D}\n{geg}\n{text}")
#-------------------------------------------------------------------------------------------------------------


#каркас интерфейса
aken=Tk()
aken.title("Square equation with gui")
aken.geometry("650x300")
#---------------------------------------------------------------------------------------------------------------------------------
#лейблы
lbl=Label(aken,text="Решение квадратного уравнения ",height=2,width=37,font="Arial 15",fg="green",bg="lightblue")
lbl.pack()
vast=Label(aken,text="Решение",height=4,width=27,font="Arial 20",fg="black",bg="yellow")
#--------------------------------------------------------------------------------------------------------------
#текстовые сообщения
text1=Label(aken,text="x**2+",height=1,width=4,font="Arial 20",fg="green",bg="white")
text2=Label(aken,text="x+",height=1,width=2,font="Arial 20",fg="green",bg="white")
text3=Label(aken,text="=0",height=1,width=2,font="Arial 20",fg="green",bg="white")
#-------------------------------------------------------------------------------------------------------------
#кнопки
BT=Button(aken,text="Решение",font="Arial 20",height=1,width=8,bg="green",fg="black",command=SQUARE)

btn_g=Button(aken,text="График",font="Calibri 26",bg="green",fg="black",command=graafik)
btn_g.pack(side=RIGHT)


a=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
b=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)
c=Entry(aken,width=4,font="Arial 20",fg="blue",bg="lightblue", justify=CENTER)




a.place(x=0,y=100)
b.place(x=150,y=100)
c.place(x=250,y=100)

text1.place(x=68,y=100)
text2.place(x=215,y=100)
text3.place(x=320,y=100)

vast.place(x=70,y=150)
BT.place(x=370,y=90)









aken.mainloop()