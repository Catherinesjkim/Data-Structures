"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order (LIFO). i.e. printer, back button, and undo hotkey.  

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList
 
list1 = LinkedList


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        if self.size is None:
            self.size = Node(value)
        else: 
            new_node = Node(value)
            new_node.next = self.size
            self.size = new_node

    def pop(self):
        if self.size is None:
            return None
        else:
            popped = self.size.value
            self.size = self.size.next_node
            return popped
        
a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
            break
