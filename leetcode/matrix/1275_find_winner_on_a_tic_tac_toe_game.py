class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag1 = diag2 = 0
        for index, move in enumerate(moves):
            i, j = move
            sign = 1 if index % 2 == 0 else -1
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag1 += sign
            if i + j == n-1:
                diag2 += sign
            if abs(rows[i]) == n or abs(cols[j]) == n or abs(diag1) == n or abs(diag2) == n:
                return 'A' if sign == 1 else 'B'
        return "Draw" if len(moves) == (n * n) else 'Pending'


"""
Let's use the following sequence of moves:

1. Player A places a mark at (0, 0)
2. Player B places a mark at (1, 1)
3. Player A places a mark at (0, 1)
4. Player B places a mark at (2, 0)
5. Player A places a mark at (0, 2)

### Initial State:
- Board: 3x3 grid
- Rows, Columns, Diagonals: `rows = [0, 0, 0]`, `cols = [0, 0, 0]`, `diag1 = 0`, `diag2 = 0`
- No moves made yet.

### Move 1: Player A at (0, 0)
- Sign: `1` (since it's Player A's turn)
- Update Rows and Columns: `rows[0] += 1` (now `rows = [1, 0, 0]`), `cols[0] += 1` (now `cols = [1, 0, 0]`)
- Diagonals Update: `diag1 += 1` (now `diag1 = 1`) because (0, 0) is on the main diagonal.
- Diagonal 2 not affected.
- Check for win: No absolute value equals 3, so no win yet.

### Move 2: Player B at (1, 1)
- Sign: `-1` (Player B's turn)
- Update Rows and Columns: `rows[1] -= 1` (now `rows = [1, -1, 0]`), `cols[1] -= 1` (now `cols = [1, -1, 0]`)
- Diagonals Update: `diag1 -= 1` (now `diag1 = 0`), `diag2 -= 1` (now `diag2 = -1`) because (1, 1) is on both diagonals.
- Check for win: No absolute value equals 3, so no win yet.

### Move 3: Player A at (0, 1)
- Sign: `1` (Player A's turn)
- Update Rows and Columns: `rows[0] += 1` (now `rows = [2, -1, 0]`), `cols[1] += 1` (now `cols = [1, 0, 0]`)
- Diagonals not affected.
- Check for win: No absolute value equals 3, so no win yet.

### Move 4: Player B at (2, 0)
- Sign: `-1` (Player B's turn)
- Update Rows and Columns: `rows[2] -= 1` (now `rows = [2, -1, -1]`), `cols[0] -= 1` (now `cols = [0, 0, 0]`)
- Diagonals not affected.
- Check for win: No absolute value equals 3, so no win yet.

### Move 5: Player A at (0, 2)
- Sign: `1` (Player A's turn)
- Update Rows and Columns: `rows[0] += 1` (now `rows = [3, -1, -1]`), `cols[2] += 1` (now `cols = [0, 0, 1]`)
- Diagonals not affected.
- Check for win: `abs(rows[0])` equals 3, so Player A wins.

The function would now return 'A', indicating that Player A has won the game by marking a complete row (row 0). This breakdown shows how the function tracks the state of each row, column, and diagonal after each move to determine the game status.

### Time Complexity

1. Initialization: Initializing the rows, columns, and diagonal counters takes constant time, O(1), as their sizes are fixed and independent of the input.

2. Processing Moves:
   - For each move in the `moves` list, the function updates the corresponding row, column, and possibly the diagonals. This update operation is constant time, O(1), for each move.
   - After each move, the function checks if any row, column, or diagonal has an absolute value equal to the board size (3 in this case). This check is also O(1) as it involves a fixed number of comparisons.

Since each move is processed in constant time, and there are `m` moves, where `m` is the length of the `moves` list, the total time complexity for processing all moves is O(m).

### Space Complexity

1. Data Structures: The function uses fixed-size arrays for rows and columns (`rows`, `cols`), and two variables for diagonals (`diag1`, `diag2`). These structures do not scale with the number of moves, so their space requirement is constant, O(1).

2. Input Storage: The function takes the `moves` list as input, but it does not allocate additional space that scales with the size of this list.

3. Auxiliary Space: No additional significant space is used in the function.

Considering these factors, the overall space complexity of the function is O(1), as the space used does not scale with the input size (number of moves).

In summary:
- Time Complexity: O(m), where m is the number of moves.
- Space Complexity: O(1), constant space.
"""