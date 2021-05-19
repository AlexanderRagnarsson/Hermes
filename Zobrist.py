from State import State

class Zobrist:
    def __init__(self) -> None:
        pass

    def get_full_hash(state:State):
        pass

    def get_piece_hash(piece):
        pass

    def get_new_state_hash(state:State, move):
        pass

    def update_state_hash(state:State, hash_addition):
        state.hash = state.hash ^ hash_addition
