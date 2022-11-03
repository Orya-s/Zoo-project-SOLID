from food import Food

class Animal:
    def __init__(self, name, species, food:Food):
        self.name = name 
        self.species = species
        self.food = food    
    
    def get_food(self):
        return self.food
    
    def __repr__(self):
        return "animal: \033[94m{}\033[0m - {}".format(self.name, self.species)