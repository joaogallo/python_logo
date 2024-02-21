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
        print(f"Avançando {distance} passos")
        turtle.forward(distance)
    
    def para_tras(self, distance=100):
        print(f"Retornando {distance} passos")
        turtle.forward(distance)

    def virar_esquerda(self, angle=90):
        if angle != 90:
            print(f"Girando {angle}o a esquerda")
        turtle.left(angle)

    def virar_direita(self, angle=90):
        if angle != 90:
            print(f"Girando {angle}o a esquerda")
        turtle.right(angle)

window = turtle.Screen()

# # -----------------------------------
# my_turtle = tartaruga()
# my_turtle.para_frente()
# my_turtle.virar_esquerda()
# my_turtle.para_tras()
# my_turtle.virar_direita()
# # -----------------------------------

# window.mainloop()
