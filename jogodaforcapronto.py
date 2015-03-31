# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:01:11 2015

@author: Felipe
"""


import turtle 
import random
import time
from unicodedata import normalize
def formatar(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')    
if __name__=='__main__':
    from doctest import testmod
    testmod()
    
    

    
listalimpa = []
arquivo=open("entrada.txt",encoding="utf-8")
leitura=arquivo.readlines()
lista=[]

print(leitura)

z = ""
ganhou=0
for i in range(len(leitura)):
    listalimpa.append(leitura[i].strip().lower())
    print(listalimpa)
    z= random.choice(listalimpa)
    print(z)
listalimpa.remove(z)
t=formatar(z)    
print(t)

conta_as_letras=len(z)
window = turtle.Screen()    
window.bgcolor("lightblue")
window.title("Poligonos")


forca   = turtle.Turtle()  
forca.color("blue")
forca.speed(3)             
forca.penup()      
forca.setpos(-50,-100)
forca.pendown()
forca.backward(200)
forca.forward(100)
forca.left(90)
forca.forward(300)
forca.right(90)
forca.forward(100)
forca.right(90)
forca.forward(50)
forca.hideturtle()
erros=0
'''
s= " _ "
forca=turtle.Turtle()
forca.color("red")
forca.penup()   
forca.setpos(-25, -100)
forca.write(s*len(z),font = ("Arial", 16))
forca.hideturtle()
'''

for i in range(len(z)):
    if z[i]==" ":
        forca.penup()
        forca.setpos(-25+(i +1)*16,-100 )
        forca.write(" ", False, font=("Arial", 16))
        
    else:
        forca.penup()
        forca.setpos(-25+(i +1)*16,-100 )
        forca.write("_", False, font=("Arial", 16))
         
k=0
digitadas=[]
acertos= t.count(' ')
lista = []  

   #window = turtle.write
while k < conta_as_letras:
      if t[k] == " ":
          ganhou+=1
      k+=1
while True:    
    
    
   tentativa=window.textinput("\nDigite uma letra:", "\nDigite uma letra:").strip()
   while tentativa  in lista:
         tentativa=window.textinput("\nDigite uma letra:", "\nDigite uma letra:").strip()   
   lista.append(tentativa)
   if tentativa in lista:
        print("Voce ja escolheu esta letra")
        erros+=0
   if tentativa in t:
      p = t.find(tentativa) 
       
      i=0
      if i == conta_as_letras and ganhou != conta_as_letras:
           i=0
      while i < conta_as_letras:
           b=t[i]
           if  b== tentativa:
               forca.penup()
               forca.setpos(-8 +16*i, -99)
               forca.pendown()
               forca.write(t[i],font=("Arial", 16))
               ganhou+=1
               i+=1
               
           elif tentativa == " ":
               forca.penup()
               forca.setpos(-8 +16*i, -99)
               forca.pendown()
               forca.write(t[i],font=("Arial", 16))
               i+=1
               i=len(z)
           elif tentativa in t:
               i+=1
           else:
               erros+=1
               print("Voce errou")
               i=len(z)
               
           
      

       
       
   if tentativa not in t:
        erros+=1
        
        
        if erros==1:       
           forca.penup()
           forca.setpos(-50,150)
           forca.pendown()
           forca.right(90)
           forca.circle(20)
         
        if erros==2:
           forca.penup()
           forca.setpos(-50,150)
           forca.pendown()
           forca.circle(20, 180)
           forca.right(90)
           forca.forward(100)
           
                    
        if erros==3:
           forca.penup() 
           forca.setpos(-50,10)
           forca.pendown()
           forca.right(330)
           forca.forward(80)
           forca.right(180) 
           forca.forward(80)
    
                    
        if erros==4:
           forca.penup()
           forca.setpos(-50,10)
           forca.pendown()
           forca.right(225) 
           forca.forward(80)
           forca.right(180)
           forca.forward(80)
        
                    
        if erros==5:
           forca.penup()
           forca.setpos(-50,10)
           forca.pendown()
           forca.right(345)
           forca.forward(70)
           forca.right(120)
           forca.forward(60)
     
                    
        if erros==6:
           forca.penup()
           forca.setpos(-50,80)
           forca.pendown()
           forca.left(225)
           forca.forward(60)
           forca.penup()
           forca.setpos(200,200)
           forca.pendown()
           forca.write("Que pena!!Voce foi enforcado!!", align="center", font=("Arial", 12))
           time.sleep(3)
           break
           
        
   if ganhou==len(z):
        forca.penup()
        forca.setpos(200,200)
        forca.pendown()
        forca.write("Parabéns, você ganhou!!", align="center", font=("Arial", 16))
        time.sleep(3)
        
        
        window.exitonclick()