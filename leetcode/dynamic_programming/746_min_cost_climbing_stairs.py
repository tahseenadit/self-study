class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = 0
        
        if len(cost) > 2:
            cost.append(0)
        elif len(cost) == 2:
            return min(cost[0],cost[1])
        else:
            return result
        
        for i in range(2, len(cost)):
            result = min(cost[i-1]+cost[i], cost[i-2]+cost[i])
            cost[i] = result
            
        return result

"""
- If there are more than two steps, a zero is appended to the cost list. This represents the cost of stepping off the stairs, making it easier to handle the final step.
- If there are exactly two steps, the function returns the minimum of these two costs.
- If there's less than two steps (including no steps), the function returns result, which is 0.
- Iterates through the cost list starting from the third element (index 2).
- For each step i, it calculates the minimum cost to reach that step either from the previous step (i-1) or the step before that (i-2).
- Updates the cost at index i with this minimum value.
- Returns the last calculated result, which is the minimum cost to reach the top of the stairs.

### Example Test Case
Consider `cost = [10, 15, 20]`.

1. Initialize `result = 0`.
2. Since `len(cost) > 2`, append `0` to `cost`. Now, `cost = [10, 15, 20, 0]`.
3. Iterate from `i = 2` to `i = 3` (length of `cost`):
   - For `i = 2`: `result = min(15 + 20, 10 + 20) = min(35, 30) = 30`. Update `cost[2] = 30`.
   - For `i = 3`: `result = min(30 + 0, 15 + 0) = min(30, 15) = 15`. Update `cost[3] = 15`.
4. Return `result = 15`.

### Time Complexity
- The time complexity is (O(n)), where (n) is the length of the `cost` list. This is due to the single for-loop iterating through the list.

### Space Complexity
- The space complexity is (O(1)). No additional space is used proportional to the input size, except for the variable `result`. 
(Note: Modifying the input list itself does not count towards extra space complexity in this analysis.)
"""