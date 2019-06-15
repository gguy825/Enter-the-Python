import time

responses = ["Welcome to Enter the Python. ",
			"\n\nHello. ",
			"....",
			"\nThis is your last chance. After this... ",
			"there is no turning back. ",
			"\nGood choice",
			"\nThen I have nothing more to show you. \n",
			"\nsignal lost....",
			"\nNow on to the final test. ",
			"\nIf you get bit by the blue snake, the story ends.",
			"You wake up in your bed and believe whatever you want to believe.\n",
			"But if you get bit by the yellow snake, you stay in Wonderland, ",
			"and I show you how deep the console hole goes.... ",
			"\nYou wake up in your bed.... ",
			"believing whatever you want to believe....",
			"\nHere is the truth. ",
			"Nothing more. ",
			"Nothing less.",
			"\nconnection to python.org established",
			"downloading TheTruth.py.jpg.exe",
			"Goodbye. "
]

inputs = ["\nPress 'enter' to continue. ",
			"\nShall we continue? (yes or no) ",
			"\nPress 'enter' wake up. ",
			"\nBlue or yellow? ",
			"\nAccept or run? ",
			"\nShall we go again? (yes or no) "
]

again = True
while again:

	print(responses[0])
	input(inputs[0])

	print(responses[1])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[3])
	time.sleep(1)
	print(responses[4])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)

	yes_no = input(inputs[1])

	if yes_no == 'yes':
		print(responses[5])
		time.sleep(1)
	if yes_no == 'no':
		print(responses[6])
		time.sleep(1)
		print(responses[2])
		time.sleep(1)
		print(responses[2])
		time.sleep(1)
		print(responses[7])
		time.sleep(1)
		input(inputs[2])
		exit(0)

	print(responses[8])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[2])
	time.sleep(1)
	print(responses[9])
	time.sleep(1)
	print(responses[10])
	time.sleep(1)
	print("....\n")
	time.sleep(1)
	print(responses[11])
	time.sleep(1)
	print(responses[12])
	time.sleep(1)

	snake = input(inputs[3])

	if snake == 'blue':
		print(responses[13])
		time.sleep(1)
		print(responses[14])
		time.sleep(1)
		print(responses[7])
		time.sleep(1)
		input(inputs[2])
	if snake == 'yellow':
		print(responses[15])
		time.sleep(1)
		print(responses[16])
		time.sleep(1)
		print(responses[17])
		time.sleep(1)

	the_truth = input(inputs[4])

	if the_truth == 'accept':
		print(responses[2])
		time.sleep(1)
		print(responses[18])
		time.sleep(1)
		print(responses[2])
		time.sleep(0.8)
		print(responses[2])
		time.sleep(0.5)
		print(responses[19])
		time.sleep(1)
	if the_truth == 'run':
		print(responses[20])
		time.sleep(1)

	no_answer = True
	while no_answer:
		yes_no = input(inputs[5])
		if yes_no == 'yes':
			no_answer = False
			print(responses[5])
		if yes_no == 'no':
			no_answer = False
			again = False
			print(responses[20])
			time.sleep(1)
			input(inputs[2])
			exit(0)
