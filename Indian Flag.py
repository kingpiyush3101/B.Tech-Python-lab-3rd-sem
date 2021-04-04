import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(10)

a=300
b=74.5

t.penup()
t.goto(-a/2,a/2)
t.pendown()

t.color("orange")
t.begin_fill()
t.forward(a)
t.right(90)
t.forward(b)
t.right(90)
t.forward(a)
t.end_fill()
t.left(90)
t.pencolor("white")
t.forward(b)
t.color("green")
t.begin_fill()
t.forward(b)
t.left(90)
t.forward(a)
t.left(90)
t.forward(b)
t.end_fill()

t.penup()
t.goto(a/8,a/8)
t.pendown()
t.pensize(2)
t.pencolor("navy")
t.circle(b/2)

t.penup()
t.goto(0,a/10+a/40)
t.pendown()
t.pensize(2)
t.pencolor("navy")
for i in range(24):
    t.forward(b/2)
    t.backward(b/2)
    t.left(15)

t.penup()
t.goto(0,-a/2)
t.pendown()
t.write("Happy Republic Day",font=[a/10],align="center")

s.exitonclick()