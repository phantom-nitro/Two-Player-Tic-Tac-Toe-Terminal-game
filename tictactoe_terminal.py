def display():
	print("{} | {} | {}".format(g[0], g[1], g[2]))
	print("--+---+--")
	print("{} | {} | {}".format(g[3], g[4], g[5]))
	print("--+---+--")
	print("{} | {} | {}".format(g[6], g[7], g[8]))


def win(g):
	if (g[0] == g[1] == g[2] == 'X') | (g[0] == g[1] == g[2] == 'O') : return 1
	if (g[3] == g[4] == g[5] == 'X') | (g[3] == g[4] == g[5] == 'O') : return 1
	if (g[6] == g[7] == g[8] == 'X') | (g[6] == g[7] == g[8] == 'O') : return 1

	if (g[0] == g[3] == g[6] == 'X') | (g[0] == g[3] == g[6] == 'O') : return 1
	if (g[1] == g[4] == g[7] == 'X') | (g[1] == g[4] == g[7] == 'O') : return 1
	if (g[2] == g[5] == g[8] == 'X') | (g[2] == g[5] == g[8] == 'O') : return 1

	if (g[0] == g[4] == g[8] == 'X') | (g[0] == g[4] == g[8] == 'O') : return 1
	if (g[6] == g[4] == g[2] == 'X') | (g[6] == g[4] == g[2] == 'O') : return 1

def isinside(n):
	test = 0
	if n == 'X':
		val = int(input("Player 'X' position: "))
		if (val > 8) | (val < 0):
			while test == 0:
				val = int(input("Player 'X' position should be between 0 and 8: "))
				if (val <= 8) and (val >= 0):
					test = 1
				else:
					continue

	elif n == 'O':
		val = int(input("Player 'O' position: "))
		if (val > 8) | (val < 0):
			while test == 0:
				val = int(input("Player 'O' position should be between 0 and 8: "))
				if (val <= 8) and (val >= 0):
					test = 1
				else:
					continue
	test = 0
	return val

def engine(moves, movecheck):
	poscheck = 0
	while True:
		if (moves%2) == 0:
			val = isinside('X')
			if movecheck[val] == 1:
				print(movecheck)
				while poscheck == 0:
					print("Player 'X' should input different position")
					val = isinside('X')
					if movecheck[val] == 1:
						continue
					else:
						movecheck[val] = 1
						poscheck = 1
			else:
				movecheck[val] = 1
				print(movecheck)

		else:
			val = isinside('O')
			if movecheck[val] == 1:
				print(movecheck)
				while poscheck == 0:
					print("Player 'O' should input different position")
					val = isinside('O')
					
					if movecheck[val] == 1:
						continue
					else:
						movecheck[val] = 1
						poscheck = 1
						
			else:
				movecheck[val] = 1
				print(movecheck)
			
		poscheck = 0
		return val, movecheck
				

g = [' ']*9
movecheck = [0]*9
moves = 9

start = input('Start? y/n: ')

while start == 'y':
	display()

	for i in range(moves):
		if (moves%2) == 0:
			val, movecheck = engine(moves, movecheck)
			g[val] = 'X'
			display()
			if win(g):
				print('Player X won!')
				break

		else:
			val, movecheck = engine(moves, movecheck)
			g[val] = 'O'
			display()
			if win(g):
				print('Player O won!')
				break		
		
		moves -= 1
		if moves == 0:
			print('DRAW')
			break
	moves = 9
	g = [' ']*9 #clear
	movecheck = [0]*9 #clear

	start = input('do you want to continue? y/n: ')
