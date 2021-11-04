import copy
import random
from prob_test import testing

# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for colour, count in balls.items():
            i = 0
            while i < count:
                self.contents.append(colour)
                i += 1



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

testing(Hat)