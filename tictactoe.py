import random
board = {}
end = False
win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def board():
	print('    |       |   ')
	#print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('    |       |   ')
	print('------------------')
	print('    |       |    ')
	#print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('    |       |    ')
	print('------------------')
	print('    |       |    ')
	#print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('    |       |    ')

def playerletter():
	plylt = raw_input("what letter do you want to play with [O or X]: ")
	plylt = plylt.upper()
	if plylt == "X":
		return ['X', 'O' ]
		firstmove(plylt)
	elif plylt == "O":
		return ['O', 'X']
		firstmove(plylt)
	else:
		print "Please select the right option, it has to be from X or O"
		playerletter()

def firstmove(plylt):
	if random.randint(0,1) == 0:
		print "computer's move"
	else:
		print "your move, you have chosen " + plylt 
		registermoves(plylt)

def registermoves(plylt):
	a = int (raw_input("enter a number from 1 to 9"))
	if board[a] == "X" or "O":
		print "please enter a new number"
		registermoves()
	else:
		board[a] =  plylt
		
def gamecheck(plylt):
	count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == plylt:
                print("Player 1 Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] != plylt:
                print("Player 2 Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
            




#playerletter()
