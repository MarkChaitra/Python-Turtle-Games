import turtle  
import time     #To have delay in movement
import random   #To have random food placements

#Setup screen
window = turtle.Screen()
window.title("Snake by @MarkChaitra")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

#Creates the snakes head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

body = []
delay = 0.1

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.goto(250,250)

#Score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

#Current score
score = 0
#Highest score
high = 0

#Snakes constant movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#User inputted movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_right, "d")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")

while True:
    window.update()

    #Checks borders
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:        
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        food.goto(0,100)

        #Moves body out of the screen
        for bodys in body:
            bodys.goto(700,700)

        #Clears the array
        body.clear()

        #Resets score
        score = 0

        #Rewrites score board
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high), align="center", font=("Courier", 24, "normal"))

    #Checks if the head eats the food
    if head.distance(food) < 15: 

        #Gets random x and y values and places the food there
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x, y)

        #Creates a new snakes body and adds to the array
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()    
        body.append(new_segment)

        #Adds points to score
        score += 10

        #Replaces high with score if higher
        if score > high:
            high = score
        
        #Rewrites score board
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high), align="center", font=("Courier", 24, "normal"))

    #Constantly moves the body segments to the segment infront 
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)

    #Constantly moves the first body segment to the heads x and y values
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    #Snakes contant movement
    move() 

    #Checks if head touches any body segment
    for bodys in body:
        if bodys.distance(head) < 15:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            food.goto(0,100)

            #Moves segments off of the screen
            for bodys in body:
                bodys.goto(700,700)

            #Clears the array
            body.clear()

            #Resets score
            score = 0

            #Rewrites score board
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay) 
