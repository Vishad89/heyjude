class node(object):
	
	def __init__(self, data = None):
		self.data = data
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

class LinkedList(node):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		

	def insert(self, data):
		temp = node(data)
		temp.set_next(self.head)
		self.head = temp

# Search the Linked list for a specific value	
# Need some work here

	def search(self, data):
		current = self.head
		found = False
		while current != None and found == False:
			#print found
			#print data, current.get_data()
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

	# 
	def printlist(self):
		temp = self.head
		print "List elements are as below:"
		while(temp):
			
			print "%d" %(temp.data)
			#print %d temp.data
			temp = temp.next


	
	# delete a node by its value
	def delete(self, value):

		#in case when the list is an empty one
		if self.head == None:
			return False

		#in case head has to be removed
		while self.head != None and self.head.data == value:
			temp = self.head
			self.head = self.head.next 
			temp = None

		#in this case, there are two pointers that are assigned, which scans the list, 
		# and the temp pointer is assigned to the node which would be removed / deleted
		current = self.head
		while current.next != None:
			if current.next.data == value:
				temp = current.next
				current.next = temp.next
				temp = None
			else: 
				current = current.next 






llist = LinkedList()
llist.insert(15)
llist.insert(7)
llist.insert(100)
print llist.search(15)
print llist.size()
llist.printlist()
llist.delete(7)
llist.printlist()