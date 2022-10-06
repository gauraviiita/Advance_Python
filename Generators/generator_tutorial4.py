# generator is memory efficient technique it save lot of data
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
mylist = firstn(10)
#print(mylist)
#print(sum(mylist))
print(sys.getsizeof(firstn(100000)))
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
    
#print(sum(firstn_generator(10)))
print(sys.getsizeof(firstn_generator(100000)))