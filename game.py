from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("===========================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("===========================================")
	print(" ")
	print("Chosose your weapon!\n")
	player=input("choose rock, paper or scissors:")
	compare.compareChoices(player)


	if gameVars.player_lives == 0:
		winlose.winorlose("Lost")
		
	elif gameVars.computer_lives == 0:
		winlose.winorlose("Won")
		
	else:
		player = False
		gameVars.computer=gameVars.choices[randint(0,2)]