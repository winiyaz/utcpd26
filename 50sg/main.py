# Game work is being done here
import turtle

import pandas as pd

from getcor import get_mouse_click_corr

# Screen Setup
scr = turtle.Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("USBootyMap")
img = "bsg.gif"
scr.addshape(img)
turtle.shape(img)

# Loading the data into a datframe
data = pd.read_csv('s50.csv')
all_states = data.state.to_list()
gues = []

while len(gues) < 50:

	# Setting dialog
	ans = scr.textinput(title=f"{len(gues)}/50 StateCorrect", prompt="WhichFlavor").title()
	print(ans)

	# Logic with data from the dataframe
	if ans == "Exit":
		miss = []
		for s in all_states:
			if s not in gues:
				miss.append(s)
		print(f'Missed = {len(miss)}')  # Missed States
		print(miss)
		new_data = pd.DataFrame(miss)
		new_data.to_csv("bastard.csv")
		break
	if ans in all_states:
		gues.append(ans)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		t.color("#facc15")
		state_data = data[data.state == ans]
		t.goto(state_data.x.item(), state_data.y.item())
		t.write(state_data.state.item())

# --- Project Setup ---
# Getting the coordinates in the image
getMouseClick = get_mouse_click_corr  # This already done  s50.csv
# Using Main loop
# scr.exitonclick()
# turtle.mainloop()
