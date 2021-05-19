from abc import ABC, abstractclassmethod

class Piece(ABC):
    @abstractclassmethod
    def get_moves(self):pass
    