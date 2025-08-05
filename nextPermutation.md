# Next Permutation Algorithm

## Problem Description

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be **in-place** and use only constant extra memory.

**Examples:**
- Input: `[1,2,3]` → Output: `[1,3,2]`
- Input: `[3,2,1]` → Output: `[1,2,3]` (wrap around to smallest)
- Input: `[1,1,5]` → Output: `[1,5,1]`

## Algorithm Approach

The algorithm follows a systematic approach to find the next lexicographically larger permutation:

### Step-by-Step Strategy

1. **Find the Pivot**: Scan from right to left to find the first element that is smaller than its next element
2. **Find the Successor**: From right to left, find the smallest element that is larger than the pivot
3. **Swap**: Swap the pivot with its successor
4. **Reverse**: Reverse the suffix after the pivot position to get the smallest arrangement
5. **Edge Case**: If no pivot exists (descending order), sort the entire array

### Why This Works

The key insight is understanding lexicographic ordering:
- We want the **smallest** increase possible
- The pivot is the rightmost position where we can make an increase
- After swapping, we need the smallest possible arrangement for the suffix

### Visual Example

For `[1, 2, 3, 6, 5, 4]`:

```
Step 1: Find pivot
[1, 2, 3, 6, 5, 4]
       ↑ pivot (3 < 6)

Step 2: Find successor  
[1, 2, 3, 6, 5, 4]
           ↑ successor (4 > 3, rightmost)

Step 3: Swap
[1, 2, 4, 6, 5, 3]

Step 4: Reverse suffix
[1, 2, 4, 3, 5, 6]
       ↑ reverse from here
```

## Complete Solution

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        Find the next lexicographically greater permutation in-place.
        
        Algorithm:
        1. Find pivot: rightmost element smaller than its next element
        2. Find successor: rightmost element greater than pivot
        3. Swap pivot and successor
        4. Reverse the suffix after pivot
        5. Handle edge case: if no pivot, sort entire array
        
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # Step 1: Find the pivot element
        # Scan from right to left to find first decreasing element
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # Step 2 & 3: Find successor and swap (only if pivot exists)
        if pivot != -1:
            # Find the rightmost element greater than pivot
            for j in range(len(nums) - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # Swap pivot with its successor
                    nums[j], nums[pivot] = nums[pivot], nums[j]
                    break
        
        # Step 4: Reverse the suffix after pivot
        # This gives us the lexicographically smallest arrangement
        left = pivot + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        # Step 5: Handle edge case
        # If no pivot found, array was in descending order
        # Sort to get the smallest permutation (ascending order)
        if pivot == -1:
            nums.sort()
```

## Detailed Examples

### Example 1: Normal Case
```
Input: [1, 2, 3]

Step 1: Find pivot
[1, 2, 3] → pivot = 1 (nums[1] = 2 < nums[2] = 3)

Step 2: Find successor
[1, 2, 3] → successor at index 2 (nums[2] = 3 > nums[1] = 2)

Step 3: Swap
[1, 3, 2]

Step 4: Reverse suffix (from index 2)
[1, 3, 2] → No change needed (single element)

Output: [1, 3, 2]
```

### Example 2: Wrap Around Case
```
Input: [3, 2, 1]

Step 1: Find pivot
[3, 2, 1] → No pivot found (descending order)

Step 5: Sort entire array
[1, 2, 3]

Output: [1, 2, 3]
```

### Example 3: Complex Case
```
Input: [1, 3, 5, 4, 2]

Step 1: Find pivot
[1, 3, 5, 4, 2] → pivot = 1 (nums[1] = 3 < nums[2] = 5)

Step 2: Find successor
[1, 3, 5, 4, 2] → successor at index 3 (nums[3] = 4 > nums[1] = 3)

Step 3: Swap
[1, 4, 5, 3, 2]

Step 4: Reverse suffix (from index 2)
[1, 4, 2, 3, 5]

Output: [1, 4, 2, 3, 5]
```

## Step-by-Step Trace

Let's trace through `nums = [1, 2, 3, 6, 5, 4]`:

| Step | Action | Array State | Notes |
|------|--------|------------|-------|
| 1 | Find pivot | `[1,2,3,6,5,4]` | pivot = 2 (nums[2]=3 < nums[3]=6) |
| 2 | Find successor | `[1,2,3,6,5,4]` | successor at index 5 (nums[5]=4 > nums[2]=3) |
| 3 | Swap | `[1,2,4,6,5,3]` | Swapped nums[2] and nums[5] |
| 4 | Reverse suffix | `[1,2,4,3,5,6]` | Reversed from index 3 to end |

**Final Result:** `[1, 2, 4, 3, 5, 6]`

## Complexity Analysis

### Time Complexity: O(n)
- **Finding pivot**: O(n) - single scan from right to left
- **Finding successor**: O(n) - single scan from right to left  
- **Swapping**: O(1) - constant time operation
- **Reversing suffix**: O(n) - at most n/2 swaps
- **Edge case sorting**: O(n log n) - but this happens only when array is in descending order

**Average Case**: O(n)  
**Worst Case**: O(n log n) (only for descending arrays)

### Space Complexity: O(1)
- Only uses a constant amount of extra space
- All operations are performed in-place
- No additional data structures required

## Edge Cases Handled

1. **Single element**: `[1]` → `[1]` (already largest)
2. **Two elements ascending**: `[1,2]` → `[2,1]`
3. **Two elements descending**: `[2,1]` → `[1,2]`  
4. **All same elements**: `[1,1,1]` → `[1,1,1]`
5. **Descending order**: `[3,2,1]` → `[1,2,3]`
6. **Already largest**: `[3,2,1]` → wraps to smallest `[1,2,3]`

## Key Insights

### Why Scan from Right to Left?
- We want the **rightmost** position where we can make a change
- This ensures we get the **next** permutation (smallest possible increase)

### Why Reverse the Suffix?
- After swapping, the suffix is in descending order
- We want the lexicographically smallest arrangement
- Reversing gives us ascending order (smallest possible)

### Why This is Optimal?
- Single pass algorithms for each step
- In-place modifications
- Handles all edge cases correctly
- Minimal number of swaps required

## Usage Example

```python
# Test the algorithm
solution = Solution()

test_cases = [
    [1, 2, 3],        # Expected: [1, 3, 2]
    [3, 2, 1],        # Expected: [1, 2, 3]  
    [1, 1, 5],        # Expected: [1, 5, 1]
    [1, 3, 5, 4, 2],  # Expected: [1, 4, 2, 3, 5]
    [1]               # Expected: [1]
]

for i, nums in enumerate(test_cases):
    original = nums.copy()
    solution.nextPermutation(nums)
    print(f"Test {i+1}: {original} → {nums}")
```

