import os

pos = ["0","1","2","3","4","5","6","7", "8", "9"]

def drawBoard():
	print(f"   {pos[1]}   |   {pos[2]}   |   {pos[3]}    ")
	print("--------------------------")
	print(f"   {pos[4]}   |   {pos[5]}   |   {pos[6]}    ")
	print("--------------------------")
	print(f"   {pos[7]}   |   {pos[8]}   |   {pos[9]}    ")
	print("--------------------------")



clear = lambda: os.system("cls")

def checkDraw():
	#Match Tie or Draw Condition
	if (pos[1]!='1' and pos[2]!='2' and pos[3]!='3' and pos[4]!='4' and pos[5]!='5' and pos[6]!='6' and pos[7]!='7' and pos[8]!='8' and pos[9]!='9'):
		return True
	else:
		return False

def checkWin():
	#Horizontal winning condition    
	if(pos[1] == pos[2] and pos[2] == pos[3] and pos[1] != ' '):
		return True
	elif(pos[4] == pos[5] and pos[5] == pos[6] and pos[4] != ' '):
		return True
	elif(pos[7] == pos[8] and pos[8] == pos[9] and pos[7] != ' '):
		return True
	#Vertical Winning Condition    
	elif(pos[1] == pos[4] and pos[4] == pos[7] and pos[1] != ' '):
		return True
	elif(pos[2] == pos[5] and pos[5] == pos[8] and pos[2] != ' '):
		return True
	elif(pos[3] == pos[6] and pos[6] == pos[9] and pos[3] != ' '):
		return True
	#Diagonal Winning Condition    
	elif(pos[1] == pos[5] and pos[5] == pos[9] and pos[5] != ' '):
		return True
	elif(pos[3] == pos[5] and pos[5] == pos[7] and pos[5] != ' '):
		return True


	else:            
		return False


def game():
	print("Hello World!!!\n===TIC TAC TOE===")

	player1 = input("Input the name first player: ")
	player2 = input("Input the name second player: ")

	print("Ok...")

	wait = input("Wait input")
	clear()
	play = True
	win = False
	draw = False
	correctInput = False
	turn = 1
	choice = 0
	countCell = 0
	c = 0
	while play == True:
		while win == False:
			c = 0
			drawBoard()
			if turn == 1:
				print(f"Step {player1} - 'X' ")

				while correctInput == False:
					choice = int(input())
					if choice > 0 and choice < 10:
						correctInput = True

			correctInput = False
			if turn == 2:
				print(f"Step {player2} - 'O' ")

				while correctInput == False:
					choice = int(input())
					if choice > 0 and choice < 10:
						correctInput = True

			correctInput = False

			
			win = checkWin()
			draw = checkDraw()
			if draw == True:
				break

			if turn == 1:
				if pos[choice] == "O":
					print("This cells also have value!!!")
				else:
					pos[choice] = "X"
					countCell += 1
					print(countCell)
			if turn == 2:
				if pos[choice] == "X":
					print("This cells also have value!!!")
				else:
					pos[choice] = "O"
					countCell += 1
					print(countCell)

			

			if turn == 1:
				turn = 2
			elif turn == 2:
				turn = 1

			clear()

		for i in range(len(pos)):
			pos[i] = str(c)
			c += 1

		if win == True:
			if turn == 1:
				print("{0} - 'X' winner ".format(player1))
				print("Choose the next step!!!")
				print("1.Play again\n2.Quit")
				while correctInput == False:
					choice = int(input())
					if choice > 0 and choice < 3:
						correctInput = True
			correctInput = False

			if turn == 2:
				print("{0} - 'X' winner ".format(player2))
				print("Choose the next step!!!")
				print("1.Play again\n2.Quit")
				while correctInput == False:
					choice = int(input())
					if choice > 0 and choice < 3:
						correctInput = True
			correctInput = False

		if win == False and draw == True:
			print("It is a draw!!!")
			print("Choose the next step!!!")
			print("1.Play again\n2.Quit")
			while correctInput == False:
				choice = int(input())
				if choice > 0 and choice < 3:
					correctInput = True
		correctInput = False

		
		if choice == 1:
			win = False
		if choice == 2:
			play = False

if __name__ == "__main__":
	game()

