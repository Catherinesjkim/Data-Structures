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

# root node == self
class BSTNode:
    # Node class used by the BST
    def __init__(self, value):
        # current root node's value == None
        self.value = value
        # less than value
        self.left = None
        # greater than value
        self.right = None

    # BST is an ordered DS. Upon insertion, the nodes are placed in an orderly fashion
    # Insert the given value into the tree
    # Similar to factorial operations
    def insert(self, value):
        # make a new BSTNode with our value
        # check whether new node's value is less than current node's value
        if value < self.value: # self == the root BSTNode
            if self.left is None: # there's no self.left
                self.left = BSTNode(value) # factorial - turn it into a node
            else: # recursion is about to start
                self.left.insert(value)
                 
        else: 
            if self.right is None: # there's nothing - no node & value
                self.right = BSTNode(value) # turn it into a node
            else:
                self.right.insert(value)
                
           
    # Return True if the tree contains the value
    # False if it does not
    # check if value == target
    # check if value is in left node
    # if self.left is none, return false, else return true do same for right
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
    
    # Return the maximum value found in the tree
    # In BST, we can find maximum by traversing right pointers until we reach the rightmost node. 
    # We start with the root node, then we move to the right node, we keep on moving to right until we see NULL. The last leaf node is NULL, that is the node with maximum value.
    
    # Function to find the node with maximum value
    # i.e. reightmost leaf node
    # each node in a BST is in itself a BST.
    def get_max(self):
        current = self # root node 
        
        # loop down to find the rightmost leaf node
        while(current.right):
            current = current.right
        return current.value
        
    # Call the function `fn` on the value of each node - update the value calling the function? - TL
    # this function performs a traversal of every node in the tree executing the passed-in callback function on each tree node value.
    # for_each() 
    # For every node in the tree, we have sth, we want to do to the value of that.
    # fn is a "call back function"
    # def add_2(value):
    # return value + 2
    # Recursive: print statements everywehere - condition breaks it. Return is not needed. 
    def for_each(self, fn):
        # start at the root!
        # call the function fn
        fn(self.value) # this is for updating each node's value
        if self.left:
            # one way of doing recursion - the left node is passed in to self
            self.left.for_each(fn)
            
        if self.right:
            self.right.for_each(fn) # the right node is passed in to self
             

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

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
