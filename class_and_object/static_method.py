# understanding static method
class Myclass:
    # defining a class variable or static variable
    n=0

    def __init__(self):
        Myclass.n = Myclass.n+1

    # static method to display the no. of instance

    @staticmethod
    def no_object():
        print("No of instances created: ", Myclass.n)


# Creating 3 instances

obj1 = Myclass()
obj1 = Myclass()
obj1 = Myclass()
obj1 = Myclass()
obj1 = Myclass()

Myclass.no_object()