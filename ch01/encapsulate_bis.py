class Circle:
    def __init__(self, radius : int):
        self.radius = radius


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


# object consider valid if it has certain attributes or methods
# not enforce at runtime
from typing import Protocol

class Logger(Protocol):
    def log(self, message:str):
        ...

class ConsoleLogger:
    def log(self,message:str):
        print(f"Console : {message}")

    def log2(self,message:str):
        print(f"Console : {message}")



class FileLogger:
    def log(self, message:str):
        print(f"FileLogger : {message}")

def log_message(logger:Logger,message:str):
    logger.log(message)


log_message(ConsoleLogger(),"A console Log")
log_message(FileLogger(),"A file log")


