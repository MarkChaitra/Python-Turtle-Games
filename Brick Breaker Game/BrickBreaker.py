import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Brick Breaker by @MarkChaitra")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player turtle
player = turtle.Turtle()
player.shape("square")
player.shapesize(1,5)
player.color("white")
player.penup()
player.goto(0, -250)
player_H, player_L, _= player.shapesize()

brick_x = [-250, -150, -50, 50, 150, 250]
brick_y = [250, 150, 50]
brick_colour = ["red", "blue", "white"]
bricks = []
brick_H, brick_L = 5, 5
broken = 0

for i in range(len(brick_y)):
    for x in brick_x:
        brick = turtle.Turtle()
        brick.shape("square")
        brick.shapesize(4.8,4.8)
        brick.color(brick_colour[i])
        brick.penup()
        brick.goto(x, brick_y[i])
        bricks.append(brick)

# Create ball turtle
ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(1,1)
ball.color("white")
ball.penup()
ball.goto(0,-10)

ball_x = 4
ball_y = -4

left = False
right = False

def go_left():
    global left
    left = True
def stop_left():
    global left
    left = False
def go_right():
    global right
    right = True
def stop_right():
    global right
    right = False
def move():
    global left, right
    if left == True and player.xcor() > -250:
        x = player.xcor()
        y = player.ycor()
        player.goto(x-5,y)
    elif right == True and player.xcor() < 250:
        x = player.xcor()
        y = player.ycor()
        player.goto(x+5,y)

def move_ball():
    global broken

    if broken != 18:
        ball.setx(ball.xcor() + ball_x)
        ball.sety(ball.ycor() + ball_y)
        screen.ontimer(move_ball, 20)
def reset():
    global brick, bricks, broken, ball_x, ball_y
    for brick in bricks[:]:
        brick.showturtle()
        if brick.ycor() == 250: brick.color("red") 
        elif brick.ycor() == 150: brick.color("blue") 
        else: brick.color("white") 
    
    ball_x = 4
    ball_y = -4

    player.setx(0)
    broken = 0
    ball.goto(0,-10)

screen.listen()
screen.onkeypress(go_left, "a")
screen.onkeyrelease(stop_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeyrelease(stop_right, "d")
screen.ontimer(move_ball, 2000)

while True:
    screen.update()
    move()

    if ball.ycor() > 290:
        ball.sety(290)
        ball_y*= -1
    elif ball.xcor() < -290:
        ball.setx(-290)
        ball_x*= -1
    elif ball.xcor() > 290:
        ball.setx(290)
        ball_x*= -1

    if ball.xcor() > player.xcor()-player_L*10 and ball.xcor() < player.xcor()+player_L*10 and ball.ycor() > player.ycor()-player_H*10 and ball.ycor() < player.ycor()+player_H*10:
        ball.sety(player.ycor()+player_H*10)
        ball_y*= -1

    for brick in bricks[:]:

        if brick.isvisible() == True and ball.xcor() > brick.xcor()-50 and ball.xcor() < brick.xcor()+50 and ball.ycor() > brick.ycor()-50 and ball.ycor() < brick.ycor()+50:
            
            if ball.ycor() < brick.ycor()+60 and ball.ycor() > brick.ycor()+40:
                ball_y*= -1
            if ball.ycor() > brick.ycor()-60 and ball.ycor() < brick.ycor()-40:
                ball_y*= -1
            if ball.xcor() > brick.xcor()-60 and ball.xcor() < brick.xcor()-40:
                ball_x*= -1
            if ball.xcor() < brick.xcor()+60 and ball.xcor() > brick.xcor()+40:
                ball_x*= -1

            if brick.color()[0] == "red":
                brick.color("blue")
            elif brick.color()[0] == "blue":
                brick.color("white")
            else:
                brick.hideturtle()
                broken+=1

    if broken == 18 or ball.ycor() < -300:
        reset()

    


