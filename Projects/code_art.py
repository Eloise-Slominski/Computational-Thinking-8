import turtle

t = turtle.Turtle()

t.goto(-15, 15)

t.pendown()
t.goto(0,0)

#red spiral
t.color("red")
for i in range(60):
    t.forward(20+i)
    t.left(45)

#orange spiral
t.color("orange")
for i in range (60):
    t.forward(20+i)
    t.left(45)

    t.penup()
    t.goto(-100,70)
    t.pendown()

#blue star thing
    t.color("blue")
for i in range (60):
    t.forward(20+i)
    t.left(45)

#purple spiral
    t.color("purple")
for i in range (30):
    t.forward(20+i)
    t.left(45)

t.penup()
t.goto(-90,-120)
t.pendown()
#yellow spiral
t.color("yellow")
for i in range (60):
    t.forward(20+i)
    t.left(45)


t.penup()
t.goto(130,0)
t.pendown()

#green spiral
t.color("green")
for i in range (60):
    t.forward(20+i)
    t.left(45)

t.penup()
t.goto(170,70)
t.pendown()
#blue spiral
t.color("blue")
for i in range(60):
    t.forward(20+i)
    t.left(45)

turtle.exitonclick()












