def testing(test_class):
    
    hat1 = test_class(yellow=3, blue=2, green=6)
    
    def test_contents(test_class):
        print(test_class.contents)
   
    test_contents(hat1)