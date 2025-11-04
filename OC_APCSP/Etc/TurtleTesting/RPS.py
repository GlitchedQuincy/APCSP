import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.color("white")
t.pensize(5)
def f():
    t.forward(10)
def r():
    t.right(30)
def l():
    t.left(30)
def b():
    t.backward(10)
s.listen()
s.onkey(f,"Up")
s.onkey(r,"Right")
s.onkey(l,"Left")
s.onkey(b,"Down")

turtle.done()    