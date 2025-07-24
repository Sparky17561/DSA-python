# 560. Subarray Sum Equals K - Prefix Sum + HashMap Solution

**Difficulty**: Medium  
**Topics**: Array, Hash Table, Prefix Sum

## Problem Description

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`. A subarray is a contiguous non-empty sequence of elements within an array.

## Approach: Prefix Sum with HashMap

This solution uses **prefix sums** combined with a **hash map** to efficiently count subarrays with sum equal to `k` in O(n) time complexity.

### Key Insight

For any subarray from index `i` to `j` to have sum `k`:
**`prefix_sum[j] - prefix_sum[i-1] = k`**

Rearranging: **`prefix_sum[i-1] = prefix_sum[j] - k`**

So when we're at position `j` with prefix sum `curr_sum`, we need to check how many times `curr_sum - k` has appeared before.

### Key Concepts

1. **Prefix Sum**: Running sum from start of array to current position
2. **Hash Map**: Store frequency of each prefix sum encountered
3. **Mathematical Relationship**: Use `curr_sum - k` to find valid starting positions
4. **Count Accumulation**: Add frequency of `curr_sum - k` to result

### Algorithm Steps

1. Initialize `res = 0`, `curr_sum = 0`, and `prefix_sums = {0: 1}`
   - `{0: 1}` handles subarrays starting from index 0
2. For each number in the array:
   - Add number to `curr_sum` (calculate prefix sum)
   - Calculate `diff = curr_sum - k`
   - Add `prefix_sums.get(diff, 0)` to result (count of valid subarrays ending here)
   - Increment count of current prefix sum in hash map
3. Return total count

### Time Complexity: O(n)
- Single pass through the array
- Hash map operations are O(1) average case

### Space Complexity: O(n)
- Hash map can store up to n different prefix sums

## Example Walkthrough

Let's trace through `nums = [1, 1, 1]` and `k = 2`:

```
Initial: res=0, currSum=0, prefixSums={0:1}

Step 1: num=1
  currSum = 0 + 1 = 1
  diff = 1 - 2 = -1
  res += prefixSums.get(-1, 0) = 0 + 0 = 0
  prefixSums[1] = 1 + prefixSums.get(1, 0) = 1
  prefixSums = {0:1, 1:1}

Step 2: num=1  
  currSum = 1 + 1 = 2
  diff = 2 - 2 = 0
  res += prefixSums.get(0, 0) = 0 + 1 = 1  ← Found subarray [1,1]
  prefixSums[2] = 1 + prefixSums.get(2, 0) = 1
  prefixSums = {0:1, 1:1, 2:1}

Step 3: num=1
  currSum = 2 + 1 = 3
  diff = 3 - 2 = 1
  res += prefixSums.get(1, 0) = 1 + 1 = 2  ← Found subarray [1,1] at positions 1-2
  prefixSums[3] = 1 + prefixSums.get(3, 0) = 1
  prefixSums = {0:1, 1:1, 2:1, 3:1}

Result: 2
```

The two subarrays with sum 2 are: `[1,1]` (indices 0-1) and `[1,1]` (indices 1-2).

## Another Example

Let's trace through `nums = [1, 2, 3]` and `k = 3`:

```
Initial: res=0, currSum=0, prefixSums={0:1}

Step 1: num=1
  currSum = 1, diff = 1-3 = -2
  res += prefixSums.get(-2, 0) = 0
  prefixSums = {0:1, 1:1}

Step 2: num=2
  currSum = 3, diff = 3-3 = 0
  res += prefixSums.get(0, 0) = 0 + 1 = 1  ← Found [1,2]
  prefixSums = {0:1, 1:1, 3:1}

Step 3: num=3
  currSum = 6, diff = 6-3 = 3
  res += prefixSums.get(3, 0) = 1 + 1 = 2  ← Found [3]
  prefixSums = {0:1, 1:1, 3:1, 6:1}

Result: 2
```

The two subarrays with sum 3 are: `[1,2]` (indices 0-1) and `[3]` (index 2).

## Complex Example with Negative Numbers

Let's trace through `nums = [1, -1, 0]` and `k = 0`:

```
Initial: res=0, currSum=0, prefixSums={0:1}

Step 1: num=1
  currSum = 1, diff = 1-0 = 1
  res += prefixSums.get(1, 0) = 0
  prefixSums = {0:1, 1:1}

Step 2: num=-1
  currSum = 0, diff = 0-0 = 0
  res += prefixSums.get(0, 0) = 0 + 1 = 1  ← Found [1,-1]
  prefixSums[0] = 1 + prefixSums.get(0, 0) = 2
  prefixSums = {0:2, 1:1}

Step 3: num=0
  currSum = 0, diff = 0-0 = 0
  res += prefixSums.get(0, 0) = 1 + 2 = 3  ← Found [0] and [-1,0]
  prefixSums[0] = 1 + 2 = 3
  prefixSums = {0:3, 1:1}

Result: 3
```

The three subarrays with sum 0 are: `[1,-1]`, `[0]`, and `[-1,0]`.

## Why Hash Map is Essential

The hash map serves two critical purposes:

1. **Fast Lookup**: Check if `curr_sum - k` exists in O(1) time
2. **Count Tracking**: Handle multiple subarrays ending at different positions but having the same required prefix sum

## Edge Cases

- **k = 0**: Count subarrays with sum 0
- **All negatives**: Algorithm works with negative numbers
- **Single element equals k**: Hash map with `{0:1}` handles this
- **No valid subarrays**: Returns 0

## Complete Solution

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        currSum = 0
        prefixSums = {0: 1}
        
        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        
        return res
```

## Why This Approach Works

The prefix sum + hash map technique is optimal because:

1. **Mathematical Foundation**: Uses the property that subarray sum = prefix_sum[end] - prefix_sum[start-1]
2. **Efficient Counting**: Instead of checking all subarrays (O(n²)), we use past computations
3. **Handles Duplicates**: Hash map counts frequency, so multiple valid starting positions are handled correctly
4. **Works with Negatives**: Unlike sliding window, this approach handles negative numbers correctly

This solution efficiently transforms a quadratic problem into a linear one by leveraging the mathematical relationship between prefix sums and subarray sums.