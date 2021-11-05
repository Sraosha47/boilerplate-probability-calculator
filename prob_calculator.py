import copy
import random
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
            if amount >= len(self.contents):
                drawn.extend(self.contents)
                self.contents.clear()
                return(drawn)
            else:    
                while i < amount:
                    x = len(self.contents)
                    ran_ball = random.choice(self.contents)
                    drawn.append(ran_ball)
                    self.contents.remove(ran_ball)
                    i += 1
                drawn.sort()
                return(drawn)



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = 0
    count = 0
    drawn_dic = []
    keys_expected = list(expected_balls.keys())
    print("expected keys:", keys_expected)
        
    if len(hat.contents) <= num_balls_drawn:
        return(1.0)

    else:
        while i <= num_experiments:
            print("\nExperiment " + str(i))
            copyhat = copy.deepcopy(hat)
            keycount = 0
            drawn_list = copyhat.draw(num_balls_drawn)
            print(drawn_list)
            print(list(expected_balls.keys()))
            for item in drawn_list:
                if list(expected_balls.keys()).count(item) != 0: 
                    drawn_dic.append(item)
                print("Drawndic:",drawn_dic)
            for key, value in expected_balls.items():
                if value <= drawn_dic.count(key):
                    print("Balls expected:", expected_balls[key], "Balls drawn:", drawn_dic.count(key))
                    keycount += 1
                    print("keycount:", keycount)
            if keycount == len(keys_expected):
                print("\nball types expected: ", (len(keys_expected)))
                count += 1
                print("Count:",count)
            drawn_dic.clear()
            i += 1
        return(count/num_experiments)


