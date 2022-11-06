from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, food, preg_duration):    # preg_duration in months
        Animal.__init__(self, name, species, food)
        self.preg_duration = preg_duration
        
    def __repr__(self):
        return super().__repr__() + ": mammal, pregnancy duration = {} months".format(self.preg_duration)