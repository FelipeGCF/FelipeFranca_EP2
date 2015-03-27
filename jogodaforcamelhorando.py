# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:20:06 2015

@author: Felipe
"""



import turtle 
import random
from unicodedata import normalize
def formatar(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')    
if __name__=='__main__':
    from doctest import testmod
    testmod()
    
    
listalimpa = []
arquivo=open("entrada.txt",encoding="utf-8")
leitura=arquivo.readlines()
print(leitura)

z = ""
ganhou=0
for i in range(len(leitura)):
    listalimpa.append(leitura[i].strip())
    print(listalimpa)
    z= random.choice(listalimpa)
    print(z)
formatado=formatar(z)    
print(formatado)

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
         

digitadas=[]
acertos=0
lista = []  
while True:
   #window = turtle.write
    
    
    
    tentativa=window.textinput("\nDigite uma letra:", "\nDigite uma letra:").strip()
    #p = z.find(tentativa)
    if tentativa in z:
       p = z.find(tentativa) 
       print("Voce acertou!")
       
       if i == conta_as_letras and ganhou != conta_as_letras:
           i=0
       while i < conta_as_letras:
           b=z[i]
           if tentativa in z and b== tentativa:
               forca.penup()
               forca.setpos(-25 +(16*(i+1)), -99)
               forca.pendown()
               forca.write(formatado[i],font=("Arial", 16))
               ganhou+=1
               i+=1
           elif tentativa == "":
               forca.penup()
               forca.setpos(-25 +(1*(i+1)), -99)
               forca.pendown()
               forca.write(formatado[i],font=("Arial", 16))
               i+=1
           elif tentativa in z:
               i+=1
           else:
               erros+=1
               print("Voce errou")
               i=len(z)
               
           

       for i in range(len(z)):
           if tentativa ==z[i]:
               forca.penup()
               forca.setpos(-20 + p*24, -99)
               forca.write(tentativa, font=("Arial", 16))
               
       
    if tentativa not in z:
        erros+=1
        print("Voce errou!")
        if erros==1:       
            
           forca.right(90)
           forca.circle(20)
         
        if erros==2:
           forca.circle(20, 180)
           forca.right(90)
           forca.forward(100)
           
                    
        if erros==3:
           forca.right(330)
           forca.forward(80)
           forca.right(180) 
           forca.forward(80)
    
                    
        if erros==4:
           forca.right(225) 
           forca.forward(80)
           forca.right(180)
           forca.forward(80)
        
                    
        if erros==5:
           forca.right(345)
           forca.forward(70)
           forca.right(120)
           forca.forward(60)
     
                    
        if erros==6:
           forca.right(180)
           forca.forward(60)
           forca.right(300)
           forca.forward(60)
           print("Enforcado!")
           break
        
    if ganhou==len(z):
       forca.penup()
       forca.setpos(0,0)
       forca.pendown()
       window.exitonclick()
       forca.write("Parabéns, você ganhou!!", align="center", font=("Arial", 25))