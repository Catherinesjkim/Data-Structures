# Module 1: Implement the Stack and Queue classes using built-in Python lists and the Node and LinkedList classes you created during the Module 1 Guided Project.
# Stack: adds an item to the top of the stack (push) and removes and returns the element at the top of the stack (pop). Last Item In, First Item Out (LIFO)
# Queue: adds to the back and removes at the front. First In First Out (FIFO)
# LL: Adding to the back and the front, efficient linear deletion and addition runtime. 

# LL: a collection of nodes.
# This is how list traversal works - not changing the list
# All LL/class Node has to know is somewhere needs to store value + where the next node is. 
class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
# LL obj needs to keep track of the Head and Tail
# Class LinkedList is like a node manager - add, delete, etc.
# What is head going to store? A node that corresponse to our first node in the list
class LinkedList:
    def __init__(self):
        self.head = None # stores a node, that corresponds to our first node in the list
        self.tail = None # stores a node that is the end of the list
    
    # like an append/prepend/shift method in an array
    # Insertion - keep track of head
    def add_to_head(self, value):
        # create a node to add to head
        new_node = Node(value)
        # check if list is empty
        if  self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else: 
            # new_node should point to current head
            new_node.next_node = self.head
            # move ehad to new node
            self.head = new_node
    
    # Insertion - keep track of tail
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
    
    # Delete - remove the head and return its value
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
            return head_value # return to the user that lets them know that it ran smoothly
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value        
    
    # traverse that some element exists, we did it correctly by adding a value and see that it exists
    # need to Search through the LL - no divide & conquer, need to do it one by one
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
    
    def get_max(self):
        current = self.head
        
        if (self.head == None):
            print("List is empty")
        else:
            # initializing max to initial node data
            max = self.head.value
            while(True):
                # if current node's value is greater than max, then replace value of max with current nodes' value
                if(max < current.value):
                   max = current.value
                if (current == self.tail):
                    break # because the tail in singly_linked_list doesn't have a pointer/reference to the next node
                current = current.next_node
            print("Maximum value node in the list: " + str(max))
            
            return max

    
    
linked_list = LinkedList()

linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(f'Does our LL contain 0? {linked_list.contains(0)}')
print(f'Does our LL contain 1? {linked_list.contains(1)}')
print(f'Does our LL contain 2? {linked_list.contains(2)}')

linked_list.add_to_head(2)
print(f'The start of the list is {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'The start of the list is {linked_list.head.value}')
linked_list.remove_head()
print(f'The start of the list is {linked_list.head.value}')
