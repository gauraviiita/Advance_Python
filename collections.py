# Collections: Counter, namedtuple, OrderedDict,
# defaultdict, deque


from collections import Counter

a = 'sabldaaaabbbccc'
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter.most_common(2))

print(list(my_counter.elements()))

from collections import namedtuple

point = namedtuple('point', 'x,y')
pt = point(1,-4)
print(pt)

print(pt.x, pt.y)

from collections import OrderedDict

order_dict = OrderedDict()
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['d'] = 4
print(order_dict)

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])

from collections import deque
d = deque()
d.append(1)
d.append(3)
print(d)
d.appendleft(4)
print(d)
d.pop()
print(d)
d.extend([4,5,6,7])
print(d)

d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)