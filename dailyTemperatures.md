# LeetCode 739: Daily Temperatures

## Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Examples

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Explanation:
Day 0: 73°F → Next warmer day is day 1 (74°F) → wait 1 day
Day 1: 74°F → Next warmer day is day 2 (75°F) → wait 1 day
Day 2: 75°F → Next warmer day is day 6 (76°F) → wait 4 days
Day 3: 71°F → Next warmer day is day 5 (72°F) → wait 2 days
Day 4: 69°F → Next warmer day is day 5 (72°F) → wait 1 day
Day 5: 72°F → Next warmer day is day 6 (76°F) → wait 1 day
Day 6: 76°F → No warmer day ahead → 0
Day 7: 73°F → No warmer day ahead → 0
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Solution Approach: Monotonic Stack

### Algorithm Overview
**Time Complexity: O(n) | Space Complexity: O(n)**

The key insight is to use a **monotonic decreasing stack** that stores indices of temperatures waiting for a warmer day.

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Stack to store indices of temperatures waiting for a warmer day
        stack = []
        
        # Total number of days
        n = len(temperatures)
        
        # Initialize result array with 0s
        res = [0] * n
        
        # Loop through each day's temperature
        for i in range(n):
            # While stack has elements AND current temp > temp at stack's top index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  # Get index of the colder day
                res[prev_index] = i - prev_index  # Calculate days waited
            
            # Add current day's index to stack (waiting for warmer day)
            stack.append(i)
        
        # Indices left in stack never found warmer day → remain 0
        return res
```

## Step-by-Step Visual Walkthrough

Let's trace through `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`:

```
Initial: stack = [], res = [0, 0, 0, 0, 0, 0, 0, 0]

i = 0 → temp = 73
├─ stack is empty → just push index 0
└─ stack = [0], res = [0, 0, 0, 0, 0, 0, 0, 0]

i = 1 → temp = 74
├─ 74 > temperatures[0] (73) → pop index 0
├─ res[0] = 1 - 0 = 1 (found warmer temp after 1 day)
├─ stack becomes empty → push index 1
└─ stack = [1], res = [1, 0, 0, 0, 0, 0, 0, 0]

i = 2 → temp = 75
├─ 75 > temperatures[1] (74) → pop index 1  
├─ res[1] = 2 - 1 = 1 (found warmer temp after 1 day)
├─ stack becomes empty → push index 2
└─ stack = [2], res = [1, 1, 0, 0, 0, 0, 0, 0]

i = 3 → temp = 71
├─ 71 < temperatures[2] (75) → no popping
├─ push index 3
└─ stack = [2, 3], res = [1, 1, 0, 0, 0, 0, 0, 0]

i = 4 → temp = 69
├─ 69 < temperatures[3] (71) → no popping
├─ push index 4
└─ stack = [2, 3, 4], res = [1, 1, 0, 0, 0, 0, 0, 0]

i = 5 → temp = 72
├─ 72 > temperatures[4] (69) → pop index 4
├─ res[4] = 5 - 4 = 1
├─ 72 > temperatures[3] (71) → pop index 3
├─ res[3] = 5 - 3 = 2
├─ 72 < temperatures[2] (75) → stop popping
├─ push index 5
└─ stack = [2, 5], res = [1, 1, 0, 2, 1, 0, 0, 0]

i = 6 → temp = 76
├─ 76 > temperatures[5] (72) → pop index 5
├─ res[5] = 6 - 5 = 1
├─ 76 > temperatures[2] (75) → pop index 2
├─ res[2] = 6 - 2 = 4
├─ stack becomes empty → push index 6
└─ stack = [6], res = [1, 1, 4, 2, 1, 1, 0, 0]

i = 7 → temp = 73
├─ 73 < temperatures[6] (76) → no popping
├─ push index 7
└─ stack = [6, 7], res = [1, 1, 4, 2, 1, 1, 0, 0]

Final: Indices 6 and 7 remain in stack → no warmer days found → keep 0s
```

## Why This Algorithm Works

### Key Insights:

1. **Monotonic Stack Property:** The stack maintains indices in decreasing order of their temperatures
2. **Immediate Processing:** When we find a warmer temperature, we can immediately calculate the waiting days for all colder temperatures in the stack
3. **One-Pass Solution:** Each element is pushed and popped at most once → O(n) time complexity

### Stack Behavior:
```
Stack stores indices where temperatures[stack[i]] > temperatures[stack[i+1]]
This creates a "decreasing temperature sequence" waiting for warmer days
```

## Alternative Solutions

### Brute Force Approach
**Time Complexity: O(n²) | Space Complexity: O(1)**

```python
def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    res = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
                break
    return res
```

### Backward Iteration with Optimization
**Time Complexity: O(n) average | Space Complexity: O(1)**

```python
def dailyTemperatures(self, temperatures):
    n = len(temperatures)
    res = [0] * n
    hottest = 0
    
    for i in range(n - 1, -1, -1):
        current_temp = temperatures[i]
        if current_temp >= hottest:
            hottest = current_temp
            continue
            
        days = 1
        while temperatures[i + days] <= current_temp:
            days += res[i + days]
        res[i] = days
        
    return res
```

## Complexity Analysis

| Method | Time Complexity | Space Complexity | Notes |
|--------|----------------|------------------|-------|
| Monotonic Stack | O(n) | O(n) | Optimal solution |
| Brute Force | O(n²) | O(1) | Simple but inefficient |
| Backward Iteration | O(n) average | O(1) | Space-optimized |

## Key Concepts

### Monotonic Stack
- **Definition:** Stack where elements follow a monotonic order (increasing/decreasing)
- **Usage:** Perfect for "next greater/smaller element" problems
- **Property:** Maintains sorted order while processing elements linearly

### When to Use This Pattern:
- Find next greater/smaller element
- Calculate spans or waiting times
- Process elements that depend on future elements

## Common Mistakes to Avoid

1. **Storing temperatures instead of indices** in the stack
2. **Forgetting to handle remaining stack elements** at the end
3. **Not understanding that each element is processed at most twice** (push + pop)

## Related Problems

- **496. Next Greater Element I**
- **503. Next Greater Element II** 
- **901. Online Stock Span**
- **1019. Next Greater Node In Linked List**

## Test Cases

```python
# Test the solution
solution = Solution()

# Example 1
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
# Expected: [1,1,4,2,1,1,0,0]

# Example 2  
print(solution.dailyTemperatures([30,40,50,60]))
# Expected: [1,1,1,0]

# Example 3
print(solution.dailyTemperatures([30,60,90]))
# Expected: [1,1,0]

# Edge cases
print(solution.dailyTemperatures([30]))  # Expected: [0]
print(solution.dailyTemperatures([90,80,70]))  # Expected: [0,0,0]
```

## Constraints

- `1 <= temperatures.length <= 10⁵`
- `30 <= temperatures[i] <= 100`

## Tags

- **Stack**
- **Monotonic Stack**
- **Array**

---

*This problem is a classic example of using monotonic stacks to solve "next greater element" type problems efficiently.*