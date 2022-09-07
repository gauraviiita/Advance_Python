# Strings: ordered, immutable, text representation
my_string = "hello world"
print(my_string)

st = 'I\'m a programmer'
print(st)
new_st = "I'm a pro"
print(new_st)

st = """Hello
world"""
print(st)

my_st = 'hello world'
char = my_st[-3]
print(char)
sub = my_st[1:5]
print(sub)

sub1 = my_st[::1]
print(sub1)
sub2 = my_st[::2]
print(sub2)

a1 = 'hello'
a2 = 'gaurav'
new = a1 + " " + a2
print(new)

for i in a1:
    print(i)

if 'e' in a1:
    print('yes')
else:
    print('no')

s = '    hello world   '
print(s)
s = s.strip()
print(s)

strg = 'hello world'
print(strg.startswith('hell'))
print(strg.endswith('rld'))

print(strg.find('0'))
print(strg.find('llo'))

print(strg.count('l'))

print(strg.replace('world', 'universe'))

st = 'how are you doing'
lt = st.split()
print(lt)
from timeit import default_timer as timer

nw = ' '.join(lt)
print(nw)

list = ['a']*6
print(list)

my_str = ''
for i in list:
    my_st += i
print(my_str)
print(my_st)

my_string = ''.join(list)
print(my_string)

# %, .format

var = 'Tom'
my_string = 'the variable is %s'%var
print(my_string)

var = 3.1234
m = 'the variable has %.3f'%var
print(m)
var2 = 9
n = 'the variable is {} and second is: {}'.format(var, var2)
print(n)
var1 = 'gaurav'
new_way = f"my name is {var1} and my age is {var2+2}"
print(new_way)
