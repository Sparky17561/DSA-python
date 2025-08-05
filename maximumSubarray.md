# Kadane's Algorithm - Maximum Subarray Problem

## Problem Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**
- Input: `[-2,1,-3,4,-1,2,1,-5,4]`
- Output: `6`
- Explanation: `[4,-1,2,1]` has the largest sum = `6`

## Algorithm Explanation

**Kadane's Algorithm** is a dynamic programming approach that efficiently solves the maximum subarray problem in linear time. The key insight is that at each position, we decide whether to:

1. **Start a new subarray** from the current element
2. **Extend the existing subarray** by including the current element

### Core Logic

At each position `i`, we maintain:
- `currSum`: Maximum sum ending at position `i`
- `maxSum`: Maximum sum seen so far

The decision rule is:
```
currSum = max(nums[i], currSum + nums[i])
```

This means:
- If `currSum + nums[i] < nums[i]`, start fresh from `nums[i]`
- Otherwise, extend the current subarray

### Why It Works

The algorithm works because:
- If the cumulative sum becomes negative, it's better to start fresh
- We keep track of the maximum sum encountered so far
- Each element is considered exactly once

## Complete Solution

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        Find the contiguous subarray with the largest sum using Kadane's Algorithm
        
        :type nums: List[int]
        :rtype: int
        """
        # Initialize both current sum and maximum sum to first element
        currSum = maxSum = nums[0]
        
        # Iterate through the rest of the array
        for i in range(1, len(nums)):
            # Decide: start new subarray or extend current one
            currSum = max(nums[i], currSum + nums[i])
            
            # Update maximum sum if current sum is larger
            maxSum = max(maxSum, currSum)
            
        return maxSum
```

## Step-by-Step Example

Let's trace through `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

| i | nums[i] | currSum calculation | currSum | maxSum |
|---|---------|-------------------|---------|--------|
| 0 | -2      | Initialize        | -2      | -2     |
| 1 | 1       | max(1, -2+1) = 1  | 1       | 1      |
| 2 | -3      | max(-3, 1-3) = -2 | -2      | 1      |
| 3 | 4       | max(4, -2+4) = 4  | 4       | 4      |
| 4 | -1      | max(-1, 4-1) = 3  | 3       | 4      |
| 5 | 2       | max(2, 3+2) = 5   | 5       | 5      |
| 6 | 1       | max(1, 5+1) = 6   | 6       | 6      |
| 7 | -5      | max(-5, 6-5) = 1  | 1       | 6      |
| 8 | 4       | max(4, 1+4) = 5   | 5       | 6      |

**Result:** Maximum subarray sum = `6` (subarray `[4, -1, 2, 1]`)

## Complexity Analysis

### Time Complexity: O(n)
- Single pass through the array
- Constant time operations at each step
- Linear time complexity regardless of input values

### Space Complexity: O(1)
- Only uses two variables (`currSum` and `maxSum`)
- No additional data structures needed
- Constant extra space

## Edge Cases

The algorithm handles various edge cases:

1. **All negative numbers**: `[-3, -2, -5, -1]` → Returns `-1` (least negative)
2. **Single element**: `[5]` → Returns `5`
3. **All positive numbers**: `[1, 2, 3, 4]` → Returns `10` (sum of all)
4. **Mixed positive/negative**: `[-2, 1, -3, 4]` → Returns `4`

## Alternative Approaches

| Approach | Time | Space | Description |
|----------|------|-------|-------------|
| Brute Force | O(n³) | O(1) | Check all possible subarrays |
| Optimized Brute Force | O(n²) | O(1) | Avoid recalculating sums |
| **Kadane's Algorithm** | **O(n)** | **O(1)** | **Dynamic programming approach** |
| Divide & Conquer | O(n log n) | O(log n) | Recursive solution |

## Usage

```python
# Create solution instance
solution = Solution()

# Test cases
test_cases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Expected: 6
    [1],                               # Expected: 1
    [5, 4, -1, 7, 8],                 # Expected: 23
    [-1, -2, -3, -4]                  # Expected: -1
]

for nums in test_cases:
    result = solution.maxSubArray(nums)
    print(f"Input: {nums}")
    print(f"Maximum subarray sum: {result}\n")
```

## Key Takeaways

- Kadane's Algorithm is the optimal solution for the maximum subarray problem
- The key insight is the greedy choice: extend or restart at each position  
- Time complexity is linear, making it suitable for large datasets
- The algorithm demonstrates the power of dynamic programming in optimization problems