# 🔄 Permutation in String - LeetCode 567

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](https://leetcode.com/problems/permutation-in-string/)
[![Topics](https://img.shields.io/badge/Topics-Hash%20Table%20%7C%20Two%20Pointers%20%7C%20String%20%7C%20Sliding%20Window-blue.svg)]()
[![Python](https://img.shields.io/badge/Language-Python-3776ab.svg)](https://www.python.org/)

## 🎯 Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Examples

**Example 1:**
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**
```
Input: s1 = "ab", s2 = "eidboaoo"  
Output: false
```

---

## 💡 Approach & Algorithm

### Core Insight
Instead of generating all permutations of `s1` (which would be O(n!)), we use the key observation that **two strings are permutations of each other if and only if they have the same character frequency**.

### Sliding Window + Hash Map Strategy

1. **Fixed-size sliding window**: Use a window of size `len(s1)` that slides across `s2`
2. **Character frequency matching**: Compare frequency maps instead of actual permutations
3. **Efficient window updates**: Add new character, remove old character as window slides

### Algorithm Steps

1. **Early termination**: If `s1` is longer than `s2`, no permutation can exist
2. **Initialize frequency maps**: Create hash maps for both strings
3. **Initial window setup**: Count frequencies for first `len(s1)` characters of `s2`
4. **Check initial window**: If frequencies match, we found a permutation
5. **Slide the window**: For each remaining position:
   - Add the new character (right side)
   - Remove the old character (left side)
   - Compare frequency maps
6. **Clean up**: Remove zero-count entries to ensure accurate comparison

---

## 🔧 Complete Solution

```python
from collections import defaultdict

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Early termination: if s1 is longer than s2, no permutation possible
        if len(s1) > len(s2):
            return False
            
        # Create frequency maps for both strings
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        # Initialize the frequency maps for the first window
        for i in range(len(s1)):
            s1_count[s1[i]] += 1     # Count characters in s1
            s2_count[s2[i]] += 1     # Count first len(s1) characters in s2

        # Check if the initial window is a permutation
        if s1_count == s2_count:
            return True

        # Slide the window across the rest of s2
        left = 0
        for right in range(len(s1), len(s2)):
            # Add new character to the window (expand right)
            s2_count[s2[right]] += 1
            
            # Remove old character from the window (shrink left)
            s2_count[s2[left]] -= 1
            
            # Clean up: remove zero-count entries for accurate comparison
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
                
            # Move left pointer
            left += 1
            
            # Check if current window contains a permutation
            if s1_count == s2_count:
                return True

        return False
```

---

## 📊 Example Walkthrough

### Example 1: `s1 = "ab"`, `s2 = "eidbaooo"`

**Step-by-step execution:**

1. **Initialize frequency maps:**
   ```
   s1_count = {'a': 1, 'b': 1}
   s2_count = {'e': 1, 'i': 1}  # First 2 chars of s2
   ```

2. **Slide the window:**
   ```
   Window "ei" → s2_count = {'e': 1, 'i': 1} ≠ s1_count
   
   Window "id" → s2_count = {'i': 1, 'd': 1} ≠ s1_count
   
   Window "db" → s2_count = {'d': 1, 'b': 1} ≠ s1_count
   
   Window "ba" → s2_count = {'b': 1, 'a': 1} = s1_count ✅
   ```

3. **Result:** `True` - Found permutation "ba"

### Example 2: `s1 = "ab"`, `s2 = "eidboaoo"`

**Visual sliding process:**
```
s2 = "eidboaoo"
      ^^        Window "ei" 
       ^^       Window "id"
        ^^      Window "db" 
         ^^     Window "bo"
          ^^    Window "oa"
           ^^   Window "ao"
            ^^  Window "oo"
```

None of these windows have the same character frequency as `s1 = "ab"`, so return `False`.

---

## 🎨 Visual Representation

```
s1 = "ab" → frequency: {a:1, b:1}

s2 = "eidbaooo"
     [ei]        {e:1, i:1} ≠ {a:1, b:1}
      [id]       {i:1, d:1} ≠ {a:1, b:1}  
       [db]      {d:1, b:1} ≠ {a:1, b:1}
        [ba]     {b:1, a:1} = {a:1, b:1} ✅ MATCH!
```

---

## ⚡ Complexity Analysis

- **Time Complexity:** O(|s1| + |s2|)
  - O(|s1|) to build initial frequency map
  - O(|s2| - |s1|) to slide the window
  - Each hash map operation is O(1) on average
  
- **Space Complexity:** O(|s1|)
  - Hash maps store at most |s1| unique characters
  - In worst case, all characters in s1 are unique

---

## 🧠 Key Insights & Optimizations

### Why This Approach Works
1. **Permutation property**: Two strings are permutations ⟺ same character frequencies
2. **Sliding window efficiency**: Instead of checking every substring, maintain a moving window
3. **Hash map comparison**: Direct dictionary comparison in Python is efficient

### Important Implementation Details
1. **Zero cleanup**: Removing zero-count entries ensures accurate hash map comparison
2. **Early termination**: Quick check for impossible cases
3. **defaultdict usage**: Automatically handles missing keys

### Alternative Approaches
- **Array-based counting**: Use fixed-size arrays for lowercase letters only
- **Character difference tracking**: Maintain a single counter of differences
- **Rolling hash**: More complex but can be faster for very long strings

---

## 🎯 Pattern Recognition

This problem demonstrates the classic **Sliding Window** pattern combined with **Hash Map frequency counting**:

```
🔄 Sliding Window Pattern:
├── Fixed window size (len(s1))
├── Efficient add/remove operations  
└── Continuous comparison at each step

📊 Frequency Counting Pattern:
├── Character frequency as permutation identifier
├── Hash map for O(1) updates
└── Dictionary comparison for matching
```

---

## 🚀 Extensions & Variations

- **Find all permutation indices**: Return all starting positions where permutations occur
- **Multiple string permutations**: Check if s2 contains permutations of multiple strings
- **Case-sensitive variations**: Handle uppercase/lowercase considerations
- **Unicode support**: Extend beyond ASCII characters

This elegant solution showcases how the right data structure (hash map) combined with an efficient algorithm pattern (sliding window) can solve complex permutation problems with optimal time complexity! 🔄✨