# understnding class method

class Bird:
    # declaring a class variable:

    wings = 2

    # declaring a class method:

    @classmethod
    def fly(cls, name):
        print("{} flies with {} wings".format(name, cls.wings))


# Now display information for 2 birds

Bird.fly('Sparrow')
Bird.fly('Pigeon')
print('\n')