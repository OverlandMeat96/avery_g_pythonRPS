# check a temperature and output a result

temperature = int(input("input a number between 0 and 100"))

if temperature <= 4:
	print("Water is a solid. cuz it's frozen")
elif temperature < 100:
	print("Water is a liquid")
else:
	print("Water is a gas. cuz it's boiling!")

