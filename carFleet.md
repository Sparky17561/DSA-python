# 🚗 Car Fleet Problem - LeetCode 853

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange.svg)](https://leetcode.com/problems/car-fleet/)
[![Topics](https://img.shields.io/badge/Topics-Array%20%7C%20Stack%20%7C%20Sorting-blue.svg)]()
[![Python](https://img.shields.io/badge/Language-Python-3776ab.svg)](https://www.python.org/)

## 🎯 Problem Statement

There are `n` cars at given miles away from the starting mile 0, traveling to reach the mile `target`. You are given two integer arrays `position` and `speed`, both of length `n`, where:
- `position[i]` is the starting mile of the `ith` car
- `speed[i]` is the speed of the `ith` car in miles per hour

**Key Rules:**
- A car cannot pass another car, but it can catch up and travel next to it at the speed of the slower car
- A **car fleet** is a car or cars driving next to each other
- The speed of the car fleet is the **minimum** speed of any car in the fleet
- If a car catches up to a car fleet at the mile `target`, it will still be considered part of the car fleet

**Goal:** Return the number of car fleets that will arrive at the destination.

---

## 💡 Approach & Algorithm

### Core Insight
The key insight is to think about this problem in **reverse order** - from the cars closest to the target backwards. If a car behind can catch up to a car ahead before reaching the target, they form a fleet.

### Algorithm Steps

1. **Sort cars by position**: Pair each car's position with its speed and sort by position
2. **Process from closest to target**: Start with the car closest to the target and work backwards
3. **Calculate arrival time**: For each car, calculate how long it takes to reach the target: `time = (target - position) / speed`
4. **Fleet formation logic**: 
   - If the current car takes **longer** to reach the target than the car ahead, it will form a separate fleet
   - If it takes **less time**, it will catch up and join the fleet ahead
5. **Use stack to track fleets**: Maintain a stack of arrival times for fleet leaders

### Why This Works
- Cars are processed from closest to target to farthest
- A car can only join a fleet if it can catch up before reaching the target
- If a car takes longer than the car ahead, it will never catch up → separate fleet
- The stack keeps track of the "fleet leaders" (cars that determine fleet arrival times)

---

## 🔧 Complete Solution

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []
       
        # Pair positions with speeds and sort by position
        cars = sorted(zip(position, speed))
        
        # Process cars from closest to target (reverse order)
        for pos, spd in reversed(cars):
            # Calculate time to reach target
            time = float(target - pos) / spd
            
            # If stack is empty OR current car takes longer than the car ahead,
            # it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
           
        return len(stack)
```

---

## 📊 Example Walkthrough

### Example 1
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
```

**Step-by-step execution:**

1. **Pair and sort by position:**
   ```
   cars = [(0,1), (3,3), (5,1), (8,4), (10,2)]
   ```

2. **Process in reverse (closest to target first):**
   ```
   Car at pos=10, speed=2: time = (12-10)/2 = 1.0
   stack = [1.0]
   
   Car at pos=8, speed=4: time = (12-8)/4 = 1.0  
   time = stack[-1], so joins fleet
   stack = [1.0]
   
   Car at pos=5, speed=1: time = (12-5)/1 = 7.0
   time > stack[-1], forms new fleet
   stack = [1.0, 7.0]
   
   Car at pos=3, speed=3: time = (12-3)/3 = 3.0
   time < stack[-1], joins fleet ahead
   stack = [1.0, 7.0]
   
   Car at pos=0, speed=1: time = (12-0)/1 = 12.0
   time > stack[-1], forms new fleet
   stack = [1.0, 7.0, 12.0]
   ```

3. **Result:** 3 fleets

**Visual representation:**
```
Target = 12

Fleet 1: Cars at pos 10,8 → arrive at time 1.0
Fleet 2: Cars at pos 5,3 → arrive at time 7.0  
Fleet 3: Car at pos 0 → arrives at time 12.0
```

---

## ⚡ Complexity Analysis

- **Time Complexity:** O(n log n) - dominated by sorting the cars by position
- **Space Complexity:** O(n) - for storing the sorted pairs and the stack

---

## 🧠 Key Insights

1. **Sorting is crucial** - we need to process cars in position order
2. **Reverse iteration** - start from cars closest to target
3. **Time-based thinking** - fleets are determined by arrival times, not speeds
4. **Stack pattern** - perfect for tracking fleet leaders
5. **Greedy approach** - once a car joins a fleet, it's committed to that fleet's speed

---

## 🎨 Alternative Visualization

Think of it like a highway where:
- Faster cars behind slower cars get "stuck" and form convoys
- Each convoy travels at the speed of its slowest member
- We count how many independent convoys reach the destination

This elegant solution captures the essence of traffic flow dynamics in just a few lines of code! 🚗💨