# 一切皆对象
# 类的实例化中. self 指代实例自己的一块内存空间，一切操作均在自己的内存空间执行，绝不会影响别的其他空间
# 实例中如果使用实例过程中未进行定义的属性或方法，则实例会逐级向上寻找基类、父类等空间中的同名属性或方法，直到找到为止


class B(object):
    description = "livings..."

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.foo()

    def foo(self):
        print("B foo")


class Animal(B):
    name = "xxx"
    note = "livings of animal..."

    foo = 100

    def foo(self):
        print("A foo")


alex = Animal("alex", 23)
print(alex.name, alex.age)
print(alex.description, alex.note)

alex.note = "alex livings of animal..."
alex.description = "alex livings..."
print(alex.description, alex.note)

lee = Animal("lee", 49)
print(lee.name, lee.age, lee.description, lee.note)

B.description = "LIVINGS..."
shuang = Animal("shuang", 45)
print(shuang.name, shuang.description, shuang.note)
