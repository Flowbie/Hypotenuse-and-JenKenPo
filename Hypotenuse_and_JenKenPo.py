# Dolan, Austin
# ICS 110P Assignment 05
# September 29, 2022
# This program asks a user to choose between 2 options: finding a hypotenuse of a triangle with a right angle or playing JenKenPo against my program

import math
import random
play = True
user_choice = 0

# Welcome user to my program, ask their name, and which part of my program they want to use
user_name = input("Hello, welcome to my program! What's your name?\n")
try:
	user_choice = int(input(f"Thanks for trying my program {user_name}, it can do two things:\n  1. Find the hypotenuse of a right triangle\n  2. Play JenKenPo\nWhich would you like to do? (Enter 1 or 2)\n"))

except ValueError as e:
	print("So far my program only has 2 options\nCome back next semester and it might have more!")
	print("Error: ")
	print(e)

# If user enters 1 they will use the pythagrean theorem to find the hypotnuse of a right triangle
if user_choice == 1:
	print(f"{user_name}, you chose to find the hypotenuse of a right angle.")
	print("If you give me the length of the base and height of a triangle I can tell you the hypotenuse.")
	# Loop program
	while play == True:
		try:
			# Take input from user: length of base, and length of height of triangle to output hypotenuse
			side_one = float(input("Length of base: "))
			side_two = float(input("Length of height: "))
			side_three = math.sqrt(side_one**2 + side_two**2)
			print(f"The hypotenuse of a right triangle with a base of {side_one} and height of {side_two} is {side_three}.")
			# Loop program to ask user if they want to run another evaluation
			play_again = input("Evaluate another hypotenuse?: (enter or type q to quit)")
			play_again = play_again.lower()
			if play_again == "q":
				play = False
			else:
				play = True
		# Accept error from user if they enter a string or char into side_one or side_two instead of an int or float
		except ValueError as e:
			print("That is not a valid number. Please try again")
			print("Error:")
			print(e)

# If user enters 2 they will play against my program in JenKenPo
elif user_choice == 2:
	print(f"{user_name}, you chose to play JenKenPo. Make a choice of either Rock, Paper, or Scissors where paper beats rock, scissors beat paper, and rock beats scissors.\n")
	# Loop program
	while play == True:
		# Take input from user rock, paper, or scissors to play against my randomly generated move
		user_move = input("What is your choice? (type R for rock, P for paper, or S for Scissors)\n")
		user_move = user_move.upper()
		# Check to make sure user enters R, P, or S else say move isn't valid
		if user_move != "R" and user_move != "P" and user_move != "S":
			print("Your move isn't valid!")
		else:
			# Assign comp_move random value between 0-2 to represent R, P, and S
			comp_move = random.randint(0,2)
			opponent_move = ()
			if comp_move == 0:
				opponent_move = "R"
			elif comp_move == 1:
				opponent_move = "P"
			else:
				opponent_move = "S"
			print(f"Opponent move: {opponent_move}")

			# Calculate if the user won, lost, or tied and loop to ask if they want to play again
			if user_move == opponent_move:
				print("You tied!")
				play_again = input("Play again: (enter or type q to quit)")
				play_again = play_again.lower()
				if play_again == "q":
					play = False
				else:
					play = True
			elif (user_move == "R" and opponent_move == "S") or (user_move == "S" and opponent_move == "P") or (user_move == "P" and opponent_move == "R"):
				print("You won!")
				play_again = input("Play again: (enter or type q to quit)")
				if play_again == "q":
					play = False
				else:
					play = True
			else:
				print("You lost!")
				play_again = input("Play again: (enter or type q to quit)")
				if play_again == "q":
					play = False
				else:
					play = True
else:
	print("Invalid input. Please enter only 1 or 2")
print("Thank's for playing!")




