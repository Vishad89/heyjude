# queue implementationi
# FIFO (First in first out)

#  5 ---- >  4 3 2 1  
#  5 4 3 2  ---- > 1

class queue:
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.insert(0,item)

	def pop(self):
		self.items.pop()

	def isEmpty(self):
		return self.items == []

	def get_stack(self):
		return self.items

	def peek(self):
		if not self.isEmpty():
			return self.items[-1]

	def size(self):
		return len(self.items)

s = queue()
print(s.isEmpty)
s.push("a")
s.push("b")
print(s.isEmpty)
print(s.peek())
print(s.size())