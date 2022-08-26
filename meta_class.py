def hello():
    class Hi:
        pass

    return Hi


class Test:
    pass


print(Test)
print(type(Test()))
print(type(hello))
print(Test())
print("****")


class Foo:
    def show(self):
        print("hello!")


def add_attribute(self):
    self.z = 9


Test1 = type("Test1", (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test1()
t.add_attribute()
t.wy = "ni hao"
t.show()
print(t.z)
print("***** Meta class **********")


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hi, Meta class can change the fuc name uppercase.")


d = Dog()
print(d.X)
d.HELLO()
