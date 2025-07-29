#Composition - 'has a' relationship
class Engine:
    def start(self):
        print("Engine Started...")
    def stop(self):
        print("Engine Stopped...")

class Petrol(Engine):
    def start(self):
        print("Vroom! Petrol engine started")
    
    def stop(self):
        print("Brrrrr! Petrol engine stopped")

class Electric(Engine): 
    def start(self):
        print("ZZZZZ! Electric engine started")
    
    def stop(self):
        print("ZZZZZZ! Electric engine stopped")

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()
        print("Car is now driving...")
    
    def stop(self):
        print("Car has stopped...")
        self.engine.stop()


#Abstraction

'''💳 Abstraction Challenge: PaymentMethod System
🎯 Goal:
Create a base PaymentMethod class that defines how payments work, but doesn't implement the actual logic.

✅ Requirements:
Define an abstract class PaymentMethod with an abstract method pay(amount).

Create at least two subclasses that inherit from PaymentMethod:
- CreditCard
- UPI

Each subclass should implement the pay() method differently:
CreditCard → should print something like "Paid ₹500 using Credit Card."
UPI → should print "Paid ₹500 using UPI."

⚠️ Rules:
- You must use from abc import ABC, abstractmethod.
- You cannot create an object of PaymentMethod.
- Only the subclasses can be used to make payments.'''

from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Creditcard(PaymentMethod):
    def pay(self,amount):
        print(f'Paid ₹{amount} using Credit Card.')

class UPI(PaymentMethod):
    def pay(self,amount):
        print(f'Paid ₹{amount} using UPI.')