from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, food, wing_span):   # wing_span in cm 
        Animal.__init__(self, name, species, food)
        self.wing_span = wing_span
        
    def __repr__(self):
        return super().__repr__() + ": bird, wing span = {} cm".format(self.wing_span)