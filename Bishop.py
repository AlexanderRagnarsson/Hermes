from Board import Board
from Piece import Piece

class Bishop(Piece):
    def __init__(self,is_white,x,y) -> None:
        self.is_white = is_white
        self.x = x
        self.y = y
    
    def get_moves(self,board:Board):
        moves = []
        
        for i in range(1,8):
            x2 = self.x + i
            y2 = self.y + i
            if not board.is_valid(x2,y2):
                break
            if board.contains_piece_on(x2,y2):
                if board.get_piece_on(x2,y2).is_white != self.is_white:
                    moves.append([self.x,self.y,x2,y2])
                break
            moves.append([self.x,self.y,x2,y2])

        for i in range(1,8):
            x2 = self.x - i
            y2 = self.y + i
            if not board.is_valid(x2,y2):
                break
            if board.contains_piece_on(x2,y2):
                if board.get_piece_on(x2,y2).is_white != self.is_white:
                    moves.append([self.x,self.y,x2,y2])
                break
            moves.append([self.x,self.y,x2,y2])

        for i in range(1,8):
            x2 = self.x + i
            y2 = self.y - i
            if not board.is_valid(x2,y2):
                break
            if board.contains_piece_on(x2,y2):
                if board.get_piece_on(x2,y2).is_white != self.is_white:
                    moves.append([self.x,self.y,x2,y2])
                break
            moves.append([self.x,self.y,x2,y2])

        for i in range(1,8):
            x2 = self.x - i
            y2 = self.y - i
            if not board.is_valid(x2,y2):
                break
            if board.contains_piece_on(x2,y2):
                if board.get_piece_on(x2,y2).is_white != self.is_white:
                    moves.append([self.x,self.y,x2,y2])
                break
            moves.append([self.x,self.y,x2,y2])

        return moves
    
    def __copy__(self):
        return Bishop(self.is_white,self.x,self.y)


    def __str__(self) -> str:
        if self.is_white:
            return "Wb"
        else:
            return "Bb"
