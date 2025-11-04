import turtle
t = turtle.Turtle()
s = t.getscreen()
t.shape("turtle")
t.color("green")
s.bgcolor("black")
isRainbow = False
def l():
  t.left(90)
def r():  
  t.right(90)
def f():
  t.forward(20)
def b():  
  t.forward(-20)
def u():
  t.penup()
def d():
  t.pendown()
def wow():
  global isRainbow
  isRainbow = not isRainbow
def c():
  for i in range (10):
    t.color("red")
    t.circle(50,5.15)
    t.color("orange")
    t.circle(50,5.15)
    t.color("yellow")
    t.circle(50,5.15)
    t.color("green")
    t.circle(50,5.15)
    t.color("blue")
    t.circle(50,5.15)
    t.color("purple")
    t.circle(50,5.15)
    t.color("pink")
    t.circle(50,5.15)
  t.color("green")
def rainbow():
  if (isRainbow):
    t.color("red")
    t.color("orange")
    t.color("yellow")
    t.color("green")
    t.color("blue")
    t.color("purple")
    t.color("pink")
s.onkey(l, "Left")
s.onkey(r, "Right")
s.onkey(f, "Up")
s.onkey(b, "Down")
s.onkey(u,"a")
s.onkey(d,"z")
s.onkey(c,"space")
s.onkey(wow,"b")
s.listen()
s.ontimer(rainbow,100)