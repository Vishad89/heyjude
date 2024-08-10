"""
19. Remove Nth Node From End of List
Medium
Topics
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
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
    
    def remove(self, num:int):
        slow = self.head
        fast = self.head
        for i in range(num):
            fast = fast.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return self.head
                   
             
list = LinkedList()
list.insert(15)
list.insert(7)
list.insert(8)
list.insert(21)
list.insert(1)

print ("Given Linked List") 
list.printList() 
list.remove(4)
print ("\n Updated Linked List") 
list.printList() 
            
