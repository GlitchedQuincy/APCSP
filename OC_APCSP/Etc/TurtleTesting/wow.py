import turtle
pat = turtle.Turtle()
pat.colormode(250)

#pat.penup()
#pat.left(90)
#pat.forward(50)
#pat.pendown()
R=int(input("enter the red value"))
G=int(input("enter the green value"))
B=int(input("enter the blue value"))
pat.color(R, G, B)
pat.begin_fill()
pat.circle(50,360)
pat.end_fill()


