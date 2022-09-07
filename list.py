mylist = ['banana', 'cherry', 'apple']
print(mylist)

item = mylist[0]
print(item)
item1 = mylist[-1]
print(item1)

for i in mylist:
    print(i)

# check the item available in list
if 'banana' in mylist:
    print('yes')
else:
    print('no')

# number of element in the list
print(len(mylist))

#append
mylist.append('lemon')
print(mylist)

# append at specific place.
mylist.insert(1, 'blueberry')
print(mylist)

# push and pop in list
# pop remove the last element of thelist.
item2 = mylist.pop()
print(item2)
print(mylist)

# remove a specific element
item3 = mylist.remove('cherry')
print(mylist)

# clear all the list element
item4 = mylist.clear()
print(mylist)


newlist = ['gaurav', 'anupam', 'padmini', 'sitges']
print(newlist)
#reverse the list
item5 = newlist.reverse()
print(newlist)

# sort the list
item = newlist.sort()
print(newlist)

num = [4, 3, 1, -1, -5, 10]


new_list = sorted(num)
print(num)
print(new_list)

print(num)
item = num.sort()
print(num)

l1 = [0]*5
print(l1)

l2 = [1,2,3,4,5]
l3 = l1 + l2
print(l3)

# slicing
l4 = [1,2,3,4,5,6,7,8,9]
l5 = l4[1:5]
print(l5)
l6 = l4[::2]
print(l6)

# coping a list
list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org
print(list_cpy)

list_cpy.append('lemon')
print(list_cpy)
print(list_org)

new_copy = list_org.copy()
print(new_copy)

# list comprehention

a = [1,2,3,4,5,6]
b = [i*i for i in a]
print(a)
print(b)