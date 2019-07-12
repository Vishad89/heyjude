class contact:
	
	def __init__(self, first, last, number):
		self.first = first
		self.last = last
		self.number = number
		self.email = first + last + "@helloworld.us"

person1 = contact("vishad", "sanghvi", 9495054695)

print(person1.email)

