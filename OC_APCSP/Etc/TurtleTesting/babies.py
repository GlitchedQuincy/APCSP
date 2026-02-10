import turtle
import random

#This function sets the background
def setScene():
    screen = turtle.Screen()
    screen.bgcolor('cyan')
    bgTurtle = turtle.Turtle()
    bgTurtle.speed(0)
    bgTurtle.penup()
    bgTurtle.goto(-360, 200)
    bgTurtle.pendown()
    bgTurtle.color("burlywood")
    bgTurtle.begin_fill()
    for i in range(4):
        bgTurtle.forward(400)
        bgTurtle.right(90)
    bgTurtle.end_fill()
    bgTurtle.hideturtle()

#This function spawns turtles in random locations.
#The number of turtles spawned is based on user input.
turtleX = []
turtleY = []
stampIDs = []
pat = turtle.Turtle()

def createTurtles(numTurtles):
    pat.shape('turtle')
    pat.penup()
    pat.speed(0)
    pat.color('black')
    for i in range(numTurtles):
        x = random.randint(-360, 0)
        y = random.randint(-200, 200)
        pat.setposition(x, y)
        stamp_id = pat.stamp()            # stamp() returns an id we can clear later
        turtleX.append(x)
        turtleY.append(y)
        stampIDs.append(stamp_id)

def turtleSwim():
    # Move through the saved positions in the same order they were created.
    # For each turtle: cover the sand-stamped turtle by stamping burlywood, pick it up and move it into the ocean,
    # then leave a turtle stamp in the ocean.
    while stampIDs:
        x = turtleX.pop(0)
        y = turtleY.pop(0)
        sid = stampIDs.pop(0)

        # Instead of clearing the original stamp, go to its position,
        # change pat to burlywood and stamp to visually "erase" it.
        pat.penup()
        pat.goto(x, y)
        pat.color('burlywood')   # cover the sand turtle
        pat.shape('turtle')
        pat.showturtle()
        pat.stamp()

        # Change back to black and swim the turtle into the ocean
        pat.color('black')
        pat.setheading(0)   # face right / into the ocean

        # Animate to the ocean edge (x = 360) using turtle speed
        pat.speed(8)
        target_x = 360
        distance = target_x - pat.xcor()
        if distance > 0:
            step = 10
            steps = int(distance / step)
            for _ in range(steps):
                pat.forward(step)
            # move any remaining fraction
            remainder = distance - steps * step
            if remainder > 0:
                pat.forward(remainder)
        else:
            # already at/ past the target, just stamp where we are
            pass

        pat.speed(0)
        # leave the turtle in the ocean
        pat.stamp()
        pat.hideturtle()
        # short pause removed (no time.sleep)

setScene()
numTurtles = int(input("How many turtles? "))
createTurtles(numTurtles)
turtleSwim()