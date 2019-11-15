from gameFunctions import gameVars


def compareChoices(player):
	if player == gameVars.computer:
		print(" ")
		print("Tie, no one wins! try again", "\n")

	elif player == "quit":
		print(" ")
		print("You chose to quit, quitter.", "\n")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print(" ")
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print(" ")
			print("You won!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print(" ")
			print("You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print(" ")
			print("You won!", player, "cover", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You won!", player, "cuts", gameVars.computer, "\n")
			gameVars.computerlives = gameVars.computer_lives -1