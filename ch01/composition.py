class Engine:
    def start(self):
        print("Engine Start")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("car started")


my_car = Car()
my_car.start()