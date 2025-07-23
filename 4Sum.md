# Four Sum Problem

## Problem Description

Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are distinct
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

The solution set must not contain duplicate quadruplets.

**Example:**
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

## Approach

This solution extends the **Two-Pointer Technique** from the Three Sum problem by adding an additional nested loop. It uses **sorting** combined with **two nested loops** and **two-pointer technique** to efficiently find all unique quadruplets that sum to the target.

### Algorithm Steps

1. **Sort the Array**: First, sort the input array in ascending order. This enables:
   - Use of two-pointer technique
   - Easy handling of duplicates
   - Optimization opportunities

2. **First Loop (i)**: Iterate through each element as the first element of a potential quadruplet.

3. **Skip Duplicates for First Element**: If the current element is the same as the previous one, skip it to avoid duplicate quadruplets.

4. **Second Loop (j)**: For each first element, iterate through the remaining elements as the second element of the quadruplet.

5. **Skip Duplicates for Second Element**: If the current second element is the same as the previous one (after the first element), skip it to avoid duplicates.

6. **Two-Pointer Search**: For the remaining part of the array (from `j+1` to end):
   - Set left pointer `l` at `j+1`
   - Set right pointer `r` at the last element
   - Calculate the sum of the quadruplet: `nums[i] + nums[j] + nums[l] + nums[r]`

7. **Adjust Pointers Based on Sum**:
   - If sum > target: Move right pointer left (decrease sum)
   - If sum < target: Move left pointer right (increase sum)
   - If sum == target: Found a valid quadruplet!

8. **Handle Duplicates for Valid Quadruplets**: When a valid quadruplet is found:
   - Move both pointers inward
   - Skip duplicate values for both left and right pointers to avoid duplicate results

### Why This Approach Works

- **Sorting**: Enables the two-pointer technique and makes duplicate handling straightforward
- **Nested Loops + Two-Pointer**: Systematically explores all possible combinations while maintaining efficiency
- **Duplicate Handling**: Prevents duplicate quadruplets by skipping identical values at all levels
- **Two-Pointer Optimization**: Reduces the innermost search from O(n²) to O(n)

## Complexity Analysis

- **Time Complexity**: O(n³)
  - Sorting: O(n log n)
  - First loop: O(n) iterations
  - Second loop: O(n) iterations for each first loop
  - Inner two-pointer loop: O(n) in worst case
  - Overall: O(n log n) + O(n³) = O(n³)

- **Space Complexity**: O(1) or O(n)
  - O(1) extra space if we don't count the output array
  - O(n) if we count the space used by sorting (depending on sorting algorithm)

## Key Differences from Three Sum

1. **Additional Loop**: One more nested loop to fix the second element
2. **Duplicate Handling**: Must handle duplicates for both the first and second fixed elements
3. **Two-Pointer Movement**: When a valid quadruplet is found, both pointers move and both need duplicate checking
4. **Complexity**: Time complexity increases from O(n²) to O(n³)

## Edge Cases Handled

1. **Array with less than 4 elements**: Returns empty list
2. **No valid quadruplets exist**: Returns empty list
3. **Duplicate elements**: Properly handled to avoid duplicate quadruplets
4. **Target can be any integer**: Positive, negative, or zero
5. **All same elements**: Correctly handles cases like [2,2,2,2] with target 8

## Example Walkthrough

For `nums = [1,0,-1,0,-2,2]`, `target = 0`:

1. **After sorting**: `[-2,-1,0,0,1,2]`

2. **i=0, nums[i]=-2**:
   - **j=1, nums[j]=-1**: Two pointers l=2(0), r=5(2)
     - Sum: -2 + (-1) + 0 + 2 = -1 < 0, move l right
     - l=3(0), r=5(2): Sum = -1 < 0, move l right
     - l=4(1), r=5(2): Sum = 0 ✓ → Add [-2,-1,1,2]
   
   - **j=2, nums[j]=0**: Two pointers l=3(0), r=5(2)
     - Sum: -2 + 0 + 0 + 2 = 0 ✓ → Add [-2,0,0,2]

3. **i=1, nums[i]=-1**:
   - **j=2, nums[j]=0**: Two pointers l=3(0), r=5(2)
     - Sum: -1 + 0 + 0 + 2 = 1 > 0, move r left
     - l=3(0), r=4(1): Sum = 0 ✓ → Add [-1,0,0,1]

4. **Continue for remaining elements...**

**Final Result**: `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

## Optimizations

The algorithm can be further optimized with early termination conditions:

1. **Early Break**: If `nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target`, break (smallest possible sum is too large)
2. **Early Continue**: If `nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target`, continue (largest possible sum is too small)
3. **Similar optimizations can be applied for the second loop**

## Usage

```python
solution = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = solution.fourSum(nums, target)
print(result)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

## Complete Code

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        Find all unique quadruplets in the array that sum to the target.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []  # Store all valid quadruplets
        nums.sort()  # Sort array to enable two-pointer technique and handle duplicates
        
        # First loop: iterate through each element as the first element of potential quadruplet
        for i in range(len(nums)):
            # Skip duplicate values for the first element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Second loop: iterate through each element as the second element of potential quadruplet
            for j in range(i + 1, len(nums)):
                # Skip duplicate values for the second element to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Use two-pointer technique for the remaining two elements
                l, r = j + 1, len(nums) - 1  # Left pointer starts after j, right at end
                
                while l < r:
                    # Calculate sum of current quadruplet
                    foursum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if foursum > target:
                        # Sum too large, move right pointer left to decrease sum
                        r -= 1
                    elif foursum < target:
                        # Sum too small, move left pointer right to increase sum
                        l += 1
                    else:
                        # Found a valid quadruplet that equals target
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        # Skip duplicate values for left pointer to avoid duplicate quadruplets
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        
                        # Skip duplicate values for right pointer to avoid duplicate quadruplets  
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        
        return res


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    result1 = solution.fourSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    result2 = solution.fourSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    nums3 = [1, 0, -1, 0, -2, 2]
    target3 = 2
    result3 = solution.fourSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
```