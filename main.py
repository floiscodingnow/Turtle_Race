from turtle import  Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt ="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100

for index_number in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_position)
    tim.color(colors[index_number])
    y_position = y_position + 40


screen.exitonclick()
