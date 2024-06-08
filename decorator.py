def log(func):
    def wrapper(*args, **kwargs):
        print(f'start {func.__name__} function')
        func(*args, **kwargs)
        print(f'end {func.__name__} function')

    return wrapper


def wow(func):
    def wrapper(*args, **kwargs):
        print('wow')
        func(*args, **kwargs)

    return wrapper


def limit_calls_decorator(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                raise Exception("함수 호출 횟수 초과")

        return wrapper

    return decorator


@limit_calls_decorator(3)
def example_function():
    print("예제 함수 실행")


@log
@wow
def printHello():
    print("Hello")


class TestExample:
    def _decorator(func):
        def wrap(self, *args, **kargs):
            print("Start", func.__name__)
            func(self, *args, **kargs)
            print("End", func.__name__)

        return wrap

    @_decorator
    def test(self, a, b, c):
        print("Variables :", a, b, c)


class emoticon:
    def __init__(self, emoticon):
        self.count = 0  # 호출 회수 저장 필드
        self.emoticon = emoticon

    def __call__(self, func):
        def inner(*args, **kwargs):
            self.count += 1
            inner.count = self.count  # 함수 객체에서 바로 사용 할 수 있도록
            print(self.emoticon, ' ', end='')

            return func(*args, **kwargs)

        return inner


@emoticon('-_-')
def say_hi(name):
    print(f'hi {name}!')


say_hi('Jason')
print(say_hi.count)
