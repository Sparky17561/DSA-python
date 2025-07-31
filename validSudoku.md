# Valid Sudoku Checker

This `isValidSudoku` function checks whether a 9×9 Sudoku board is valid according to the rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine 3×3 sub-boxes must contain the digits `1-9` without repetition.

## Approach

1. **Data Structures**: Use three dictionaries (`rows`, `cols`, `boxes`) mapping indices to sets of seen digits.

   * `rows[r]` stores the digits seen so far in row `r`.
   * `cols[c]` stores the digits seen so far in column `c`.
   * `boxes[(r//3, c//3)]` stores the digits seen so far in the 3×3 sub-box containing cell `(r, c)`.

2. **Iteration**: Traverse each cell `(r, c)` in the board:

   * If the cell contains `'.'`, skip it (empty).
   * Otherwise, let `val = board[r][c]`. Check if `val` already exists in:

     * `rows[r]`
     * `cols[c]`
     * `boxes[(r//3, c//3)]`
   * If it does, return `False` (violation of Sudoku rules).
   * If not, add `val` to each corresponding set.

3. If no violations are found, return `True`.

## Box Index Calculation Explanation

* The board is divided into nine 3×3 boxes. To identify which box a cell `(r, c)` belongs to, use integer division by 3:

  * `r // 3` yields the box-row index (0, 1, or 2).
  * `c // 3` yields the box-column index (0, 1, or 2).

* Pairing them as `(r//3, c//3)` gives a unique identifier for each of the nine boxes:

  | `(r//3, c//3)` | Box Region    |
  | -------------- | ------------- |
  | (0, 0)         | top-left      |
  | (0, 1)         | top-middle    |
  | (0, 2)         | top-right     |
  | (1, 0)         | middle-left   |
  | (1, 1)         | center        |
  | (1, 2)         | middle-right  |
  | (2, 0)         | bottom-left   |
  | (2, 1)         | bottom-middle |
  | (2, 2)         | bottom-right  |

## Time Complexity

* We visit each of the 81 cells exactly once.
* For each cell, operations on sets (membership checks and insertions) take **O(1)** time on average.

**Overall Time Complexity**: O(1) (constant 81 checks), effectively **O(n²)** for an n×n board; here n=9.

## Space Complexity

* We store at most 81 entries across the three dictionaries:

  * `rows`: up to 9 sets, each containing up to 9 digits.
  * `cols`: up to 9 sets, each containing up to 9 digits.
  * `boxes`: up to 9 sets, each containing up to 9 digits.

**Overall Space Complexity**: O(n²) auxiliary space; here n=9.

## Full Code with Comments

```python
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dictionaries to record seen numbers in rows, columns and boxes
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Traverse each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cells
                if val == ".":
                    continue

                # Compute box index as (row_group, col_group)
                box_index = (r // 3, c // 3)

                # If the value has already been seen in row, column or box, it's invalid
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_index]):
                    return False

                # Record the seen value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        # If no duplicates found, it's a valid Sudoku
        return True
```

## Example

```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(board))  # Output: True
```

This example returns `True`, indicating the provided Sudoku board is valid.
