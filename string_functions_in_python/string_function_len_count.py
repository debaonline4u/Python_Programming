# Python code to demonstrate working of 
# len() and count()
str = "geeksforgeeks is for geeks"
  
# Printing length of string using len()
print (" The length of string is : ", len(str));
 
# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""geeks"" is : ",end="")
print (str.count("geeks"))
