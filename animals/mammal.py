from animal import animal

class mammal(animal):
    def __init__(self, name, species, food, preg_duration):    # preg_duration in months
        animal.__init__(self, name, species, food)
        self.preg_duration = preg_duration