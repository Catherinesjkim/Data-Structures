"""
- Linear
- FIFO (First In, First Out)
- Checkout line at the grocery stores

Example operations:

    enqueue(item) - adding an item to the end of the queue
    dequeue() - removing the item at the beginning of the queue
    
All queue operations take O(1) time. 
"""

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order (FIFO) i.e. printer, back button, and undo hotkey.  

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     # how do we remove from a queue?
#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)
        
        
# Queue implementaiton using a LL
# LL starts with 2 Nones
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    # if someone get into a line
    def enqueue(self, item):
        # add the item to the LL
        self.storage.add_to_tail(item)
        self.size += 1

    # how do we remove from a queue?
    def dequeue(self): # It's my turn to checkout
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head() # LL taking care of the pointers
