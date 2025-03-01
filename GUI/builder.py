class Burger:
    def __init__(self, bun, patty, cheese=False, lettuce=False, sauce=None):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese
        self.lettuce = lettuce
        self.sauce = sauce

    def __str__(self):
        return f"🍔 Burger with {self.bun} bun, {self.patty} patty, cheese: {self.cheese}, lettuce: {self.lettuce}, sauce: {self.sauce}"

class BurgerBuilder:
    def __init__(self):
        self.bun = "Regular"
        self.patty = "Beef"
        self.cheese = False
        self.lettuce = False
        self.sauce = None

    def set_bun(self, bun):
        self.bun = bun
        return self

    def set_patty(self, patty):
        self.patty = patty
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_lettuce(self):
        self.lettuce = True
        return self

    def set_sauce(self, sauce):
        self.sauce = sauce
        return self

    def build(self):
        return Burger(self.bun, self.patty, self.cheese, self.lettuce, self.sauce)

burger = BurgerBuilder().set_bun("Sesame").set_patty("Meet").set_sauce("BBQ").build()

print(burger)  
