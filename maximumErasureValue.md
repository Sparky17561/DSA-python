# LeetCode 1695: Maximum Erasure Value

## Problem Statement

You are given an array of positive integers `nums` and want to erase a subarray containing **unique elements**. The **score** you get by erasing the subarray is equal to the **sum** of its elements.

Return the **maximum score** you can get by erasing **exactly one** subarray.

An array `b` is called to be a subarray of `a` if it forms a contiguous subsequence of `a`, that is, if it is equal to `a[l], a[l+1], ..., a[r]` for some `(l, r)`.

### Examples

**Example 1:**
```
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
```

**Example 2:**
```
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
```

**Example 3:**
```
Input: nums = [1]
Output: 1
```

## Solution Approach: Sliding Window

### Algorithm Overview
**Time Complexity: O(n) | Space Complexity: O(n)**

This problem is a classic **sliding window** with **unique elements constraint**. We use:
- **Two pointers** (left and right) to maintain the window
- **HashMap** to track element frequencies in current window
- **Running sum** to avoid recalculating sums

```python
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = {}     # Dictionary to track elements in current window
        left = 0        # Left pointer of the window
        max_t = 0       # Maximum sum found so far
        tot = 0         # Current sum of the window

        # Right pointer moves through the array
        for right in range(len(nums)):
            
            # If nums[right] is duplicate, shrink window from left
            while nums[right] in window:
                window[nums[left]] -= 1       # Decrease count
                tot -= nums[left]             # Remove from sum
                if window[nums[left]] == 0:   # Fully removed
                    del window[nums[left]]
                left += 1                     # Shrink window

            # Add current element to window
            window[nums[right]] = window.get(nums[right], 0) + 1
            tot += nums[right]               # Add to sum

            # Update maximum sum
            max_t = max(max_t, tot)

        return max_t
```

## Step-by-Step Visual Walkthrough

Let's trace through `nums = [4, 2, 4, 5, 6]`:

```
Initial State:
├─ window = {}, left = 0, tot = 0, max_t = 0
└─ Array: [4, 2, 4, 5, 6]
           ↑
         right=0

Step 1: right = 0, nums[right] = 4
├─ 4 not in window → add directly
├─ window = {4: 1}, tot = 4, max_t = 4
└─ Current subarray: [4]

Step 2: right = 1, nums[right] = 2  
├─ 2 not in window → add directly
├─ window = {4: 1, 2: 1}, tot = 6, max_t = 6
└─ Current subarray: [4, 2]

Step 3: right = 2, nums[right] = 4
├─ 4 already in window → DUPLICATE DETECTED!
├─ Shrink from left:
│   ├─ Remove nums[0] = 4: window = {2: 1}, tot = 2
│   └─ left = 1
├─ Now add nums[2] = 4: window = {2: 1, 4: 1}, tot = 6
├─ max_t remains 6
└─ Current subarray: [2, 4]

Step 4: right = 3, nums[right] = 5
├─ 5 not in window → add directly  
├─ window = {2: 1, 4: 1, 5: 1}, tot = 11, max_t = 11
└─ Current subarray: [2, 4, 5]

Step 5: right = 4, nums[right] = 6
├─ 6 not in window → add directly
├─ window = {2: 1, 4: 1, 5: 1, 6: 1}, tot = 17, max_t = 17
└─ Current subarray: [2, 4, 5, 6] ← MAXIMUM!

Final Result: 17
```

## Algorithm Intuition

### Why Sliding Window Works:

1. **Expand Phase:** Keep adding elements to the right until we hit a duplicate
2. **Contract Phase:** Remove elements from the left until the duplicate is eliminated
3. **Optimization:** Each element is added once and removed at most once → O(n) total

### Key Insights:

```
Valid Subarrays in [4, 2, 4, 5, 6]:
├─ [4] → sum = 4
├─ [4, 2] → sum = 6  
├─ [2] → sum = 2
├─ [2, 4] → sum = 6
├─ [2, 4, 5] → sum = 11
├─ [2, 4, 5, 6] → sum = 17 ✓ (Maximum)
├─ [4] → sum = 4
├─ [4, 5] → sum = 9
├─ [4, 5, 6] → sum = 15
├─ [5] → sum = 5
├─ [5, 6] → sum = 11
└─ [6] → sum = 6
```

