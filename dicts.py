mydict = {'name':'Gaurav', 'age':28, 'city':'sitges'}
print(mydict)

dict1 = dict(name='anupam', age='26', city='pune')
print(dict1)

value = mydict['age']
print(value)

# a dictionary is mutable so we can change and update
# item in dictionary

mydict['email'] = 'gky@gmail.com'
print(mydict)

# delete element

del mydict['name']
print(mydict)

dict1.pop('age')
print(dict1)

dict1.popitem()
print(dict1)

d2 = {'name':'Gaurav', 'age':28, 'city':'sitges'}
if "name" in d2:
    print(d2['name'])

try:
    print(d2['name'])
except:
    print('error')

for key in d2.keys():
    print(key)

for key, value in d2.items():
    print(key, value)

# copy a dictionary

d_cpy = dict(d2)
d_cpy1 = d2.copy()

# update method

d1 = {'name':'Gaurav', 'age':28, 'city':'sitges', 'email':"a@gamil.com"}
print(d1)

d2 = dict(name='anupam', age='26', city='pune')
print(d2)

d1.update(d2)
print(d1)

d11 = {1:3, 5:12, 7:123}
print(d11)
value = d11[1]
print(value)

mytuple = (8,7)
mydict = {mytuple:15}
print(mydict)