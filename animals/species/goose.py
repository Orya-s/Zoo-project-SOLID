from food import Food
from animals.bird import Bird

class Goose(Bird):
    def __init__(self, name, species="goose", food=Food("seeds", 1, "kg"), wing_span=150):
        Bird.__init__(self, name, species, food, wing_span)