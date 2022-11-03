from animal import animal

class mammal(animal):
    def __init__(self, name, species, food, preg_duration):    # preg_duration in months
        animal.__init__(self, name, species, food)
        self.preg_duration = preg_duration
        
    def __repr__(self):
        return "\033[94m{}\033[0m-{}: mammal, pregnancy duration = {} months".format(self.name, self.species, self.preg_duration)