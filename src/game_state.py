from .user import User, ColorUser
from .chess_board import ChessBoard
from .notation_parser import NotationParser
from random import randint
from enum import Enum

class GameState:
    def __init__(self, color: Enum, mode: None):
        if color == ColorUser.RANDOM:
            self.__color__ = self.random_user_color()
        else:
            self.__color__ = color

        if self.__color__ == ColorUser.WHITE:
            self.__turn_move__ = True
        else:
            self.__turn_move__ = False

        self.runtime()
             
    @staticmethod
    def random_user_color() -> ColorUser:
        if randint(0, 1):
            return ColorUser.WHITE
        return ColorUser.BLACK

    def runtime(self):
        parser = NotationParser
        if self.__turn_move__:
            board = ChessBoard()
            board.refresh_board()
            user_input  = input("enter your move > ")
            move = parser.decode_user_input(user_input=user_input)
            print(move)
    
    def is_legal():
        pass

    def check_mate():
        pass
    

    
        
        

    
        
