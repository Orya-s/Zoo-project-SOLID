from animal import animal

class bird(animal):
    def __init__(self, name, species, food, wing_span):
        super().__init__(name, species, food)
        self.wing_span = wing_span