# Search in Rotated Sorted Array II (With Duplicates)

## Problem Overview
This algorithm searches for a target value in a rotated sorted array **that may contain duplicates**. It returns `True` if the target exists, `False` otherwise. This is an enhanced version of the classic "Search in Rotated Sorted Array" problem.

## Key Differences from Search in Rotated Sorted Array I

### What's New in This Version?
1. **Array can contain duplicates**: `[2,5,6,0,0,1,2]` instead of `[4,5,6,7,0,1,2]`
2. **Return type changed**: Returns `boolean` instead of `int` (index)
3. **Additional edge case handling**: When `nums[left] == nums[mid]`, we can't determine which half is sorted

### The Duplicate Problem
In the original problem, we could always determine which half was sorted by comparing `nums[mid]` with `nums[left]`. But with duplicates:

```
Array: [1, 0, 1, 1, 1]
        l     m     r
```
Here, `nums[left] = nums[mid] = 1`, so we can't tell if the left half `[1,0,1]` or right half `[1,1]` is properly sorted!

### Solution: Linear Scan When Ambiguous
When `nums[left] == nums[mid]`, we increment `left` by 1 and continue. This removes the ambiguity at the cost of potentially degrading to O(n) in worst case.

## Intuition Behind the Algorithm

### The Core Logic Remains the Same
1. **One half is always sorted** (when we can determine it)
2. **Check if target is in the sorted range**
3. **Eliminate the half that doesn't contain the target**

### The New Challenge: Handling Ambiguity
When duplicates make it unclear which half is sorted, we use a simple but effective strategy:
- **Skip the ambiguous element** by incrementing `left`
- **Continue the search** with a clearer view

## Code with Detailed Comments

```python
class Solution(object):
    def search(self, nums, target):
        """
        Search for target in rotated sorted array with duplicates
        :type nums: List[int] - rotated sorted array (may contain duplicates)
        :type target: int - value to search for
        :rtype: bool - True if target exists, False otherwise
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # Found the target!
            if nums[mid] == target:
                return True
            
            # NEW: Handle the duplicate ambiguity case
            elif nums[left] == nums[mid]:
                """
                When nums[left] == nums[mid], we cannot determine which half is sorted
                Example: [1, 0, 1, 1, 1] where left=0, mid=2
                         nums[0] = nums[2] = 1, but left half [1,0,1] is not sorted
                         
                Solution: Skip the leftmost element to remove ambiguity
                This is safe because:
                1. If nums[left] was our target, nums[mid] would also be target (already checked above)
                2. We're just removing one duplicate occurrence
                """
                left += 1
                continue  # Skip to next iteration
                
            # Left half is sorted: nums[left] < nums[mid] 
            elif nums[left] < nums[mid]:
                """
                Left half: nums[left] to nums[mid] is in ascending order
                Check if target lies within this sorted range
                """
                if nums[left] <= target <= nums[mid]:
                    # Target is in the sorted left half
                    right = mid - 1  # Search left half, exclude mid
                else:
                    # Target must be in right half
                    left = mid + 1   # Search right half, exclude mid
                    
            # Right half is sorted: nums[left] > nums[mid]
            else:
                """
                Right half: nums[mid] to nums[right] is in ascending order
                Check if target lies within this sorted range
                """
                if nums[mid] <= target <= nums[right]:
                    # Target is in the sorted right half
                    left = mid + 1   # Search right half, exclude mid
                else:
                    # Target must be in left half
                    right = mid - 1  # Search left half, exclude mid
        
        # Target not found in the array
        return False
```

## Step-by-Step Test Case Walkthrough

**Input**: `nums = [2,5,6,0,0,1,2]`, `target = 0`

### Iteration 1:
```
Array: [2, 5, 6, 0, 0, 1, 2]
        l=0   m=3      r=6
```
- `nums[mid] = 0`, `target = 0`
- `nums[mid] == target` → **Found!**
- Return `True`

Let's try a more complex example: `nums = [2,5,6,0,0,1,2]`, `target = 3`

### Iteration 1:
```
Array: [2, 5, 6, 0, 0, 1, 2]
        l=0   m=3      r=6
```
- `nums[mid] = 0`, `target = 3`
- `nums[left] = 2 > nums[mid] = 0` → Right half is sorted
- Is `0 ≤ 3 ≤ 2`? **No** → Target not in sorted right half
- Move to left half: `right = mid - 1 = 2`

### Iteration 2:
```
Array: [2, 5, 6, 0, 0, 1, 2]
        l=0 m=1 r=2
```
- `nums[mid] = 5`, `target = 3`
- `nums[left] = 2 < nums[mid] = 5` → Left half is sorted
- Is `2 ≤ 3 ≤ 5`? **Yes** → Target should be in sorted left half
- Move to left half: `right = mid - 1 = 0`

### Iteration 3:
```
Array: [2, 5, 6, 0, 0, 1, 2]
        l=0,r=0,m=0
```
- `nums[mid] = 2`, `target = 3`
- `nums[mid] ≠ target` and `left > right` will be true after this
- Return `False`

## Example with Duplicate Handling

**Input**: `nums = [1,0,1,1,1]`, `target = 0`

### Iteration 1:
```
Array: [1, 0, 1, 1, 1]
        l=0   m=2   r=4
```
- `nums[mid] = 1`, `target = 0`
- `nums[left] = 1 == nums[mid] = 1` → **Ambiguous case!**
- Increment `left = 1` and continue

### Iteration 2:
```
Array: [1, 0, 1, 1, 1]
           l=1 m=2 r=4
```
- `nums[mid] = 1`, `target = 0`
- `nums[left] = 0 < nums[mid] = 1` → Left half is sorted
- Is `0 ≤ 0 ≤ 1`? **Yes** → Target is in sorted left half
- Move to left half: `right = mid - 1 = 1`

### Iteration 3:
```
Array: [1, 0, 1, 1, 1]
           l=1,r=1,m=1
```
- `nums[mid] = 0`, `target = 0`
- `nums[mid] == target` → **Found!**
- Return `True`

## Additions Made to Handle Duplicates

### 1. **New Condition: `nums[left] == nums[mid]`**
```python
elif nums[left] == nums[mid]:
    left += 1
    continue
```
This handles the ambiguity when we can't determine which half is sorted.

### 2. **Return Type Change**
- **Original**: Returns index (`int`) or -1 if not found
- **With Duplicates**: Returns boolean (`True`/`False`)

### 3. **Degraded Time Complexity in Worst Case**
- **Best/Average Case**: O(log n) - when duplicates don't cause much ambiguity
- **Worst Case**: O(n) - when array is mostly duplicates like `[1,1,1,1,0,1]`

### 4. **Same Space Complexity**
- **Space**: O(1) - still constant extra space

## When Does Performance Degrade?

**Worst case scenario**: `nums = [1,1,1,1,1,0,1,1,1]`, `target = 0`
- Many `nums[left] == nums[mid]` situations
- Algorithm degrades to linear scan: O(n)

**Best case scenario**: `nums = [4,5,6,7,0,1,2]` (no duplicates)
- Behaves exactly like the original algorithm: O(log n)

## Key Takeaways

1. **Handle ambiguity first**: Check `nums[left] == nums[mid]` before determining sorted half
2. **Skip duplicates safely**: Incrementing `left` removes ambiguity without missing the target
3. **Trade-off**: Handling duplicates can degrade performance to O(n) in worst case
4. **Same core logic**: Once ambiguity is resolved, use the same sorted-half strategy
5. **Boolean return**: Focus on existence rather than position