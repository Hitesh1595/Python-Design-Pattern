# use of abstract method
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message:str):
        pass


class ConsoleLogger(Logger):
    def log(self,message:str):
        print(f"Console : {message}")


class FileLogger(Logger):
    def log(self, message:str):
        print(f"FileLogger : {message}")


def log_message(logger:Logger,message:str):
    logger.log(message)


if __name__ == "__main__":


    log_message(ConsoleLogger(),"A console Log")
    log_message(FileLogger(),"A file log")




