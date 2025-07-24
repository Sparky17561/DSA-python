# 994. Rotting Oranges - BFS Multi-Source Solution

**Difficulty**: Medium  
**Topics**: Array, Breadth-First Search, Matrix

## Problem Description

You are given an `m x n` grid where each cell can have one of three values:
- `0` representing an empty cell
- `1` representing a fresh orange  
- `2` representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Approach: Multi-Source BFS (Breadth-First Search)

The intuition behind the solution is to use a Breadth-First Search (BFS) approach, which is well-suited for problems involving levels or minutes passing by as in this case.

### Key Insight

This is a **multi-source BFS** problem where:
- All initially rotten oranges start spreading rot simultaneously
- Each minute represents one level of BFS expansion  
- We need to track time and ensure all fresh oranges can be reached

### Key Concepts

1. **Multi-Source BFS**: Start BFS from all rotten oranges simultaneously
2. **Level-by-Level Processing**: Each level represents one minute passing
3. **4-Directional Spread**: Rot spreads up, down, left, right only
4. **Reachability Check**: Verify all fresh oranges can eventually rot

### Algorithm Steps

1. **Initialize**:
   - Create a queue with all initially rotten orange positions
   - Count total fresh oranges
   - Set minutes to 0

2. **BFS Level Processing**:
   - While queue has rotten oranges AND fresh oranges remain:
     - Increment minutes
     - Process all oranges at current level (current queue size)
     - For each rotten orange, check 4 adjacent cells
     - If adjacent cell has fresh orange, make it rotten and add to queue

3. **Return Result**:
   - If no fresh oranges remain: return minutes
   - If fresh oranges still exist: return -1 (impossible)

### Time Complexity: O(m × n)
- Each cell is visited at most once during BFS
- Initial grid traversal is O(m × n)

### Space Complexity: O(m × n)
- Queue can store up to m × n cells in worst case

## Example Walkthrough

Let's trace through this grid with initial state:
```
[[2,1,1],
 [1,1,0], 
 [0,1,1]]
```

```
Initial Setup:
- rotten = [(0,0)] (initially rotten orange)
- fresh_cnt = 5 (count of 1's)
- minutes_passed = 0

Minute 1:
Process (0,0):
- Check (1,0): fresh → rotten, add to queue
- Check (0,1): fresh → rotten, add to queue
- fresh_cnt = 3
- rotten = [(1,0), (0,1)]
- minutes_passed = 1

Grid after minute 1:
[[2,2,1],
 [2,1,0],
 [0,1,1]]

Minute 2:
Process (1,0):
- Check (1,1): fresh → rotten, add to queue
Process (0,1): 
- Check (0,2): fresh → rotten, add to queue
- fresh_cnt = 1  
- rotten = [(1,1), (0,2)]
- minutes_passed = 2

Grid after minute 2:
[[2,2,2],
 [2,2,0],
 [0,1,1]]

Minute 3:
Process (1,1):
- Check (2,1): fresh → rotten, add to queue
Process (0,2): (no adjacent fresh oranges)
- fresh_cnt = 0
- rotten = [(2,1)]
- minutes_passed = 3

Grid after minute 3:
[[2,2,2],
 [2,2,0],
 [0,2,1]]

Minute 4:
Process (2,1):
- Check (2,2): fresh → rotten, add to queue
- fresh_cnt = 0 (already 0)
- rotten = [(2,2)]
- minutes_passed = 4

Final Grid:
[[2,2,2],
 [2,2,0],
 [0,2,2]]

Result: 4 minutes
```

## Example with Impossible Case

Grid: `[[2,1,1],[0,1,1],[1,0,1]]`

```
Initial: rotten=[(0,0)], fresh_cnt=5

After processing all reachable cells:
- Only (0,1) and (1,1) become rotten
- (1,0), (1,2), (2,0), (2,2) remain fresh but unreachable
- fresh_cnt > 0 but queue is empty

Result: -1 (impossible)
```

## Implementation Details

### Why Level-by-Level Processing?

```python
for _ in range(len(rotten)):  # Process current level only
    x, y = rotten.popleft()
    # Process neighbors...
```

This ensures we process all oranges that became rotten in the current minute before moving to the next minute.

### Boundary and Validity Checks

```python
if xx < 0 or xx == rows or yy < 0 or yy == cols:
    continue  # Out of bounds
if grid[xx][yy] == 2 or grid[xx][yy] == 0:  
    continue  # Already rotten or empty
```

### Fresh Orange Tracking

```python
fresh_cnt -= 1  # Decrement when orange becomes rotten
grid[xx][yy] = 2  # Mark as rotten
rotten.append((xx, yy))  # Add to queue for next level
```

## Edge Cases

- **No fresh oranges initially**: Return 0
- **No rotten oranges initially**: Return -1 if fresh oranges exist, 0 otherwise  
- **Isolated fresh oranges**: Return -1
- **Empty grid**: Return 0

## Complete Solution

```python
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return 0
            
        rotten = deque()
        minutes_passed = 0
        fresh_cnt = 0
        
        # Find all initially rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        # BFS level by level
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            
            # Process all oranges at current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                # Check 4 directions
                for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                    xx, yy = x + dx, y + dy
                    
                    # Boundary check
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    
                    # Skip if not fresh orange
                    if grid[xx][yy] == 2 or grid[xx][yy] == 0:
                        continue
                    
                    # Make fresh orange rotten
                    fresh_cnt -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        
        return minutes_passed if fresh_cnt == 0 else -1
```

## Why This Approach Works

The multi-source BFS technique is perfect because:

1. **Simultaneous Spreading**: All rotten oranges spread rot at the same time, naturally handled by BFS
2. **Level Tracking**: Each BFS level corresponds exactly to one minute
3. **Optimal Time**: BFS guarantees we find the minimum time needed
4. **Reachability**: We can detect if some oranges are unreachable (isolated)
5. **Natural Termination**: Algorithm stops when no more spreading is possible

This approach efficiently simulates the natural spreading process while tracking the exact time required.