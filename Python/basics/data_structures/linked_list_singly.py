class node(object):
	def __init__(self, data=None,next=None):
		self.data = data
		self.next = next
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def set_next(self, new_next):
		self.next = new_next

# Insert a node to the linked list

class LinkedList(node):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	def insert(self,data):
		new_node = node(data)
		new_node.set_next(self.head)
		self.head = new_node

# Search the Linked list for a specific value	
	def search(self, data):
		current = self.head
		found = False
		while current != None and found == False:
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
			count += 1
			current = current.get_next()
		return count

	def delete(self,data):
		current = self.head
		previous = None
		found = False
		while current == None and found == False:
			if current.get_data == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current == None:
			raise ValueError("data is not in list")
		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())



list = LinkedList()
list.insert(15)
list.insert(7)
print(list.search(15))
print(list.size())
list.insert(8)
print(list.size())
list.delete(8)
print(list.size())
print(list.search(8))