# Python program to implement Linear Search.


from array import *

arr = array('i', [])  # Creating an empty array.
print('How many elements you want to enter: ', end='')
n = int(input())

for i in range(n):
    print('Enter elements: ', end='')
    arr.append(int(input()))

print('Original Array: ', arr)

s = int(input('Enter element to search: \n'))

# Now implement Linear search.
#
# flag = False
# for i in range(n):
#     if s == arr[i]:
#         print('{} found at position: {}'.format(s, i+1))
#         flag = True
#
# if flag is False:
#     print('{} not found in the array. '.format(s))

# implementing position of the number using index()

try:
    pos = arr.index(s)
    print('{} found at position: {}'.format(s, pos + 1))
except ValueError:
    print('{} not found in the array. '.format(s))