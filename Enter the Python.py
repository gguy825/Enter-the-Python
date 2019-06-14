import time
again = True
while again:

	print("Welcome to Enter the Python. ")
	input("\nPress 'enter' to continue. ")

	print("\n\nHello. ")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("\nThis is your last chance. After this... ")
	time.sleep(1)
	print("there is no turning back.")
	time.sleep(1)
	print("....")
	time.sleep(1)
	print("....")
	time.sleep(1)

	yes_no = input("\nShall we continue? (yes or no) ")

	if yes_no == 'yes':
		print("\nGood choice")
		time.sleep(1)
	else:
		print("\nThen I have nothing more to show you. \n")
		time.sleep(1)
		print("....")
		time.sleep(1)
		print("....")
		time.sleep(1)
		print("\nsignal lost....")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0)

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

	# blue is ascii art, red is random stuff
	pill = input("\nBlue or yellow? ")

	if pill == 'blue':
		print("\nYou wake up in your bed.... ")
		time.sleep(1)
		print("believing whatever you want to believe....")
		time.sleep(1)
		print("\nsignal lost....")
		time.sleep(1)
		input("\nPress 'enter' wake up. ")
		exit(0)
	else:
		print("\nHere is the truth. ")
		time.sleep(1)
		print("Nothing more. ")
		time.sleep(1)
		print("Nothing less.")
		time.sleep(1)

	the_truth = input("\nAccept or run? ")

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
	else:
		print("Goodbye. ")
		time.sleep(1)
		
	no_answer = True
	while no_answer:
		yes_no = input("\nShall we go again? (yes or no) ")
		if yes_no == 'yes':
			no_answer = False
			print("\nGood choice.\n ")
		if yes_no == 'no':
			no_answer = False
			again = False
			print("Goodbye. ")
			time.sleep(1)
			input("Press 'enter' to quit. ")
			exit(0)
