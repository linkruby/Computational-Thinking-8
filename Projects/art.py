# ###############################################
# ### SETUP ###
import turtle
# ###############################################
background = ("black")
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t3.goto(0,0)
t5.goto(0,0)
t4.goto(0,0)
t2.goto(0,0)
t4.speed(100)
t3.speed(100)
t.speed(100)
t5.speed(100)
t.penup()
t.goto(0,0)
t.color("red")
t.pendown()
t2.speed (100)
turtle.bgcolor("black")
colors = ["blue","purple"]
colors2 = ["purple","blue"]




# first turtle

for i in range (500):
    t.color ( colors [ i % 2] )  
    t.forward(50 + i - 10)
    t.left(60 + 1 )


# second turtle

for i in range (500): 
    t2.forward(40 + i - 5)
    t2.left(60 + 1)
    t2.color( "red" )

# third turtle

for i in range (500):
    t3.color ( colors2 [ i % 2] )  
    t3.forward( 30 + i )
    t3.left(60 + 1 )

# fourth turtle

for i in range (500): 
    t4.forward(20 + i + 10)
    t4.left(60 + 1)
    t4.color( "white" )






# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ################################################



#t.penup()
#t.goto(100,0)

###  t.right(60 + 1)
   # t.color( "white" )