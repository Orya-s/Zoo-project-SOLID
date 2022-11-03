from food import food

class animal:
    def __init__(self, name, species, food:food):
        self.name = name 
        self.species = species
        self.food = food    
    
    def get_food(self):
        return self.food
    
    def print_animal(self):    # operator overloading __str__ ?
        pass
    