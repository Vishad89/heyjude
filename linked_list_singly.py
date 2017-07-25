class node(object):
	
	def __init__(self, data):
		self.data = None
		self.next = None

	def isEmpty(self):
		return self.head == None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

# Insert a node to the linked list

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		

	def insert(self,data):
		temp = node(data)
		temp.set_next(self.head)
		self.head = temp

# Search the Linked list for a specific value	
# Need some work here

	def search(self, data):
		current = self.head
		found = False
		while current != None and found == False:
			print found
			print data, current.get_data()
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()

		return found

# Get the size of the Linked list

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()
		
		return count



list = node(93)
list.insert(15)
list.insert(7)
print list.search(15)
print list.size()