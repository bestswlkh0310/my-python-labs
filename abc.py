from abc import *


class Flyable(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): ...


class Airplane(Flyable):
    # def fly(self):
    #     print('fly~~')
    ...

airplane = Airplane()
airplane.fly()
