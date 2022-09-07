# Sets: unordered, mutable, no duplicates

myset = {1,2,3,1,3}
print(myset)

s = set('hello')
print(s)

#empty set
s1 = {}
s2 = set()
print(type(s1))
print(type(s2))

s2.add(2)
s2.add(3)
s2.add(5)
print(s2)
s2.remove(5)
print(s2)

for i in s2:
    print(i)

if 1 in s2:
    print('yes')

else:
    print('no')

odds = {1,3,5,7,9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1, 2, 3, 10, 11, 12}
setC = {7, 8}
diff = setA.difference(setB)
print(diff)

new_diff = setA.symmetric_difference(setB)
print(new_diff)

setA.update(setB)
print(setA)

print(setA.issubset(setB))
print(setB.issubset(setA))


print(setA.issuperset(setB))

print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

new_set = setA.copy()

a = frozenset([1,2,3,4,5])
print(a)