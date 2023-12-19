class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[] for _ in range(numRows)] 
        dp[0] = [1]
        
        for row in range(1, numRows):
            for col in range(0, row + 1):
                prev_row = row - 1
                prev_col_left = 0 if col == 0 else col - 1
                prev_col_right = col - 1 if col >= len(dp[prev_row]) else col
                if prev_col_left == prev_col_right:
                    sum = dp[prev_row][prev_col_left]
                else:
                    sum = dp[prev_row][prev_col_left] + dp[prev_row][prev_col_right]
                
                dp[row].append(sum)

        return dp

"""
The output of the function `generate` for `numRows = 5` is Pascal's Triangle with 5 rows. Let's break down the output and explain how it's generated in each loop iteration:

1. **Initialization**:
   - `dp[0] = [1]`: The first row of Pascal's Triangle is always `[1]`.

2. **Iterations**:
   - **Row 1**: `[1, 1]`
     - This row has two columns. Both are edges, so they are set to 1.
   - **Row 2**: `[1, 2, 1]`
     - First and last columns (edges) are 1.
     - Middle column (2) is the sum of the two elements above it: `1 (from row 1, col 0) + 1 (from row 1, col 1)`.
   - **Row 3**: `[1, 3, 3, 1]`
     - First and last columns are 1.
     - Second column is `1 (from row 2, col 0) + 2 (from row 2, col 1) = 3`.
     - Third column is `2 (from row 2, col 1) + 1 (from row 2, col 2) = 3`.
   - **Row 4**: `[1, 4, 6, 4, 1]`
     - First and last columns are 1.
     - Second column is `1 (from row 3, col 0) + 3 (from row 3, col 1) = 4`.
     - Third column is `3 (from row 3, col 1) + 3 (from row 3, col 2) = 6`.
     - Fourth column is `3 (from row 3, col 2) + 1 (from row 3, col 3) = 4`.

### Time Complexity:
- The time complexity of this function is `O(n^2)`, where `n` is the number of rows.
- This is because there are two nested loops: the outer loop runs `n` times (for each row), and the inner loop runs a number of times equal to the current row number, which sums up to `1 + 2 + 3 + ... + n`, a series that has a sum of `n(n+1)/2`, which is `O(n^2)`.

### Space Complexity:
- The space complexity is also `O(n^2)`.
- This is because the function constructs Pascal's Triangle, which occupies `n(n+1)/2` elements in total when considering all rows. Since `n(n+1)/2` simplifies to `O(n^2)`, the space complexity is `O(n^2)`.

In summary, the function efficiently builds Pascal's Triangle row by row, calculating each element as the sum of the two elements directly above it in the previous row, with time and space complexities both being `O(n^2)`.
"""
