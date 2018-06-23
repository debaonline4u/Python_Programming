# Python code to demonstrate working of 
# find() and rfind()
str = "geeksforgeeks is for geeks"
str2 = "geeks"
 
# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) )
 
# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )