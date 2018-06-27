# Python code to demonstrate the working of
# index() and count()
# initializing list 1
lis = [2, 1, 3, 5, 4, 3]
 
# using index() to print first occurrence of 3
# prints 5
print ("The first occurrence of 3 after 3rd position is : ", end="")
print (lis.index(3, 3, 6))
 
# using count() to count number of occurrence of 3
print ("The number of occurrences of 3 is : ", end="")
print (lis.count(3))
