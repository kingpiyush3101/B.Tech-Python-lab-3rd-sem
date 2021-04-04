import turtle
c=turtle.Turtle()
c.speed(100)
w=turtle.Screen()
c.pencolor("Red")
c.pensize("0")
c.penup()
c.goto(0,-100)
c.pendown()
d=0
a=10
i=0
while i<=210:
    c.forward(d)
    c.left(a)
    d+=3
    a+=1
    i+=1
c.hideturtle()
w.exitonclick()