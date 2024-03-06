import turtle

# Classe base Turtle
class Tartaruga(turtle.Turtle):
    def __init__(self, name: str):
        self.name = name
        super().__init__()
        # Inicializações adicionais, se necessário
        turtle.bgcolor("black")
        turtle.pencolor("white")

    def desenha_quadrado(self, size=100):
        for _ in range(4):
            self.forward(size)
            self.right(90)

    def para_frente(self, distance=100):
        turtle.forward(distance)
        return(f"{self.name} andou {distance} passos para frente")

    
    def para_tras(self, distance=100):
        turtle.backward(distance)
        return(f"{self.name} andou {distance} passos para trás")


    def virar_esquerda(self, angle=90):
        turtle.left(angle)
        if angle != 90:
            return(f"{self.name} girou {angle}o a esquerda")
        else:
            return(f"{self.name} virou à esquerda")
        

    def virar_direita(self, angle=90):
        turtle.right(angle)
        if angle != 90:
            return(f"{self.name} girou {angle}o à direita")
        else:
            return(f"{self.name} virou à direita")

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
nome = input("Digite o nome do seu robô: ") 
tartaruga = Tartaruga(nome)

lista_de_comandos = ["para_frente", "para_tras", "virar_esquerda", "virar_direita"]
programa = []

linha_programa = 0
while True:
    while True:
        if len(programa) > 0:
            print(f"\nPrograma: {programa}")
        print(f"Lista de comandos: {lista_de_comandos}\n")
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
        linha_programa += 1
        print(f"{linha_programa}: {tartaruga.executa_comando(comando)}")
    programa = []
    
    confirmacao = ""
    while confirmacao not in ["S", "N"]:
        confirmacao = str.upper(input("Deseja encerrar o programa? (S/N)"))
    if confirmacao == "S":
        break
    else:
        continue

# window.mainloop()
