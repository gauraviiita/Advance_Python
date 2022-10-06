def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

val = next(cd)
print(val)
val = next(cd)
print(val)
print(next(cd))
print(next(cd))