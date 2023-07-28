import pygame
import time
from movement import Movement

pygame.init()

win = pygame.display.set_mode((500, 500))

class Pieces:
    def __init__(self, start, board):
        self.start = start
        self.board = board

        # Movement for pieces
        self.movement = Movement(board)

    def makeBoard(self):
        x = 0
        y = 0

        # Squares
        width = 62.5
        height = 62.5

        run = True

        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Drawing each square for the chess board
            for row in range(8):
                for col in range(8):
                    x = col * 62.5
                    y = row * 62.5
                    color = (118, 150, 86) if (row + col) % 2 == 0 else (238, 238, 210)
                    pygame.draw.rect(win, color, (x, y, 62.5, 62.5))



            # Adding images for each piece
            for number in range(1, 9):
                for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                    if self.board[letter][number][2] == 'w':
                        win.blit(pygame.image.load('images/' + self.board[letter][number][3] + '.png'), (self.board[letter][number][0], self.board[letter][number][1]))
                    elif self.board[letter][number][2] == 'b':
                        win.blit(pygame.image.load('images/' + self.board[letter][number][3] + '.png'), (self.board[letter][number][0], self.board[letter][number][1]))

            # Piece Movement
            if event.type == pygame.constants.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.movement.clicked:  # Runs if the player has decided which piece is to be moved
                        self.movement.movePosition()
                        # Running the movement functions to move the pieces
                        if 'pawn' in self.movement.piece:
                            self.movement.pawns(self.movement.moveTo, self.movement.position, self.movement.piece)
                        elif 'rook' in self.movement.piece:
                            self.movement.rooks(self.movement.moveTo, self.movement.position, self.movement.piece)
                        elif 'knight' in self.movement.piece:
                            self.movement.knights(self.movement.moveTo, self.movement.position, self.movement.piece)
                        elif 'bishop' in self.movement.piece:
                            self.movement.bishops(self.movement.moveTo, self.movement.position, self.movement.piece)
                        elif 'queen' in self.movement.piece:
                            self.movement.queen(self.movement.moveTo, self.movement.position, self.movement.piece)
                        elif 'king' in self.movement.piece:
                            self.movement.king(self.movement.moveTo, self.movement.position, self.movement.piece)
                        else:
                            self.movement.reset()

                    else:
                        if self.movement.getPosition() is not None:  # Runs if a player has not yet selected the desired piece to be moved
                            letter = self.movement.movePosition()[0]
                            number = self.movement.movePosition()[1]

                            pygame.draw.rect(win, (255, 51, 51), (self.board[letter][number][0], self.board[letter][number][1], width, height))


                    pygame.time.delay(200)

            pygame.display.update()

        pygame.quit()

