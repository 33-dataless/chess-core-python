from .chess_piece import Pawn, Knight, King, Queen, Rook, Bishop


class NotationParser:
    cord = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    
    def decode_user_input(user_input: str):
        if isinstance(user_input, str):
            user_input = [i for i in user_input]
            print(user_input)
            
            current_piece = user_input[0]
            chess_field = user_input[1]
            action = user_input[-1]
            vertical, horizontal = cord.get(chess_field[0]), chess_field[1]
            
            
        return (current_piece, (vertical, horizontal), action)
        
        
