import turtle

n = -200
o = -100


turtle.penup()
turtle.goto(n,o)
turtle.pendown()
turtle.pencolor('red')
turtle.goto(n,o+100)
turtle.goto(n+100,o+100)
turtle.goto(n+100,o)
turtle.goto(n,o)
turtle.penup()

turtle.mainloop()
