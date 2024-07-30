# Function is for generating a text file with random numbers in a single line

import random


def gen_random_number(filename):
	# Generate a list of 20 random numbers between 0 and 200
	numbers = [random.randint(0, 200) for _ in range(20)]

	# Write the numbers to a text file, with each number on a new line
	with open(filename + '.txt', 'w') as f:
		for number in numbers:
			f.write(str(number) + '\n')

# Calling the function

gen_random_number("f1")
gen_random_number("f2")