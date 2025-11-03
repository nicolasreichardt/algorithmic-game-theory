import random

# Defining the base class for all strategies

class Strategy:
    def __init__(self, name: str):
        self.name = name
        self.reset()
    
    # Reset for new game
    def reset(self):
        self.history = []
        self.opponent_history = []
    
    # Return 'C' for cooperate or 'D' for defect, error if none
    def make_move(self):
        raise NotImplementedError
    
    # Update history
    def update_history(self, my_move, opponent_move):
        self.history.append(my_move)
        self.opponent_history.append(opponent_move)


# Always Cooperate strategy

class AlwaysCooperate(Strategy):
    def __init__(self):
        super().__init__("Always Cooperate")
    
    def make_move(self):
        return 'C'


# Always Defect strategy

class AlwaysDefect(Strategy):
    def __init__(self):
        super().__init__("Always Defect")
    
    def make_move(self):
        return 'D'


# Tit for tat strategy (cooperation first movem then copy of opponent's last move)

class TitForTat(Strategy):
    def __init__(self):
        super().__init__("Tit-for-Tat")
    
    def make_move(self):
        if not self.opponent_history:
            return 'C'
        return self.opponent_history[-1]


# Grim Trigger strategy (cooperation until opponent defects, then defect forever)

class GrimTrigger(Strategy):
    def __init__(self):
        super().__init__("Grim Trigger")
        self.triggered = False
    
    def reset(self):
        super().reset()
        self.triggered = False
    
    def make_move(self) -> str:
        if self.triggered:
            return 'D'
        if 'D' in self.opponent_history:
            self.triggered = True
            return 'D'
        return 'C'


# Random cooperation/defection (50% probability each)

class Random(Strategy):
    def __init__(self):
        super().__init__("Random")
    
    def make_move(self):
        return random.choice(['C', 'D'])
    

