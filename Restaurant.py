class MenuItem():
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

class MainCourse(MenuItem):
    def __init__(self, flour:str, protein:str, salad:str, name:str, price:float):
        super().__init__(name, price)
        self.flour = flour
        self.protein = protein
        self.salad = salad
        
    def __str__(self):
        return f"{self.name} ({self.flour}, {self.protein}, {self.salad}) - ${self.price:.2f}"

class Dessert(MenuItem):
    def __init__(self, name:str, price:float, type:str):
        super().__init__(name, price)
        self.type = type
    def __str__(self):
        return f"{self.name} ({self.type}) - ${self.price:.2f}"
    
class Drink(MenuItem):
    def __init__(self, name:str, price:float, size:str, hasSugar:bool):
        super().__init__(name, price)
        self.size = size
    def __str__(self):
        return f"{self.name} ({self.size}) - ${self.price:.2f}"

class Order():
    def __init__(self, items:list[MenuItem]):
        self.items = items
    
    def add_item(self, item:MenuItem):
        self.items.append(item)
    
    def __calcSubcounts(self, partial):
        dicounts = 0
        if len(self.items) >= 3:
            dicounts += 0.1 * partial
        return dicounts
            
    
    def getTotalBill(self):
        self.partial = sum(item.price for item in self.items)
        self.discounts = self.__calcSubcounts(self.partial)
        return self.partial - self.discounts
    
    def __str__(self):
        return "\n".join(str(item) for item in self.items)
    
if __name__ == "__main__":
    # Example usage
    grilled_Chicken = MainCourse("Wheat", "Chicken", "Caesar Salad", "Grilled Chicken", 12.99)
    cake = Dessert("Chocolate Cake", 4.99, "Cake")
    coke = Drink("Coke", 1.99, "Medium", True)
    taco = MainCourse("Corn", "Beef", "Greek Salad", "Taco", 8.99)
    lemonade = Drink("Lemonade", 2.49, "Large", False)
    coockies = Dessert("Cookies", 3.49, "Cookies")
    burrito = MainCourse("Wheat", "Chicken", "Greek Salad", "Burrito", 10.99)
    hotdog = MainCourse("Corn", "Beef", "Caesar Salad", "Hot Dog", 5.99)
    beer = Drink("Beer", 4.99, "Large", True)
    candy = Dessert("Candy", 1.99, "Candy")
    
    order = Order([grilled_Chicken, cake, coke, taco, lemonade, coockies, burrito, hotdog, beer, candy])
    print("Order Details:")
    print(order)
    print(f"Total Bill: ${order.getTotalBill():.2f}")
    print(f"aplicable discounts: ${order.discounts:.2f}")
