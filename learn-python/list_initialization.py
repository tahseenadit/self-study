num_of_items = 5

my_list = [[1]] *  num_of_items

for item in range(0, num_of_items):
    my_list[item] = 2


"""
When you use the expression [[]] * num_of_items, you are creating a list of numRows references to the same list, not numRows independent lists. 
As a result, when you append to one of these lists, it appears as though you're appending to every element in my_list, because all elements in my_list are references 
to the same list.

Here's how you can fix it:

Instead of initializing dp with [[]] * num_of_items, you should create a new list for each row. You can do this with a list comprehension. Replace the line:

dp = [[]] * num_of_items 
with:

dp = [[] for _ in range(num_of_items)]
This will create numRows separate lists, and appending to one will not affect the others.
"""

my_list2 = [[] for _ in range(num_of_items)]

for item in range(0, num_of_items):
    my_list2[item] = 2

 