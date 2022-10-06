def my_generator():
    yield 28
    yield 7
    yield 34
g = my_generator()
print(sorted(g))


