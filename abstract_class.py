from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def __str__(self):
        return f"The car model is {self.model}."

    @abstractmethod
    def drive(self):
        pass

    def start(self):
        print("Car is starting....")


class Tesla(Car):
    def __init__(self, year, model, info):
        super().__init__(year, model)
        super().__str__()
        self.info = info

    def stop(self):
        print("Tesla was stopped....")

    def drive(self):
        print("Tesla is driving...")


tesla = Tesla("2021", "Model X", "E Car")
tesla.drive()
tesla.stop()
print(tesla)
