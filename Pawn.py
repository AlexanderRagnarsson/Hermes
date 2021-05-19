from Board import Board
from Piece import Piece

class Pawn(Piece):
    def __init__(self,is_white,x,y):
        self.is_white = is_white
        self.en_passant = False
        self.x = x
        self.y = y

    def get_moves(self,board:Board):
        moves = []
        if self.is_white:
            yx = 1
        else:
            yx = -1
        if board.is_valid(self.x,self.y+yx) and not board.contains_piece_on(self.x,self.y+yx):
            moves.append([self.x,self.y,self.x,self.y+yx])

        if board.is_valid(self.x-1,self.y+yx) and board.contains_piece_on(self.x-1,self.y+yx):
            if board.get_piece_on(self.x-1,self.y+yx).is_white != self.is_white:
                moves.append([self.x,self.y,self.x-1,self.y+yx])

        if board.is_valid(self.x+1,self.y+yx) and board.contains_piece_on(self.x+1,self.y+yx):
            if board.get_piece_on(self.x+1,self.y+yx).is_white != self.is_white:
                moves.append([self.x,self.y,self.x+1,self.y+yx])

        if self.is_white and self.y == 1:
            if not board.contains_piece_on(self.x,self.y+2):
                moves.append([self.x,self.y,self.x,self.y+2])
        elif (not self.is_white) and self.y == 6:
            if not board.contains_piece_on(self.x,self.y-2):
                moves.append([self.x,self.y,self.x,self.y-2])

        return moves

    def __copy__(self):
        return Pawn(self.is_white,self.x,self.y)


    def __str__(self) -> str:
        if self.is_white:
            return "Wp"
        else:
            return "Bp"
