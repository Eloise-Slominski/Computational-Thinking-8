# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(30, -100)
t.color("purple")
t.pendown()


# square
for i in range(4):
    t.forward(100)
    t.right(90)



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
