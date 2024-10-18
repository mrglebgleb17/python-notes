#py0ch11
#turtle graphics
#what if we wanted to draw shapes, or make a simple interface in python? well, we can use turtle!
#turtle is a graphics module that helps you make (mostly) dawings and games
import turtle as t #this allows us to use turtle graphics,but as "t" instead of typing out turtle each time
s=t.getscreen()#opens the screen
t.shape("turtle")
t.speed("slowest")
t.forward(100)#moves the turtle 100 pixels
t.right(90)#turns 90 degrees right
#one way to make a square is the following
'''t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)'''
#we can also do this:
for i in range(4):
    t.color("red")#you can also use hexadecimal colors for this
    t.forward(50)
    t.right(90)
    
t.penup()#make sure we wont draw anything
t.right(180)
t.forward(200)
t.pendown()
t.circle(50)#makes a cicle with 50 pixles radius
    
