import turtle


screen = turtle.Screen()
screen.bgcolor("white")

li = turtle.Turtle()
li.speed(5)
li.shape("turtle")

def draw_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

draw_circle(li, 0, -50, 50, "yellow")  
draw_circle(li, 0, 20, 30, "yellow")   

draw_circle(li, -10, 40, 5, "black")    
draw_circle(li, 10, 40, 5, "black")     

li.penup()
li.goto(-5, 30)
li.pendown()
li.color("orange")
li.begin_fill()
li.goto(0, 20)  
li.goto(5, 30)
li.goto(-5, 30)
li.end_fill()

li.penup()
li.goto(-15, -100)
li.pendown()
li.color("orange")
li.pensize(3)
li.goto(-25, -120) 

li.penup()
li.goto(15, -100)
li.pendown()
li.goto(25, -120)   

turtle.done()
