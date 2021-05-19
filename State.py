from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Board import Board

class State:
    def __init__(self,add=True) -> None:
        self.board = Board()                
        self.white_moves = False
        self.hash = 0
        self.move_history = []
        self.king_taken = False
        if add:
            self.__add_pieces()

    def __add_pieces(self):
        for x in range(8):
            self.board.add_piece(Pawn(is_white=True,x=x,y=1),x,1)
            self.board.add_piece(Pawn(is_white=False,x=x,y=6),x,6)
        for x in [0,7]:
            self.board.add_piece(Rook(is_white=True,x=x,y=0),x,0)
            self.board.add_piece(Rook(is_white=False,x=x,y=7),x,7)
        for x in [1,6]:
            self.board.add_piece(Knight(is_white=True,x=x,y=0),x,0)
            self.board.add_piece(Knight(is_white=False,x=x,y=7),x,7)
        for x in [2,5]:
            self.board.add_piece(Bishop(is_white=True,x=x,y=0),x,0)
            self.board.add_piece(Bishop(is_white=False,x=x,y=7),x,7)
        self.board.add_piece(Queen(is_white=True,x=3,y=0),3,0)
        self.board.add_piece(Queen(is_white=False,x=3,y=7),3,7)
        self.board.add_piece(King(is_white=True,x=4,y=0),4,0)
        self.board.add_piece(King(is_white=False,x=4,y=7),4,7)

    def __copy__(self):
        state = State(False)
        state.board = self.board.copy()
        state.white_moves = self.white_moves
        state.move_history = self.move_history.copy()
        state.king_taken = self.king_taken
        state.hash = self.hash
        return state

    def __eq__(self,other):
        return self.board == other.board and self.white_moves == other.white_moves

    def is_king(self,x,y):
        if type(self.board.get_piece_on(x,y)) == King:
            return True
        return False
