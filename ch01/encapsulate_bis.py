class Circle:
    def __init__(self, radius : int):
        self._radius = radius


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value:int):
        if value < 0:
            raise ValueError("Radius can not be negative")
        self._radius = value


if __name__ == "__main__":
    circle = Circle(10)
    print(f" Intiliaz radius : {circle.radius}")

    circle.radius = 10
    print(f" New Radius: {circle.radius}")


