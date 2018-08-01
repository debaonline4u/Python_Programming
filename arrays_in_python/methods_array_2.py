# Python program to store students' marks into an array and finding total marks and percentage of marks.


from array import *

# accept marks as string

str = input('Enter Marks: ').split(' ')  # enter marks one after another along with white space.
# print(str)
# store marks into marks array:

marks = [int(num) for num in str]
print('marks in the array: ', marks)
# display the marks and find total
total = 0
for x in marks:
    print(x)
    total += x
print('Total marks = ', total)

# Percentage calculation:

n = len(marks)
percent = total / n
print('Percentage: ', percent)

