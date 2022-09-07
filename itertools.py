# itertools: product, permutations, combinations, accumulate,
# groupby, and infinite iterators

from itertools import cycle, product
from timeit import repeat
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))
c = [5]
prod1 = product(a, c, repeat=2)
print(list(prod1))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))
perm1 = permutations(a, 2)
print(list(perm1))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))


from itertools import accumulate
import operator
a = [1,2,5, 3,4]
acc = accumulate(a)
print(a)
print(list(acc))

acc1 = accumulate(a, func=operator.mul)
print(a)
print(list(acc1))

acc2 = accumulate(a, func=max)
print(a)
print(list(acc2))


from itertools import groupby

def smaller_than_3(x):
    return x < 3
a = [1,2,3,4] 
groub_obj = groupby(a, key=smaller_than_3)

for key, value in groub_obj:
    print(key, list(value))

     
persons = [{'name':'Gaurav', 'age':28}, {'name':'Anupam', 'age':26},
            {'name':'Lisa', 'age':28}, {'name':'Padmini', 'age':29}]

group_obj = groupby(persons, key=lambda x: x['age'])

for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1,2,3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

for i in repeat(1,5):
    print(i)
    