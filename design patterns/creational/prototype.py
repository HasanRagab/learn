import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Product(Prototype):
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, details={self.details})"

original = Product("Laptop", 1200, {"brand": "Dell", "ram": "16GB"})

clone1 = original.clone()
clone1.details["ram"] = "32GB"  

print("Original:", original)  # Laptop with 16GB RAM
print("Clone1:", clone1)      # Laptop with 32GB RAM
