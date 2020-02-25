#functions as lambdas. old functions are commented out
from functools import reduce

my_list = [1,2,3]

# def multiply_by2(item):
#   return item * 2

print(list(map(lambda item: item*2, my_list)))
  
# def check_odd(item):
#   return item % 2 != 0

print(list(filter(lambda item: item % 2 != 0, my_list)))

# def accumulator(acc, item):
#   print(acc, item)
#   return acc + item

print(reduce(lambda acc, item: acc+item, my_list))

#Square a list
new_list = [5,4,3]

print(list(map(lambda item: item**2, new_list)))

#Sort a list
a = [(0,2), (4,3), (9,9), (10, -1)]

a.sort(key = lambda x: x[1])
# sort function passes each tuple to the lambda as x and by setting the lambda to return x[1] the lambda will return 2 and so the key will be 2
print(a)