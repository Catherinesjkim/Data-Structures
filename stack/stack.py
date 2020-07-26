"""
- Linear
- LIFO (Last In, First Out)
- Like a stack of papers on your desktop

Example of operations:

push(item) - adding an item to the top of the stack - append() == O(n)
pop() - removing the item on the top of the stack; typically returns the item that is removed
peek() - returns the value of the item on the op of the stack without removing it

All stack operations take O(1) time. 
"""

"""
A stack is a data structure whose primary purpose is to store and return elements in Last In, First-Out (LIFO) order/abstract data type (the last value added to the stack will be the first value removed from the stack). It is used for recursive parsing in Natural Language Processing.

1. Implement the Stack class using a dynamic array (when elements are added or removed, the storage area is resized every time accordingly) as the underlying storage structure. Make sure the Stack tests pass. Array implementation.

2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure. Make sure the Stack tests pass.
   
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack? How we interact with it and the size variable. LL == 2
"""
import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# 1: Stack class with Array implementation
# class Stack:
      # Constructor
#     def __init__(self):
#         self.storage = [] # empty array - will fill up with items that are pushed to the stack

    # find length of an Array iteratively
    # def __len__(self):
        # returns the number of array items
        # return len(self.storage)
    
    # Adds new value to the Stack
    # The worst case runtime complexity in an append in the dynamic array? Doubling process == O(n)
    # def push(self, value):
    #    self.storage.append(value)

    # Retrieves and removes value from Stack
    # python = dynamic arrays
#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop()
    
# stack = Stack()


# 2: Stack implementation using a Linked List
# The Node underlies the LL, the LL underlies the Stack structure.
# Tail is the last item we put in and remove in a LL so it's perfect for stack
class Stack:
    # Constructor
    def __init__(self):
        self.size = 0 # size variable 
        self.storage = LinkedList() # empty LL (head = None, tail = None)

    # find length of a Linked List iteratively
    def __len__(self):
        # returns the number of list items
        return self.size

    # Adds new value to the Stack
    def push(self, value):
       self.storage.add_to_tail(value)
       self.size += 1 # keeping track of how big this stack is
   
   # Retrieves and removes value from Stack
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

# test: 
# add a string method and for loop - call the string method 
