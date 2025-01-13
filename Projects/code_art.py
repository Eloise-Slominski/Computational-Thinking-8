import turtle

t = turtle.Turtle()

t.goto(-15, 15)

#blue and pink star
colors=["pink","blue"]
for i in range(20):
    t.color(colors[i%2])
    t.forward(15+14)
    t.left(144+1)

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

turtle.exitonclick()












