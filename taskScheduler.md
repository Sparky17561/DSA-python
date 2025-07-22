# LeetCode 621: Task Scheduler

## Problem Description

Given a characters array `tasks` representing tasks to do and a positive integer `n` representing the cooling time between two same tasks, return the least number of units of time needed to complete all tasks.

Each task takes one unit of time to complete, and identical tasks must be separated by at least `n` units of time.

**Constraints:**
- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter
- `0 <= n <= 100`

## Examples

### Example 1
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B
```

### Example 2
```
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
```

### Example 3
```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: One possible solution is: A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

## Solution Strategy

The key insight is to think about the problem in terms of **frames** or **slots**:

1. **Identify the bottleneck**: The task that appears most frequently will determine the minimum schedule length
2. **Create frames**: Each frame consists of one instance of the most frequent task plus `n` cooling slots
3. **Fill the slots**: Other tasks can fill the cooling slots between the most frequent tasks

## Algorithm Breakdown

### Step 1: Count Task Frequencies
Count how many times each task appears in the input array.

### Step 2: Find Maximum Frequency
Identify which task(s) appear most frequently. This determines our scheduling constraint.

### Step 3: Count Tasks with Maximum Frequency
Count how many different tasks share the maximum frequency. These will all need to be scheduled in the final frame.

### Step 4: Calculate Minimum Time Slots
```
total_slots = (max_freq - 1) × (n + 1) + max_count
```

Where:
- `(max_freq - 1)`: Number of complete frames between the first and last occurrence of max frequency tasks
- `(n + 1)`: Size of each frame (1 slot for the max freq task + n cooling slots)
- `max_count`: Tasks that need to be placed in the final frame

### Step 5: Handle Edge Cases
Return `max(len(tasks), total_slots)` because:
- If we have enough diverse tasks, we might not need any idle time
- The answer can never be less than the total number of tasks

## Visual Example

For `tasks = ["A", "A", "A", "B", "B", "B"]` and `n = 2`:

```
Frame structure:
A _ _ | A _ _ | A

Filled with other tasks:
A B _ | A B _ | A B

Final schedule:
A B idle A B idle A B
```

**Time units: 8**

## Time & Space Complexity

- **Time Complexity**: O(n) where n is the number of tasks
  - Single pass to count frequencies
  - Single pass to find max frequency and count
- **Space Complexity**: O(1) 
  - At most 26 different tasks (uppercase English letters)
  - Dictionary size is bounded by constant

## Key Insights

1. **Greedy doesn't work**: Simply alternating tasks won't always give the optimal solution
2. **Frame thinking**: Structure the problem around the most constraining task
3. **Idle time calculation**: The formula elegantly handles when idle time is needed vs. when we have enough diverse tasks
4. **Edge case handling**: The `max()` operation naturally handles scenarios where we have abundant task diversity

## Common Pitfalls

- Trying to simulate the actual scheduling (unnecessary complexity)
- Forgetting to handle cases where no idle time is needed
- Not accounting for multiple tasks with the same maximum frequency
- Off-by-one errors in frame calculation

## Alternative Approaches

While this mathematical approach is optimal, the problem can also be solved using:
- **Heap-based simulation**: More intuitive but less efficient
- **Priority queue**: Similar to heap approach
- **Greedy with detailed tracking**: More complex implementation

The mathematical approach shown here is preferred for its elegance and efficiency.