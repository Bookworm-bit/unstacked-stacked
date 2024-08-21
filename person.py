import random

class Person:
    def __init__(self):
        self.knowledge = random.uniform(0, 1)
        self.consistency = random.uniform(0, 1)

    def get_performance(self):
        return min(max((self.knowledge + random.uniform(-(1-self.consistency), 0)) * 100, 0), 100)
    
    def get_good_consistent(self):
        return self.knowledge > 0.75 and self.consistency > 0.75

    def __repr__(self):
        return f"k={self.knowledge}, c={self.consistency}"