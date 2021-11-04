def testing(test_class):
    
    hat1 = test_class(yellow=3, blue=2, green=6)
    
    def test_contents(test_class):
        print("Contents:", test_class.contents)
   


    def test_draw(test_class):
        print("Drawn balls", test_class.draw(3))

    test_contents(hat1)
    test_draw(hat1)
    test_contents(hat1)