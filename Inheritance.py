class Person(object):
  def __init__(self):
		self.name = None
		self.age = None
	def info(self):
		print "my Name is %s" % self.name
		print "I'm %s years old." % self.age

class me(Person):
	def __init__(self):
		self.name = "ung"
		self.age = "26"

class Car(object):
	def __init__(self):
		self.name = None
	def value(self):
		print "{0} is a Car." .format(self.name)

class Bus(Car):
	def __init__(self):
		self.name ="Bus"

class Animal(object):
	def info(self):
		print "{0} is a Animal." .format(self.value)

class Dog(Animal):
	def __init__(self):
		self.value = "Dog"
		super(Dog,self).info()
