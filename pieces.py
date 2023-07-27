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
            row = 1
            for i in range(1, 65):
                if row % 2 != 0:
                    if i % 2 == 0:
                        pygame.draw.rect(win, (118, 150, 86), (x, y, width, height))
                    else:
                        pygame.draw.rect(win, (238, 238, 210), (x, y, width, height))
                else:
                    if i % 2 == 0:
                        pygame.draw.rect(win, (238, 238, 210), (x, y, width, height))
                    else:
                        pygame.draw.rect(win, (118, 150, 86), (x, y, width, height))

                x += 62.5
                if i % 8 == 0:
                    y += 62.5
                    x = 0
                    row += 1

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
                        if 'rook' in self.movement.piece:
                            self.movement.rooks(self.movement.moveTo, self.movement.position, self.movement.piece)
                        if 'knight' in self.movement.piece:
                            self.movement.knights(self.movement.moveTo, self.movement.position, self.movement.piece)
                        if 'bishop' in self.movement.piece:
                            self.movement.bishops(self.movement.moveTo, self.movement.position, self.movement.piece)
                        if 'queen' in self.movement.piece:
                            self.movement.queen(self.movement.moveTo, self.movement.position, self.movement.piece)
                        if 'king' in self.movement.piece:
                            self.movement.king(self.movement.moveTo, self.movement.position, self.movement.piece)
                    else:
                        if self.movement.getPosition() is not None:  # Runs if a player has not yet selected the desired piece to be moved
                            letter = self.movement.movePosition()[0]
                            number = self.movement.movePosition()[1]

                            pygame.draw.rect(win, (255, 51, 51), (self.board[letter][number][0], self.board[letter][number][1], width, height))

                    for number in range(1, 9):
                        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                            if self.board[letter][number][2] == 'w':
                                win.blit(pygame.image.load('images/' + self.board[letter][number][3] + '.png'), (self.board[letter][number][0], self.board[letter][number][1]))
                            elif self.board[letter][number][2] == 'b':
                                win.blit(pygame.image.load('images/' + self.board[letter][number][3] + '.png'), (self.board[letter][number][0], self.board[letter][number][1]))


                    pygame.time.delay(200)

            pygame.display.update()

        pygame.quit()

