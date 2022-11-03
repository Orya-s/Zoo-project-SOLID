from animal import animal

class bird(animal):
    def __init__(self, name, species, food, wing_span):   # wing_span in cm 
        animal.__init__(self, name, species, food)
        self.wing_span = wing_span
        
    def __repr__(self):
        return "\033[94m{}\033[0m-{}: bird, wing span = {} cm".format(self.name, self.species, self.wing_span)