# tuples is a collection datatype
# it is ordered imutable. The main differenc
# between tuples and list is tuples can not
# be changed once it is created.

mytuple = ("max", 28, "Sitges") # () are optional
t1 = 'gaurav', 28, 'barcelona'
print(mytuple)
print(t1)
print(type(mytuple))
t2 = ('gaurav',)
print(type(t2))

t = tuple(['max', 28, 'sitges'])
print(t)
item = t[0]
print(item)

# change the element inside the list
#t[0] = 'tim' # it show error bcz tuple is not changeable

for i in t:
    print(i)

if 'max' in t:
    print('yes')
else:
    print('no')

t4 = ('a', 'p', 'p', 'l', 'e')
print(t4.count('p'))

print(t4.index('l'))

#convert a list into tuples
mylist = list(t4)
print(type(mylist))
t5 = tuple(mylist)
print(type(t5))

a = (1,2,3,4,5,6,7,8,9)
b = a[2:5]
print(b)
c = a[:6]
print(c)
d = a[::2]
print(d)
e = a[::-1]
print(e)

new_t = 'max', 28, 'sitges'
name, age, city = new_t
print(name)
print(age)
print(city)

t = (0,1,2,3,4,5,6)
i1, *i2, i3 = t
print(i1)
print(i2)
print(i3)

# compare list and tuple
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
