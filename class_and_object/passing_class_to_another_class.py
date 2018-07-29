# Program to create Emp class and make all the members of the Emp class available to another class, i.e. Myclass.


class Emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # define an instance method:

    def display(self):
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Salary = ", self.salary)


# Another class which displays the details of the employee class:

class Myclass:
    # method to receive Emp class instance, and display employee details.

    @staticmethod
    def my_method(e):
        # increment salary of e by 1000
        e.salary += 1000
        e.display()


# Now create Emp class instance

e = Emp(10, 'Debashis', 50000)

# Call static method of the class - Myclass with passing e

Myclass.my_method(e)

