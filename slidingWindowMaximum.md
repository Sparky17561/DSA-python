# 239. Sliding Window Maximum

## Problem Description

Given an array of integers `nums` and a sliding window of size `k` moving from left to right, return the maximum value in each window position.

**Difficulty**: Hard

## Examples

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Window positions:
[1  3  -1] -3  5  3  6  7  → Max: 3
 1 [3  -1  -3] 5  3  6  7  → Max: 3
 1  3 [-1  -3  5] 3  6  7  → Max: 5
 1  3  -1 [-3  5  3] 6  7  → Max: 5
 1  3  -1  -3 [5  3  6] 7  → Max: 6
 1  3  -1  -3  5 [3  6  7] → Max: 7
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Solutions

### Solution 1: Deque (Optimal - O(n))

```python
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = deque()
        res = []
        
        for i, cur in enumerate(nums):
            # Remove smaller elements from back
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)

            # Remove elements outside window
            if q[0] == i - k:
                q.popleft()
            
            # Add result when window is complete
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res
```

**Time Complexity**: O(n) - each element is added and removed at most once  
**Space Complexity**: O(k) - deque stores at most k elements

**How it works**:
- Uses a deque to maintain indices of potentially maximum elements
- Keeps deque in decreasing order of values
- Front of deque always contains index of current window's maximum
- Removes indices outside current window

### Solution 2: HashMap with Sliding Window (Alternative)

```python
from collections import defaultdict

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 1:
            return nums

        res = []
        window = defaultdict(int)
        left = 0
        
        # Initialize first window
        for i in range(k):
            window[nums[i]] += 1
            
        # Slide the window
        for right in range(k, len(nums)):
            res.append(max(window.keys()))
            
            # Add new element
            window[nums[right]] += 1
            
            # Remove leftmost element
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                del window[nums[left]]
            left += 1

        # Add last window result
        res.append(max(window.keys()))
        return res
```

**Time Complexity**: O(n × k) - max() operation takes O(k) time  
**Space Complexity**: O(k) - hashmap stores at most k unique elements

## Algorithm Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Deque | O(n) | O(k) | Optimal time complexity | More complex logic |
| HashMap | O(n×k) | O(k) | Intuitive approach | Slower due to max() calls |

## Key Insights

1. **Deque Approach**: Maintains a monotonic decreasing deque of indices
2. **HashMap Approach**: Tracks element frequencies in current window
3. The deque solution is optimal as it avoids redundant comparisons
4. Both solutions use sliding window technique but with different data structures

## Test Cases

```python
# Test the solutions
sol = Solution()

# Basic test
assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

# Single element
assert sol.maxSlidingWindow([1], 1) == [1]

# All same elements
assert sol.maxSlidingWindow([1,1,1,1], 2) == [1,1,1]

# Decreasing array
assert sol.maxSlidingWindow([7,6,5,4,3], 3) == [7,6,5]
```