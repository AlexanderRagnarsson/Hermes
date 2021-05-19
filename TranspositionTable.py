from Zobrist import Zobrist
from Evaluation import Evaluation
from Environment import Environment
from TableEntry import *
import time

class TranspositionTable:
    def __init__(self,environment:Environment,evaluation:Evaluation,max_time) -> None:
        self.environment = environment
        self.evaluation = evaluation
        self.zobrist = Zobrist()
        self.transposition_table = {}
        self.max_time = max_time

    def search_root(self,depth,state):
        best_move = [0,0,0,1]
        best_value = self.evaluation.loss
        alpha = self.evaluation.loss
        beta = self.evaluation.win
        state.hash = self.zobrist.get_full_hash(state)
        try:
            for move in self.environment.legal_moves(state):
                hash_addition = self.zobrist.get_new_state_hash(state,move)
                self.zobrist.update_state_hash(hash_addition)
                
                self.environment.apply_move(state,move)
                value = -self.search(depth-1,1,state,-beta,-alpha)
                self.environment.undo_move(state)
    
                self.zobrist.update_state_hash(hash_addition)

                if value > best_value:
                    best_value = value
                    best_move = move
                
                if best_value > alpha:
                    alpha = best_value
                    if alpha >= beta:
                        break

            return best_move

        except:
            raise Exception

    def search(self,depth,current_depth,state,alpha,beta):
        if self.times_up():
            raise Exception
        
        alpha_original = alpha
        if state.hash in self.transposition_table:
            table_entry = self.transposition_table[state.hash]
            if table_entry.depth >= depth:
                if table_entry.flag == Flag.Exact:
                    return table_entry.value
                elif table_entry.flag == Flag.LOWERBOUND:
                    alpha = max(alpha,table_entry.value)
                elif table_entry.flag == Flag.UPPERBOUND:
                    beta = min(beta,table_entry.value)
                if alpha >= beta:
                    return table_entry.value
        else:
            table_entry = TableEntry(0,Flag.EXACT,0)
        
        if self.environment.is_terminal(state) or depth == 0:
            return self.evaluation.evaluate(state)
        
        best_value = self.evaluation.loss
        for move in self.environment.legal_moves(state):
                hash_addition = self.zobrist.get_new_state_hash(state,move)
                self.zobrist.update_state_hash(hash_addition)
                
                self.environment.apply_move(state,move)
                value = -self.search(depth-1,1,state,-beta,-alpha)
                self.environment.undo_move(state)
    
                self.zobrist.update_state_hash(hash_addition)

                if value > best_value:
                    best_value = value
                    best_move = move
                
                if best_value > alpha:
                    alpha = best_value
                    if alpha >= beta:
                        break

        table_entry.value = best_value
        if best_value <= alpha_original:
            table_entry.flag = Flag.UPPERBOUND
        elif best_value >= beta:
            table_entry.flag = Flag.LOWERBOUND
        else:
            table_entry.flag = Flag.EXACT
        table_entry.depth = depth
        self.transposition_table[state.hash] = table_entry
        return best_value

    def start_clock(self):
        self.start = time.time()

    def times_up(self):
        return time.time() - self.start > self.max_time
