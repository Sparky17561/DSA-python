# Three Sum Problem

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

**Example:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

## Approach

This solution uses a **Two-Pointer Technique** combined with **sorting** to efficiently find all unique triplets that sum to zero.

### Algorithm Steps

1. **Sort the Array**: First, sort the input array in ascending order. This enables:
   - Use of two-pointer technique
   - Easy handling of duplicates
   - Optimization opportunities

2. **Iterate Through First Element**: For each element at index `i`, treat it as the first element of a potential triplet.

3. **Skip Duplicates for First Element**: If the current element is the same as the previous one, skip it to avoid duplicate triplets.

4. **Two-Pointer Search**: For the remaining part of the array (from `i+1` to end):
   - Set left pointer `l` at `i+1`
   - Set right pointer `r` at the last element
   - Calculate the sum of the triplet: `nums[i] + nums[l] + nums[r]`

5. **Adjust Pointers Based on Sum**:
   - If sum > 0: Move right pointer left (decrease sum)
   - If sum < 0: Move left pointer right (increase sum)
   - If sum == 0: Found a valid triplet!

6. **Handle Duplicates for Valid Triplets**: When a valid triplet is found, skip duplicate values for the left pointer to avoid duplicate results.

### Why This Approach Works

- **Sorting**: Enables the two-pointer technique and makes duplicate handling straightforward
- **Two-Pointer Technique**: Reduces time complexity from O(n²) to O(n) for finding pairs that sum to a target
- **Duplicate Handling**: Prevents duplicate triplets by skipping identical values
- **Early Termination**: If the first element is positive, we can break early since all remaining sums will be positive

## Complexity Analysis

- **Time Complexity**: O(n²)
  - Sorting: O(n log n)
  - Main loop: O(n) iterations
  - Inner two-pointer loop: O(n) in worst case
  - Overall: O(n log n) + O(n²) = O(n²)

- **Space Complexity**: O(1) or O(n)
  - O(1) extra space if we don't count the output array
  - O(n) if we count the space used by sorting (depending on sorting algorithm)

## Edge Cases Handled

1. **Empty array or array with less than 3 elements**: Returns empty list
2. **All positive or all negative numbers**: No valid triplets possible
3. **Duplicate elements**: Properly handled to avoid duplicate triplets
4. **Array with zeros**: Correctly identifies [0,0,0] if present

## Example Walkthrough

For `nums = [-1,0,1,2,-1,-4]`:

1. **After sorting**: `[-4,-1,-1,0,1,2]`

2. **i=0, a=-4**: 
   - Two pointers: l=1(-1), r=5(2)
   - Sum: -4 + (-1) + 2 = -3 < 0, move l right
   - Continue until l >= r, no valid triplets found

3. **i=1, a=-1**:
   - Two pointers: l=2(-1), r=5(2)
   - Sum: -1 + (-1) + 2 = 0 ✓ → Add [-1,-1,2]
   - Move l right, skip duplicate
   - l=3(0), r=5(2): Sum = 1 > 0, move r left
   - l=3(0), r=4(1): Sum = 0 ✓ → Add [-1,0,1]

4. **i=2, a=-1**: Skip (duplicate of previous)

5. **Continue for remaining elements...**

**Final Result**: `[[-1,-1,2], [-1,0,1]]`

## Usage

```python
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

## Complete Code

```python
class Solution(object):
    def threeSum(self, nums):
        """
        Find all unique triplets in the array that sum to zero.
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []  # Store all valid triplets
        nums.sort()  # Sort array to enable two-pointer technique and handle duplicates
        
        # Iterate through each element as the first element of potential triplet
        for i, a in enumerate(nums):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if a == nums[i-1] and i > 0:
                continue
            
            # Use two-pointer technique for remaining elements
            l, r = i + 1, len(nums) - 1  # Left pointer starts after current element, right at end
            
            while l < r:
                threesum = a + nums[l] + nums[r]  # Calculate sum of current triplet
                
                if threesum > 0:
                    # Sum too large, move right pointer left to decrease sum
                    r -= 1
                elif threesum < 0:
                    # Sum too small, move left pointer right to increase sum
                    l += 1
                else:
                    # Found a valid triplet that sums to zero
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    
                    # Skip duplicate values for left pointer to avoid duplicate triplets
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
```