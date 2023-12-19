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

"""
my_list Output:
my_list: [[1, 2, 2, 2, 2, 2], [1, 2, 2, 2, 2, 2], [1, 2, 2, 2, 2, 2], [1, 2, 2, 2, 2, 2], [1, 2, 2, 2, 2, 2]]
Explanation: In my_list, each element is a reference to the same list. Therefore, when you append 2 in the loop, it appends 2 five times to this single shared list. 
That's why you see each element of my_list reflecting the same list with [1] followed by five 2s.

my_list2 Output:
my_list2: [[2], [2], [2], [2], [2]]
Explanation: In my_list2, each element is an independent list. So, when you append 2 in the loop, it appends 2 once to each separate list. As a result, each element 
in my_list2 is an individual list containing [2].
This demonstrates how list initialization impacts the behavior of the lists, especially when modifying them in loops. my_list contains multiple references to the same 
list, leading to collective changes, whereas my_list2 contains independent lists, leading to individual changes.
"""

 