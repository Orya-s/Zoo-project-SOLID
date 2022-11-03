from animal import animal

class mammal(animal):
    def __init__(self, name, species, food, preg_duration):
        super().__init__(name, species, food)
        self.preg_duration = preg_duration