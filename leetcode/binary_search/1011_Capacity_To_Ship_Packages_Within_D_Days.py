class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_packages = len(weights)
        left = max(weights)
        right = math.ceil(len(weights) / days) * max(weights)
        
        
        
        if days == 1:
          right = 0
          for weight in weights:
            right += weight
          return right

        

        while left < right:                   
          days_count = 1
          sum_of_weights = 0
          mid = int((left + right)/2)

          for idx,weight in enumerate(weights):
            sum_of_weights += weight

            if sum_of_weights > mid:
              sum_of_weights = weight
              days_count += 1
            if sum_of_weights == mid:
              sum_of_weights = 0
              if len(weights)-1 != idx:
                days_count += 1

            if days_count > days:
              break

          if days_count > days:
              left = mid + 1
          else:
            right = mid

        return left


"""

Example Setup
Suppose we have weights = [1, 2, 3, 4, 5] and we want to ship these packages within days = 3.

Initial Boundaries
Lower Boundary (left): This is set to the heaviest package. In our example, left = max(weights) = 5.
Upper Boundary (right): It's an overestimation of the required capacity. Here, right = math.ceil(len(weights) / days) * max(weights). There are 5 weights and 3 days, so it's math.ceil(5/3) * 5 = 2 * 5 = 10.

Binary Search Process
Now, we'll use binary search to find the minimum capacity. Here's how it goes:

First Iteration
left = 5, right = 10, so mid = (5 + 10) // 2 = 7.
We try to fit the packages into 3 days with a capacity of 7.
Day 1: We can fit 1 + 2 + 3 = 6 (Adding 4 would exceed 7).
Day 2: Next, we fit 4 (Adding 5 would exceed 7).
Day 3: Finally, we fit 5.
We successfully fit all packages in 3 days, so the capacity of 7 works. Now, we check if there's a smaller capacity that also works: right = mid = 7.

Second Iteration
left = 5, right = 7, so mid = (5 + 7) // 2 = 6.
We try with a capacity of 6.
Day 1: We can fit 1 + 2 + 3 = 6.
Day 2: Next, we fit 4 (Adding 5 would exceed 6).
Day 3: Finally, we fit 5.
Again, it works. We update right = mid = 6.

Third Iteration
left = 5, right = 6, so mid = (5 + 6) // 2 = 5.
We try with a capacity of 5 (which is the minimum possible).
Day 1: We can only fit 5 (since it's the maximum capacity).
Day 2: We can fit 1 + 2 + 3 = 6, but this exceeds the capacity of 5. Thus, we fail to fit all packages within 3 days.
This means a capacity of 5 is too small, so we update left = mid + 1 = 6.

Conclusion
After the third iteration, left = 6 and right = 6, so the loop ends.
The algorithm returns left, which is 6. This is the minimum capacity needed to ship all the packages within 3 days.

Key Observations
Why left < right Instead of left <= right?

Suppose we have a different set of weights, say weights = [1, 2, 4, 8, 16], and we want to ship these within days = 3.

Initial Boundaries
Lower Boundary (left): Set to the heaviest package, so left = 16.
Upper Boundary (right): For simplicity, let's say right = 31 (the sum of all weights).
Binary Search Process

First Iteration
left = 16, right = 31, so mid = (16 + 31) // 2 = 23.
Test if a capacity of 23 can ship the packages in 3 days:
Day 1: 16 (can't add more without exceeding 23).
Day 2: 1 + 2 + 4 = 7.
Day 3: 8.
Capacity of 23 works, so update right to 23.

Second Iteration
left = 16, right = 23, so mid = (16 + 23) // 2 = 19.
Test capacity of 19:
Day 1: 16 (can't add more without exceeding 19).
Day 2: 1 + 2 = 3.
Day 3: 4 + 8 = 12.
Capacity of 19 also works, so update right to 19.

Third Iteration
left = 16, right = 19, so mid = (16 + 19) // 2 = 17.
Test capacity of 17:
Day 1: 16 (can't add more without exceeding 17).
Day 2: 1 (can't add more without exceeding 17).
Day 3: 2 + 4 + 8 = 14.
Capacity of 17 doesn't work because we need an extra day. So, update left to mid + 1 = 18.

Fourth Iteration
left = 18, right = 19, so mid = (18 + 19) // 2 = 18.
Test capacity of 18:
Day 1: 16 (can't add more without exceeding 18).
Day 2: 1 + 2 = 3.
Day 3: 4 + 8 = 12.
Capacity of 18 works, update right to 18

Key Iteration
When, mid = (18 + 19) // 2 = 18, if we used left < mid, since left (18) is not less than mid (18), the loop would terminate.

Why left < right is Preferable
The issue with left < mid is that it can prematurely terminate the search. In the case where left equals mid, the condition fails, and the loop ends, even though we haven't conclusively determined if left is indeed the minimum capacity that works.
In binary search, the goal is to keep narrowing the search range until left and right converge, meaning there are no other values to consider. left < right ensures that the search continues until this convergence is definitively reached.
Using left < mid could stop the loop too early, potentially missing the exact solution. In contrast, left < right guarantees that we explore every possibility within our defined range.

Conclusion
The left < right condition ensures that the binary search algorithm exhaustively and accurately narrows down the search range. It avoids premature termination of the loop and ensures that when the loop does terminate, the values of left and right have converged to the point where they represent the optimal solution. This is why left < right is a standard and effective condition for binary search loops.

Why Return left?
We return left because it is the smallest value that we haven't disproven. It's the first value at which we found it was impossible to ship the packages in days days, so any value smaller than left is also impossible.

Initial Calculation of right
Formula: right = math.ceil(len(weights) / days) * max(weights)

Understanding the Calculation

Dividing the Total Number of Packages by Days:
len(weights) / days: This part calculates the average number of packages that need to be shipped per day to meet the deadline.
math.ceil(...): The ceiling function ensures that this average is rounded up. This is crucial because you cannot ship a fraction of a package – even if the average is, say, 4.5 packages per day, you need to be prepared to ship 5 on some days.

Multiplying by the Maximum Weight:
* max(weights): This part multiplies the rounded-up average number of packages by the weight of the heaviest package.
Why the heaviest package? It's a conservative estimate to ensure the ship is capable of handling the worst-case daily load. For any given day, the heaviest load possible (under the constraint of the number of packages) would be if all shipped packages were as heavy as the heaviest one.

Time Complexity
Binary Search: The core of the algorithm is a binary search, which repeatedly halves the search range until the minimum possible capacity is found. The time complexity of a binary search is O(logN), where N is the range of numbers being searched. In this case, N is the difference between the maximum individual weight and the sum of all weights.

Weight Summation in Each Iteration: Inside each binary search iteration, the algorithm sums up the weights to check if the packages can be shipped within the given days with the current mid-capacity. This summing up is linear with respect to the number of packages, which we'll denote as M.
Combining these two aspects, the overall time complexity is O(MlogN). Here, M is the number of weight elements, and N is the range between the maximum weight and the total weight.

Space Complexity
The space complexity of the algorithm is relatively straightforward:

Constant Extra Space: The solution uses a fixed amount of extra space for variables like left, right, mid, days_count, and sum_of_weights. This does not depend on the input size.
No Additional Data Structures: The algorithm does not use any additional data structures that grow with the input size. It operates directly on the input array.
Hence, the space complexity is O(1), meaning it requires constant space regardless of the input size.

Iterative Approach
Loop Variables: In an iterative approach, such as the one used in the provided binary search algorithm, the variables (left, right, mid, etc.) are updated in place within the loop. These variables occupy a fixed amount of space in the stack, regardless of how many times the loop iterates.
Constant Space: Since no additional stack space is required for each iteration, the space complexity remains constant, O(1).
Recursive Approach
Function Calls: In a recursive approach, every recursive call adds a new frame to the call stack. This frame contains the function's local variables and other information.
Stack Space: Each recursive call consumes stack space. If the recursion goes d levels deep, there will be d frames on the stack.
Space Complexity: For a binary search implemented recursively, the depth of recursion would be proportional to the number of times we can halve the search range, leading to a space complexity of O(logN), where N is the range of the search space.
Example: Binary Search
Iterative Binary Search: The variables used to determine the search range are reused in each iteration, leading to O(1) space complexity.
Recursive Binary Search: Each recursive call requires its own set of variables (left, right, mid, etc.), stored in separate stack frames, leading to O(logN) space complexity.
"""
        