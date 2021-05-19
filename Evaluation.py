from abc import ABC, abstractclassmethod

class Evaluation(ABC):
    loss = -1000000
    win = 1000000
    @abstractclassmethod
    def evaluate(): pass