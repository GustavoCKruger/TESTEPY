import turtle

# Configuração da tela e da tartaruga
screen = turtle.Screen()
screen.bgcolor("white")

li = turtle.Turtle()  # Corrige para 'Turtle' com T maiúsculo
li.pensize(2)
li.color("green")
li.left(100)
li.backward(80)
li.speed(6000)  # '6000' é muito alto; use um valor razoável como 10


# Função recursiva para desenhar o padrão
def love(i):
    if i < 10:
        return
    else:
        li.forward(i)
        li.color("red")
        li.circle(3)
        li.color("green")
        li.left(30)

        love(3 * i / 4)

        li.right(60)

        love(3 * i / 4)

        li.left(30)
        li.backward(i)

# Chama a função de desenho
love(60)

# Mantém a janela aberta até ser fechada
turtle.done()
