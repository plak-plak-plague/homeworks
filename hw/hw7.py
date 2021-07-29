def cancel_func(func):
    def wrapper():
        print(f'{func.__name__} is canceled!')

    return wrapper


from datetime import datetime


def time_counter(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()

        print(f'Function moving {end - start} times')

    return wrapper


class Counter:
    instance = {}

    @staticmethod
    def call_func(func):

        def wrapper():

            if func.__name__ in Counter.instance.keys():
                Counter.instance[func.__name__] += 1
            else:
                Counter.instance[func.__name__] = 1

            print(f'{func.__name__} is called {Counter.instance[func.__name__]} times')

        return wrapper


def logger(func):
    print('Decorator created!')

    def wrapper():
        print('Func start here!')
        func()
        print('Func ends!')

    return wrapper


def catcher(func):
    def wrapper():

        try:
            func()
        except Exception as e:
            print('In func was error: ', e)

    return wrapper


from functools import reduce

print(list(map(lambda x: x % 5, [1, 4, 5, 30, 99])))
print(list(map(lambda x: str(x), [3, 4, 90, -2])))
print(list(filter(lambda x: not isinstance(x, str), ['some', 1, 'v', 40, '3a', str])))
print(reduce(lambda x, y: x + y, list(len(x) for x in ['some', 'other', 'value'])))

