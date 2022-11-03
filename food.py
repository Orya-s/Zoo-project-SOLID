class Food:
    def __init__(self, food_type, quantity, unit):
        self.food_type = food_type
        self.qantity = quantity
        self.unit = unit
        
    def get_type(self):
        return self.food_type
    
    def get_amount(self):
        return self.qantity