# Abstract class demonstrating Abstraction
from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @abstractmethod
    def prepare(self):
        pass

    def display_dish(self):
        print(f"Dish: {self.name}, Ingredients: {', '.join(self.ingredients)}")

# Inheritance: IndianDish and SouthIndianDish inherit from Dish
class IndianDish(Dish):
    def __init__(self, name, ingredients, spice_level):
        super().__init__(name, ingredients)  # Constructor demonstrating Inheritance
        self.spice_level = spice_level

    # Encapsulation: Private attribute __is_prepared
    __is_prepared = False

    def prepare(self):
        if not self.__is_prepared:
            self.__is_prepared = True
            print(f"{self.name} is being prepared with spice level: {self.spice_level}")
        else:
            print(f"{self.name} is already prepared.")

    def serve(self):
        if self.__is_prepared:
            print(f"{self.name} is served.")
        else:
            print(f"{self.name} is not prepared yet.")

class SouthIndianDish(Dish):
    def __init__(self, name, ingredients, type_of_dosa):
        super().__init__(name, ingredients)
        self.type_of_dosa = type_of_dosa

    def prepare(self):
        print(f"{self.name} ({self.type_of_dosa}) is being prepared.")

    def serve(self):
        print(f"{self.name} ({self.type_of_dosa}) is served hot with chutney and sambar.")

# Polymorphism: Same method name but different behavior
def serve_dish(dish):
    dish.prepare()
    dish.serve()

# Destructor: Demonstrating cleanup when object is deleted
class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Customer {self.name} arrived at the restaurant.")

    def __del__(self):
        print(f"Customer {self.name} has left the restaurant.")

# Creating dishes
paneer_bhurji = IndianDish("Paneer Bhurji", ["Paneer", "Onion", "Tomato", "Spices"], "Medium")
masala_dosa = SouthIndianDish("Masala Dosa", ["Rice Batter", "Potato", "Spices"], "Crispy")

# Creating a customer
customer1 = Customer("Rahul")

# Encapsulation and Inheritance in action
paneer_bhurji.display_dish()
masala_dosa.display_dish()

# Polymorphism in action
serve_dish(paneer_bhurji)
serve_dish(masala_dosa)

# Destructor demonstration
del customer1
