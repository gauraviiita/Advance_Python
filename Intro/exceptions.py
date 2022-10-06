# errors and exceptions
#a = 5  print(a) # give syntex error

#a = 5 + '10' #give type error
#import somemodule #give module not found error

#a = 5
#b = c # name error

#f = open('somefile.txt') #filenot found error

#a = [1,3,8]
#a.remove(2) #value error

#a = [1,2,3]
#a[4] #index error

#my_dict = {'name': 'Gaurav'}
#my_dict['age'] #keyerror

#x = -5
#if x < 0:
#    raise Exception('x should be positive')

#assert (x >=0), 'x is not positive' #assertion error

####
#a = 5/0 # zero division error
'''
try:
    a = 5/0
#except:
    #print('an error happend')
except Exception as e:
    print(e)
'''
'''
try:
    a = 5/1
    b = a +4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up....')
'''

class ValueToHighError(Exception):
    pass

class ValuetoSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueToHighError('Value is too high')
    if x < 5:
        raise ValuetoSmallError('Value is too small', x)
try:
    test_value(1)
except ValueToHighError as e:
    print(e)
except ValuetoSmallError as e:
    print(e.message, e.value)