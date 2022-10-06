# lambda arguments: expression
from functools import reduce


add10 = lambda x: x + 10

print(add10(5))

def add10_fun(x):
    return x + 10

print(add10_fun(5))

#lambda func with multiple arguments
mult = lambda x, y: x*y
print(mult(2,4))

points2d = [(1,2), (15, 1), (15, -1), (10, 4)]
point2d_sorted = sorted(points2d)
print(points2d)
print(point2d_sorted)

point2d_sorted_using_lambda = sorted(points2d, key=lambda x: x[1])
print(point2d_sorted_using_lambda)

def sort_by_y(x):
    return x[1]

point2d_sorted_using_fun = sorted(points2d, key=sort_by_y)
print(point2d_sorted_using_fun)


sort_lambda_sum = sorted(points2d, key=lambda x: x[0] + x[1])
print(sort_lambda_sum)

print('map function')

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(b)
print(list(b))

c = [x*2 for x in a]
print(c)

print('filter function')

a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)
print('reduce function')

from functools import reduce
a = [1,2,3,4,5,6]
prod = reduce(lambda x, y: x*y, a)
print(prod)