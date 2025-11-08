import turtle
import math
import random

#Setup screen
window_width, window_length = 500, 500
window = turtle.Screen()
window.title("Tanks by @MarkChaitra")
window.bgcolor("blue")
window.setup(width=window_width, height=window_length)
window.tracer(0)

playerA_healthCount = 3
#playerA_health
playerA_health = turtle.Turtle()
playerA_health.speed(0)
playerA_health.color("white")
playerA_health.penup()
playerA_health.hideturtle()
playerA_health.goto(-((window_length/2)-20), ((window_length/2)-30))
playerA_health.write("Health: {}".format(playerA_healthCount), align="left", font=("Courier", 15, "normal"))

playerB_healthCount = 3
#playerB_health
playerB_health = turtle.Turtle()
playerB_health.speed(0)
playerB_health.color("white")
playerB_health.penup()
playerB_health.hideturtle()
playerB_health.goto((window_length/2)-20, (window_length/2)-30)
playerB_health.write("Health: {}".format(playerB_healthCount), align="right", font=("Courier", 15, "normal"))

# Ground
Ground = turtle.Turtle()
Ground.shape("square")
Ground.color("green")
Ground.penup()
Ground.shapesize(stretch_wid=10, stretch_len=25)
Ground.goto(0, -200)

# Wall
Wall = turtle.Turtle()
Wall.shape("square")
Wall.color("black")
Wall.penup()
Wall.shapesize(stretch_wid=random.randint(25,35), stretch_len=3)
Wall.goto(0, -250)

# Create bullet turtle
playerA = turtle.Turtle()
playerA.shape("square")
playerA.color("orange")
playerA.penup()
playerA.shapesize(stretch_wid=1, stretch_len=2)
playerA.goto(random.randint(-230,-90), -100)
playerA_cannon = turtle.Turtle()
playerA_cannon.shape("square")
playerA_cannon.color("black")
playerA_cannon.penup()
playerA_cannon.shapesize(stretch_wid=0.5, stretch_len=1.5)
playerA_cannon.goto(playerA.xcor()+15, playerA.ycor()+10)
playerA_cannon.left(50)

playerB = turtle.Turtle()
playerB.shape("square")
playerB.color("red")
playerB.penup()
playerB.shapesize(stretch_wid=1, stretch_len=2)
playerB.goto(random.randint(90,230), -100)
playerB_cannon = turtle.Turtle()
playerB_cannon.shape("square")
playerB_cannon.color("black")
playerB_cannon.penup()
playerB_cannon.shapesize(stretch_wid=0.5, stretch_len=1.5)
playerB_cannon.goto(playerB.xcor()-15, playerB.ycor()+10)
playerB_cannon.left(150)

playerA_turn = True
player = playerA 
player_cannon = playerA_cannon

# Bullet
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
bullet.color("white")
bullet.penup()
bullet.goto(400,400)
# Physics constants
gravity = 0.5
initial_velocity = 18
angle_deg = playerA_cannon.heading()
angle_rad = math.radians(angle_deg)
# Starting values
time = 0
x0, y0 = bullet.pos()

'''
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
    global left, right, player, player_cannon
    if left == True and player.xcor() > -230:
        x = player.xcor()
        player.setx(x-2)
        player_cannon.setx(player_cannon.xcor()-2)
    elif right == True and player.xcor() < 230:
        x = player.xcor()
        player.setx(x+2)
        player_cannon.setx(player_cannon.xcor()+2)
'''

def cannon_up():
    global angle_rad, player_cannon, time

    if time <=0:
        player_cannon.left(2)
        angle_rad = math.radians(player_cannon.heading())
def cannon_down():
    global angle_rad, player_cannon, time
    if time <= 0 and (player_cannon.heading() > 0 or player_cannon.heading() < 180):
        player_cannon.right(2)
        angle_rad = math.radians(player_cannon.heading())

def shoot():

    global time, x0, y0, player_cannon, angle_rad

    if time <= 0:
        bullet.goto(player_cannon.xcor(),player_cannon.ycor())
        bullet.setheading(player_cannon.heading())
        bullet.forward(15)
        angle_rad = math.radians(player_cannon.heading())
        x0, y0 = bullet.pos()

        jump()

def jump():
    global time, x0, y0, player, player_cannon, angle_rad, playerA_healthCount, playerB_healthCount

    time += 0.1

    # Calculate new position
    x = x0 + initial_velocity * math.cos(angle_rad) * time * 10
    y = y0 + (initial_velocity * math.sin(angle_rad) * time * 10 - 0.5 * gravity * (time * 10) ** 2)

    bullet.goto(x, y)

    enemy_player = playerA if player == playerB else playerB
    player_W, player_L, _ = enemy_player.shapesize()
    player_x, player_y = enemy_player.pos() 
    Wall_W, Wall_L, _ = Wall.shapesize()
    Wall_x, Wall_y = Wall.pos()

    if x < player_x+player_L*10+5 and x > player_x-player_L*10-5 and y < player_y+player_W*10+5 and y > player_y-player_W*10-5:

        if enemy_player == playerA:
            playerA_healthCount -= 1
        else: 
            playerB_healthCount -= 1
    
        time = 0  # Reset for another jump

        win_check()
        switch_player()
    elif x < Wall_x+Wall_L*10 and x > Wall_x-Wall_L*10 and y < Wall_y+Wall_W*10 and y > Wall_y-Wall_W*10:
        time = 0  # Reset for another jump
        switch_player()
    # Stop if bullet hits ground (or simulate floor)
    elif y > -100:
        window.ontimer(jump, 40)
    else:
        time = 0  # Reset for another jump
        switch_player()

def switch_player():
    global playerA_turn, player, player_cannon
    playerA_turn = not playerA_turn
    player = playerA if playerA_turn == True else playerB
    player_cannon = playerA_cannon if playerA_turn == True else playerB_cannon

    random_placement()

def random_placement():

    bullet.goto(400,400)

    playerA.setx(random.randint(-230,-90))
    playerA_cannon.setx(playerA.xcor()+15)

    playerB.setx(random.randint(90,230))
    playerB_cannon.setx(playerB.xcor()-15)

    Wall.shapesize(stretch_wid=random.randint(25,35), stretch_len=3)

def win_check():
    global playerA_healthCount, playerB_healthCount

    if playerA_healthCount == 0 or playerB_healthCount == 0:
        playerA_healthCount = 3
        playerB_healthCount = 3

    playerA_health.clear()
    playerA_health.write("Health: {}".format(playerA_healthCount), align="left", font=("Courier", 15, "normal"))
        
    playerB_health.clear()
    playerB_health.write("Health: {}".format(playerB_healthCount), align="right", font=("Courier", 15, "normal"))

window.listen()
window.onkeypress(shoot, "space")
#window.onkeypress(go_left, "a")
#window.onkeyrelease(stop_left, "a")
#window.onkeypress(go_right, "d")
#window.onkeyrelease(stop_right, "d")
window.onkeypress(cannon_up, "a")
window.onkeypress(cannon_down, "d")

while True:
    window.update()
    #move()
