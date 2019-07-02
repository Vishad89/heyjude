class Node:
    count = 1
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value > data:
            if self.left is None:
                self.left = Node(data)
                Node.count += 1
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
                Node.count += 1
            else:
                self.right.insert(data)

# Using preorder
def serialize(root, serial):
    if root != None:
        serial.append(root.value)
        serialize(root.left, serial)
        serialize(root.right, serial)
    else:
        serial.append('x')

def deserialize(serial):
    serial.reverse()
    return _deserialize(serial)

def _deserialize(serial):
    if not serial:
        return None

    node = None
    value = serial.pop()
    if value != 'x':
        node = Node(value)
        node.left = _deserialize(serial)
        node.right = _deserialize(serial)
    return node

def printLevelOrder(root):
    # Base Case
    if root is None:
        return     
    # Create an empty queue for level order traversal
    queue = []
    # Enqueue Root and initialize height
    queue.append(root)
    while(len(queue) > 0):
        # Print front of queue and remove it from queue
        print queue[0].value,
        node = queue.pop(0)
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
            


root = Node(3)
root.insert(1)
root.insert(2)
root.insert(4)
root.insert(5)
root.insert(0)

print("serializes a tree\n")
# Serialize
serial = []
serialize(root, serial)
print(serial)
print serial.reverse()

print("deserializes a tree\n")
# Deserialize
newRoot=deserialize(serial)
printLevelOrder(newRoot)
