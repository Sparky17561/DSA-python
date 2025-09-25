# Triangle - Minimum Path Sum

## Problem Description

Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

## Examples

### Example 1
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3

The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11
```

### Example 2
```
Input: triangle = [[-10]]
Output: -10
```

## Constraints

- `1 <= triangle.length <= 200`
- `triangle[0].length == 1`
- `triangle[i].length == triangle[i - 1].length + 1`
- `-10^4 <= triangle[i][j] <= 10^4`

## Solution Approach

### Algorithm: Bottom-Up Dynamic Programming

The solution uses a bottom-up dynamic programming approach that modifies the input triangle in-place to achieve O(1) extra space complexity.

**Key Insight**: Instead of tracking all possible paths from top to bottom, we work backwards from the bottom row to the top, at each position storing the minimum sum needed to reach the bottom from that position.

### Step-by-Step Process

1. **Start from the second-to-last row** and move upwards
2. **For each element in the current row**, add the minimum of the two adjacent elements from the row below
3. **Continue until we reach the top** of the triangle
4. **The top element** now contains the minimum path sum

### Code Implementation

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start from second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Add the current value with the min of the two adjacent values from the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        return triangle[0][0]  # Top element now contains the minimum path sum
```

### Example Walkthrough

For triangle `[[2],[3,4],[6,5,7],[4,1,8,3]]`:

**Initial state:**
```
   2
  3 4
 6 5 7
4 1 8 3
```

**Step 1 - Process row 2 (6,5,7):**
- `triangle[2][0] = 6 + min(4,1) = 6 + 1 = 7`
- `triangle[2][1] = 5 + min(1,8) = 5 + 1 = 6`
- `triangle[2][2] = 7 + min(8,3) = 7 + 3 = 10`

State: `[[2],[3,4],[7,6,10],[4,1,8,3]]`

**Step 2 - Process row 1 (3,4):**
- `triangle[1][0] = 3 + min(7,6) = 3 + 6 = 9`
- `triangle[1][1] = 4 + min(6,10) = 4 + 6 = 10`

State: `[[2],[9,10],[7,6,10],[4,1,8,3]]`

**Step 3 - Process row 0 (2):**
- `triangle[0][0] = 2 + min(9,10) = 2 + 9 = 11`

Final state: `[[11],[9,10],[7,6,10],[4,1,8,3]]`

**Result: 11**

## Complexity Analysis

- **Time Complexity**: O(n²) where n is the number of rows
  - We visit each element in the triangle exactly once
  - Total elements in triangle = 1 + 2 + 3 + ... + n = n(n+1)/2 = O(n²)

- **Space Complexity**: O(1) extra space
  - We modify the input triangle in-place
  - Only using constant extra space for loop variables

## Alternative Approaches

### 1. Top-Down with Memoization
- Time: O(n²), Space: O(n²)
- Uses recursion with memoization table

### 2. Bottom-Up with Separate DP Array
- Time: O(n²), Space: O(n)
- Maintains a separate array for DP values

### 3. Top-Down without Modification
- Time: O(n²), Space: O(n)
- Processes from top to bottom using additional space

## Key Advantages of This Solution

1. **Space Efficient**: Uses only O(1) extra space by modifying input in-place
2. **Simple Logic**: Bottom-up approach is intuitive and easy to understand
3. **Optimal Time**: Achieves the best possible time complexity O(n²)
4. **No Recursion**: Iterative solution avoids potential stack overflow

## Usage

```python
# Example usage
solution = Solution()
triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(solution.minimumTotal(triangle1))  # Output: 11

triangle2 = [[-10]]
print(solution.minimumTotal(triangle2))  # Output: -10
```

## LeetCode Problem Link
[120. Triangle](https://leetcode.com/problems/triangle/)