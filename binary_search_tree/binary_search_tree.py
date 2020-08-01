from collections import deque

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

# a binary tree node has data, pointer to left child and a pointer to right child
# for all nodes n and it states that all left descendants <= n < all right descendants.
# time complexity has an average of O(log n) - no need to go through each node in the tree
# there's no HEAD in binary search tree, just series of nodes that are connected

# Only one class instead of 2 classes - trees are simpler - no need to keep track of pointers
# Only need to keep track of root node
# root node == self
class BSTNode: # test starts with value of 8
    # Node class used by the BST
    def __init__(self, value): # value is not optional - you will always have a value
        # current root node's value == None
        self.value = value
        
        # initial node = None is valid so that we could use it/build out more trees
        self.left = None  # less than value - valid node
        self.right = None  # greater than value - valid node
        
    # Insert the given value into the tree 
    
    # recursive function
    # self == BSTNode
    # value == 8 
    # root.insert(8)
    def insert(self, value):  # a classic Recursive function 
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        if value < self.value: # (3 < 8)
            # IF self.left is already taken by a node
                # make that (left) node, call insert
            # set the left to the new node with the new value 
            if self.left is None: # base case
                self.left = BSTNode(value) # base case - if the base case runs, then the recursive case does not run -->
                
            # if self.left is Not None: recursion about to happen - a function that's calling itself
            else: 
                self.left.insert(value) # we don't know how to instantiate this but maybe 3 will know - calling itself == Recursive
            
        if value >= self.value: # we are calling the second insert here since 8 (root node) doesn't know how to do it (5 > 3)
            # IF self.right is already taken by a node
                # make that (right) node call insert
            # set the right child to the new node with new value
            if self.right is None: # base case - if the base case runs, then the recursive case does not run -->
                self.right = BSTNode(value)

            # if self.left is Not None: recursion about to happen - a function that's calling itself
            else:
                self.right.insert(value) # calling intself == Recursive
    # runtime complexity: O(log n) - always code running on one side of the node - left or right, not both

    # Recursive case/steps:
        # repeat function until we reach base case 
        # repeating the problems until the base case is hit
        
    # Base case:
        # usually where "code" that does the whatever you need it to do

           
    # Return True if the tree contains the value (Search function - If 8 inside the tree? Yes)
    # False if it does not
    # recursive contains function needs to return sth. - more complicated
    # root.contains(8)
    def contains(self, target): 
        if self.value == target: # base case - easiest scenario possible
            return True  # base case - figures out if the current value if what we are looking for
        # compare the target to current value
        
        # if current value is more than the target
        # found = False
        if self.value >= target: # equal sign is not necessary - line 44 already handled it
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:  # base case - if your base case returns sth, then also return what your recursive also finds
                return False  # base case
            return self.left.contains(target) # found - because the base case returns sth.
            
        # if current value is less than target
        if self.value < target: # 8 <12
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:  # base case
                return False  # base case
            # does the right tree contain the target?
            return self.right.contains(target) # first recursive case - the problem is not simple enough to solve with our base case - found - because the base case returns sth.
        
             
    # Return the maximum value found in the tree
    # In BST, we can find maximum by traversing right pointers until we reach the rightmost node. 
    # We start with the root node, then we move to the right node, we keep on moving to right until we see NULL. The last leaf node is NULL, that is the node with maximum value.
    
    # Function to find the node with maximum value
    # i.e. rightmost leaf node
    # each node in a BST is in itself a BST.
    # needs to return sth.
    # could use iterative solution like LL
    # but using recursive in this case - left or right or both
    def get_max(self):  # start with the node that's 8
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree
        if self.right is None: # base case works, we just need to reach the base case
            # figures out the biggest value
            return self.value # current.value -
        # if there's a value to the right
        max_val = self.right.get_max() # reaching the base case - go further right
        return max_val
        
        
    # Call the function `fn` on the value of each node
    # I don't know what the numbers are going to be because the test function is generating random numbers but I'm guessing between 1 - 101
    
    # an example of DFT
    # JS: Arr.ForEach(() => { do something }) anonymous function
    def for_each(self, fn): # who is calling what? 
        # 8.for_each(fn) -->
        # call function on the current value fn(self.value)
        fn(self.value)  # base case - calls a function
        # fn(8) --> [8]
        # fn(3) --> [8, 3]
        # fn(9) --> [8, 3, 9]
        # fn(10) --> [8, 3, 8, 9]
        # fn(12) --> [8, 3, 8, 9, 12]
        
        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)  # 3.for_each(fn) --> [3]
        # implicit return is None
        
        # if you can go right, call for_each on the right tree 
        if self.right:
            self.right.for_each(fn)  # the right node is passed in to self
            # 10.for_each(fn) --> fn(10) --> [8, 3, 10]
            # 9.for_each(fn) --> fn(9) --> [8, 3, 10, 9]
            # 12.for_each(fn) --> fn(12) --> [8, 3, 10, 9, 12]
        # implicit return is None 
        
        
    # Part 2 -----------------------
    
    # Unlike linear data structures (Array, LL, Queues Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. There are 2 widely used ways for traversing trees:
    
    # 1. Depth First Search (DFS) - technique used for traversing tree or graph. Backtracking is used for traversal. In this traversal, first the deepest node is visited and then bracktracks to it's parent node if no sibling of that node exists. We can simply begin from a node, then traverse its adjacent (or children) without caring about cycles. And if we begin from a single node (root), and traverse this way, it is guaranteed that we traverse the whole tree. 
    
    
    # 2. Breadth First Search (BFS) - Level order traversal of a tree. 
    
    # Search is completed when the target of the search is found
    # Traversal is completed when every node has been explored - just visiting each node
    # DFT: Continues traveling forward on each branch until a dead end is reached - You go as deep as possible down One path before backing up and going down a different One to search for an item - alway go left first
    
    # Call stack is the going to help me. It builds up and then tears down. Go all the way down to the bottom before going up
    # in_order_print(1)
    # in_order_print(None)
        
    # Tree Traversal
    # 1. visit each node once
    # 2. probably do fn()

    # Print all the values in order from low to high
    # Hint: Use a recursive, Depth First Traversal (DFT) - prioritize going deep first
    def in_order_print(self):  # node is the new pointer that we get to pass in
        # Lowest number is always the furthest to the left
        # left --> root --> right
        if self.left is not None:
        # recursive case? closest to the base case
            self.left.in_order_print()
        print(self.value) # from BST node
        
        if self.right is not None:
            self.right.in_order_print()
        # build up my call stack to see what happens
        
    # BFT: You first explore all the nodes one step away, then all the nodes two steps away, etc.
    # Level 1 (node level) first, and then level 2 (child node level) second, etc.
    
    # Print the value of every node, starting with the given node,
    # in an iterative Breadth First Traversal - we are not working with recursion - How about QUEUE? First In, First Out (FIFO) data structure.
    def bft_print(self): # this function will only get called once
        # create a queue for nodes
        qq = deque()
        # add the first node to the queue
        qq.append(self)
        
        # while queue is not empty
        while len(qq) > 0:
            # remove the first node from the queue
            current = qq.popleft()
            # print the removed node
            print(current.value)
            
            # add all children into the queue
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal (DFT) - not recursion
    def dft_print(self):
        # create a stack for nodes
        s = []
        # add the first node to the stack
        s.append(self)
        
        # while the stack is not empty
        while len(s) > 0:
            # get the current node from the top of the stack
            current = s.pop()
            # print that node
            print(current.value)
            # add all children to the stack
            # keep in mind, the order you add to the children, will matter
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)
                

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass
    
root_node = BSTNode(8) # no insert function needs to be called
root_node.insert(3)
root_node.insert(10)
root_node.insert(9)
root_node.insert(12)

# JS: const print_node = (x) => { console.log(x) }
print_node = lambda x: print(f'current_node is: {x}')

root_node.for_each(print_node)


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

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
