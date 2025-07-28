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

