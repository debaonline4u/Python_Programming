# example of static method; to calculate x to the power of n


class Myclass:
    @staticmethod
    def my_method(x, n):
        result = x ** n
        print('{} to the power of {} is {}'.format(x, n, result))


# Using the static method

Myclass.my_method(2, 3)
Myclass.my_method(4, 5)
