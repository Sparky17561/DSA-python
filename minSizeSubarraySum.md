# 209. Minimum Size Subarray Sum - Sliding Window Solution

**Difficulty**: Medium  
**Topics**: Array, Binary Search, Sliding Window, Prefix Sum

## Problem Description

Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Approach: Sliding Window (Two Pointers)

This solution uses the **sliding window** technique with two pointers to efficiently find the minimum subarray length in O(n) time complexity.

### Key Concepts

1. **Two Pointers**: `left` and `right` pointers define the current window
2. **Expanding Window**: Move `right` pointer to expand the window and increase the sum
3. **Contracting Window**: When sum ≥ target, move `left` pointer to minimize window size
4. **Track Minimum**: Keep track of the smallest valid window size found

### Algorithm Steps

1. Initialize `left = 0`, `min_len = infinity`, and `curr_sum = 0`
2. For each `right` position from 0 to n-1:
   - Add `nums[right]` to `curr_sum` (expand window)
   - While `curr_sum >= target`:
     - Update `min_len` with current window size (`right - left + 1`)
     - Remove `nums[left]` from `curr_sum` and increment `left` (contract window)
3. Return `min_len` if found, otherwise return 0

### Time Complexity: O(n)
- Each element is visited at most twice (once by `right`, once by `left`)

### Space Complexity: O(1)
- Only using constant extra space

## Example Walkthrough

Let's trace through the algorithm with `target = 7` and `nums = [2,3,1,2,4,3]`:

```
Initial: left=0, right=0, curr_sum=0, min_len=∞

Step 1: right=0, nums[0]=2
  curr_sum = 0 + 2 = 2
  2 < 7, continue

Step 2: right=1, nums[1]=3  
  curr_sum = 2 + 3 = 5
  5 < 7, continue

Step 3: right=2, nums[2]=1
  curr_sum = 5 + 1 = 6
  6 < 7, continue

Step 4: right=3, nums[3]=2
  curr_sum = 6 + 2 = 8
  8 >= 7, found valid window [2,3,1,2]
  min_len = min(∞, 3-0+1) = 4
  curr_sum = 8 - nums[0] = 8 - 2 = 6, left=1
  6 < 7, continue

Step 5: right=4, nums[4]=4
  curr_sum = 6 + 4 = 10
  10 >= 7, found valid window [3,1,2,4]
  min_len = min(4, 4-1+1) = 4
  curr_sum = 10 - nums[1] = 10 - 3 = 7, left=2
  7 >= 7, found valid window [1,2,4]
  min_len = min(4, 4-2+1) = 3
  curr_sum = 7 - nums[2] = 7 - 1 = 6, left=3
  6 < 7, continue

Step 6: right=5, nums[5]=3
  curr_sum = 6 + 3 = 9
  9 >= 7, found valid window [2,4,3]
  min_len = min(3, 5-3+1) = 3
  curr_sum = 9 - nums[3] = 9 - 2 = 7, left=4
  7 >= 7, found valid window [4,3]
  min_len = min(3, 5-4+1) = 2
  curr_sum = 7 - nums[4] = 7 - 4 = 3, left=5
  3 < 7, continue

Result: min_len = 2
```

The minimum subarray length is **2**, corresponding to the subarray `[4,3]` with sum 7.

## Edge Cases

- **No valid subarray**: If no subarray sum ≥ target, return 0
- **Single element**: If any single element ≥ target, return 1
- **Entire array needed**: If only the entire array sum ≥ target, return array length

## Complete Solution

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        min_len = float('inf')
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
```

## Why This Approach Works

The sliding window technique is perfect for this problem because:

1. **Monotonic Property**: As we add elements, the sum only increases
2. **Optimal Substructure**: If a window is valid, we want to minimize its size
3. **No Need to Backtrack**: Once we shrink a window, we don't need to re-examine those combinations
4. **Linear Time**: Each element is processed at most twice, giving us O(n) complexity

This makes it much more efficient than a brute force O(n²) approach that checks all possible subarrays.