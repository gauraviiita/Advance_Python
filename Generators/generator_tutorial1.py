def mygenerator():
    yield 28
    yield 'gaurav'
    yield 'yadav'

g = mygenerator()

"""
for i in g:
    print(i)

"""
val = next(g)
print(val)

val = next(g)
print(val)

val = next(g)
print(val)
