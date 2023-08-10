import turtle

class Ball(turtle.Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.xmove = 10
		self.ymove = 10

	def move(self):
		x_cor = self.xcor() +  self.xmove
		y_cor = self.ycor() + self.ymove
		self.goto(x_cor, y_cor)

	def bounce(self):
		self.ymove = (-1) * self.ymove

	def bounceBack(self):
		self.xmove = (-1) * self.xmove

	def ballReset(self):
		self.goto(0,0)
		