"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode: # there are 2 pointers now = prev + next
    # Constructor to create a new node
    def __init__(self, value, prev=None, next=None): # both pointers are None
        self.prev = prev
        self.value = value
        self.next = next
        
    """
    Wrap the given value in a ListNode and insert it after this node. 
    Note that this node could already have a next node it is point to.
    """
    def insert_after(self, value):
        current_next = self.next # None
        self.next = ListNode(value, self, current_next) # Create a new ListNode, prev pointer points to the previous node ("Matt"), & what's going to be the next value?
        if current_next: # is this a node or None? If it's a None, we leave it alone & current_next goes away
            current_next.prev = self.next 
            
    """
    Wrap the given value in a ListNode and insert it before this node. 
    Note that this node could already have a previous node it is point to.
    """
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    
    """
    Rearranges this ListNode's previous and next pointers
    accordingly effectively deleting this ListNode.
    """
    # delete method - modularizing my code - will be used later in the remove_from_head method
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            # 1 <--> 2 <--> 3 
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    # Constructor for the empty DLL
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new_node = use the ListNode class
        new_node = ListNode(value, None, None) # prev=None, next=None
        self.length += 1
        # check if the DLL is empty:
        if not self.head and not self.tail: # head is pointing to None, tail is pointing to None
            self.head = new_node
            self.tail = new_node
        else: # in all other cases
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
            
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            # creating the last new node
            self.tail.next = new_node
            # change the pointer/flag/tag
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
         
    """
    Removes the input node from its current spot in the (what is an input node?)
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check to make sure it's not already at head
        if node is self.head:
            return
        # capture the value of that node first
        value = node.value
        # if the node is in the tail, we will pop it and get rid of it
        if node is self.tail: 
            self.remove_from_tail()
        else: 
            node.delete()
            self.length -= 1 # big cause of bugs
        self.add_to_head(value) # create a new node from the value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    # use insert_after method
    def move_to_end(self, node):
        if node == self.tail:
            return
        value = node.value
        self.delete(node)
        
        self.add_to_tail(value)
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node): # use the delete method above under ListNode
        # if prev is != None, take that item's next to my item's next, after me. 
        # if next is != None, take its prev pointer and jump over me to the previous node. 
        # there are pointers coming out of my node (middle node) but none towards me. Memory doesn't know my node's existence.
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        for i in range(1, self.length):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value

# Testing DLL Functions
new_linked_list = DoublyLinkedList()

new_linked_list.add_to_head(10)
new_linked_list.add_to_head(5)
new_linked_list.add_to_head(18)

new_linked_list.add_to_tail(29)
new_linked_list.add_to_tail(39)
new_linked_list.add_to_tail(49)

new_linked_list.remove_from_head()

new_linked_list.remove_from_tail()

