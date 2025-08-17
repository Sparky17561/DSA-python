Search a 2D Matrix (LeetCode 74)

Intuition (short)

You are given a matrix where each row is sorted in ascending order and the first integer of every row is greater than the last integer of the previous row. This means the whole matrix can be thought of as one sorted list if you read rows left-to-right, top-to-bottom.

Two common, correct approaches:

Two-step binary search (what your code does)

Binary-search the row that could contain the target by comparing target with the first and last element of a row.

Then binary-search inside that row to find the target.

Flattened-binary search (single binary search over indices)

Treat index i of the flattened list as row = i // cols, col = i % cols. Do one binary search on range [0, rows * cols - 1] and map mid to (r, c).

Both are O(log rows + log cols) or O(log(rows*cols)) time, which are equivalent asymptotically. The flattened approach is often simpler and less bug-prone.

When to use which

Two-step is intuitive and matches your code; good if you naturally think row-first.

Flattened is concise and reduces corner cases (no separate row-search loop). I recommend flattened for clarity unless you need row-specific logic.

Code — two-step binary search (clean, commented)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Two-step binary search:
          1) find the candidate row using binary search on rows
          2) search inside that row using binary search on columns
        """

        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # 1) binary search on rows to find the row that could contain target
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            # If target is inside this row's range, we've found candidate row
            if matrix[mid_row][0] <= target <= matrix[mid_row][cols - 1]:
                row = mid_row
                break
            elif matrix[mid_row][cols - 1] < target:
                # target is larger than this row's last element -> go down
                top = mid_row + 1
            else:
                # target is smaller than this row's first element -> go up
                bottom = mid_row - 1
        else:
            # loop finished without break -> no candidate row
            return False

        # 2) binary search within the row
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

Code — flattened single binary search (recommended)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        Treat the matrix as one sorted array of length rows*cols.
        Map an index i -> (i // cols, i % cols) to fetch the value.
        """

        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            val = matrix[r][c]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

Example (worked)

Input:

matrix = [
  [1, 3, 5, 7],
  [10,11,16,20],
  [23,30,34,50]
]
target = 3

Flattened search idea (indices shown):

index: 0  1  2  3   4  5   6   7   8   9   10  11
value: 1, 3, 5, 7, 10,11,16,20,23,30,34,50

Binary search finds index 1 → maps to row 1//4 = 0, col 1%4 = 1 → matrix[0][1] = 3 → found.

Complexity

Time: O(log(rows * cols)) using flattened or O(log rows + log cols) for two-step.

Space: O(1) extra.

Tips & pitfalls

Always check matrix and matrix[0] for emptiness to avoid index errors.

Be consistent with <= vs < in row-range checks. Using matrix[row][0] <= target <= matrix[row][cols - 1] is clear and safe.

Flattened mapping must use correct cols value: r = mid // cols, c = mid % cols.

