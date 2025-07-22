# LeetCode 338: Counting Bits

## Problem Statement

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the **number of 1's** in the binary representation of `i`.

### Examples

**Example 1:**
```
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0 (binary) --> 0 ones
1 --> 1 (binary) --> 1 one
2 --> 10 (binary) --> 1 one
```

**Example 2:**
```
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0 (binary) --> 0 ones
1 --> 1 (binary) --> 1 one
2 --> 10 (binary) --> 1 one
3 --> 11 (binary) --> 2 ones
4 --> 100 (binary) --> 1 one
5 --> 101 (binary) --> 2 ones
```

## Solution Approach

### Method 1: Brute Force (Built-in Functions)
**Time Complexity: O(n log n) | Space Complexity: O(1)**

```python
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n + 1):
            bin_no = bin(i)  # Convert to binary string
            # bin_no = format(i, 'b')  # Alternative way
            ones_count = bin_no.count('1')  # Count '1's in string
            res.append(ones_count)
        return res
```

#### How It Works:

1. **Iterate through range [0, n]:** For each number `i` from 0 to n
2. **Convert to binary:** Use `bin(i)` to get binary representation as string
3. **Count ones:** Use `.count('1')` to count occurrences of '1' character
4. **Store result:** Append the count to result array

#### Alternative Binary Conversion:
```python
# Instead of bin(i), you can use:
bin_no = format(i, 'b')  # Returns binary string without '0b' prefix
```

#### Step-by-Step Example (n = 5):
```
i = 0: bin(0) = '0b0'    → count('1') = 0
i = 1: bin(1) = '0b1'    → count('1') = 1  
i = 2: bin(2) = '0b10'   → count('1') = 1
i = 3: bin(3) = '0b11'   → count('1') = 2
i = 4: bin(4) = '0b100'  → count('1') = 1
i = 5: bin(5) = '0b101'  → count('1') = 2

Result: [0, 1, 1, 2, 1, 2]
```

### Method 2: Bit Manipulation (Manual Counting)
**Time Complexity: O(n log n) | Space Complexity: O(1)**

```python
class Solution(object):
    def countBits(self, n):
        res = []
        for i in range(n + 1):
            count = 0
            num = i
            while num:
                count += num & 1  # Check if last bit is 1
                num >>= 1         # Right shift by 1
            res.append(count)
        return res
```

### Method 3: Dynamic Programming (Optimal)
**Time Complexity: O(n) | Space Complexity: O(1)**

```python
class Solution(object):
    def countBits(self, n):
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            # Key insight: res[i] = res[i >> 1] + (i & 1)
            res[i] = res[i // 2] + (i % 2)
        return res
```

#### DP Approach Explanation:
- **Pattern Recognition:** `countBits(i) = countBits(i // 2) + (i % 2)`
- **Logic:** Removing the last bit (i >> 1) and adding 1 if last bit was 1
- **Example:** For i = 5 (binary: 101)
  - `res[5] = res[2] + 1 = 1 + 1 = 2`
  - Because 5 >> 1 = 2, and 5 & 1 = 1

## Complexity Analysis

| Method | Time Complexity | Space Complexity | Notes |
|--------|----------------|------------------|-------|
| Built-in Functions | O(n log n) | O(1) | Simple but slower |
| Bit Manipulation | O(n log n) | O(1) | Manual bit counting |
| Dynamic Programming | O(n) | O(1) | Optimal solution |

## Key Concepts

### Binary Representation
- `bin(n)` returns string like `'0b101'` for n = 5
- `format(n, 'b')` returns string like `'101'` for n = 5
- Both represent the same binary number

### Bit Operations Used in Optimal Solution
- `i >> 1` or `i // 2`: Remove rightmost bit
- `i & 1` or `i % 2`: Check if rightmost bit is 1

### Pattern Recognition
```
Number | Binary | Count | Relationship
-------|--------|-------|-------------
0      | 0      | 0     | Base case
1      | 1      | 1     | res[0] + 1
2      | 10     | 1     | res[1] + 0  
3      | 11     | 2     | res[1] + 1
4      | 100    | 1     | res[2] + 0
5      | 101    | 2     | res[2] + 1
```

## Follow-up Questions

1. **Can you solve it in O(n) time?** ✅ Yes, using DP approach
2. **Can you solve it without using built-in functions?** ✅ Yes, using bit manipulation
3. **Can you solve it using only O(1) extra space?** ✅ Yes, output array doesn't count as extra space

## Alternative Solutions

### Using Brian Kernighan's Algorithm
```python
def countBits(self, n):
    res = []
    for i in range(n + 1):
        count = 0
        num = i
        while num:
            num &= num - 1  # Remove rightmost set bit
            count += 1
        res.append(count)
    return res
```

### Using Offset Pattern
```python
def countBits(self, n):
    res = [0] * (n + 1)
    offset = 1
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        res[i] = 1 + res[i - offset]
    return res
```

## Test Cases

```python
# Test the solution
solution = Solution()

print(solution.countBits(2))  # Expected: [0, 1, 1]
print(solution.countBits(5))  # Expected: [0, 1, 1, 2, 1, 2]
print(solution.countBits(0))  # Expected: [0]
print(solution.countBits(1))  # Expected: [0, 1]
```

## Constraints

- `0 <= n <= 10^5`

## Tags

- **Bit Manipulation**
- **Dynamic Programming** 
- **Array**

---

*This problem is excellent for understanding bit manipulation and recognizing patterns in binary representations.*