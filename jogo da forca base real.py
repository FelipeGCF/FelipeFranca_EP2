

import turtle 
import random
listalimpa = []
arquivo=open("entrada.txt",encoding="utf-8")
leitura=arquivo.readlines()
print(leitura)
for i in range(len(leitura)):
    listalimpa.append(leitura[i].strip())
    print(listalimpa)
    z= random.choice(listalimpa)
    print(z)
window = turtle.Screen()    
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
forca.color("blue")
erros=0
while True:
   
    digitadas=[]
    acertos=0
    lista = []    
    
  
    
    window = turtle.write
    senha=''
    
    tentativa=input("\nDigite uma letra:").lower().strip()
    if digitadas in leitura:
       print("Voce acertou!")
       digitadas += senha
       continue
       while True:
             acertos+=1
             print("Voce acertou!")
         
    
    else:
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
    
    
    if digitadas in leitura :
       print("Voce acertou")
       
          
       
                





        
    
    
    




