class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


"""
### Initialization

Before we start the loops, we initialize a `dp` (dynamic programming) array of size `amount + 1`. We use `amount + 1` because we want 
to include a solution for every amount from `0` to `amount` inclusive. The `0th` index represents the minimum number of coins needed 
for an amount of `0`, which is always `0` since no coins are needed to make up an amount of `0`. The rest of the indices (from `1` to `
amount`) are initialized to a large value (like `float('inf')`) to indicate that they haven't been computed yet.

### Iteration Breakdown

Now, let's iterate over each coin and then for each amount from the coin value to the total amount. 
We'll use the same example: coins `[1, 2, 5]` and an amount of `11`.

#### Processing Coin 1

1. **Amount 1 (dp[1])**: The minimum of `dp[1]` (currently `inf`) and `dp[1 - 1] + 1` (which is `dp[0] + 1 = 0 + 1 = 1`). So, `dp[1]` becomes `1`.
2. **Amount 2 (dp[2])**: The minimum of `dp[2]` (currently `inf`) and `dp[2 - 1] + 1` (which is `dp[1] + 1 = 1 + 1 = 2`). So, `dp[2]` becomes `2`.
3. This process continues up to **Amount 11 (dp[11])**, where `dp[11]` becomes `11`.
- dp array progresses as: [0,1,2,3,4,5,6,7,8,9,10,11]

#### Processing Coin 2

1. **Amount 2 (dp[2])**: The minimum of `dp[2]` (currently `2`) and `dp[2 - 2] + 1` (which is `dp[0] + 1 = 0 + 1 = 1`). So, `dp[2]` becomes `1`.
2. **Amount 3 (dp[3])**: The minimum of `dp[3]` (currently `3`) and `dp[3 - 2] + 1` (which is `dp[1] + 1 = 1 + 1 = 2`). So, `dp[3]` becomes `2`.
3. This process continues up to **Amount 11 (dp[11])**, where `dp[11]` becomes `6`.
- Updated dp array: [0,1,1,2,2,3,3,4,4,5,5,6]

#### Processing Coin 5

1. **Amount 5 (dp[5])**: The minimum of `dp[5]` (currently `5`) and `dp[5 - 5] + 1` (which is `dp[0] + 1 = 0 + 1 = 1`). So, `dp[5]` becomes `1`.
2. **Amount 6 (dp[6])**: The minimum of `dp[6]` (currently `3`) and `dp[6 - 5] + 1` (which is `dp[1] + 1 = 1 + 1 = 2`). So, `dp[6]` becomes `2`.
3. This process continues up to **Amount 11 (dp[11])**, where `dp[11]` becomes `3`.
- Final dp array: [0,1,1,2,2,1,2,2,3,3,2,3]

The minimum number of coins needed to make up the amount 11 is 3 (which is achieved by using one 5-coin and two 2-coins or three 5-coins)

### Why `amount + 1`

We use `amount + 1` to create an array that includes an index for every possible amount from `0` to `amount`. This allows us to directly 
use the amount as an index into the `dp` array. For example, `dp[5]` gives us the answer for the amount `5`. If we only had an array of 
size `amount`, we wouldn't have an index for the full amount, as array indices start from `0`. Hence, `dp[amount]` would be out of bounds. 

In summary, the `dp` array stores the minimum number of coins needed for all amounts from `0` to `amount`, and using `amount + 1` 
ensures that we have a direct mapping from the amount to its corresponding index in the `dp` array.

The Coin Change algorithm is a dynamic programming solution because it builds up the solution to the problem by using the solutions of 
its sub-problems, which are stored and reused in subsequent calculations. This reuse of previously computed results is a key 
characteristic of dynamic programming.

Let's break down the steps even more granularly to illustrate how dynamic programming is at work here:

### Basic Concept

1. **Sub-problems**: The algorithm breaks down the main problem (finding the minimum number of coins for a total amount) into smaller 
sub-problems (finding the minimum number of coins for smaller amounts).

2. **Storing Results**: It stores the results of these sub-problems in a `dp` (dynamic programming) array. Once the minimum number of 
coins needed for a smaller amount is calculated, it's stored and doesn't need to be recalculated.

3. **Building Up**: The solution to the larger problem is built up from these stored results. For each coin and each amount, the algorithm 
checks if using that coin improves (i.e., reduces) the number of coins needed.

### Detailed Breakdown

Consider the coins `[1, 2, 5]` and the amount `11`. We'll focus on how the solution for amount `6` is built using previously calculated 
results:

1. **Initial State**: Initially, the `dp` array is `[0, 1, 1, 2, 2, 1, inf, ..., inf]`.

2. **Amount 6 - Coin 1**:
   - To make `6` using 1-coin, we can use the solution for `6 - 1 = 5` and add one more 1-coin.
   - The minimum coins for `5` is already calculated as `1` (from previous iterations).
   - Thus, using a 1-coin for `6` gives us `1 (for 5) + 1 (extra 1-coin) = 2` coins.

3. **Amount 6 - Coin 2**:
   - To make `6` using 2-coin, we look at the solution for `6 - 2 = 4`.
   - The minimum coins for `4` is `2` (using two 2-coins).
   - Thus, using a 2-coin for `6` gives us `2 (for 4) + 1 (extra 2-coin) = 3` coins.

4. **Amount 6 - Coin 5**:
   - To make `6` using 5-coin, we look at the solution for `6 - 5 = 1`.
   - The minimum coins for `1` is `1` (using one 1-coin).
   - Thus, using a 5-coin for `6` gives us `1 (for 1) + 1 (extra 5-coin) = 2` coins.

5. **Choosing the Best Option**:
   - For amount `6`, the options are `2 coins` (using 1-coins), `3 coins` (using 2-coins), and `2 coins` (using 5 and 1-coins).
   - The algorithm chooses the minimum of these, which is `2 coins`.

6. **Update `dp` Array**:
   - `dp[6]` is updated to `2`, indicating the minimum coins needed for `6` is `2`.

7. **Proceeding Further**:
   - This process continues for amounts `7, 8, ...` up to `11`, each time using the solutions of smaller sub-problems stored in 
   the `dp` array.

### Summary

- **Reusing Solutions**: The algorithm doesn't recompute the minimum coins for amounts like `5`, `4`, `1` etc., every time. It uses the 
stored values in the `dp` array.
- **Optimizing Step by Step**: For each new amount and each coin, it only needs to make a simple calculation based on already computed 
values.
- **Dynamic Programming**: This method of solving a problem by combining solutions of sub-problems and optimizing at each step exemplifies 
dynamic programming.

The time and space complexity of the Coin Change problem solved with dynamic programming are as follows:

1. **Time Complexity**: The time complexity is (O(m * n)), where (m) is the amount and (n) is the number of coin denominations. 
This is because the algorithm iterates through all coin denominations for each amount up to the target amount. 
For each combination of amount and coin, the algorithm performs a constant time operation (a minimum comparison).

2. **Space Complexity**: The space complexity is (O(m)), where (m) is the amount. This is due to the use of a one-dimensional 
array (`dp`) of size `m + 1` (to include the amount 0). This array is used to store the minimum number of coins needed for each amount 
up to (m). No additional significant space is used, so the space complexity is linear with respect to the amount.
"""