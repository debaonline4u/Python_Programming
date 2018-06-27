# Python code to demonstrate working of 
# center(), ljust() and rjust()
str = "geeksforgeeks"
  
# Printing the string after centering with '-'
print ("The string after centering with '-' is : ",end="")
print ( str.center(20,'-'))
 
# Printing the string after ljust()
print ("The string after ljust is : ",end="")
print ( str.ljust(20,'-'))
 
# Printing the string after rjust()
print ("The string after rjust is : ",end="")
print ( str.rjust(20,'-'))