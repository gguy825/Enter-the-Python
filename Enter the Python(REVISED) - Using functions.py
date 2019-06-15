import time

def welcome_message():
	"""welcome message and prompt"""
	print("Welcome to Enter the Python. ")
	input("\nPress 'enter' to continue. ")
	intro()

def intro():
	"""displays intro"""
	print("\n\nHello. ")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("\nThis is your last chance. After this... ")
	time.sleep(1)
	print("there is no turning back. ")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)
	yes_or_no()

def yes_or_no():
	"""continue to the rabbit hole"""
	yes_no1 = input("\nShall we continue? (yes or no) ")
	return first_choice(yes_no1)

def first_choice(yes_no1):
	"""first yes no choice into learning the way of the python"""
	if yes_no1 == 'yes':
		print("\nGood choice")
		time.sleep(1)
		final_test()
	if yes_no1 == 'no':
		print("\nThen I have nothing more to show you. \n")
		time.sleep(1)
		print("....")
		time.sleep(1)
		print("....")
		time.sleep(1)
		print("\nsignal lost....")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0) # will exit when user presses enter

def final_test():
	"""this is where the user chooses the snake"""
	print("\nNow on to the final test. ")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("\nIf you get bit by the blue snake, the story ends.")
	time.sleep(1)
	print("You wake up in your bed and believe whatever you want to believe.\n")
	time.sleep(1)
	print("....\n")
	time.sleep(1)
	print("But if you get bit by the yellow snake, you stay in Wonderland, ")
	time.sleep(1)
	print("and I show you how deep the console hole goes.... ")
	time.sleep(1)
	snake_juice()

def snake_juice():
	"""blue snake or yellow snake choice?"""
	snake = input("\nBlue or yellow? ")
	return blue_yellow(snake)

def blue_yellow(snake):
	"""choices of the blue or yellow snake"""
	if snake == 'blue':
		print("\nYou wake up in your bed.... ")
		time.sleep(1)
		print("believing whatever you want to believe....")
		time.sleep(1)
		print("\nsignal lost....")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0) # will exit when user presses enter
	if snake == 'yellow':
		print("\nHere is the truth. ")
		time.sleep(1)
		print("Nothing more. ")
		time.sleep(1)
		print("Nothing less.")
		time.sleep(1)
		truth_exe()

def truth_exe():
	"""making the choice to accept the truth or to run"""
	the_truth = input("\nAccept or run? ")
	return truth_choice(the_truth)

def truth_choice(the_truth):
	"""the options for the truth"""
	if the_truth == 'accept':
		print('....')
		time.sleep(1)
		print('\nconnection to python.org established')
		time.sleep(1)
		print('....')
		time.sleep(0.8)
		print('....')
		time.sleep(0.5)
		print('downloading TheTruth.py.jpg.exe')
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		play_again_choice() 
	if the_truth == 'run':
		print("Goodbye. ")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0) # will exit when user presses enter

def play_again_choice():
	"""yes or no thing for the user"""
	yes_no2 = input("\nShall we go again? (yes or no) ")
	return play_again_loop(yes_no2)

def play_again_loop(yes_no2):
	"""asking users if they want to play again or wake up (quit the program)"""
	if yes_no2 == 'yes':
		print("\nGood choice.\n ")
		time.sleep(1)
		print("\nreconnecting....")
		time.sleep(1)
		print("\nreconnecting....")
		time.sleep(0.5)
		print("\nconnection successful")
		time.sleep(1)
		welcome_message() # will go back to the start of the game
	if yes_no2 == 'no':
		print("\nGoodbye. ")
		time.sleep(1)
		print("\nsignal lost....")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0) # finishes

welcome_message()