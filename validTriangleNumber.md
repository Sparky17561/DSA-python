# Triangle Number

## Problem Description

Given an integer array `nums`, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

## Triangle Formation Rule

For three sides `a`, `b`, `c` to form a valid triangle, they must satisfy the triangle inequality theorem:
- `a + b > c`
- `a + c > b` 
- `b + c > a`

However, if we sort the sides such that `a ≤ b ≤ c`, we only need to check: **`a + b > c`**

This is because:
- `a + c > b` is automatically satisfied (since `c ≥ b`)
- `b + c > a` is automatically satisfied (since `b ≥ a` and `c > 0`)

## Algorithm Approach

### Intuition
1. Sort the array to arrange elements in ascending order
2. Fix the largest side (rightmost element) and use two pointers to find valid pairs for the two smaller sides
3. For each valid pair, count all possible combinations

### Steps
1. **Sort the array** - This ensures the largest element is always at the end
2. **Fix the largest side** - Iterate from the last element to the first (`i` from `n-1` to `0`)
3. **Two-pointer technique**:
   - `left = 0` (smallest available element)
   - `right = i-1` (second largest available element)
   - If `nums[left] + nums[right] > nums[i]`:
     - All pairs from `left` to `right-1` with `nums[right]` are valid
     - Add `(right - left)` to count
     - Move `right--` to try smaller second element
   - Otherwise, move `left++` to try larger first element

### Example Walkthrough
```
nums = [2,2,3,4]
After sorting: [2,2,3,4]

i=3 (nums[i]=4): left=0, right=2
- nums[0] + nums[2] = 2 + 3 = 5 > 4 ✓
- Valid pairs: (0,2), (1,2) → count += 2-0 = 2
- right = 1: nums[0] + nums[1] = 2 + 2 = 4 > 4 ✗
- left = 1: left >= right, exit

i=2 (nums[i]=3): left=0, right=1  
- nums[0] + nums[1] = 2 + 2 = 4 > 3 ✓
- Valid pairs: (0,1) → count += 1-0 = 1
- Total count = 2 + 1 = 3
```

## Implementation

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
```

## Complexity Analysis

- **Time Complexity**: `O(n²)`
  - Sorting: `O(n log n)`
  - Two nested loops: `O(n²)` 
  - Overall: `O(n²)`

- **Space Complexity**: `O(1)`
  - Only using constant extra space for pointers and counters
  - Sorting is done in-place

## Key Insights

1. **Sorting optimization**: By sorting first, we only need to check one triangle inequality condition
2. **Two-pointer efficiency**: Instead of checking all pairs individually, we can count multiple valid combinations at once
3. **Mathematical property**: When `nums[left] + nums[right] > nums[i]`, all elements between `left` and `right-1` paired with `nums[right]` will also satisfy the condition

## Edge Cases

- Array with less than 3 elements → return 0
- Array with all zeros → return 0  
- Array with identical elements → count all possible combinations
- Array with one very large element → may result in fewer valid triangles