# Module 1: Implement the Stack and Queue classes using built-in Python lists and the Node and LinkedList classes you created during the Module 1 Guided Project.
# Stack: adds an item to the top of the stack (push) and removes and returns the element at the top of the stack (pop). Last Item In, First Item Out (LIFO)
# Queue: adds to the back and removes at the front. First In First Out (FIFO)
# LL: Adding to the back and the front, efficient linear deletion and addition runtime. 

# LL: a collection of nodes.
# This is how list traversal works - not changing the list
# All LL/class Node has to know is somewhere needs to store value + where the next node is. 

# 2 Classses - Node & LL
# Node = value & next 
# self == whole Node (value and next_node)
class Node: 
    def __init__(self, value=None, next_node=None): # pass in value and nex_node, default to None
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    
    # getter methods
    # def get_value(self):
    #     return self.value
    
    # def get_next(self):
    #     return self.next_node
    
    # def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        # self.next_node = new_next

# LL obj needs to keep track of the Head and Tail
# LinkedList class is like a node manager - add, delete, etc.
# What is head going to store? A node that corresponse to our first node in the list

# What do we need? Head & Tail, variable pointing to the node
# The only method needed: add_to_tail or remove_head
# Dependent on the Node class that we have above
class LinkedList:
    def __init__(self): # initialize an empty LL
        # reference to the head of the list
        self.head = None # stores a node, that corresponds to our first node in the list
        # reference to the tail of the list
        self.tail = None # stores a node that is the end of the list
    
    # logic that interacts with variables head & tail
    # like an append/prepend/shift method in an array
    # Insertion - keep track of head
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
            # move ahead to new node
            self.head = new_node
    
    # Insertion - keep track of tail
    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value) 
        # check if there is no head (i.e., the list is empty)
        if self.head is None and self.tail is None: 
            # if the list is initially empty, set both head and tail to the nnew_node
            self.head = new_node
            self.tail = new_node 
        # we have a non-empty list, add the new node to the tail
        else: 
            # set the current tail's next reference to our new node
            self.tail.next_node = new_node
            # set the list's tail reference to the new node
            self.tail = new_node
    
    # Delete - remove the head and return its value
    # why do we want to remove the head? Append: change the head pointer
    def remove_head(self): # self == The LL instance
        # No Item: return None if there's no head (i.e. the list is empty == there's no node)  
        if not self.head:
            return None 
        # One Item: if head has no next, then we have a single element in our list
        if self.head.next_node is None:
            # get a reference to the head
            head_value = self.head.value # 1 single item
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None 
            # return the value
            return head_value
        # Else: More than one item: otherwise we have more than one element in our list 
        head_value = self.head.value # value === just the string, not the node
        # set the head reference to the current head's next node in the list
        self.head = self.head.next_node
        return head_value
        
    # traverse that some element exists, we did it correctly by adding a value and see that it exists
    # need to Search through the LL - no divide & conquer, need to do it one by one
    # contains = true or false
    def contains(self, value):
        if self.head is None:
            return False
        # get a reference to the node we're currently at; update this as we traverse the
        current_node = self.head
        # check to see if we're at a valid node 
        while current_node is not None:
        # return True if the current value we're looking at matches our target value
            if current_node.value == value:
                return True
            # update our current node to the current node's next node
            current_node = current_node.next_node
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
                # if current node's value is greater than max, then replace value of max with current nodes values
                if(max < current.value):
                    max = current.value
                if (current == self.tail):
                    break
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

linked_list.get_max()
