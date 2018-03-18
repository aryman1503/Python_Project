# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 04:26:17 2018
Project ::: turtle race
@author: aryman
"""
from turtle import * #turtle is module
from random import randint #genrate randome number

write("Turtle Race", align='left')
speed(30)
penup()
goto(-140, 140)
for step in range(7):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

  
a = Turtle()
a.color('red')
a.shape('turtle')

a.penup()
a.goto(-160, 100)
a.pendown()

b = Turtle()
b.color('blue')
b.shape('turtle')

b.penup()
b.goto(-160, 80)
b.pendown()

c = Turtle()
c.color('yellow')
c.shape('turtle')

c.penup()
c.goto(-160, 60)
c.pendown()

d = Turtle()
d.color('green')
d.shape('turtle')

d.penup()
d.goto(-160, 40)
d.pendown()


for turn in range(50):
  a.forward(randint(1, 5))
  b.forward(randint(1, 5))
  c.forward(randint(1, 5))
  d.forward(randint(1, 5))
  
exit = input("Enter to exit!!!")
  