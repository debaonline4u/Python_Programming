import static_method_2
from static_method_2 import Sample as sam
num = int(input('Enter Number for square root \n'))
print("Square root of {} is {:.3f}".format(num, static_method_2.Sample.calculate(num)))
print("\nAccessing Sample class variable",sam.data)
