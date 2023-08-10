import turtle

class ScoreBoard(turtle.Turtle):

	def __init__(self, x_pos):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.goto(x_pos, 180)
		self.color("white")
		self.score = 0
		self.score_update()	
	
	def score_update(self):
		self.score += 1
		self.clear()
		self.write(f"{self.score}", True, align="center", font=("courier", 80, "normal"))
