from food import food
from animals.bird import bird

class goose(bird):
    def __init__(self, name, species="goose", food=food("seeds", 1, "kg"), wing_span=150):
        bird.__init__(self, name, species, food, wing_span)