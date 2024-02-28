import turtle

# Classe base Turtle
class tartaruga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicializações adicionais, se necessário
        turtle.bgcolor("black")
        turtle.pencolor("white")

    def desenha_quadrado(self, size=100):
        for _ in range(4):
            self.forward(size)
            self.right(90)

    def para_frente(self, distance=100):
        turtle.forward(distance)
        return(f"Avançando {distance} passos")

    
    def para_tras(self, distance=100):
        turtle.backward(distance)
        return(f"Retornando {distance} passos")


    def virar_esquerda(self, angle=90):
        turtle.left(angle)
        if angle != 90:
            return(f"Girando {angle}o a esquerda")
        else:
            return("Girando à esquerda")
        

    def virar_direita(self, angle=90):
        turtle.right(angle)
        if angle != 90:
            return(f"Girando {angle}o à direita")
        else:
            return("Girando à direita")

    def executa_comando(self, comando: str):
        if comando == "para_frente":
            return(self.para_frente())
        elif comando == "para_tras":
            return(self.para_tras())
        elif comando == "virar_esquerda":
            return(self.virar_esquerda())
        elif comando == "virar_direita":
            return(self.virar_direita())
        else:
            print("Comando não reconhecido")

window = turtle.Screen() 

# # -----------------------------------
michelangelo = tartaruga()

lista_de_comandos = ["para_frente", "para_tras", "virar_esquerda", "virar_direita"]
programa = []
while True:
    while True:
        print(f"Programa: {programa}")
        comando = input("Digite o comando ([ENTER] para encerrar): ")
        if comando == "":
            confirmacao = ""
            while confirmacao not in ["S", "N"]:
                confirmacao = str.upper(input("Deseja executar o programa? (S/N)"))
            if confirmacao == "S":
                break
            else:
                continue
        if comando in lista_de_comandos:
            programa.append(comando)
        else:
            print(f"{comando} não é um comando conhecido")

    for comando in programa:
        print(f"{comando}: {michelangelo.executa_comando(comando)}")
    programa = []
    
    confirmacao = ""
    while confirmacao not in ["S", "N"]:
        confirmacao = str.upper(input("Deseja encerrar o programa? (S/N)"))
    if confirmacao == "S":
        break
    else:
        continue

# window.mainloop()
