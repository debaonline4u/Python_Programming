# instance vars example


class Sample:

    # defining constructor

    def __init__(self):
        self.x = 10

    def modify(self):
        self.x += 1


# Now create instance of the sample class

s1 = Sample()
s2 = Sample()

print('Before modify: ')
print("s1.x = ", s1.x)
print("s2.x = ", s2.x)

s1.modify()

print('After modify: ')
print("s1.x = ", s1.x)
print("s2.x = ", s2.x)
