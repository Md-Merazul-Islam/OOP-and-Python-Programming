class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return "Engine Start"


class Driver:
    def __init__(self) -> None:
        pass


class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        print(self.engine.start())


run = Car()
run.start()
