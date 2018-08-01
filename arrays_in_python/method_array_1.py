# Python program to understand various methods of array class.

from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70])   # Creating an array.
print('Original Array: ', arr)

# append 30 to the array

arr.append(30)
arr.append(60)
print('After appending 30 and 60: ', arr)

# insert 999 at position number 1 in arr

arr.insert(1, 999)
print('After inserting 999 in 1st position: ', arr)

# remove an element from arr

arr.remove(20)
print('After remove 20: ', arr)

# remove last element using pop()

n = arr.pop()
print('Array after using pop()', arr)
print('Popped element: ', n)

# finding position of element using index() method

n = arr.index(30)
print('First occurance of 30: ', n)

# convert the array into a list using tolist() method

lst = arr.tolist()
print('List: ', lst)
print('Array: ', arr)

