import turtle
import time
import random

#Setup screen
window = turtle.Screen()
window.title("Space Invader by @MarkChaitra")
window.bgcolor("black")
window.setup(width=500, height=500)
window.tracer(0)

#Ship
Ship = turtle.Turtle()
Ship.shape("triangle")
Ship.left(90)
Ship.color("brown")
Ship.shapesize(stretch_wid=1, stretch_len=1)
Ship.penup()
Ship.goto(0,-180)

Score = 0
highScore = 0

#ScoreBoard
ScoreBoard = turtle.Turtle()
ScoreBoard.speed(0)
ScoreBoard.color("white")
ScoreBoard.penup()
ScoreBoard.hideturtle()
ScoreBoard.goto(0, 220)
ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

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
    if left == True and Ship.xcor() > -240:
        x = Ship.xcor()
        y = Ship.ycor()
        Ship.goto(x-5,y)
    elif right == True and Ship.xcor() < 240:
        x = Ship.xcor()
        y = Ship.ycor()
        Ship.goto(x+5,y)

bullets = []
enemyShips = []
enemyBullets =[]

def shoot():
        bullet = turtle.Turtle()
        bullet.shape("square")
        bullet.color("red")
        bullet.shapesize(stretch_wid=0.4, stretch_len=0.4)
        bullet.penup()
        bullet.goto(Ship.xcor(), Ship.ycor())
        bullets.append(bullet)

def on_close():
    global Run
    Run = False

window.listen()
window.onkeypress(go_left, "a")
window.onkeyrelease(stop_left, "a")
window.onkeypress(go_right, "d")
window.onkeyrelease(stop_right, "d")
window.onkeypress(shoot, "space")

window._root.protocol("WM_DELETE_WINDOW", on_close)

Run = True
while Run:
    window.update()

    move()

    # Chance of enemy ship creation
    x = random.randint(0,100)
    if x < 2:
        enemyShip = turtle.Turtle()
        enemyShip.shape("triangle")
        enemyShip.right(90)
        enemyShip.color("green")
        enemyShip.shapesize(stretch_wid=1, stretch_len=1)
        enemyShip.penup()
        enemyShip.goto(random.randint(-220,220),250)
        enemyShips.append(enemyShip)

    # Move enemy ships forward to the certain point, chance of enemy bullet being created
    for enemyShip in enemyShips[:]:
        if enemyShip.ycor() > 50:
            enemyShip.goto(enemyShip.xcor(), enemyShip.ycor()-0.5)

        if random.randint(0,200) < 1:
            enemybullet = turtle.Turtle()
            enemybullet.shape("square")
            enemybullet.color("green")
            enemybullet.shapesize(stretch_wid=0.4, stretch_len=0.4)
            enemybullet.penup()
            enemybullet.goto(enemyShip.xcor(), enemyShip.ycor())
            enemyBullets.append(enemybullet)

    # Remove off screen enemy bullets, reset if enemy bullet hits player, or move enemy bullet down
    for enemybullet in enemyBullets[:]:
        if enemybullet.ycor() < -250:
            enemyBullets.remove(enemybullet)
            enemybullet.hideturtle()
            continue
        elif enemybullet.distance(Ship) < 12:
            Ship.goto(0,-180)

            for bullet in bullets[:]:
                bullet.goto(500,500)
                del bullet
            for enemybullet in enemyBullets[:]:
                enemybullet.goto(500,500)
                del enemybullet
            for enemyShip in enemyShips[:]:
                enemyShip.goto(500,500)
                del enemyShip

            bullets.clear()
            enemyBullets.clear()
            enemyShips.clear()
            Score = 0
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))
            time.sleep(1)
            break
        else:
            enemybullet.goto(enemybullet.xcor(), enemybullet.ycor()-4)


    # Remove off screen player bullets, remove bullet and enemy ship if hit
    for bullet in bullets[:]:

        bullet.goto(bullet.xcor(), bullet.ycor()+4)

        if bullet.ycor() > 260:
            bullet.hideturtle()
            bullets.remove(bullet)
            continue
        else:
            for enemyShip in enemyShips[:]:
                if enemyShip.distance(bullet) < 12:
                    enemyShip.goto(500,500)
                    enemyShips.remove(enemyShip)

                    Score +=1
                    highScore = Score if Score > highScore else highScore
                    ScoreBoard.clear()
                    ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

                    bullet.goto(500,500)
                    bullets.remove(bullet)

                    break
