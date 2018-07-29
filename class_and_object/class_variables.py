# class vars or static variable example

class sample:
	# defining constructor
	x = 10
	y = 20

	@classmethod			
	def modify(cls):
		cls.x +=1

	def __init__(self):
		self.a = 50
		self.b = 60

	#def printab(self):
		


# Now create instance of the sample class

s1 = sample()
s2 = sample()

print('Before modify: ')
print("s1.x = ",s1.x)
print("s2.x = ",s2.x)

s1.modify()

print('After modify: ')
print("s1.x = ",s1.x)
print("s2.x = ",s2.x)

print("Accessing class variable outside of class: y = ", sample.y)
print("Printing instance variable a = {}, b = {}".format(s1.a,s1.b))