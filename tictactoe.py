import random

def display_board(board):
	initial_board = [None] * 10 
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	
def player_input():
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O? ').upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def place_marker(board, marker, position):
	board[position] = marker
	return board

def win_check(board, mark):
	if board[7] == board[8] == board[9] == mark:
		return True
	elif board[4] == board[5] == board[6] == mark:
		return True
	elif board[1] == board[2] == board[3] == mark:
		return True
	elif board[7] == board[4] == board[1] == mark:
		return True
	elif board[9] == board[6] == board[3] == mark:
		return True
	elif board[8] == board[5] == board[2] == mark:
		return True
	elif board[7] == board[5] == board[3] == mark:
		return True
	elif board[9] == board[5] == board[1] == mark:
		return True
	else: 
		return False

def choose_first():
	myint = random.randint(0,1)
	if myint == 0:
		return "Player 1"
	else: 
		return "Player 2"

def space_check(board, position):
	
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True    		

def player_choice(board):
	position = 0
	
	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
		position = int(input('Choose your next position: (1-9) '))
		
	return position

def replay():
	boolean = input('Do you want to play again?')
	if boolean.lower() == 'yes':
		return True
	else:
		return False


print('Welcome to Tic Tac Toe!')

while True:
	initial_board = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first.')
	
	play_game = input('Are you ready to play? Enter Yes or No.')
	
	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player 1':
			display_board(initial_board)
			position = player_choice(initial_board)
			place_marker(initial_board,player1_marker,position)
			print('\n'*100)

			if win_check(initial_board, player1_marker):
				display_board(initial_board)
				print('Congrats Player 1 you have won the game!')
				game_on = False

			else:
				if full_board_check(initial_board):
					display_board(initial_board)
					print('The game is a draw!')
					break 

				else: turn = 'Player 2'

		else:
			display_board(initial_board)
			position = player_choice(initial_board)
			place_marker(initial_board,player2_marker,position)
			print('\n'*100)

			if win_check(initial_board, player2_marker):
				display_board(initial_board)
				print('Congrats Player 2 you have won the game!')
				game_on = False

			else:
				if full_board_check(initial_board):
					display_board(initial_board)
					print('The game is a draw!')
					break 

				else: turn = 'Player 1'

	if not replay():
		break






