class SuperClass:
    def __init__(self):
        self.b = 10


class SuperSuperClass:
    def __init__(self):
        self.c = 10


MyClass = type('MyClass', (SuperClass,), {
    'a': 10,
    'fun': lambda _: print("Hello")
})


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass


foo = Foo()


# print(foo.attr)


class Base:
    attr = 100


class X(Base):
    pass


class Y(Base):
    pass


class Z(Base):
    pass


# print(X.attr)
# print(Y.attr)
# print(Z.attr)


def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


print(X.attr)
print(Y.attr)
print(Z.attr)
