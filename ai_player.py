import random


# creates the node used by the ai To calculate it's next move
class Node:

    def __init__(self, move = None, parent = None, state = None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.get_moves()
        self.current_player = state.current_player

    #seelect the child using a  cw/cv + UCTK * squared(2*log(self.visits)/c.visits))[-1]
    def UCTSelectChild(self):
        s = sorted(self.childNodes, key = lambda c: c.wins/c.visits + squa(2))








def choose_move(board):
    """ Takes a game board, and returns a move to play
    """
    
    available_moves = board.get_moves()
    return random.choice(available_moves)
