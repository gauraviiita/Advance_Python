import random

a = random.random()
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10)
print(a)

a = random.randrange(1,5)
print(a)

a = random.normalvariate(0, 1)
print(a)

mylist = list('abcdefgh')
print(mylist)
a = random.choice(mylist)
print(a)
a = random.sample(mylist, 3)
print(a)

a = random.choices(mylist, k=3)
print(a)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

