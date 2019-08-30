import random

class Example:

    @staticmethod
    def add(x,y):
        return float(x + y)
    
    @staticmethod
    def random_with_constant(constant):
        return constant +  random.randint(1,3)