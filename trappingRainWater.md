# LeetCode 42: Trapping Rain Water

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Constraints:**
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 3 * 10^4`

## Examples

### Example 1
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Visualization:
   █
   █   █
   █ ▓ █ █
 █ █▓█▓█▓█ █ █
 0 1 0 2 1 0 1 3 2 1 2 1

Water trapped (▓): 6 units
```

### Example 2
```
Input: height = [4,2,0,3,2,5]
Output: 9

Visualization:
 █     █
 █ ▓ ▓ █
 █▓█▓█▓█
 █▓█▓█▓█
 4 2 0 3 2 5

Water trapped (▓): 9 units
```

## Solution Approaches

### Approach 1: Two Pointer (Optimal) ⭐

The key insight: **Water at any position is bounded by the minimum of the maximum heights to its left and right**.

#### Core Logic
```
water_trapped = min(left_max, right_max) - current_height
```

#### Why Two Pointers Work
- We process the side with the smaller height first
- This guarantees that the water level at that position is determined by the smaller maximum
- We don't need to know the exact right_max for the left side (and vice versa) as long as we know which side is limiting

#### Algorithm Steps
1. Initialize two pointers: `left = 0`, `right = n-1`
2. Track `left_max` and `right_max` as we move inward
3. Always process the pointer with smaller height:
   - If current height ≥ max_height: update the max
   - Otherwise: add trapped water = max_height - current_height
4. Move the processed pointer inward
5. Continue until pointers meet

### Approach 2: Dynamic Programming
```python
def trap_dp(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Fill right_max array
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water
    water = 0
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - height[i])
    
    return water
```

### Approach 3: Stack-Based
```python
def trap_stack(height):
    stack = []
    water = 0
    
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            water += distance * bounded_height
        stack.append(i)
    
    return water
```

## Detailed Example Walkthrough

For `height = [0,1,0,2,1,0,1,3,2,1,2,1]`:

```
Initial: l=0, r=11, lmax=0, rmax=0, water=0

Step 1: height[0]=0 < height[11]=1
        lmax = max(0,0) = 0, water += 0-0 = 0, l=1

Step 2: height[1]=1 = height[11]=1 
        lmax = max(0,1) = 1, l=2

Step 3: height[2]=0 < height[11]=1
        water += 1-0 = 1, l=3

Step 4: height[3]=2 > height[11]=1
        rmax = max(0,1) = 1, r=10

Step 5: height[3]=2 > height[10]=2? No, equal
        lmax = max(1,2) = 2, l=4

...continuing this process...

Final result: 6 units of trapped water
```

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Two Pointer | O(n) | O(1) | ⭐ Optimal |
| Dynamic Programming | O(n) | O(n) | Easier to understand |
| Stack | O(n) | O(n) | Good for variations |

## Key Insights

### 1. Water Trapping Principle
Water can only be trapped between higher bars. The amount of water at any position is determined by the **bottleneck** - the minimum of maximum heights on both sides.

### 2. Two Pointer Optimization
Instead of pre-computing all left_max and right_max values, we can:
- Process both ends simultaneously
- Always work on the side with smaller height (the limiting factor)
- This ensures we always have enough information to calculate trapped water

### 3. Why Process Smaller Height First?
```
If height[left] < height[right]:
    - We know left_max ≤ height[right]
    - So min(left_max, right_max) = left_max (regardless of actual right_max)
    - We can safely calculate water trapped at left position
```

## Common Pitfalls

1. **Boundary conditions**: Handle arrays with length < 3 (no water can be trapped)
2. **Pointer movement**: Always move the pointer after processing
3. **Max tracking**: Update max before calculating trapped water
4. **Integer overflow**: Generally not an issue given constraints, but be aware

## Visual Understanding

Think of the problem as:
1. **Containers**: Each position can hold water up to `min(left_max, right_max)`
2. **Current level**: Subtract current bar height to get actual trapped water
3. **Scanning**: Process from both ends to efficiently find the bottlenecks

## Alternative Applications

This algorithm pattern (two pointers with max tracking) appears in:
- Container With Most Water (LeetCode 11)
- Largest Rectangle in Histogram variations
- Stock price problems with constraints

## Practice Variations

1. **2D Rain Water Trapping** (LeetCode 407)
2. **Container With Most Water** (LeetCode 11)
3. **Candy Distribution** (LeetCode 135)
4. **Product of Array Except Self** (LeetCode 238)