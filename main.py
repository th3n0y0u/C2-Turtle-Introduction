import turtle
# "Turtle" Class

turtle.shape("turtle")
turtle.color("red")

turtle.speed(10) 
turtle.pensize(5)
#turtle.shapesize(10, 10, 10);

turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(100):
  turtle.right(10)
  turtle.forward(15)
turtle.end_fill()

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.circle(100)
turtle.clear()

pro = turtle.Turtle()
pro.shape("turtle")
pro.penup()
pro.forward(200)
pro.pendown()

pro.fillcolor("brown")
pro.begin_fill()
for i in range(4):
  pro.right(90)
  pro.forward(100)
pro.end_fill()
pro.fillcolor("gray")
pro.begin_fill()
pro.left(135)
pro.forward(75)
pro.left(90)
pro.forward(75)
pro.end_fill()
pro.penup()
pro.left(45)
pro.forward(100)
pro.left(90)
pro.forward(50)
pro.left(90)
pro.pendown()
pro.fillcolor("white")
pro.begin_fill()
for i in range(3):
  pro.forward(25)
  pro.right(90)
  pro.forward(12.5)
  pro.right(90)
pro.end_fill()
pro.forward(12.5)
pro.right(90)
pro.forward(1)
pro.circle(0.5)