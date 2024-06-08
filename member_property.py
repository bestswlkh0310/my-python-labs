class MyClass:
    def __init__(self):
        self.a = 1


c = MyClass()
# print(dir(c))
# print(c.__dict__)


import inspect

print(inspect.getmembers(c))
