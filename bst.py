#######################################################
##### BINARY SEARCH TREE ##############################
######################################################



class Node:
	def __init__(self,value):
		self.value = value
		self.leftchild = None
		self.rightchild = None
	

# Function to insert data to the tree

	def insert(self, data):
		if self.value == data:
			return False
		if self.value > data:
			if self.leftchild:
				return self.leftchild.insert(data)
			else:
				self.leftchild = Node(data)
				return True
		if self.value < data:
			if self.rightchild:
				return self.rightchild.insert(data)
			else:
				self.rightchild = Node(data)
				return True

# Function to find if the data node exists in the tree

	def find(self,data):
		if self.value == data:
			return True
		if self.value > data:
			if self.leftchild:
				return self.leftchild.find(data)
			else:
				return False
		if self.value < data:
			if self.rightchild:
				return self.rightchild.find(data)
			else:
				return False


	def getht(self):
		if self.rightchild and self.leftchild:
			return 1 + max(self.rightchild.getht(), self.leftchild.getht())	
		elif self.leftchild:
			return 1 + self.leftchild.getht()
		elif self.rightchild:
			return 1 + self.rightchild.getht()
		else: 
			return 1


	def inorder(self):
		if self:
			if self.leftchild:
				return self.leftchild.inorder()
			print str(self.value)
			if self.rightchild:
				return self.rightchild.inorder()

	
	def preorder():
		if self:
			print str(self.value)
			if self.leftchild:
				return self.leftchild.preorder()
			if self.rightchild:
				return self.rightchild.preorder()


	def postorder(self):
		if self:
			if self.leftchild:
				return self.leftchild.postorder()
			if self.rightchild:
				return self.rightchild.postorder()
			print str(self.value)




class Tree:
	def __init__(self):
		self.root = None

	
	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True
	

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False


	def getht(self):
		if self.root:
			return self.root.getht()
		else:
			return -1


	def inorder(self):
		if self.root != None:
			print "Inorder Traversal"
			self.root.inorder()


	def preorder(self):
		if self.root != None:
			print "Preorder Traversal"
			self.root.preorder()


	def postorder(self):
		if self.root != None:
			print "Postorder Traversal"
			self.root.postorder()


def main():
	a = Tree()
	a.insert(15)
	print a.getht()
	a.insert(18)
	a.insert(16)
	print a.getht()


if __name__ == '__main__':
	main()
