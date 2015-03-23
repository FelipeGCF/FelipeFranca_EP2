# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:40:31 2015

@author: Felipe
"""
import turtle        # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

forca   = turtle.Turtle()  
forca.speed(5)             
forca.penup()      
forca.setpos(150,-150)
forca.pendown()
forca.backward(250)
forca.left(90)
forca.forward(300)
forca.right(90)
forca.forward(100)
forca.right(90)
forca.forward(50)
forca.right(90)
forca.circle(20)
forca.color("blue")