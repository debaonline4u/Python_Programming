# instance method to process data of the objects
class Student:
    # defining the constructor
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m
    # defining an instance method

    def display(self):
        print('Hi ', self.name)
        print('Marks = ', self.marks)
    # function to calculate the gardes of the student

    def calculate(self):
        if(self.marks >= 600):
            print('{} got first division with marks{}'.format(self.name, self.marks))
        elif(self.marks >= 500 ):
            print('{} got second division with marks{}'.format(self.name, self.marks))
        elif(self.marks >= 350):
            print('{} got third division with marks{}'.format(self.name, self.marks))
        else:
            print("{}, You are failed. Good Luck for next attempt. You mark is {}".format(self.name, self.marks))

# Now create some instances of the Student class.

number = int(input('How many students? \n'))

i=0
while(i < number):
    name = input('Enter name of student: \n')
    marks = int(input('Enter marks \n'))

    # Now create student class instance and store name and marks
    s = Student(name,marks)
    s.display()
    s.calculate()

    i += 1
    print('\n')