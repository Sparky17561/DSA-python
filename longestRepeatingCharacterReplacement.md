# 424. Longest Repeating Character Replacement - Sliding Window Solution

**Difficulty**: Medium  
**Topics**: Hash Table, String, Sliding Window

## Problem Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Approach: Sliding Window with Character Frequency

This solution uses the **sliding window** technique combined with a frequency map to efficiently find the longest valid substring in O(n) time complexity.

### Key Insight

For any window to be valid, we need:
**`window_length - max_frequency_in_window ≤ k`**

This means the number of characters we need to change (non-most-frequent characters) should not exceed `k`.

### Key Concepts

1. **Sliding Window**: Use two pointers `i` (left) and `j` (right) to maintain a valid window
2. **Frequency Tracking**: Keep count of each character in the current window
3. **Max Frequency**: Track the most frequent character in the current window
4. **Dynamic Adjustment**: Shrink window when it becomes invalid

### Algorithm Steps

1. Initialize frequency map, result, and left pointer `i = 0`
2. For each right pointer `j` from 0 to n-1:
   - Add `s[j]` to frequency map
   - Find the maximum frequency in current window
   - Calculate current window length: `j - i + 1`
   - If `window_length - max_frequency > k`:
     - Remove `s[i]` from frequency map and increment `i`
   - Update result with current valid window length
3. Return the maximum length found

### Time Complexity: O(n)
- Each character is visited at most twice
- Finding max frequency is O(26) = O(1) for uppercase English letters

### Space Complexity: O(1)
- Frequency map stores at most 26 characters (constant space)

## Example Walkthrough

Let's trace through `s = "ABAB"` and `k = 2`:

```
Initial: freq={}, res=0, i=0

Step 1: j=0, s[0]='A'
  freq = {'A': 1}
  maxFreq = 1
  currLen = 0-0+1 = 1
  1 - 1 = 0 ≤ 2 ✓ (valid)
  res = max(0, 1) = 1

Step 2: j=1, s[1]='B'
  freq = {'A': 1, 'B': 1}
  maxFreq = 1
  currLen = 1-0+1 = 2
  2 - 1 = 1 ≤ 2 ✓ (valid)
  res = max(1, 2) = 2

Step 3: j=2, s[2]='A'
  freq = {'A': 2, 'B': 1}
  maxFreq = 2
  currLen = 2-0+1 = 3
  3 - 2 = 1 ≤ 2 ✓ (valid)
  res = max(2, 3) = 3

Step 4: j=3, s[3]='B'
  freq = {'A': 2, 'B': 2}
  maxFreq = 2
  currLen = 3-0+1 = 4
  4 - 2 = 2 ≤ 2 ✓ (valid)
  res = max(3, 4) = 4

Result: 4
```

The entire string "ABAB" can be made into "AAAA" or "BBBB" by changing 2 characters, so the answer is 4.

## Another Example

Let's trace through `s = "AABABBA"` and `k = 1`:

```
Initial: freq={}, res=0, i=0

j=0: 'A' → freq={'A':1}, maxFreq=1, len=1, 1-1=0≤1 ✓, res=1
j=1: 'A' → freq={'A':2}, maxFreq=2, len=2, 2-2=0≤1 ✓, res=2
j=2: 'B' → freq={'A':2,'B':1}, maxFreq=2, len=3, 3-2=1≤1 ✓, res=3
j=3: 'A' → freq={'A':3,'B':1}, maxFreq=3, len=4, 4-3=1≤1 ✓, res=4
j=4: 'B' → freq={'A':3,'B':2}, maxFreq=3, len=5, 5-3=2>1 ✗
  Invalid! Shrink window:
  freq={'A':2,'B':2} (remove s[0]='A'), i=1
  New len = 4-1+1 = 4, res=max(4,4)=4
j=5: 'B' → freq={'A':2,'B':3}, maxFreq=3, len=5, 5-3=2>1 ✗
  Invalid! Shrink window:
  freq={'A':1,'B':3} (remove s[1]='A'), i=2
  New len = 5-2+1 = 4, res=max(4,4)=4
j=6: 'A' → freq={'A':2,'B':3}, maxFreq=3, len=5, 5-3=2>1 ✗
  Invalid! Shrink window:
  freq={'A':2,'B':2} (remove s[2]='B'), i=3
  New len = 6-3+1 = 4, res=max(4,4)=4

Result: 4
```

The longest valid substring is "ABBA" (positions 3-6), which can be made into "AAAA" by changing 1 'B'.

## Edge Cases

- **k = 0**: Only contiguous identical characters count
- **k ≥ string length**: Can change entire string to one character, return string length
- **Single character**: Always return 1
- **All same characters**: Return string length

## Key Observations

1. **Window Validity**: A window is valid if `(characters to change) ≤ k`
2. **Greedy Approach**: Always try to keep the most frequent character unchanged
3. **No Need to Shrink Aggressively**: We only need to maintain window validity, not necessarily find the minimum valid window

## Complete Solution

```python
from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        res = 0
        i = 0

        for j in range(len(s)):
            freq[s[j]] += 1
            maxFreq = max(freq.values())
            currLen = j - i + 1
            if currLen - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
```

## Why This Approach Works

The sliding window technique is optimal because:

1. **Monotonic Property**: We're looking for the longest valid window
2. **Efficient Validation**: Check validity in O(1) time using frequency counts
3. **No Backtracking**: Once we expand, we only need to shrink when necessary
4. **Optimal Substructure**: Longer valid windows are built from shorter valid windows

This approach efficiently explores all possible substrings while maintaining the constraint that at most `k` characters need to be changed.