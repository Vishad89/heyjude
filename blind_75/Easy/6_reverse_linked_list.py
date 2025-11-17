"""
206. Reverse Linked List
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

"""

class node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
        
class LinkedList(node):
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None): 
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 
    
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.next
    
    def search(self, data):
        current = self.head
        found = False
        while current != None and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
    def delete(self, data):
        current = self.head
        found = False
        prev = None
        while current != None and found == False:
            if current.get_data() == data:
                found = True
            else:
                prev = current
                current = current.get_next()
        if current == None:
            raise ValueError("data is not in list")
        elif prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())


    def hasCycle(self):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
                
        
        
        
        
        
        
        
            
list = LinkedList()
list.insert(15)
list.insert(7)
list.insert(8)
list.insert(21)
print ("Given Linked List") 
list.printList() 
print(list.size())
print(list.search(8))
list.delete(15)
print ("Given Linked List") 
list.printList() 
list.reverse() 
print ("\nReversed Linked List") 
list.printList() 
            
