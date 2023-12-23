class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        min_purchase = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_purchase)
            min_purchase = min(min_purchase, prices[i])
        
        return max_profit

"""
The example list of prices `[7, 1, 5, 3, 6, 4]`. 

### Iteration Breakdown:
1. **Initial Setup:**
   - `max_profit = 0`
   - `min_purchase = 7` (price on day 1)

2. **Day 2: Price = 1**
   - `max_profit` calculation: `max(0, 1 - 7) = 0`
   - Update `min_purchase`: `min(7, 1) = 1`
   - Outputs: `max_profit = 0`, `min_purchase = 1`

3. **Day 3: Price = 5**
   - `max_profit` calculation: `max(0, 5 - 1) = 4`
   - Update `min_purchase`: `min(1, 5) = 1`
   - Outputs: `max_profit = 4`, `min_purchase = 1`

4. **Day 4: Price = 3**
   - `max_profit` calculation: `max(4, 3 - 1) = 4`
   - Update `min_purchase`: `min(1, 3) = 1`
   - Outputs: `max_profit = 4`, `min_purchase = 1`

5. **Day 5: Price = 6**
   - `max_profit` calculation: `max(4, 6 - 1) = 5`
   - Update `min_purchase`: `min(1, 6) = 1`
   - Outputs: `max_profit = 5`, `min_purchase = 1`

6. **Day 6: Price = 4**
   - `max_profit` calculation: `max(5, 4 - 1) = 5`
   - Update `min_purchase`: `min(1, 4) = 1`
   - Outputs: `max_profit = 5`, `min_purchase = 1`

### Final Result:
- At the end of the iterations, `max_profit = 5`. This is the maximum profit you can achieve by buying at a price of 1 (on day 2) and selling at a price of 6 (on day 5).

Each day, the algorithm compares the current price with the minimum price seen so far to calculate the potential profit. It updates `max_profit` if the current day's profit exceeds the previous maximum. Simultaneously, it keeps updating `min_purchase` to ensure it always has the lowest price seen so far for buying.

Time Complexity:
The time complexity of this solution is O(n), where n is the number of days (length of the prices list). This is because the function iterates through the list of prices once.

Space Complexity:
The space complexity of this solution is O(1). This is because the function uses a fixed amount of extra space (for variables max_profit and min_purchase), regardless of the input size.
"""