import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

class Movement:
	def __init__(self, board):
		self.position = None #(x, y) coordinate gets assigned for the original position of the first click
		self.moveTo = None #(x, y) coordinate gets assigned for the square that the player wants to move to
		self.piece = None #Piece name gets assigned after getPosition() runs
		self.clicked = False #Checks if a piece has been clicked, and resets to false after the square player wants to move to has been clicked
		self.board = board

	def getPosition(self):
		# gets coordinate of mouse click
		pos = pygame.mouse.get_pos()
		x = float(62.5 * round(pos[0]/62.5))
		y = float(62.5 * round(pos[1]/62.5))


		# Checks if a piece is in the coordinate
		for i in self.board.values():
			for value in i:
				if value[0] == x:
					if value[1] == y:
						if value[3] != "None":
							self.position = (x, y)

							self.clicked = True
							self.piece = value[3]

				else:
					continue
			
		return self.position

		

		
	def movePosition(self):
		# gets coordinate of mouse click if there is a value in self.position
		if self.position != None:
			pos = pygame.mouse.get_pos()
			x = float(62.5 * round( pos[0] / 62.5))
			y = float(62.5 * round( pos[1] / 62.5))


			self.moveTo = (x, y)
			
			return self.moveTo

	def checkSquare(self, currentPosition, position, piece):
		for i in self.board.values():
			for value in i:
					if value[0] == position[0]:
						if value[1] == position[1]:					
							if value[3] == "None" or piece[0] != value[3][0]:
								self.reasignCoordinates(currentPosition, position, piece)
								
								self.cleanBoard(self.moveTo, self.position)
			

	def reset(self):
		# resets variable for the next turn
		self.position = None
		self.moveTo = None
		self.clicked = False

	def removeSelection(self, position, currentPosition):
		if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.reset()
				self.cleanBoard(position, currentPosition)

	def cleanBoard(self, position, currentPosition):
		#cleans color changes and pieces if movement is successful
		for i in self.board.values():
			for value in i:
				if value[0] == currentPosition[0]:
					if value[1] == currentPosition[1]:
						if value[4] == 'sb':
							pygame.draw.rect(win, (238,238,210), (value[0], value[1], 62.5, 62.5))
						else:
							pygame.draw.rect(win, (118,150,86), (value[0], value[1], 62.5, 62.5))
						
						self.reset() 

	def reasignCoordinates(self, currentPosition, position, piece):
	#Reassigning coordinates for changes in board
		for i in self.board.values():
			for value in i:
				if value[0] == currentPosition[0]:
					if value[1] == currentPosition[1]:					
						value[3] = "None"
						value[2] = "None"

		for i in self.board.values():
			for value in i:
				if value[0] == position[0]:
					if value[1] == position[1]:
						value[3] = piece
						value[2] = 'b'

	# Movement for each piece
	def pawns(self, position, currentPosition, piece):
		#Movement of pawns
		if piece == "bpawn":
			if currentPosition[1] == 375: #If pawn is in starting spot
				if currentPosition[1] - position[1] <= 125 and currentPosition[1] - position[1] >= 0 and currentPosition[0] - position[0] == 0:
					self.checkSquare(currentPosition, position, piece)
			else:
				if currentPosition[1] - position[1] <= 62.5 and currentPosition[1] - position[1] >= 0 and currentPosition[0] - position[0] == 0:
					self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)

		else:
			if currentPosition[1] == 62.5: #If pawn is in starting spot
				if position[1] - currentPosition[1] <= 125 and position[1] - currentPosition[1] >= 0 and currentPosition[0] - position[0] == 0:
					self.checkSquare(currentPosition, position, piece)
			else:
				if position[1] - currentPosition[1] <= 62.5 and position[1] - currentPosition[1] >= 0 and currentPosition[0] - position[0] == 0:
					self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)

		#Capturing pieces
		


	def rooks(self, position, currentPosition, piece):
		if piece == "brook":
			if currentPosition[0] - position[0] == 0 and currentPosition[1] - position[1] != 0: #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and position[0] - currentPosition[0] != 0: #Left and right
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		else:
			if currentPosition[0] - position[0] == 0 and currentPosition[1] - position[1] != 0: #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and position[0] - currentPosition[0] != 0: #Left and right
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)


	def knights(self, position, currentPosition, piece):
		if piece == "bknight":
			if (currentPosition[1] - position[1] == 125) and (currentPosition[0] - position[0] == 62.5 or position[0] - currentPosition[0] == 62.5): #Up 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] - position[1] == -125) and (currentPosition[0] - position[0] == 62.5 or position[0] - currentPosition[0] == 62.5): #Down 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[0] - position[0] == 125) and (currentPosition[1] - position[1] == 62.5 or position[1] - currentPosition[1] == 62.5): #Left 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[0] - position[0] == -125) and (currentPosition[1] - position[1] == 62.5 or position[1] - currentPosition[1] == 62.5): #Right 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		else:
			if (currentPosition[1] - position[1] == 125) and (currentPosition[0] - position[0] == 62.5 or position[0] - currentPosition[0] == 62.5): #Up 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] - position[1] == -125) and (currentPosition[0] - position[0] == 62.5 or position[0] - currentPosition[0] == 62.5): #Down 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[0] - position[0] == 125) and (currentPosition[1] - position[1] == 62.5 or position[1] - currentPosition[1] == 62.5): #Left 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[0] - position[0] == -125) and (currentPosition[1] - position[1] == 62.5 or position[1] - currentPosition[1] == 62.5): #Right 3 +- 1
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)

	def bishops(self, position, currentPosition, piece):
		if piece == "bbishop":
			if (currentPosition[1] - position[1]) == (currentPosition[0] - position[0]): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		else:
			if (currentPosition[1] - position[1]) == (currentPosition[0] - position[0]): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		


	def queen(self, position, currentPosition, piece):
		if piece == "bqueen":
			if currentPosition[0] - position[0] == 0 and currentPosition[1] - position[1] != 0: #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and position[0] - currentPosition[0] != 0: #Left and right
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] - position[1]) == (currentPosition[0] - position[0]): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		else:
			if currentPosition[0] - position[0] == 0 and currentPosition[1] - position[1] != 0: #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and position[0] - currentPosition[0] != 0: #Left and right
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] - position[1]) == (currentPosition[0] - position[0]): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)			
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)

		
	def king(self, position, currentPosition, piece):
		if piece == "bking":
			if currentPosition[0] - position[0] == 0 and (currentPosition[1] - position[1] == 62.5 or currentPosition[1] - position[1] == -62.5): #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and (position[0] - currentPosition[0] == 62.5 or position[0] - currentPosition[0] == -62.5): #Left and right
				self.checkSquare(currentPosition, position, piece)
			elif ((currentPosition[1] - position[1]) == (currentPosition[0] - position[0])) and (currentPosition[1] - position[1] == 62.5 or currentPosition[0] - position[0] == -62.5): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]) and (position[1] - currentPosition[1] == -62.5 or position[0] - currentPosition[0] == -62.5): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)
		else:
			if currentPosition[0] - position[0] == 0 and (currentPosition[1] - position[1] == 62.5 or currentPosition[1] - position[1] == -62.5): #Up and down
				self.checkSquare(currentPosition, position, piece)
			elif currentPosition[1] - position[1] == 0 and (position[0] - currentPosition[0] == 62.5 or position[0] - currentPosition[0] == -62.5): #Left and right
				self.checkSquare(currentPosition, position, piece)
			elif ((currentPosition[1] - position[1]) == (currentPosition[0] - position[0])) and (currentPosition[1] - position[1] == 62.5 or currentPosition[0] - position[0] == -62.5): #Diagonal left up or right down
				self.checkSquare(currentPosition, position, piece)
			elif (currentPosition[1] + currentPosition[0]) == (position[1] + position[0]) and (position[1] - currentPosition[1] == -62.5 or position[0] - currentPosition[0] == -62.5): #Diagonal right up or right down
				self.checkSquare(currentPosition, position, piece)
			if currentPosition[1] - position[1] == 0 and currentPosition[0] - position[0] == 0:
				self.removeSelection(position, currentPosition)

	

