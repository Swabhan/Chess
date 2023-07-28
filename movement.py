import pygame
import math

pygame.init()

win = pygame.display.set_mode((500, 500))
moves = []

def round_down_to_nearest_divisible(number, divisor):
    return math.floor(number / divisor) * divisor

class Movement:
	def __init__(self, board):
		self.position = None #(x, y) coordinate gets assigned for the original position of the first click
		self.moveTo = None #(x, y) coordinate gets assigned for the square that the player wants to move to
		self.piece = None #Piece name gets assigned after getPosition() runs
		self.clicked = False #Checks if a piece has been clicked, and resets to false after the square player wants to move to has been clicked
		self.board = board

	def getPosition(self):
		# gets coordinate of mouse click
		numbers = [8, 7, 6, 5, 4, 3, 2, 1]
		letters = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

		pos = pygame.mouse.get_pos()

		row = min(max(pos[1] // 62.5, 0), 7)
		col = min(max(pos[0] // 62.5, 0), 7)

		number = numbers[int(row)]
		letter = letters[int(col)]


		if self.board[letter][number][3] != None:
			self.position = (letter, number)
			self.clicked = True
			self.piece = self.board[letter][number][3]
	
			return self.position

		self.removeSelection((1, 1), (1, 1))
		return None

		
	def movePosition(self):
		# gets coordinate of mouse click if there is a value in self.position
		if self.position != None:
			numbers = [8, 7, 6, 5, 4, 3, 2, 1]
			letters = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

			pos = pygame.mouse.get_pos()

			row = min(max(pos[1] // 62.5, 0), 7)
			col = min(max(pos[0] // 62.5, 0), 7)

			number = numbers[int(row)]
			letter = letters[int(col)]


			self.moveTo = (letter, number)
			
			return self.moveTo

	def checkSquare(self, curLet, curNum, letter, number, pieceColor):
		#Check if square is open
		if self.board[letter][number] is None or pieceColor != self.board[letter][number][2]:
			self.reasignCoordinates(curLet, curNum, letter, number)
			self.cleanBoard(self.moveTo, self.position)
			

	def reset(self):
		# resets variable for the next turn
		self.position = None
		self.moveTo = None
		self.clicked = False

	def removeSelection(self, position, currentPosition):
		if currentPosition[1] - position[1] == 0 and currentPosition[0] == position[0]:
				self.reset()
				self.cleanBoard(position, currentPosition)

	def cleanBoard(self, position, currentPosition):
		#cleans former position's color and removes piece if movement is successful
		letter = currentPosition[0]
		number = currentPosition[1]


		if self.board[letter][number][4] == 'sb':
			pygame.draw.rect(win, (118,150,86), (self.board[letter][number][0], self.board[letter][number][1], 62.5, 62.5))
		else:
			pygame.draw.rect(win, (238,238,210), (self.board[letter][number][0], self.board[letter][number][1], 62.5, 62.5))
		
		self.reset()



	def reasignCoordinates(self, curLet, curNum, letter, number):
		#Reassigning coordinates for changes in board
		#Move Piece
		self.board[letter][number][2] = self.board[curLet][curNum][2]
		self.board[letter][number][3] = self.board[curLet][curNum][3]

		#Remove Piece
		self.board[curLet][curNum][2] = None
		self.board[curLet][curNum][3] = None

	
	def pawns(self, position, currentPosition, piece):
		# Movement of pawns
		if piece == "bpawn":
			if currentPosition[1] == 7:  # If pawn is in starting row
				# Double or single space move
				if position[1] == 5 or position[1] == 6 and currentPosition[0] == position[0]:
					self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])
				# Diagonal capture
				elif abs(ord(currentPosition[0]) - ord(position[0])) == 1 and currentPosition[1] - position[1] == 1:
					if self.board[position[0]][position[1]][2] == 'w':
						self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			else:
				# Single space move
				if currentPosition[1] - position[1] == 1 and currentPosition[0] == position[0]:
					self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])
				# Diagonal capture
				elif abs(ord(currentPosition[0]) - ord(position[0])) == 1 and currentPosition[1] - position[1] == 1:
					if self.board[position[0]][position[1]][2] == 'w':
						self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			if currentPosition[1] == position[1] and currentPosition[0] == position[0]:
				self.removeSelection(position, currentPosition)

		else:
			if currentPosition[1] == 2:  # If pawn is in starting spot
				if position[1] == 4 or position[1] == 3 and currentPosition[0] == position[0]:
					self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])
				# Diagonal capture
				elif abs(ord(currentPosition[0]) - ord(position[0])) == 1 and position[1] - currentPosition[1] == 1:
					if self.board[position[0]][position[1]][2] == 'b':
						self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			else:
				# Single space move
				if position[1] - currentPosition[1] == 1 and currentPosition[0] == position[0]:
					self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

				# Diagonal capture
				elif abs(ord(currentPosition[0]) - ord(position[0])) == 1 and position[1] - currentPosition[1] == 1:
					if self.board[position[0]][position[1]][2] == 'b':
						self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			if currentPosition[1] == position[1] and currentPosition[0] == position[0]:
				self.removeSelection(position, currentPosition)

		


	def rooks(self, position, currentPosition, piece):
		if piece == "brook" or piece == "wrook":
			# Calculate the absolute differences in the x and y coordinates
			dx = abs(ord(currentPosition[0]) - ord(position[0]))
			dy = abs(int(currentPosition[1]) - int(position[1]))

			# Check if the move is either horizontal (dx == 0 and dy != 0) or vertical (dx != 0 and dy == 0)
			if (dx == 0 and dy != 0) or (dx != 0 and dy == 0):
				self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			if currentPosition[1] - position[1] == 0 and currentPosition[0] == position[0]:
				self.removeSelection(position, currentPosition)



	def knights(self, position, currentPosition, piece):
		dx = abs(ord(currentPosition[0]) - ord(position[0]))
		dy = abs(int(currentPosition[1]) - int(position[1]))

		# Check if the move is an "L" shape for knights
		if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
			self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

		if currentPosition[1] - position[1] == 0 and currentPosition[0] == position[0]:
			self.removeSelection(position, currentPosition)




	def bishops(self, position, currentPosition, piece):
		if piece == "bbishop" or piece == "wbishop":
			# Calculate the differences in x and y coordinates
			dx = abs(ord(currentPosition[0]) - ord(position[0]))
			dy = abs(int(currentPosition[1]) - int(position[1]))
		
		# Check if the move is along a diagonal (equal magnitude of dx and dy)
		if abs(dx) == abs(dy):
			self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

		
		if currentPosition[1] - position[1] == 0 and currentPosition[0] == position[0]:
			self.removeSelection(position, currentPosition)

		


	def queen(self, position, currentPosition, piece):
		if piece == "bqueen" or piece == "wqueen":
			# Calculate the differences in x and y coordinates
			dx = abs(ord(currentPosition[0]) - ord(position[0]))
			dy = abs(int(currentPosition[1]) - int(position[1]))

			# Check if the move is along a diagonal (equal magnitude of dx and dy)
			if abs(dx) == abs(dy):
				self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])
				# Check if the move is either horizontal (dx == 0 and dy != 0) or vertical (dx != 0 and dy == 0)
			elif (dx == 0 and dy != 0) or (dx != 0 and dy == 0):
				self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			if currentPosition[1] - position[1] == 0 and currentPosition[0] == position[0]:
				self.removeSelection(position, currentPosition)


	def king(self, position, currentPosition, piece):
		if piece == "bking" or piece == "wking":
			# Calculate the differences in x and y coordinates
			dx = abs(ord(currentPosition[0]) - ord(position[0]))
			dy = abs(int(currentPosition[1]) - int(position[1]))

			# Check if the move is only one square away horizontally, vertically, or diagonally
			if dx <= 1 and dy <= 1:
				self.checkSquare(currentPosition[0], currentPosition[1], position[0], position[1], self.board[currentPosition[0]][currentPosition[1]][2])

			if currentPosition[0] == position[0] and currentPosition[1] == position[1]:
				self.removeSelection(position, currentPosition)

	

