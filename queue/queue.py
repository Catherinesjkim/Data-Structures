"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order (FIFO). 

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
from singly_linked_list import LinkedList

list1 = LinkedList

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None  # stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    # like an append/prepend/shift method in an array
    def add_to_head(self, value):
        # create a node to add to head
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move ehad to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add to tail
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            # if the list is empty, set both head and tail to new node
            self.head = new_node
            self.tail = new_node
        # otherwise, the old tail is no longer the correct value
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            # set head reference to None
            self.head = None
            # set tail reference to None
            self.tail = None
            return head_value  # return to the user that lets them know that it ran smoothly
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    # contains = true or false
    def contains(self, value):
        if self.head is None:
            return False

        # loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list1
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.storage:
            return self.storage.remove_head()
        return None
