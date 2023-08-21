import random as rd


# playable if 
#   tries > 0
#   nb_to_guess >= 0
#   difficulty > 0
class GuessGame:
    def __init__(self) -> None:
        self.nb_to_guess = -1
        self.nb_answer = 0
        self.start = 0
        self.end = 100
        self.nb_attempts = 0
        self.max_attempts = self.end
        self.best_attempts = 0

    def generate_number(self):
        self.nb_to_guess = rd.randrange(self.start, self.end)
        self.nb_answer = 0
        self.nb_attempts = 0
    
    def modify(self, start, end, max_attempts):
        self.start = start
        self.end = end
        self.max_attempts = max_attempts
    
    def check_answer(self) -> bool:
        return self.nb_to_guess == self.nb_answer
    
    def ItsMore(self) -> bool:
        return self.nb_to_guess > self.nb_answer