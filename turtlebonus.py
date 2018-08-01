import turtle
def up():
    turtle.setheading(0)
    turtle.forward(10)
def down():
    turtle.setheading(180)
    turtle.forward(10)
def right():
    turtle.setheading(90)
    turtle.forward(10)
def left():
    turtle.setheading(270)
    turtle.forward(10)
    
turtle.onkeypress(up,'d')
turtle.onkeypress(down,'a')
turtle.onkeypress(right,'w')
turtle.onkeypress(left,'s')
turtle.listen() 

turtle.mainloop()

