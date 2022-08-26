# reflection 反射 getattr method
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print("foo...")

    def good(self):
        print("good...")


alex = Animal("alex", 30)


user_input_attr = input("Please input the attributes you want to see: ")
print(getattr(alex, user_input_attr, "Sorry, your input is invalid."))


getattr(alex, "good")()
