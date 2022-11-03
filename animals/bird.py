from animal import animal

class bird(animal):
    def __init__(self, name, species, food, wing_span):   # wing_span in cm 
        animal.__init__(self, name, species, food)
        self.wing_span = wing_span