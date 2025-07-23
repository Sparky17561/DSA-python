# 1717. Maximum Score From Removing Substrings

## Problem Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times:

1. **Remove substring "ab"** and gain `x` points
2. **Remove substring "ba"** and gain `y` points

When a substring is removed, the remaining parts of the string are concatenated together.

Return the **maximum points** you can gain after performing the operations optimally.

**Example 1:**
```
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove "ba" earning 5 points. String becomes "cdbcbbaaab".
- Remove "ba" earning 5 points. String becomes "cdbcbbaaab".
- Remove "ab" earning 4 points. String becomes "cdbcbbaa".
- Remove "ba" earning 5 points. String becomes "cdbcba".
- Remove "ba" earning 5 points. String becomes "cdbcb".
Total = 5 + 5 + 4 + 5 + 5 = 24 points.
```

**Example 2:**
```
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
```

## Approach

This solution uses a **Greedy Strategy** combined with **Stack-based Pattern Matching** to achieve optimal results.

### Key Insights

1. **Greedy Choice**: Always remove the pattern that gives more points first
   - If `x >= y`: Remove all "ab" first, then "ba"
   - If `y > x`: Remove all "ba" first, then "ab"

2. **Why Greedy Works**: 
   - Removing one pattern might prevent another from forming
   - Since we want maximum points, we prioritize the higher-scoring pattern
   - After removing all instances of the higher-scoring pattern, we remove the lower-scoring one

3. **Stack-based Removal**: Use a stack to efficiently detect and remove patterns in one pass

### Algorithm Steps

1. **Determine Priority**: Compare `x` and `y` to decide which pattern to remove first

2. **First Pass**: Remove all instances of the higher-scoring pattern
   - Use stack to detect pattern formation
   - When pattern is found, remove it and add points
   - Continue until no more patterns can be formed

3. **Second Pass**: Remove all instances of the lower-scoring pattern from remaining string
   - Apply the same stack-based approach
   - Add points for each removal

4. **Return Total**: Sum points from both passes

### Stack-based Pattern Detection

The `solve` function uses a stack to efficiently detect patterns:

```python
for c in text:
    if stack and c == pattern[1] and stack[-1] == pattern[0]:
        # Pattern found: stack top + current char = pattern
        stack.pop()  # Remove first char of pattern
        points += score  # Add points
    else:
        stack.append(c)  # No pattern, keep building
```

**How it works:**
- Stack maintains characters that haven't formed patterns yet
- When we see the second character of a pattern and stack top is the first character, we found a match
- Remove the first character (pop from stack) and gain points
- Otherwise, add current character to stack

## Complexity Analysis

- **Time Complexity**: O(n)
  - First pass through string: O(n)
  - Second pass through remaining string: O(n) in worst case
  - Overall: O(n) where n is length of input string

- **Space Complexity**: O(n)
  - Stack can hold up to n characters in worst case
  - Remaining string after first pass: O(n)

## Why This Approach is Optimal

1. **Greedy Correctness**: 
   - Removing higher-scoring patterns first never reduces the optimal solution
   - Any removal order that doesn't prioritize higher scores can be improved

2. **Efficient Detection**: 
   - Stack-based approach finds all removable patterns in linear time
   - No need for multiple passes or complex string manipulations

3. **No Missed Opportunities**: 
   - The algorithm finds all possible removals for each pattern type
   - Two-pass approach ensures we don't miss any combinations

## Example Walkthrough

For `s = "aabbaaxybbaabb"`, `x = 5`, `y = 4`:

**Since x > y, remove "ab" first:**

1. **First Pass (remove "ab", score = 5)**:
   - Process: "aabbaaxybbaabb"
   - Stack progression: [a] → [a,a] → [a] (found "ab", +5) → [a] → [a,a] → [a,a,x] → [a,a,x,y] → [a,a,x] (found "yb"? No) → [a,a,x,y,b] → [a,a,x,y] (found "ba"? No, wrong pattern) → [a,a,x,y,b,a] → [a,a,x,y,b] (found "ab", +5) → [a,a,x,y,b] → [a,a,x,y] (found "bb"? No)
   - Points: 10, Remaining: "aaxybba"

2. **Second Pass (remove "ba", score = 4)**:
   - Process: "aaxybba"  
   - Find and remove "ba" patterns: +4
   - Points: 4

**Total: 10 + 4 = 14 points**

## Edge Cases Handled

1. **No patterns exist**: Returns 0
2. **Only one pattern type exists**: Correctly processes available patterns
3. **Equal scores (x == y)**: Handles either order correctly
4. **Empty string**: Returns 0
5. **Overlapping potential patterns**: Greedy approach handles optimally

## Usage

```python
solution = Solution()
s = "cdbcbbaaabab"
x = 4  # points for "ab"
y = 5  # points for "ba"
result = solution.maximumGain(s, x, y)
print(result)  # Output: 19
```

## Complete Code

```python
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        Find the maximum score by removing 'ab' and 'ba' substrings optimally.
        
        :type s: str
        :type x: int (score for removing 'ab')
        :type y: int (score for removing 'ba')
        :rtype: int
        """
        
        def solve(text, pattern, score):
            """
            Remove all occurrences of a specific pattern and calculate points.
            
            Args:
                text: String to process
                pattern: Two-character pattern to remove ('ab' or 'ba')
                score: Points gained for each removal
            
            Returns:
                tuple: (total_points, remaining_string_after_removals)
            """
            stack = []  # Stack to simulate string building and pattern matching
            points = 0  # Track total points gained
            
            for c in text:
                # Check if current character completes the pattern with stack top
                if stack and c == pattern[1] and stack[-1] == pattern[0]:
                    # Pattern found! Remove the first character from stack and gain points
                    stack.pop()
                    points += score
                else:
                    # No pattern match, add current character to stack
                    stack.append(c)
            
            # Return total points and remaining string (characters that couldn't form patterns)
            return points, "".join(stack)
        
        # GREEDY STRATEGY: Always remove the higher-scoring pattern first
        # This maximizes our total score since removing one pattern might
        # prevent formation of another, so we prioritize the more valuable one
        
        if x >= y:
            # 'ab' gives more points, so remove all 'ab' patterns first
            point1, rem_string = solve(s, 'ab', x)
            # Then remove all possible 'ba' patterns from remaining string
            point2, _ = solve(rem_string, 'ba', y)
        else:
            # 'ba' gives more points, so remove all 'ba' patterns first
            point1, rem_string = solve(s, 'ba', y)
            # Then remove all possible 'ab' patterns from remaining string
            point2, _ = solve(rem_string, 'ab', x)
        
        return point1 + point2


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "cdbcbbaaabab"
    x1, y1 = 4, 5
    result1 = solution.maximumGain(s1, x1, y1)
    print(f"Input: s = '{s1}', x = {x1}, y = {y1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    s2 = "aabbaaxybbaabb"
    x2, y2 = 5, 4
    result2 = solution.maximumGain(s2, x2, y2)
    print(f"Input: s = '{s2}', x = {x2}, y = {y2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3
    s3 = "abba"
    x3, y3 = 2, 1
    result3 = solution.maximumGain(s3, x3, y3)
    print(f"Input: s = '{s3}', x = {x3}, y = {y3}")
    print(f"Output: {result3}")
```

## Alternative Approaches

1. **Dynamic Programming**: More complex, O(n²) time complexity
2. **Recursive with Memoization**: Exponential without optimization
3. **Brute Force**: Try all possible removal orders - exponential time

The greedy stack-based approach is optimal for this problem, providing the best balance of simplicity, efficiency, and correctness.