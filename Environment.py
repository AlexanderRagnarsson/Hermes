from Piece import Piece
from State import State

class Environment:
    def __init__(self,white_moves):
        self.white_moves = white_moves
        self.current_state = State()
        self.current_state.white_moves = white_moves

    def get_current_state(self):
        return self.current_state.copy()

    def legal_moves(self,state:State):
        moves = []
        for row in state.board.get_arr():
            for square in row:
                if square != 0:
                    if state.white_moves == square.is_white:
                        for move in square.get_moves(state.board):
                            moves.append(move)
        return moves

    def apply_move(self,state:State,move):
        piece_moved = state.board.get_piece_on(move[0],move[1])
        piece_taken = state.board.get_piece_on(move[2],move[3])
        if state.is_king(move[2],move[3]):
            state.king_taken = True

        state.board.move_piece(move[0],move[1],move[2],move[3])
        piece_moved.x = move[2]
        piece_moved.y = move[3]

        state.move_history.append((move,piece_taken))
        state.white_moves = not state.white_moves

    def undo_move(self,state:State):
        move,piece = state.move_history.pop()
        state.board.move_piece(move[2],move[3],move[0],move[1])
        if type(piece) == Piece:
            state.board.add_piece(piece,move[2],move[3])
            if state.king_taken:
                state.king_taken = False
        state.white_moves = not state.white_moves

    def apply_move_to_current(self,move):
        self.apply_move(self.current_state, move)
    
    def is_terminal(self,state):
        h = self.what_happened(state)
        print(h)
        return h != 0


    def what_happened(self,state:State):
        """ Returns 1 if the white king got taken, 2 if the black king got taken, 3 if it is a stalemate 
        and 0 if the game has not terminated"""
        if state.king_taken:
            if state.white_moves:
                return 2
            else:
                return 1
        if self.legal_moves(state) == []:
            return 3
        return 0
