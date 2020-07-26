count = 0
def my_print_counter(thing_to_print):
    global count
    count += 1
    print(thing_to_print)
    
my_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # .....




"""
0(1) - Constant Time (runt time complexity - Oh of 1) the size of the input doesn't matter - more efficient - (y = 1)
"""
# def print_first_item(items): # input size
#     my_print_counter(items[0]) # One operation that runs no matter how big the input size is

# print_first_item(my_items)



"""
0(n) - Linear Time - (x)
"""
# def print_all_items(items): # input, a collection of items
#     for item in items: # No of operations == input size
#         my_print_counter(item)

# print_all_items(my_items)



"""
O(n^2) - Quadratic time - (x^2)
"""
# def print_all_possible_ordered_pairs(items): # size of the input == 10
#    for first_item in items: # outer loop will happen 10 times
#        for second_item in items: # inner loop will happen 10 times
#             my_print_counter((firs_item, second_item)) # tuple 

# print_all_possible_ordered_pairs(my_items)
# count variable will be at 100 == 10 x 10

"""
N could be the actual input, or the size of the input - the op will be linear
"""
# def say_hi_n_times(n): # input is not a list, it's an integer
#     for time in range(n): # loop through n times
#         my_print_counter("hi")
        
# say_hi_n_times(10)



# def print_all_items(items): 
#     for item in items: 
#         my_print_counter(item)

# print_all_items(my_items)


"""
Drop the constants
"""
# 0(2n) is simplified to what? - (2x)
# no nested for loops - 2 different for loops
# def print_all_items_twice(items): # items == n == x 
#     for item in items:
#          my_print_counter(item)
         
    # Once more, with feeling
#     for item in items:
#         my_print_counter(item)
        
# print_all_items_twice(my_items)


# 0(1 + n/2 + 100) is simplified to what? - O(n)
# def print_first_item_then_first_half_then_say_hi_100_times(items):
#     my_print_counter(items[0]) # 0(1) - no matter how big the items is, we only print 1 item

#     middle_index = len(items) / 2
#     index = 0
#     while index < middle_index: # 0(n/2) half of n
#         my_print_counter(items[index])
#         index += 1

#     for time in range(100): # 0(100)
#         my_print_counter("hi")

# print_first_item_then_first_half_then_say_hi_100_times(my_items)



"""
Drop the less significant test_len_returns_0_for_empty_stack - very inefficient algo
"""
# 0(n + n^2) is simplified to what? - O(n^2) == (x^2) 
# def print_all_numbers_then_all_pair_sums(numbers):
#     print("these are the numbers:")
#     for number in numbers: # O(n) - we drop the less signifant terms
#         my_print_counter(number)
    
#     print("and these are their sums:") 
#     for first_number in numbers:  # O(n^2) - nested for loop - more significant term
#         for second_number in numbers:
#             my_print_counter(first_number + second_number)
    
# print_all_numbers_then_all_pair_sums(my_items)



"""
We are usually talking about the "worst case" (linear - when people are talking about Big O)
"""
# my_haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def contains(haystack, needle):

      # Does the haystack contain the needle?
#     for item in haystack:
#         if item == needle:
#             return True
        
#     return False

# contains(my_haystack, 1)



"""
Things to remember with Big O
"""
# 1. sometimes constants matter (even though we can drop them in Big O) 1/2n is better than n
# 2. beware of premature optimizations


"""
Show DESMOS graph before the break 
https://www.desmos.com/calculator
"""
