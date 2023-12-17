class Solution:
    def __init__(self):
        left = None
        right = None

    def find(self, left, right, nums):       
        mid = int((left + right)/2)
        
        if left == mid:
            if nums[left] > nums[right]:
                return nums[right]
            return nums[mid]

        if nums[mid] > nums[right]:           
            left = mid + 1
            return self.find(left, right, nums)
        else:
            right = mid
            return self.find(left, right, nums)

    def findMin(self, nums: List[int]) -> int:
        self.left = 0
        self.right = len(nums) - 1
        
        return self.find(self.left, self.right, nums)

"""
This code defines a class `Solution` with a method `findMin` that aims to find the minimum element in a rotated sorted array. The method uses a recursive binary search approach. Let's break down the code and explain it with an example:

### Explanation of the Code

- ** Class Definition **:
  - The class `Solution` has two attributes, `left` and `right`, initialized as `None`. These are used to store the indices for searching the array.

- ** Method `findMin` **:
  - This method initializes `left` and `right` to the start and end indices of the input array `nums`, respectively.
  - It then calls the `find` method, passing these indices along with the array.

- ** Method `find` **:
  - This is a recursive method that performs a binary search.
  - `mid` is calculated as the average of `left` and `right`, rounded down to the nearest integer.
  - The base case checks if `left` is equal to `mid`. If so, it compares the elements at `left` and `right` and returns the smaller one.
  - If `nums[mid]` is greater than `nums[right]`, it indicates the smallest element is in the right half. So, the search space is updated to `[mid + 1, right]`.
  - Otherwise, the smallest element is in the left half, and the search space is updated to `[left, mid]`.
  - The method then calls itself recursively with the updated search space.

### Example

Let's consider an example: `nums = [4, 5, 6, 7, 0, 1, 2]`

- Initially, `left = 0` and `right = 6`.
- The first `mid` is `3`, and `nums[3] = 7`. Since `nums[3] > nums[6]`, the new search space is `[4, 6]`.
- The next `mid` is `5`, and `nums[5] = 1`. Since `nums[5] < nums[6]`, the new search space is `[4, 5]`.
- Eventually, the base case will be reached, comparing `nums[4]` and `nums[5]`, returning `0` as the minimum.

### Time Complexity
The time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. In the provided code, a binary search approach is used to find the minimum element in a rotated sorted array. Here's how we analyze its time complexity:

Binary Search: In each recursive call of the find method, the algorithm divides the search space in half. This is the hallmark of binary search. If the length of the array is n, after the first iteration, the size of the search space becomes n/2, after the second iteration, it becomes n/4, and so on.

Number of Iterations: The process continues until the search space is reduced to just one element. The number of times you can divide n by 2 until you get down to 1 gives you the number of iterations. This can be expressed as logn

Complexity: Therefore, the time complexity of the algorithm is O(logn), where n is the number of elements in the input array.

### Space Complexity
The space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run as a function of the length of the input. For the given code, the space complexity mainly comes from the recursive calls of the find method:

Recursive Calls: Each recursive call adds a new layer to the call stack, which takes up memory. The number of recursive calls depends on how many times the array can be halved, which, as we discussed earlier, is logn.

Auxiliary Space: Aside from the space for the input array (which we don't consider in space complexity analysis as it's not part of the algorithm's additional space requirement), the extra space used is for the variables in each recursive call, like left, right, and mid.

Complexity: Since the maximum depth of the recursive call stack would be logn, the space complexity is also O(logn).

In summary, the provided algorithm has a time complexity of O(logn) and a space complexity of O(logn), both owing to the binary search approach and the depth of recursion, respectively.
"""
        