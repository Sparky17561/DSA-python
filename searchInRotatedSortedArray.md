# Search in Rotated Sorted Array

## Problem Overview
This algorithm searches for a target value in a rotated sorted array in O(log n) time complexity using a modified binary search approach.

## Intuition Behind the Algorithm

### The Key Insight: One Half is Always Sorted
When we have a rotated sorted array like `[4,5,6,7,0,1,2]`, at any point when we split the array in half, **one half will always be properly sorted**. This is the crucial observation that makes binary search possible.

### Why This Works
1. **Original sorted array**: `[0,1,2,4,5,6,7]`
2. **After rotation**: `[4,5,6,7,0,1,2]` 
3. **When we pick middle element**: We can determine which half is sorted by comparing `nums[mid]` with `nums[left]`

### The Two Cases
- **Left half is sorted**: `nums[mid] >= nums[left]`
  - Elements from `left` to `mid` are in ascending order
- **Right half is sorted**: `nums[mid] < nums[left]`  
  - Elements from `mid` to `right` are in ascending order

### Decision Making
Once we identify the sorted half, we check if our target lies within that sorted range:
- **If target is in the sorted half**: Search there (eliminate the other half)
- **If target is not in the sorted half**: It must be in the other half

## Code with Detailed Comments

```python
class Solution(object):
    def search(self, nums, target):
        """
        Search for target in rotated sorted array using modified binary search
        :type nums: List[int] - rotated sorted array
        :type target: int - value to search for
        :rtype: int - index of target, or -1 if not found
        """
        # Initialize two pointers for binary search
        l = 0              # left pointer
        r = len(nums) - 1  # right pointer
        
        # Continue search while search space is valid
        while l <= r:
            # Calculate middle index (avoid overflow)
            m = (l + r) // 2
            
            # Found the target!
            if nums[m] == target:
                return m
            
            # Determine which half is sorted by comparing mid with left
            elif nums[m] >= nums[l]:  # Left half is sorted
                """
                Left half: nums[l] to nums[m] is in ascending order
                Check if target lies within this sorted range
                """
                if nums[l] <= target <= nums[m]:
                    # Target is in the sorted left half
                    r = m - 1  # Search left half, exclude mid
                else:
                    # Target must be in right half
                    l = m + 1  # Search right half, exclude mid
                    
            else:  # Right half is sorted (nums[m] < nums[l])
                """
                Right half: nums[m] to nums[r] is in ascending order
                Check if target lies within this sorted range
                """
                if nums[m] <= target <= nums[r]:
                    # Target is in the sorted right half  
                    l = m + 1  # Search right half, exclude mid
                else:
                    # Target must be in left half
                    r = m - 1  # Search left half, exclude mid
        
        # Target not found in the array
        return -1
```

## Step-by-Step Test Case Walkthrough

**Input**: `nums = [4,5,6,7,0,1,2]`, `target = 0`

### Iteration 1:
```
Array: [4, 5, 6, 7, 0, 1, 2]
       l=0     m=3     r=6
```
- `nums[m] = 7`, `target = 0`
- `nums[m] = 7 >= nums[l] = 4` → Left half `[4,5,6,7]` is sorted
- Is `4 ≤ 0 ≤ 7`? **No** → Target not in sorted left half
- Move to right half: `l = m + 1 = 4`

### Iteration 2:
```
Array: [4, 5, 6, 7, 0, 1, 2]
                   l=4 m=5 r=6
```
- `nums[m] = 1`, `target = 0`
- `nums[m] = 1 < nums[l] = 0`? **No** → `1 ≥ 0`, so left half is sorted
- Wait, this seems wrong. Let me recalculate: `nums[l] = nums[4] = 0`
- `nums[m] = 1 >= nums[l] = 0` → Left half `[0,1]` is sorted
- Is `0 ≤ 0 ≤ 1`? **Yes** → Target is in sorted left half
- Move to left half: `r = m - 1 = 4`

### Iteration 3:
```
Array: [4, 5, 6, 7, 0, 1, 2]
                   l=4,r=4,m=4
```
- `nums[m] = nums[4] = 0`
- `nums[m] = 0 == target = 0` → **Found!**
- Return index `4`

## Time and Space Complexity
- **Time Complexity**: O(log n) - Binary search eliminates half the search space each iteration
- **Space Complexity**: O(1) - Only using a constant amount of extra space

## Key Takeaways
1. **Always identify the sorted half** using `nums[mid] >= nums[left]`
2. **Check if target is in the sorted range** before deciding which direction to search
3. **The rotation point doesn't matter** - we just need to find which half is sorted
4. **Classic binary search logic** applies once we determine the correct half to search