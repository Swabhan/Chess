from pieces import Pieces
from movement import Movement

board = {
	1 : [[0, 0, 'w', 'wrook', 'sw'],[62.5, 0, 'w', 'wbishop', 'sb'],[125, 0, 'w', 'wknight', 'sw'],[187.5, 0, 'w', 'wqueen', 'sb'],[250, 0, 'w', 'wking', 'sw'],[312.5, 0, 'w', 'wknight', 'sb'],[375, 0, 'w', 'wbishop', 'sw'],[437.5, 0, 'w', 'wrook', 'sb']],
	2 : [[0, 62.5, 'w', 'wpawn', 'sb'],[62.5, 62.5, 'w', 'wpawn', 'sw'],[125, 62.5, 'w', 'wpawn', 'sb'],[187.5, 62.5, 'w', 'wpawn', 'sw'],[250, 62.5, 'w', 'wpawn', 'sb'],[312.5, 62.5, 'w', 'wpawn', 'sw'],[375, 62.5, 'w', 'wpawn', 'sb'],[437.5, 62.5, 'w', 'wpawn', 'sw']], 
	3 : [[0, 125, 'None', 'None', 'sw'],[62.5, 125, 'None', 'None', 'sb'],[125, 125, 'None', 'None', 'sw'],[187.5, 125, 'None', 'None', 'sb'],[250, 125, 'None', 'None', 'sw'],[312.5, 125, 'None', 'None', 'sb'],[375, 125, 'None', 'None', 'sw'],[437.5, 125, 'None', 'None', 'sb']], 
	4 : [[0, 187.5, 'None', 'None', 'sb'],[62.5, 187.5, 'None', 'None', 'sw'],[125, 187.5, 'None', 'None', 'sb'],[187.5, 187.5, 'None', 'None', 'sw'],[250, 187.5, 'None', 'None', 'sb'],[312.5, 187.5, 'None', 'None', 'sw'],[375, 187.5, 'None', 'None', 'sb'],[437.5, 187.5, 'None', 'None', 'sw']], 
	5 : [[0, 250, 'None', 'None', 'sw'],[62.5, 250, 'None', 'None', 'sb'],[125, 250, 'None', 'None', 'sw'],[187.5, 250, 'None', 'None', 'sb'],[250, 250, 'None', 'None', 'sw'],[312.5, 250, 'None', 'None', 'sb'],[375, 250, 'None', 'None', 'sw'],[437.5, 250, 'None', 'None', 'sb']], 
	6 : [[0, 312.5, 'None', 'None', 'sb'],[62.5, 312.5, 'None', 'None', 'sw'],[125, 312.5, 'None', 'None', 'sb'],[187.5, 312.5, 'None', 'None', 'sw'],[250, 312.5, 'None', 'None', 'sb'],[312.5, 312.5, 'None', 'None', 'sw'],[375, 312.5, 'None', 'None', 'sb'],[437.5, 312.5, 'None', 'None', 'sw']], 
	7 : [[0, 375, 'b', 'bpawn', 'sw'],[62.5, 375, 'b', 'bpawn', 'sb'],[125, 375, 'b', 'bpawn', 'sw'],[187.5, 375, 'b', 'bpawn', 'sb'],[250, 375, 'b', 'bpawn', 'sw'],[312.5, 375, 'b', 'bpawn', 'sb'],[375, 375, 'b', 'bpawn', 'sw'],[437.5, 375, 'b', 'bpawn', 'sb']], 
	8 : [[0, 437.5, 'b', 'brook', 'sb'],[62.5, 437.5, 'b', 'bbishop', 'sw'],[125, 437.5, 'b', 'bknight', 'sb'],[187.5, 437.5, 'b', 'bqueen', 'sw'],[250, 437.5, 'b', 'bking', 'sb'],[312.5, 437.5, 'b', 'bknight', 'sw'],[375, 437.5, 'b', 'bbishop', 'sb'],[437.5, 437.5, 'b', 'brook', 'sw']]

}

#Setting up the board
setUp = Pieces(True, board)

setUp.makeBoard()
