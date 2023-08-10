import turtle

class Paddle(turtle.Turtle):
	def __init__(self, position):
		super().__init__()
		self.color("white")
		self.shape("square")
		self.speed("fastest")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position)

	def up(self):
		y_cor = self.ycor()
		self.goto(self.xcor(), y_cor + 30)		

	def down(self):
		y_cor = self.ycor()
		self.goto(self.xcor(), y_cor - 30)		
		
	def stop(self):
		self.forward(0)				
	
