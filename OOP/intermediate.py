#Composition - 'has a' relationship
class Engine:
    def start(self):
        print("Engine Started...")
    def stop(self):
        print("Engine Stopped...")

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()
        print("Car is now driving...")
    
    def stop(self):
        print("Car has stopped...")
        self.engine.stop()