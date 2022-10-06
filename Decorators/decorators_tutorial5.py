#class decorator

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwds):
        print('Hi there!')

cc = CountCalls(None)
cc()


@CountCalls
def say_hello():
    print('hello')