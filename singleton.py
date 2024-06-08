class Singleton:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls):
        cls.__instance = cls()
        cls.instance = cls.__getInstance
        return cls.__instance


class MyClass(Singleton):
    pass


print(MyClass.instance() == MyClass.instance())  # True
