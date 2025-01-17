import turtle, time, random

# Section 1 - Variables
x1 =-200
y1 =200
x2 =-200
y2 =100
x3 =-200
y3 =0
x4 =-200
y4 =-10

# Section 2 - Setup
t1 = turtle.Turtle()
t1.penup()
t1.goto(x1,y1)
t2 = turtle.Turtle()
t2.penup()
t2.goto(x2,y2)
t3 = turtle.Turtle()
t3.penup()
t3.goto(x3,y3)
t4 = turtle.Turtle()
t4.penup()
t4.goto(x4,y4)


# Section 3 - change variables 
for i in range(10):
	x1 +=random.randint(1,50)
	x2 +=random.randint(1,50)
	x3 +=random.randint(1,50)
	x4 +=random.randint(1,50)

	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.01)

# Section 4 -
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("turtle 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("turtle 2 wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
	print("turtle 3 wins!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
	print("turtle 4 wins!")
    

turtle.exitonclick()