## Alternative Solutions

### Approach 1: Optimized Sliding Window (Set-based)
**Time Complexity: O(n) | Space Complexity: O(n)**

```python
def maximumUniqueSubarray(self, nums):
    seen = set()
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(len(nums)):
        # Shrink window until no duplicates
        while nums[right] in seen:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        
        # Add current element
        seen.add(nums[right])
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### Approach 2: HashMap with Last Seen Index
**Time Complexity: O(n) | Space Complexity: O(n)**

```python
def maximumUniqueSubarray(self, nums):
    last_seen = {}
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(len(nums)):
        # If we've seen this element and it's in current window
        if nums[right] in last_seen and last_seen[nums[right]] >= left:
            # Remove elements from left until duplicate is gone
            for i in range(left, last_seen[nums[right]] + 1):
                current_sum -= nums[i]
            left = last_seen[nums[right]] + 1
        
        # Add current element
        last_seen[nums[right]] = right
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### Approach 3: Brute Force (For Understanding)
**Time Complexity: O(n³) | Space Complexity: O(n)**

```python
def maximumUniqueSubarray(self, nums):
    max_sum = 0
    n = len(nums)
    
    # Try all possible subarrays
    for i in range(n):
        seen = set()
        current_sum = 0
        for j in range(i, n):
            if nums[j] in seen:
                break
            seen.add(nums[j])
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum
```

## Complexity Analysis

| Method | Time Complexity | Space Complexity | Notes |
|--------|----------------|------------------|-------|
| Sliding Window (HashMap) | O(n) | O(n) | Your optimal solution |
| Sliding Window (Set) | O(n) | O(n) | Cleaner implementation |
| Last Seen Index | O(n) | O(n) | Different approach |
| Brute Force | O(n³) | O(n) | For understanding only |

## Why Your Solution is Optimal

### Amortized Analysis:
- **Each element enters the window exactly once** (when right pointer reaches it)
- **Each element leaves the window at most once** (when left pointer passes it)  
- **Total operations:** 2n → O(n) time complexity

### Space Efficiency:
- HashMap stores at most `n` unique elements
- In practice, often much smaller than `n`

## Common Mistakes to Avoid

1. **Forgetting to remove from sum** when shrinking window
2. **Not handling HashMap cleanup** (leaving zero counts)
3. **Recalculating sum** instead of maintaining running total
4. **Using nested loops** for duplicate removal (making it O(n²))

## Edge Cases Handled

```python
# Single element
nums = [1] → Output: 1

# All unique elements  
nums = [1, 2, 3, 4] → Output: 10

# All same elements
nums = [5, 5, 5, 5] → Output: 5

# Alternating pattern
nums = [1, 2, 1, 2] → Output: 3 ([1,2] or [2,1])
```

## Related Problems

- **3. Longest Substring Without Repeating Characters**
- **209. Minimum Size Subarray Sum**
- **424. Longest Repeating Character Replacement**
- **76. Minimum Window Substring**

## Test Cases

```python
# Test the solution
solution = Solution()

# Example 1
print(solution.maximumUniqueSubarray([4,2,4,5,6]))  
# Expected: 17

# Example 2  
print(solution.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
# Expected: 8

# Example 3
print(solution.maximumUniqueSubarray([1]))
# Expected: 1

# Additional test cases
print(solution.maximumUniqueSubarray([1,2,3,4]))  # Expected: 10
print(solution.maximumUniqueSubarray([5,5,5,5]))  # Expected: 5
```

## Constraints

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

## Tags

- **Sliding Window**
- **Two Pointers**
- **Hash Table**
- **Array**

---

*This problem perfectly demonstrates the power of sliding window technique for subarray problems with constraints. The key insight is maintaining a valid window while tracking both sum and uniqueness efficiently.*