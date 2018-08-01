# taking input from keyboard, student marks

from array import *

# str = input('Enter marks: ').split(' ')
# print('Marks entered: (in string) ', str)
#
# marks = [int(mark) for mark in str]
# print('Marks in Array: (in int array) ', marks)

name = input('Enter your name: ').split(' ')
# print('name = ', name)

ch_str = []
for str in name:
    # print(str)
    for ch in str:
        # print(ch)
        ch_str.append(ch)


for ch in ch_str:
    print(ch)