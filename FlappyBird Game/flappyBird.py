import turtle
import time
import random

#Setup screen
window = turtle.Screen()
window.title("Flappy Bird by @MarkChaitra")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

#Bird
Bird = turtle.Turtle()
Bird.shape("triangle")
Bird.color("yellow")
Bird.shapesize(stretch_wid=1, stretch_len=1)
Bird.penup()
Bird.goto(-200,0)

Score = 0
highScore = 0

#ScoreBoard
ScoreBoard = turtle.Turtle()
ScoreBoard.speed(0)
ScoreBoard.color("white")
ScoreBoard.penup()
ScoreBoard.hideturtle()
ScoreBoard.goto(0, 280)
ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))

pipes_top = []
pipes_bottom = []
hit = False

def fly():
    global Fall_Rate, hit

    if hit == False:
        Bird.sety(Bird.ycor()+40)
        Fall_Rate = 0
        Bird.setheading(60)

Fall_Rate = 0
def fall():
    global Fall_Rate
    if Bird.ycor() > -320:
        Bird.sety(Bird.ycor()-Fall_Rate)
        Fall_Rate += 3
        Bird.right(8)
    window.ontimer(fall, 100)

def make_pipes():
    global pipes_top, pipes_bottom

    if hit == False:

        x = random.randint(10,40)
        pipeT = turtle.Turtle()
        pipeT.shape("square")
        pipeT.color("green")
        pipeT.shapesize(stretch_wid=x, stretch_len=2)
        pipeT.penup()
        pipeT.goto(300,310)
        pipes_top.append(pipeT)

        pipeB = turtle.Turtle()
        pipeB.shape("square")
        pipeB.color("green")
        pipeB.penup()
        pipeB.goto(300,-310)
        pipeB.shapesize(stretch_wid=60-x-12, stretch_len=2)
        pipes_bottom.append(pipeB)

    window.ontimer(make_pipes, 4000)

def reset():

    global pipes_top, pipes_bottom, Score, hit, Fall_Rate

    for pipeT, pipeB in zip(pipes_top[:], pipes_bottom[:]):
                pipes_top.remove(pipeT)
                pipeT.hideturtle()
                pipes_bottom.remove(pipeB)
                pipeB.hideturtle()  

    
    Bird.goto(-200, 0)
    Score = 0
    hit = False
    Fall_Rate = 0
    Bird.setheading(0)

window.listen()
window.onkeypress(fly, "space")
window.ontimer(fall, 0)
window.ontimer(make_pipes, 0)

while True:
    window.update()

    for pipeT, pipeB in zip(pipes_top, pipes_bottom):

        W_T, L_T, _ = pipeT.shapesize()
        W_B, L_B, _ = pipeB.shapesize()
        Birdx, Birdy = Bird.pos()

        if Birdx > pipeT.xcor()-(L_T*10)-10 and Birdx < pipeT.xcor()+(L_T*10)+10 and Birdy > 300-(10*W_T) and Birdy < 300+(10*W_T) or Birdx > pipeB.xcor()-(L_B*10)-10 and Birdx < pipeB.xcor()+(L_B*10)+10 and Birdy < -300+(10*W_B) and Birdy > -300-(10*W_B) or Birdy > 310 or Birdy < -310:
            hit = True

        if hit == False:

            if pipeT.xcor() < -320:
                pipes_top.remove(pipeT)
                pipeT.hideturtle()
                pipes_bottom.remove(pipeB)
                pipeB.hideturtle()  

                Score +=1
                highScore = Score if highScore < Score else highScore
            else:
                pipeT.setx(pipeT.xcor()-1)
                pipeB.setx(pipeB.xcor()-1)    
        else:

            window.ontimer(reset, 2000)            

        ScoreBoard.clear()
        ScoreBoard.write("Score: {}   High Score: {}".format(Score, highScore), align="center", font=("Courier", 15, "normal"))





