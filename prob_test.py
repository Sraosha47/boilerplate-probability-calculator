def testing(test_class, test_function):
    
    hat1 = test_class(red=5,blue=2)
    
    def test_contents(test_class):
        print("Contents:", test_class.contents)
   


    def test_draw(test_class):
        print("Drawn balls", test_class.draw(2))
        print(len(test_class.contents))

    def test_experiment(test_function):
        print( "The probability is:", test_function(hat=hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
        

    test_contents(hat1)
    test_draw(hat1)
    test_contents(hat1)
    test_experiment(test_function)