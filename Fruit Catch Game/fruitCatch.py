import turtle
import random

#Setup screen
window = turtle.Screen()
window.title("Fruit Catch by @MarkChaitra")
window.bgcolor("blue")
window.setup(width=500, height=500)
window.tracer(0)

#Ground
Ground = turtle.Turtle()
Ground.shape("square")
Ground.color("green")
Ground.shapesize(stretch_wid=3, stretch_len=25)
Ground.penup()
Ground.goto(0,-210)

#Basket
Basket = turtle.Turtle()
Basket.shape("square")
Basket.color("brown")
Basket.shapesize(stretch_wid=2, stretch_len=3)
Basket.penup()
Basket.goto(0,-170)

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
    if left == True and Basket.xcor() > -225:
        x = Basket.xcor()
        y = Basket.ycor()
        Basket.goto(x-5,y)
    elif right == True and Basket.xcor() < 225:
        x = Basket.xcor()
        y = Basket.ycor()
        Basket.goto(x+5,y)

Fruits = []
Bombs = []
    
window.listen()
window.onkeypress(go_left, "a")
window.onkeyrelease(stop_left, "a")
window.onkeypress(go_right, "d")
window.onkeyrelease(stop_right, "d")


while True:
    window.update()

    move()

    x = random.randint(0,100)
    b = random.randint(0,500)

    if x < 5:  
        fruit = turtle.Turtle()
        fruit.shape("square")
        fruit.color("red")
        fruit.shapesize(stretch_wid=0.7, stretch_len=0.7)
        fruit.penup()
        fruit.goto(random.randint(-220, 220), 250)
        Fruits.append(fruit)

    if b < 10:
        bomb = turtle.Turtle()
        bomb.shape("square")
        bomb.color("black")
        bomb.shapesize(stretch_wid=0.7, stretch_len=0.7)
        bomb.penup()
        bomb.goto(random.randint(-220, 220), 250)
        Bombs.append(bomb)

    for fruit in Fruits[:]:
        fruit.goto(fruit.xcor(), fruit.ycor()-3)

        if fruit.ycor() < -250:
            fruit.goto(500,500)
            Fruits.remove(fruit)
 

        if fruit.xcor() > Basket.xcor()-30 and fruit.xcor() < Basket.xcor()+30 and fruit.ycor() > Basket.ycor()-20 and fruit.ycor() < Basket.ycor()+20:
            fruit.goto(500,500)
            Fruits.remove(fruit)

            Score+=1

            highScore = Score if Score > highScore else highScore
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))



    for bomb in Bombs[:]:
        bomb.goto(bomb.xcor(), bomb.ycor()-8)

        if bomb.ycor() < -250:
            bomb.goto(500,500)
            Bombs.remove(bomb)

        if bomb.xcor() > Basket.xcor()-30 and bomb.xcor() < Basket.xcor()+30 and bomb.ycor() > Basket.ycor()-20 and bomb.ycor() < Basket.ycor()+20:
            
            for fruit in Fruits[:]:
                fruit.goto(500,500)
            Fruits.clear()

            for bomb in Bombs[:]:
                bomb.goto(500,500)
            Bombs.clear()

            Score = 0
            ScoreBoard.clear()
            ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

            Basket.goto(0,-170)
            
            continue







