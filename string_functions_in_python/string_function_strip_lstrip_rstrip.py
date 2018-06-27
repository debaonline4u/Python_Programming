# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"
 
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )
 
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )
 
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )
