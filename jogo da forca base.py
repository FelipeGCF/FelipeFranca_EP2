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
forca.color("blue")

palavra=input("Digite a palavra secreta").lower().strip()
for x in range(100):
    print()
digitadas=[]
acertos=[]
erros=0
while True:
    senha=""
    for letra in palavra:
        senha+=letra if letra in acertos else "."
        print(senha)
        if senha==palavra:
            print("Prabéns, voce ganhou o jogo!")
            break
        tentativa=input("\nDigite uma letra:").lower().strip()
        if tentativa in digitadas:
            print("Voce ja tentou esta letra!")
            continue
        else:
            digitadas+=tentativa
            if tentativa in palavra:
                acertos+=tentativa
            else:
                erros+=1
                print("Voce errou!")
                if erros==1:       
                    forca.right(90)
                    forca.circle(20)
                    forca.color("blue")
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





        
    
    
    




