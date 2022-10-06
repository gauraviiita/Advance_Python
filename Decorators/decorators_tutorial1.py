# there are two types of decorators, 1 function decorator and 2 is class decorator

def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('Gaurav')
#print_name = start_end_decorator(print_name)

print_name()

