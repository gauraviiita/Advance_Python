import functools
from timeit import repeat
from unittest import result

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=10)
def greet(name):
    print(f'Hello {name}')

greet('Gaurav')