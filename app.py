from pieces import Pieces
from movement import Movement

board = {
    'h': {
        1: [0, 437.5, 'w', 'wrook', 'sw'], 2: [0, 375, 'w', 'wpawn', 'sb'],
        3: [0, 312.5, 'None', 'None', 'sw'], 4: [0, 250, 'None', 'None', 'sb'],
        5: [0, 187.5, 'None', 'None', 'sw'], 6: [0, 125, 'None', 'None', 'sb'],
        7: [0, 62.5, 'b', 'bpawn', 'sw'], 8: [0, 0, 'b', 'brook', 'sb']
    },
    'g': {
        1: [62.5, 437.5, 'w', 'wbishop', 'sb'], 2: [62.5, 375, 'w', 'wpawn', 'sw'],
        3: [62.5, 312.5, 'None', 'None', 'sb'], 4: [62.5, 250, 'None', 'None', 'sw'],
        5: [62.5, 187.5, 'None', 'None', 'sb'], 6: [62.5, 125, 'None', 'None', 'sw'],
        7: [62.5, 62.5, 'b', 'bpawn', 'sb'], 8: [62.5, 0, 'b', 'bbishop', 'sw']
    },
    'f': {
        1: [125, 437.5, 'w', 'wknight', 'sw'], 2: [125, 375, 'w', 'wpawn', 'sb'],
        3: [125, 312.5, 'None', 'None', 'sb'], 4: [125, 250, 'None', 'None', 'sw'],
        5: [125, 187.5, 'None', 'None', 'sb'], 6: [125, 125, 'None', 'None', 'sw'],
        7: [125, 62.5, 'b', 'bpawn', 'sw'], 8: [125, 0, 'b', 'bknight', 'sb']
    },
    'e': {
        1: [187.5, 437.5, 'w', 'wqueen', 'sb'], 2: [187.5, 375, 'w', 'wpawn', 'sw'],
        3: [187.5, 312.5, 'None', 'None', 'sw'], 4: [187.5, 250, 'None', 'None', 'sb'],
        5: [187.5, 187.5, 'None', 'None', 'sw'], 6: [187.5, 125, 'None', 'None', 'sb'],
        7: [187.5, 62.5, 'b', 'bpawn', 'sb'], 8: [187.5, 0, 'b', 'bking', 'sw']
    },
    'd': {
        1: [250, 437.5, 'w', 'wking', 'sw'], 2: [250, 375, 'w', 'wpawn', 'sb'],
        3: [250, 312.5, 'None', 'None', 'sb'], 4: [250, 250, 'None', 'None', 'sw'],
        5: [250, 187.5, 'None', 'None', 'sb'], 6: [250, 125, 'None', 'None', 'sw'],
        7: [250, 62.5, 'b', 'bpawn', 'sw'], 8: [250, 0, 'b', 'bqueen', 'sb']
    },
    'c': {
        1: [312.5, 437.5, 'w', 'wknight', 'sb'], 2: [312.5, 375, 'w', 'wpawn', 'sw'],
        3: [312.5, 312.5, 'None', 'None', 'sw'], 4: [312.5, 250, 'None', 'None', 'sb'],
        5: [312.5, 187.5, 'None', 'None', 'sw'], 6: [312.5, 125, 'None', 'None', 'sb'],
        7: [312.5, 62.5, 'b', 'bpawn', 'sb'], 8: [312.5, 0, 'b', 'bknight', 'sb']
    },
    'b': {
        1: [375, 437.5, 'w', 'wbishop', 'sb'], 2: [375, 375, 'w', 'wpawn', 'sw'],
        3: [375, 312.5, 'None', 'None', 'sb'], 4: [375, 250, 'None', 'None', 'sw'],
        5: [375, 187.5, 'None', 'None', 'sb'], 6: [375, 125, 'None', 'None', 'sw'],
        7: [375, 62.5, 'b', 'bpawn', 'sb'], 8: [375, 0, 'b', 'bbishop', 'sw']
    },
    'a': {
        1: [437.5, 437.5, 'w', 'wrook', 'sw'], 2: [437.5, 375, 'w', 'wpawn', 'sb'],
        3: [437.5, 312.5, 'None', 'None', 'sb'], 4: [437.5, 250, 'None', 'None', 'sw'],
        5: [437.5, 187.5, 'None', 'None', 'sb'], 6: [437.5, 125, 'None', 'None', 'sw'],
        7: [437.5, 62.5, 'b', 'bpawn', 'sw'], 8: [437.5, 0, 'b', 'brook', 'sb']
    }
}





# Setting up the board
setUp = Pieces(True, board)

setUp.makeBoard()

