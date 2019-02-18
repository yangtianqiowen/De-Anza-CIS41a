time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))
if time2 < time1 : 
   time2= time2 + 2360 
difference = time2 - time1
hours = difference // 100
mintues = difference % 100
print(hours, "hours", mintues, "mintues")

import turtle
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)
turtle.done()