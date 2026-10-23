import numpy as np
from chess_piece import Pawn, Knight, King, Queen, Rook, Bishop

class ChessBoard:
    __board__ = np.array([
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook],
         ])
    
    def __init__(self) -> None:
        # todo add chess360 
        pass
    
    def refresh_board():
        pass
    
    
 
