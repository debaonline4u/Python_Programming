# create an array and then apply slicing.
# we can update an existing array through slicing.
# printing a portion of the array through slicing. 

from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

y = arr[4:]   # slicing array.
print('slicing 4 to last ', y)

y = arr[0:]   # slicing array.
print('slicing 0 to last ', y)

y = arr[:4]   # slicing array.
print('slicing first 4 element', y)

y = arr[-4:]   # slicing array.
print('slicing 4 elements from right ', y)

y = arr[-4:-1]   # slicing array.
print('slicing 3 elements towards right', y)

y = arr[0:7:2]   # slicing array.
print('slicing 0 to 7 with step count 2 ', y)

# we can update the array elements through slicing.

arr[1:3] = array('i', [200, 300])   # create a 2 element array and assign it to existing arr array
print('after updating array: ', arr)

# displaying 2 - 4 elements in the array.

for i in arr[2:5]:
    print(i)
