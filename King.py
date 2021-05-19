from Board import Board
from Piece import Piece

class King(Piece):
    arr = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,-1],[0,1]]
    def __init__(self,is_white,x,y) -> None:
        self.is_white = is_white
        self.x = x
        self.y = y

    def get_moves(self,board:Board):
        moves = []
        for m in King.arr:
            x2 = self.x + m[0]
            y2 = self.y + m[1]
            if not board.is_valid(x2,y2):
                break
            piece = board.get_piece_on(x2,y2)
            if piece != -1 and (piece == 0 or piece.is_white != self.is_white):
                moves.append([self.x,self.y,x2,y2])
            
        return moves

    def __copy__(self):
        return King(self.is_white,self.x,self.y)


    def __str__(self) -> str:
        if self.is_white:
            return "WK"
        else:
            return "BK"
