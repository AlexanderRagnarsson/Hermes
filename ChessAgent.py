from _typeshed import SupportsItemAccess
from Environment import Environment
from TranspositionTable import TranspositionTable

class ChessAgent:
    def __init__(self,role,playclock,engine):
        self.is_white = (role == "white")
        self.playclock = playclock
        self.engine = engine
        self.environment = Environment()
        self.smarts = TranspositionTable(self.environment,None)
        self.my_turn = (role == "white")

    def next_action(self,last_move):
        if self.my_turn:
            i = 2
            best_move = [0]*4
            self.smarts.start_clock()
            while i < 50:
                try:
                    best_move = self.smarts.search_root(i,self.environment.get_current_state())
                    i += 1
                except:
                    break
            print(f"move " + " ".join([str(i) for i in best_move]))
            self.environment.apply_move_to_current(best_move)
        else:
            self.environment.apply_move_to_current(last_move)
        self.my_turn = not self.my_turn
