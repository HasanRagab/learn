from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"💳 Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"💰 Paid ${amount} using PayPal.")

class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount: float):
        self.payment_strategy.pay(amount)

cart1 = ShoppingCart(CreditCardPayment())
cart1.checkout(100.0)  # 💳 Paid $100.0 using Credit Card.

cart2 = ShoppingCart(PayPalPayment())
cart2.checkout(50.0)   # 💰 Paid $50.0 using PayPal.
