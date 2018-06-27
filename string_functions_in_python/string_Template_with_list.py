# program to demonstrate string template for printing values in list. 

from string import Template

# make a list of student_name and mark for students. 
students=[('Ram',40),('Joshi',75),('Karan',55)]

#creating the basic structure to print the student name and their  marks. 
t=Template("Hi $name, you have got $mark marks. Good Luck. ")

for each_student in students:
    print(t.substitute(name=each_student[0], mark=each_student[1]))
    # here with the substitute function, we are giving values to $name and $mark from the list. 
