# Progrm to demonstate instance and class

class student:
    def __init__(self,name = 'Sachin', age = 42, msg = 'God of Cricket '):    # it's the constructor
        self.name =  name
        self.age=age
        self.description = msg

    def talk(self):
        print("Hi I am " + self.name)
        print("My age: ", self.age)
        print("I am  " + self.description)

# Now creating a student object
s1 = student('dhoni',34,'Former Indian Captain')
s1.talk()

s2 = student()
s2.talk()

