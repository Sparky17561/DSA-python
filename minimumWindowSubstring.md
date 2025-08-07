# 76. Minimum Window Substring

## Problem Description

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If no such substring exists, return an empty string.

**Difficulty**: Hard

## Examples

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters

**Follow-up**: Can you find an algorithm that runs in O(m + n) time?

## Solution: Sliding Window with Two Pointers

```python
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        # Track minimum window: (length, left_index, right_index)
        ans = float('inf'), None, None

        # Count characters needed from t
        count = defaultdict(int)
        for char in t:
            count[char] += 1

        left = 0
        formed = 0  # Number of unique characters in current window with desired frequency
        required = len(count)  # Number of unique characters in t
        window = defaultdict(int)

        for right in range(len(s)):
            # Expand window by including character from right
            window[s[right]] += 1
            
            # Check if current character's frequency matches required frequency
            if s[right] in count and window[s[right]] == count[s[right]]:
                formed += 1

            # Contract window from left while it's still valid
            while left <= right and formed == required:
                # Update minimum window if current is smaller
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right

                # Remove leftmost character from window
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    formed -= 1
                left += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

## Algorithm Explanation

### Step-by-Step Approach

1. **Initialize Data Structures**:
   - `count`: Frequency map of characters in `t`
   - `window`: Frequency map of characters in current window
   - `formed`: Count of unique characters in window with required frequency
   - `required`: Total unique characters needed from `t`

2. **Expand Window (Right Pointer)**:
   - Add characters to window until all requirements are satisfied
   - Track when a character reaches its required frequency

3. **Contract Window (Left Pointer)**:
   - Once valid window is found, try to minimize it
   - Remove characters from left while maintaining validity
   - Update minimum window when a smaller valid window is found

### Visual Walkthrough

For `s = "ADOBECODEBANC"`, `t = "ABC"`:

```
Step 1: Expand to find first valid window
A D O B E C O D E B A N C
^                       ^
left                  right
Window: "ADOBECODEBANC" (contains A, B, C)

Step 2: Contract from left
A D O B E C O D E B A N C
      ^               ^
    left            right  
Window: "OBECODEBA" (still valid, but larger)

Step 3: Continue contracting...
A D O B E C O D E B A N C
                  ^     ^
                left  right
Window: "BANC" (minimum valid window found!)
```

## Complexity Analysis

- **Time Complexity**: O(m + n)
  - Each character in `s` is visited at most twice (once by right, once by left pointer)
  - Building frequency map for `t` takes O(n)

- **Space Complexity**: O(m + n)
  - `count` hashmap stores at most n unique characters
  - `window` hashmap stores at most m unique characters

## Key Insights

1. **Two-Pointer Sliding Window**: Expand with right pointer, contract with left pointer
2. **Frequency Tracking**: Use hashmaps to track character frequencies
3. **Validity Check**: Window is valid when all characters from `t` are present with required frequencies
4. **Optimization**: Contract window immediately when valid to find minimum

## Edge Cases

```python
# Test cases
sol = Solution()

# Basic case
assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"

# Single characters
assert sol.minWindow("a", "a") == "a"

# No valid window
assert sol.minWindow("a", "aa") == ""

# Target longer than source
assert sol.minWindow("ab", "abc") == ""

# Entire string is minimum window
assert sol.minWindow("abc", "abc") == "abc"

# Repeated characters in target
assert sol.minWindow("AABBCC", "AAB") == "AAB"
```

## Common Pitfalls

1. **Off-by-one errors** in window size calculation
2. **Forgetting duplicates** - must handle repeated characters in `t`
3. **Incorrect validity check** - ensure all characters have sufficient frequency
4. **Edge case handling** - empty strings, impossible cases

## Follow-up Solution

The provided solution already achieves O(m + n) time complexity as requested in the follow-up, making it optimal for this problem.