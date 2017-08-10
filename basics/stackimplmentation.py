# Stack implementation

class stack(object):

	def __init__(self, data = None , next = None):
		self.data = data
		self.next = next

	def pop(self):
		outputvalue = self.data
		self.next = self.next.next
		self.data = self.next.data


	def push(self, data):
		oldstack = stack(self.data, self.next)
		self.data = data
		self.next = oldstack

	def peek(self):
		return self.data

	def size(self):
		ssize = 0
		nextvalue = self.next
		while (nextvalue != None):
			nextvalue = nextvalue.next
			ssize += 1
		return ssize

	def isEmpty(self):
		if (self.data == None):
			return True
		else: 
			return False









if __name__ == "__main__":
    mystack = stack()
    mystack.push(10)
    print "Size = ", mystack.size()
    mystack.push(9)
    print "Size = ", mystack.size()
    mystack.push(15)
    print "Size = ", mystack.size()
    print mystack.peek()
    mystack.pop()
    print mystack.isEmpty()
    print mystack.peek()

