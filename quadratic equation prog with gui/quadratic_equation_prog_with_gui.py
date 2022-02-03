from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t
D=-1
t=""
T=0

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

def veel() :
    global T 
    if T==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_width()+50))
        btn_veel.config(text="Уменьшить окно")
        T=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_width()-500))
        btn_veel.config(text="Увеличеть окно")
        T=0

def figura():
    valik=var.get()
    if valik==1:
        glass()
    elif valik==2:
        whale()
    elif valik==3:
        zont()
    elif valik==4:
        babochka()

def glass():
        x1 = np.arange(-9, -0.5 , 0.5)#min max step
        y1=(-1/16)*(x1+5)**2 +2       
        x2 = np.arange(1, 9.5, 0.5)
        y2=(-1/16)*(x2-5)**2 +2        
        x3 = np.arange(-9, -0.5 , 0.5)
        y3= (1/4)*(x3+5)**2 -3
        x4 = np.arange(1, 9.5 , 0.5)
        y4= (1/4)* (x4-5)** 2 -3
        x5 = np.arange(-9, -5.5 , 0.5)
        y5= у = -(x5+7)** 2 +5
        x6 = np.arange(6, 9.5 , 0.5)
        y6= -(x6-7)** 2 +5
        x7 = np.arange(-1, 1.5, 0.5)
        y7= -0.5*x7**2+1.5

        plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
        plt.title('очки')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()

def whale():
    x1 = np.arange(0, 9.5, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def zont():
    x1=np.arange(-12, 12.5, 0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4, 4.5, 0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12, -3.5, 0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4, 12.5, 0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4, -0.3, 0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4, 0.2, 0.5)
    y6=1.5*(x6+3)**2-10
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Зонт")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def babochka():
    x1 = np.arange(-9, -0.5, 0.5)
    y1 = -(1/8)*(x1+9)**2+8
    x2 = np.arange(1, 9.5, 0.5)
    y2 = -(1/8)*(x2-9)**2+8
    x3 = np.arange(-9, -7.5, 0.5)
    y3 = 7*(x3+8)**2+1
    x4 = np.arange(8, 9.5, 0.5)
    y4 = 7*(x4-8)**2+1
    x5 = np.arange(-8, -0.5, 0.5)
    y5 = 1/49*(x5+1)**2
    x6 = np.arange(1, 8.5, 0.5)
    y6=1/49*(x6-1)**2
    x7 = np.arange(-8, -0.5, 0.5)
    y7 = -4/49*(x7+1)**2
    x8 = np.arange(1, 8.5, 0.5)
    y8 = -4/49*(x8-1)**2
    x9 = np.arange(-8, -1.5, 0.5)
    y9 = 1/3*(x9+5)**2-7
    x10 = np.arange(2, 8.5, 0.5)
    y10 = 1/3*(x10-5)**2-7
    x11 = np.arange(-2, -0.5, 0.5)
    y11 = -2*(x11+1)**2-2
    x12 = np.arange(1, 2.5, 0.5)
    y12 = -2*(x12-1)**2-2
    x13 = np.arange(-1, 1.5, 0.5)
    y13 = -4*x13**2+2
    x14 = np.arange(-1, 1.5, 0.5)
    y14 = 4*x14**2-6
    x15 = np.arange(-2, 0.5, 0.5)
    y15 = -1.5*x15+2
    x16 = np.arange(0, 2.5, 0.5)
    y16 = 1.5*x16+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title('Бабочка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
#-------------------------------------------------------------------------------------------------------------


#каркас интерфейса
aken=Tk()
aken.title("Square equation with gui")
aken.geometry("900x375")
f1=Frame(aken,width=900,height=300,bg="blue")
f1.place(x=0,y=0)
f2=Frame(aken,width=900,height=600,bg="yellow")
f2.place(x=0,y=300)
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

btn_veel=Button(f2,text="Увеличеть окно", font="Calibri 26", bg="green",command=veel)

var=IntVar()
r1=Radiobutton(f2,text="очки",variable=var,value=1,font="Calibri 26",command=figura)#command=figura
r2=Radiobutton(f2,text="кит",variable=var,value=2,font="Calibri 26",command=figura)
r3=Radiobutton(f2,text="зонтик",variable=var,value=3,font="Calibri 26",command=figura)
r3=Radiobutton(f2,text="бабочка",variable=var,value=4,font="Calibri 26",command=figura)

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
btn_veel.place(x=260,y=0)
r1.place(x=200,y=200)
r2.place(x=100,y=300)
r3.place(x=300,y=100)
btn_g.place(x=550,y=80)









aken.mainloop()