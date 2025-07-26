# Asteroid Collision

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Algorithm Explanation

This problem is solved using a **stack-based approach**:

1. **Stack Usage**: We use a stack to keep track of asteroids that are still "alive" after collisions.

2. **Collision Detection**: A collision occurs when:
   - There's at least one asteroid in the stack (moving right)
   - The current asteroid is moving left (negative value)
   - The top of the stack is moving right (positive value)

3. **Collision Resolution**:
   - If the incoming left-moving asteroid is larger: the right-moving asteroid explodes (pop from stack)
   - If both asteroids are equal size: both explode (pop from stack, don't add current)
   - If the right-moving asteroid is larger: the left-moving asteroid explodes (don't add current)

4. **No Collision Cases**:
   - Both asteroids moving right (positive values)
   - Both asteroids moving left (negative values)
   - Left-moving asteroid followed by right-moving asteroid

## Code Implementation

```python
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for asteroid in asteroids:
            collision = False
            
            # Check for collision: stack not empty, current asteroid moving left, 
            # top of stack moving right
            while stack and asteroid < 0 < stack[-1]:
                # Collision occurs
                if abs(asteroid) > stack[-1]:
                    # Left-moving asteroid is larger, right-moving explodes
                    stack.pop()
                    continue  # Check for more collisions
                elif abs(asteroid) == stack[-1]:
                    # Equal size, both explode
                    stack.pop()
                    collision = True
                    break
                else:
                    # Right-moving asteroid is larger, left-moving explodes
                    collision = True
                    break
            
            # If no collision occurred, add asteroid to stack
            if not collision:
                stack.append(asteroid)
        
        return stack
```

## Examples

### Example 1
```python
Input: asteroids = [5, 10, -5]
Output: [5, 10]

Explanation:
- Start with stack = []
- Process 5: No collision, stack = [5]
- Process 10: No collision, stack = [5, 10]
- Process -5: Collision with 10, since 5 < 10, -5 explodes
- Final result: [5, 10]
```

### Example 2
```python
Input: asteroids = [8, -8]
Output: []

Explanation:
- Start with stack = []
- Process 8: No collision, stack = [8]
- Process -8: Collision with 8, since 8 == 8, both explode
- Final result: []
```

### Example 3
```python
Input: asteroids = [10, 2, -5]
Output: [10]

Explanation:
- Start with stack = []
- Process 10: No collision, stack = [10]
- Process 2: No collision, stack = [10, 2]
- Process -5: Collision with 2, since 5 > 2, 2 explodes, stack = [10]
- Check collision with 10: since 5 < 10, -5 explodes
- Final result: [10]
```

### Example 4
```python
Input: asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]

Explanation:
- All asteroids moving left (-2, -1) never collide with asteroids moving right (1, 2)
- No collisions occur
- Final result: [-2, -1, 1, 2]
```

## Time and Space Complexity

- **Time Complexity**: O(n) where n is the number of asteroids. Each asteroid is pushed and popped from the stack at most once.
- **Space Complexity**: O(n) for the stack in the worst case where no collisions occur.

## Key Insights

1. **Stack Pattern**: This is a classic stack problem where we need to handle interactions between current and previous elements.

2. **Collision Conditions**: Only right-moving asteroids (positive) can collide with left-moving asteroids (negative).

3. **Multiple Collisions**: A single left-moving asteroid might destroy multiple right-moving asteroids in sequence.

4. **Order Matters**: The relative positions and directions determine collision outcomes.

## Usage

```python
# Create solution instance
solution = Solution()

# Test cases
test_cases = [
    [5, 10, -5],
    [8, -8],
    [10, 2, -5],
    [-2, -1, 1, 2],
    [-2, -2, 1, -2]
]

for asteroids in test_cases:
    result = solution.asteroidCollision(asteroids)
    print(f"Input: {asteroids} -> Output: {result}")
```