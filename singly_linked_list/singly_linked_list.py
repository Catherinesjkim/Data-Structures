# Module 1: Implement the Stack and Queue classes using built-in Python lists and the Node and LinkedList classes you created during the Module 1 Guided Project.
# LL: a collection of nodes.
# This is how list traversal works - not changing the list.
class Node: 
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
    # getter methods
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    # set next method - for the next node to point to something else
    def set_next(self, new_next):
        self.next_node = new_next
        
    # LL obj needs to keep track of the Head and Tail
    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            
        def add_to_tail(self, value):
            # 0. create new node from get_value
            new_node = Node(value, None)
            
            # 1. check if list is test_empty
            if not self.head:
                # if the list is empty, set both head and tail to new node
                self.head = new_node
                self.tail = new_node
            # 2. create a new node with value arg
            else: 
                self.tail.set_next(new_node)
                self.tail = new_node
                
            def remove_head(self):
                if not self.head:
                    return None
                # if head has no next...
                if not self.head.get_next:
                    head = self.head
                    # set head reference to None
                    self.head = None
                    # set tail reference to None
                    self.tail = None
                    return head.get_value() # return to the user that lets them know that it ran smoothly
                value = self.haed.get_value
                self.head = self.head.get_next()
                return value
            
    