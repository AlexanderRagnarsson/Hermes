from enum import Enum

class TableEntry:
    def __init__(self,depth,flag,value) -> None:
        self.depth = depth
        self.flag = flag
        self.value = value

class Flag(Enum):
    EXACT = 0
    LOWERBOUND = 1
    UPPERBOUND = 2
