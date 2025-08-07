# 658. Find K Closest Elements

## Problem Description

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
- `|a - x| < |b - x|`, or  
- `|a - x| == |b - x|` and `a < b`

**Difficulty**: Medium

## Examples

**Example 1:**
```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Explanation: The distances from x=3 are: [2,1,0,1,2]. The 4 closest elements are [1,2,3,4].
```

**Example 2:**
```
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
Explanation: All elements have distance >= 2 from x=-1. Since we need 4 elements and ties go to smaller values, we take the first 4.
```

## Constraints
- `1 <= k <= arr.length`
- `1 <= arr.length <= 10^4`
- `arr` is sorted in ascending order
- `-10^4 <= arr[i], x <= 10^4`

## Solution: Binary Search for Optimal Window

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Find k closest elements to x using binary search.
        
        The key insight: We're looking for the best starting position
        for a window of size k, not individual elements.
        """
        low, high = 0, len(arr) - k
        
        while low < high:
            mid = (low + high) // 2
            
            # Compare distances from x to window boundaries
            # If left boundary is farther than right boundary, move window right
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
        
        return arr[low:low + k]
```

## Algorithm Explanation

### Key Insight
Instead of finding individual closest elements, we search for the optimal starting position of a sliding window of size `k`.

### Binary Search Logic
We binary search on possible starting positions `[0, len(arr)-k]`:

1. **Window Comparison**: For each potential starting position `mid`, we have a window `[mid, mid+k-1]`
2. **Distance Check**: Compare distances from `x` to window boundaries:
   - Left boundary distance: `x - arr[mid]`
   - Right boundary distance: `arr[mid+k] - x`
3. **Decision**: If left boundary is farther, move window right; otherwise, keep current or move left

### Visual Walkthrough

For `arr = [1,2,3,4,5]`, `k = 4`, `x = 3`:

```
Initial: low = 0, high = 1 (len(arr) - k = 5 - 4 = 1)

Iteration 1:
mid = 0
Window: [1,2,3,4] (indices 0-3)
Left boundary distance: |3 - 1| = 2
Right boundary distance: |5 - 3| = 2 (arr[mid+k] = arr[4] = 5)
Since 2 = 2, we choose left (high = mid = 0)

Final: low = high = 0
Return: arr[0:4] = [1,2,3,4]
```

For `arr = [1,1,2,3,4,5]`, `k = 4`, `x = -1`:

```
Initial: low = 0, high = 2

Iteration 1:
mid = 1
Window candidates: [1,2,3,4] vs [1,1,2,3]
Left distance from pos 1: |-1 - 1| = 2
Right distance: |4 - (-1)| = 5
Since 2 < 5, we keep left side (high = mid = 1)

Continue until low = high = 0
Return: arr[0:4] = [1,1,2,3]
```

## Alternative Solutions

### Approach 1: Two Pointers (O(n))
```python
def findClosestElements_twopointers(self, arr, k, x):
    left, right = 0, len(arr) - 1
    
    # Remove farthest elements until we have k elements
    while right - left >= k:
        if x - arr[left] > arr[right] - x:
            left += 1
        else:
            right -= 1
    
    return arr[left:right + 1]
```

### Approach 2: Sort by Distance (O(n log n))
```python
def findClosestElements_sort(self, arr, k, x):
    # Sort by distance, then by value for ties
    sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))
    result = sorted_arr[:k]
    return sorted(result)  # Return in ascending order
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|--------|
| Binary Search | O(log(n-k) + k) | O(1) | Optimal for large arrays |
| Two Pointers | O(n) | O(1) | Simple, good for small arrays |
| Sort by Distance | O(n log n) | O(n) | Intuitive but less efficient |

## Key Insights

1. **Window-based Thinking**: Search for optimal window position, not individual elements
2. **Boundary Comparison**: Compare distances to window edges to determine search direction  
3. **Sorted Output**: Since input is sorted and we return a contiguous subarray, output is automatically sorted
4. **Tie-breaking**: The condition `x - arr[mid] > arr[mid+k] - x` naturally handles ties by favoring smaller elements

## Edge Cases and Test Cases

```python
# Test cases
sol = Solution()

# Basic cases
assert sol.findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
assert sol.findClosestElements([1,1,2,3,4,5], 4, -1) == [1,1,2,3]

# Edge cases
assert sol.findClosestElements([1], 1, 1) == [1]  # Single element
assert sol.findClosestElements([1,2,3], 3, 2) == [1,2,3]  # Return entire array
assert sol.findClosestElements([1,3,4,5,6], 3, 2) == [1,3,4]  # x not in array
assert sol.findClosestElements([1,2,3,4,5], 1, 3) == [3]  # k=1, exact match

# Boundary cases
assert sol.findClosestElements([1,2,3,4,5], 2, 0) == [1,2]  # x smaller than all
assert sol.findClosestElements([1,2,3,4,5], 2, 6) == [4,5]  # x larger than all
```

## Why Binary Search Works

The problem has a **monotonic property**: if a window starting at position `i` is better than starting at position `i+1`, then positions `i+2, i+3, ...` are also worse than position `i`. This monotonicity allows us to use binary search to find the optimal starting position efficiently.

## Time Optimization
- **O(log(n-k))** for binary search to find starting position
- **O(k)** to extract the subarray
- **Total: O(log(n-k) + k)** which is much better than O(n) for large arrays