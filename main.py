import turtle
import pads
import scoreboard
import time
import ball

screen = turtle.Screen()
screen.listen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

left_pad = pads.Paddle((-370, 0))

right_pad = pads.Paddle((370, 0))
left_score = scoreboard.ScoreBoard(-200)
right_score = scoreboard.ScoreBoard(200)
ball = ball.Ball()

screen.update()

screen.listen()

screen.onkey(key="w", fun=left_pad.up)

screen.onkey(key="s", fun=left_pad.down)

screen.onkey(key="Up", fun=right_pad.up)

screen.onkey(key="Down", fun=right_pad.down)

move_speed = 0.1

while(True):
	screen.update()
	ball.move()
	time.sleep(move_speed)

	#wall detection & bouncing functionality

	if(ball.ycor() > 280 or ball.ycor()  < -280):
		ball.bounce()

	#paddle collision and bouncing mechanism

	if(ball.distance(right_pad) < 50 and ball.xcor() > 340):
		ball.bounceBack()
		move_speed *= 0.9
	elif(ball.distance(left_pad) < 50 and ball.xcor() < -340):
		ball.bounceBack()
		move_speed *= 0.9

	#scoring functionality

	if(ball.xcor() > 390):
		left_score.score_update()
		ball.ballReset()
		ball.bounceBack()
		move_speed = 0.1
	elif(ball.xcor() < -390):
		right_score.score_update()
		ball.ballReset()
		ball.bounceBack()
		move_speed = 0.1

screen.exitonclick()
