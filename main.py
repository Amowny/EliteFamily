########################################################################################################################

# KÜTÜPHANELER

########################################################################################################################
import turtle
from turtle import *
import math

########################################################################################################################

# TURTLE KISALTMALAR

########################################################################################################################
ws = turtle.Screen()
ws.title("SABANCI HOLDING")

ws1 = turtle.Screen()

ws2 = Screen()

ws2.addshape('images/cursor.gif')

style = ('Courier', 10, 'italic')

########################################################################################################################

# TURTLE KOMUT AYARLARI

########################################################################################################################

t = turtle.Pen()

t.speed(5)

turtle.screensize(canvwidth=1920, canvheight=1080,
                  bg="white")

t.shape('images/cursor.gif')

count = 0

familycircle = 30

########################################################################################################################

# ILERI, GERI , SAĞ, SOL FONKSIYONLARI

########################################################################################################################

def draw_square(length):
    for i in range(0,4):
        t.forward(length)
        t.right(90)

def f(amt):
    t.forward(amt)


def l(deg):
    t.left(deg)


def b(deg):
    t.backward(deg)
########################################################################################################################

# INTRO

########################################################################################################################

def intro():
    global count
    t.reset()
    Screen().setup(1920, 1080)
    t.penup()
    t.left(180)
    t.forward(300)
    t.right(90)
    t.forward(480)
    t.left(90)
    t.pendown()
    t.left(180)
    t.speed(8)
    count = 0


intro()
########################################################################################################################

# FAMILY TREE YAZISI

########################################################################################################################

# F
def FamilyF():
    l(90)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    l(90)
    f(10)
    t.pendown()


FamilyF()


# A

def FamilyA():
    l(90)
    f(40)
    l(270)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(90)
    t.penup()
    f(10)
    t.pendown()


FamilyA()


# M

def FamilyM():
    l(90)
    f(40)
    l(180)
    l(45)
    f(math.sqrt(800))
    l(90)
    f(math.sqrt(800))
    l(45)
    l(180)
    f(40)
    l(90)
    t.penup()
    f(10)
    t.pendown()


FamilyM()


# I

def FamilyI():
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    l(180)
    f(20)
    l(180)
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    t.penup()
    f(10)
    t.pendown()


FamilyI()


# L

def FamilyL():
    l(90)
    f(40)
    l(180)
    f(40)
    l(90)
    f(20)
    t.penup()
    f(10)
    t.pendown()


FamilyL()


# Y

def FamilyY():
    t.penup()
    f(10)
    l(90)
    t.pendown()
    f(20)
    l(26.5650511771)
    f(math.sqrt(2000) / 2)
    l(180)
    f(math.sqrt(2000) / 2)
    l(180 - (26.5650511771 + 26.5650511771))
    f(math.sqrt(2000) / 2)
    l(180)
    f(math.sqrt(2000) / 2)
    l(26.5650511771)
    f(20)
    l(90)
    t.penup()
    f(20)
    t.pendown()


FamilyY()


# Boşluk Family Tree

def SpaceFamilyTree():
    t.penup()
    f(45)


SpaceFamilyTree()


# TreeT

def TreeT():
    t.penup()
    f(10)
    l(90)
    f(40)
    l(90)
    f(10)
    l(180)
    t.pendown()
    f(20)
    l(180)
    f(10)
    l(90)
    f(40)
    l(90)
    t.penup()
    f(20)
    t.pendown()


TreeT()


# TreeR P

def P():
    l(90)
    f(40)
    l(270)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(90)
    f(20)
    l(90)
    t.penup()
    f(30)
    t.pendown()


# TreeR

def TreeR():
    P()
    t.penup()
    t.backward(10)
    l(90)
    l(45)
    t.pendown()
    f(math.sqrt(800))
    l(180)
    f(math.sqrt(800))
    l(45)
    t.penup()
    f(10)
    t.pendown()


TreeR()


# TreeE1

def TreeE1():
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    l(90)
    f(10)
    t.pendown()


TreeE1()


# TreeE1

def TreeE2():
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    l(180)
    f(20)
    l(270)
    f(20)
    l(270)
    f(20)
    t.penup()
    l(270)
    f(40)
    l(90)
    f(10)
    t.pendown()


TreeE2()
########################################################################################################################

# BABA TARAFI

########################################################################################################################

# Baba Tarafı Kare

def babatarafikare1():
    t.penup()
    t.goto(-718.0,335.0)
    t.pendown()
    draw_square(50)


babatarafikare1()

def babatarafidaire1():
    t.penup()
    t.goto(-620.0, 280.0)
    t.pendown()
    t.circle(familycircle)
    t.penup()


babatarafidaire1()

def babataraficizgi1():
    t.goto(-668.0,310.0)
    t.pendown()
    f(20)
    t.penup()

babataraficizgi1()

def babatarafigrandfather():
    t.goto(-699.0,335.0)
    t.write('GrandFather', font=style, align='center')
    t.hideturtle()

babatarafigrandfather()

def babatarafigrandmother():
    t.goto(-601.0, 336.0)
    t.write('GrandMother', font=style, align='center')

babatarafigrandmother()

def babataraficizgi2():
    t.showturtle()
    t.goto(-657.0, 310.0)
    t.pendown()
    l(90)
    b(65)
    t.penup()

babataraficizgi2()

def babatarafikare2():
    t.goto(-680.0,195.0)
    t.pendown()
    draw_square(50)
    t.penup()

babatarafikare2()

def babatarafiuncle():
    t.hideturtle()
    t.goto(-653.0,243.0)
    t.write('Uncle', font=style, align='center')

babatarafiuncle()

def babataraficizgi3():
    t.showturtle()
    t.goto(-630.0,218.0)
    t.pendown()
    l(270)
    f(25)
    t.penup()

babataraficizgi3()

def babatarafikare3():
    t.goto(-605.0,245.0)
    t.pendown()
    draw_square(50)
    t.penup()

babatarafikare3()

def babatarafifather():
    t.hideturtle()
    t.goto(-576.0,243.0)
    t.write('Father', font=style, align='center')

babatarafifather()

def babataraficizgi3():
    t.showturtle()
    t.goto(-703.0, 218.0)
    t.pendown()
    l(180)
    b(25)
    t.penup()

babataraficizgi3()

def babatarafikare4():
    t.goto(-703.0,195.0)
    t.pendown()
    draw_square(50)
    t.penup()

babatarafikare4()

def babatarafiuncle1():
    t.hideturtle()
    t.goto(-726.0,243.0)
    t.write('Uncle', font=style, align='center')

babatarafiuncle1()

def babataraficizgi4():
    t.showturtle()
    t.goto(-778.0,218.0)
    t.pendown()
    b(25)
    t.penup()

babataraficizgi4()

def babatarafikare5():
    t.goto(-809.0,248.0)
    t.pendown()
    t.circle(familycircle)
    t.penup()

babatarafikare5()

def babatarafiaunt():
    t.hideturtle()
    t.goto(-806.0,244.0)
    t.write('Aunt', font=style, align='center')

babatarafiaunt()

########################################################################################################################

# ANNE TARAFI

########################################################################################################################

def annetarafikare1():
    t.penup()
    t.goto(-400.0,335.0)
    t.pendown()
    draw_square(50)


annetarafikare1()

def annetarafidaire1():
    t.penup()
    t.goto(-302.0, 280.0)
    t.pendown()
    t.circle(familycircle)
    t.penup()


annetarafidaire1()

########################################################################################################################
ws1.exitonclick()