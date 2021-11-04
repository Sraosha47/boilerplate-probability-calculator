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

    def draw(self, amount):
        i = 0
        drawn = list()
        while i < amount:
            drawn.append(self.contents.pop(random.randrange(len(self.contents)-1)))
            i += 1
        return(drawn)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = 0
    count = 0
    drawn = {}

    print(expected_balls.items())
    while i < num_experiments:
        while drawn != expected_balls:
            copyhat = copy.deepcopy(hat)
            drawn_list = copyhat.draw(num_balls_drawn)
            for item in drawn_list:
                if list(expected_balls.keys()).count(item) != 0: 
                    drawn.update({item : drawn_list.count(item)})
                    print(drawn.items())
            count += 1
        i += 1
    
    return(count/num_experiments)
    


testing(Hat, experiment)