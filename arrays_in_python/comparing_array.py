# Python program to compare two arrays and display resultant Boolean type array.

from numpy import *

a = array([1, 2, 3, 0])
b = array([0, 2, 3, 1])

# c = a == b
# print('Result of a==b: ', c)

c = a > b
print('Result of a>b: ', c)

# c = a <= b
# print('Result of a<b: ', c)

# effect of any() and all() function.

print('Check if any one element is true: ', any(c))
print('Check if all elements are true: ', all(c))

if any(a > b):
    print('a contains at least one element greater than those of b')
