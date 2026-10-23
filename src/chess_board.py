import numpy as np
from .chess_piece import Pawn, Knight, King, Queen, Rook, Bishop

class ChessBoard:
    def __init__(self) -> None:
        self.__board__ = np.array([
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook],
         ])
    
   
    def refresh_board(self):
        print(self.__board__)
    
    
 
