from enum import Enum

class ColorUser(Enum):
    WHITE="white",
    BLACK="black",
    RANDOM="random"

class User:
    def __init__(self, color: Enum) -> None:
        self.color = color
        
        
    # for future online mode
    # self.id = None
    # self.nickname = None
    # self.country = None
    # self.elo = None
    
    
    
