# Module 1: Implement the Stack and Queue classes using built-in Python lists and the Node and LinkedList classes you created during the Module 1 Guided Project.
# Stack: adds an item to the top of the stack (push) and removes and returns the element at the top of the stack (pop). Last Item In, First Item Out (LIFO)
# Queue: adds to the back and removes at the front. First In First Out (FIFO)
# LL: Adding to the back and the front, efficient linear deletion and addition runtime. 

# LL: a collection of nodes.
# This is how list traversal works - not changing the list
# All LL/class Node has to know is somewhere needs to store value + where the next node is. 

# 2 Classses - Node & LL

# Node = value & next 
class Node: 
    def __init__(self, value=None, next_node=None): # pass in value and nex_node, default to None
        self.value = value
        self.next_node = next_node
    
    # getter methods
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next)
        self.next_node = new_next

# my_node = Node(1, Node())

# LL obj needs to keep track of the Head and Tail
# LinkedList class is like a node manager - add, delete, etc.
# What is head going to store? A node that corresponse to our first node in the list

# What do we need? Head & Tail
# only method needed: add_to_tail or remove_head
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
        new_node = Node(value, None)  # LL that has 1 item so far value == None
        # check if there is no head - empty list
        if not self.head: # LL that has 1 item, the head & tail are the same
            self.head = new_node
            self.tail = new_node
            
        # otherwise (if not an empty list), we will always have a tail
        else: 
            # point the node at the current tail, to the new node
            self.tail.set_next(new_node)
            self.tail = new_node
    
    # Delete - remove the head and return its value
    # why do we want to remove the head? Append: change the head pointer
    def remove_head(self):
        # is ther a head? 
        if not self.head:
            return None # empty
        
        # if head has no next, there is a single element in the LL
        if not self.head.get_next():
            head = self.head # 1 single item
            self.head None
            self.tail = None 
            
            return head.get_value() # return zero element list - single LL
        
        # more than one item 
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value
            
    # traverse that some element exists, we did it correctly by adding a value and see that it exists
    # need to Search through the LL - no divide & conquer, need to do it one by one
    # contains = true or false
    def contains(self, value):
        if not self.head:
            return False
        
        # get a reference to the node we're currently at; update this as we traverse the
        current = self.head
        # check to see if we're at a valid node 
        while current:
        # return True if the current value we're looking at matches our target value
            if current.get_value == value:
                return True
            
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
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

# print out the results of the methods
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

# linked_list.remove_head()
# print(f'The start of the list is {linked_list.head.value}')

linked_list.get_max()
# print("Maximum value node in the list: " + str(max))
