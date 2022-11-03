from food import food
from animals.bird import bird

class snowy_owl(bird):
    def __init__(self, name, species="snowy owl", food=food("worms", 100, "grams"), wing_span=52):
        bird.__init__(self, name, species, food, wing_span)