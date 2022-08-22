from enum import Enum, auto
from abc import abstractmethod, ABC


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"I am a person, and my name is {self.first_name} {self.last_name}"


foo = Person(first_name="Lee", last_name="Zhaohong")
zenith = Person(first_name="Lee", last_name="Zenith")
print(foo, zenith)


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.GREEN.value, Color.GREEN.name)
print(repr(Color.RED))
print(type(Color.RED))

# Three methods to get the memeber of enums
color1 = Color(3)
print(color1)

color2 = Color["RED"]
print(color2)

color3 = Color(2)
print(color3)

print(isinstance(color1, Color))


class State(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


print("**********")
print(State.PLAYING)
print(State.PAUSED.value, State.PAUSED.name)


my_values = {"one": 1, "two": 2}
your_values = {"three": 3, "four": 4}

new_values = dict(my_values, **your_values)
print(new_values)

print(new_values.keys())
print(new_values.values())


# something about set
names = {"jiajia", "lee", "tingting", "lee"}
print(names)
for item in names:
    print(item)
print(len(names))


# something about abstract based class
# Prevents a user from creating an object of that class(abstracted based class).
# comples a user to override abstract methods in a child class.
# abstract class = a class which contains one or more abstract methods.
# abstract method  = a method that has a declaration but does not have an implementation.


class Car(ABC):
    def __init__(self, speed, year):
        self.__speed = speed
        self.__year = year

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

    @abstractmethod
    def drive(self):
        print("Car is driving...")


class Tesla(Car):
    def __init__(self, speed, year, model):
        super().__init__(speed, year)
        self.__modle = model

    def drive(self):
        print("Tesla is driving...")


# Can't instantiate abstract class Car with abstract methods drive
# car = Car()
tesla = Tesla(100, 2023, "Model X")
tesla.start()
tesla.drive()
tesla.stop()


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Getting the name for you...")
        return self.__name

    @name.setter
    def name(self, new_value):
        if new_value == "Foo":
            raise ValueError("This is not acceptable")
        else:
            self.__name = new_value


person = Person("kate")
person.name = "lee"
print(person.name)
