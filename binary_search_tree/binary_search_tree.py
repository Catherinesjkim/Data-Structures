"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
   
Traversing: walking through a tree
"""
import sys
import math

# a binary tree node has data, pointer to left child and a pointer to right child
# for all nodes n and it states that all left descendants <= n < all right descendants.
# time complexity has an average of O(log n) - no need to go through each node in the tree
# there's no HEAD in binary search tree, just series of nodes that are connected

# root node == self
class BSTNode: # test starts with value of 5 
    # Node class used by the BST
    def __init__(self, value): # value is not optional - you will always have a value
        # current root node's value == None
        self.value = value
        # less than value
        self.left = None
        # greater than value
        self.right = None
        
    # Insert the given value into the tree
    # BST is an ordered DS. Upon insertion, the nodes are placed in an orderly fashion
    # Similar to factorial operations
    def insert(self, value): # 2 is passed as value
        # make a new BSTNode with our value
        # check whether new node's value is less than current node's value
        if value < self.value: # self == the root of BSTNode: 2 < 5
            if self.left is None: # there's no node or value on the  self.left
                self.left = BSTNode(value) # if None then turn it into a node (factorial) - create a new node to the left spot - our insert with 2 is done. 
            else: # recursion is about to start - subtree level - self.left = 2
                self.left.insert(value) # on the subtree, insert 3 - Call Stack: 2.insert(3)
                
        # to make clear that this is the greater and equal case        
        elif value >= self.value: # is 3 > 2? 
            if self.right is None: # there's nothing - no node & value - yes, it's none
                self.right = BSTNode(value) # create our first new right node - subtree of 2
            else:
                self.right.insert(value) 
    # implicit return from line 43
    # return None again  
              
           
           
    # Return True if the tree contains the value - Search function
    # False if it does not
    # check if value == target
    # check if value is in left node
    # if self.left is none, return false, else return true to do the same for the right nodes
    # Call Stack: 5.contains(7)
    def contains(self, target): # start with the node that's 5
        if self.value == target: # 7 == 7
            return True
        # Which direction? Implied direction is right since 7 > 5
        if target > self.value:
            if self.right is None:
                return False
            else:
                # need to return recursive calls: True or False
                return self.right.contains(target) # this is where we start recursion --> returns True == 7.contains(7)
            
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
    
    
    # Return the maximum value found in the tree
    # In BST, we can find maximum by traversing right pointers until we reach the rightmost node. 
    # We start with the root node, then we move to the right node, we keep on moving to right until we see NULL. The last leaf node is NULL, that is the node with maximum value.
    
    # Function to find the node with maximum value
    # i.e. reightmost leaf node
    # each node in a BST is in itself a BST.

    def get_max(self):  # start with the node that's 5
        if self.right is None: 
            return self.value
        else:
            return self.right.get_max() # will return 30
        
        
    # Call the function `fn` on the value of each node
    # I don't know what the numbers are going to be because the test function is generating random numbers but I'm guessing between 1 - 101
    def for_each(self, fn):
        # the starting node always has a value 
        # 5.for_each(fn) -->
        fn(self.value)
        # fn(5) --> [5]
        # fn(50) - -> [5, 50]
        # fn(75) --> [5, 50, 75]
        # fn(3) --> [5, 50, 75, 3]
        
        if self.right is not None:
            self.right.for_each(fn)  # the right node is passed in to self
            # 50.for_each(fn) --> fn(50) --> [5, 50]
            # 75.for_each(fn) --> fn(75) --> [5, 50, 75]
        # implicit return is None 
        
        if self.left is not None:
            # one way of doing recursion - the left node is passed in to self
            self.left.for_each(fn) # 3.for_each(fn) --> []
        # implicit return is None
        
             


    # Part 2 -----------------------
    
    # Search is completed when the target of the search is found
    # Traversal is completed when every node has been explored - just visiting each node
    # DFT: Continues traveling forward on each branch until a dead end is reached - You go as deep as possible down One path before backing up and going down a different One to search for an item - alway go left first
    
    # Print all the values in order from low to high
    # Hint:  Use a recursive, Depth First Traversal (DFT)
    # Call stack is the going to help me. It builds up and then tears down. Go all the way down to the bottom before going up
    # in_order_print(1)
    # in_order_print(None)
    
    # Starter code

    def in_order_print(self, node):  # node is the new pointer that we get to pass in
        # Lowest number is always the furthest to the left
        
        # base case?
        if node is None:
            return 
        # if node is None?
        
        # recursive case? closest to the base case
        self.in_order_print(self.left)
    
        # build up your call stack to see what happens? 
        

    # BFT: You first explore all the nodes one step away, then all the nodes two steps away, etc.
    # Level 1 first, and then level 2 second, etc.
    
    # Print the value of every node, starting with the given node,
    # in an iterative Breadth First Traversal - we are not working with recursion - How about QUEUE or Stack?
    def bft_print(self, node): # this function will only get called once
        pass
        # use a queue to
        # start queue with root node
    
    
        # while loop that checks the size of queue
            # pointer variable that updates at the beginning of each loop
            
        


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (DFT) - not recursion
    def dft_print(self, node):
        pass
        # use a stack
        # start your stack with the root node
        
        # while loop that checks stack size
            # use a pointer variable to keep updating it
            
        
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
