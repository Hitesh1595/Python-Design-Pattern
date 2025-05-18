class Bird:
    def move(self):
        print("I am moving")

class FlyingBird(Bird):
    def move(self):
        print("I am walking")

class FlightlessBird(Bird):
    def move(self):
        print("I ma walking")



def make_bird(bird):
    bird.move()



if __name__ == "__main__":

    generic_bird = Bird()
    eagle = FlyingBird()
    penguin = FlightlessBird()

    make_bird(generic_bird)
    make_bird(eagle)
    make_bird(penguin)

