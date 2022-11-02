
class zoo:
    def __init__(self):
        self.animals = []
        self.food_supply = {}   # {"food_type":amount}
        self.restock_amount = 100
        
    def add_animal(self, animal):
        self.animals.append(animal)
        self.add_food(animal.get_food().get_type())
        
    def add_food(self, food):
        if food not in self.food_supply:
            self.food_supply[food] = self.restock_amount
            
    def print_zoo(self):
        print(self.animals)
        
    def feed_animal(self, food_type, amount):
        if self.food_supply[food_type] - amount < 0:
            self.restock(food_type)
        self.food_supply[food_type] -= amount
        
    def restock(self, food):
        print("{} ran out, filling the suplly...".format(food))
        self.food_supply[food] += self.restock_amount
        