# Boats to Save People - Minimum Boats Required

## Problem Statement

You are given an array `people` where `people[i]` is the weight of the *i-th* person, and an integer `limit` which represents the maximum weight capacity of a boat. Each boat can carry at most two people at the same time, provided the sum of their weights does not exceed the `limit`.

Return the **minimum number of boats** required to save all people.

---

## Approach

We use a **two-pointer greedy strategy**:

1. Sort the array `people` in non-decreasing order.
2. Maintain two pointers:

   * `left` → lightest person.
   * `right` → heaviest person.
3. Try to pair the lightest and heaviest person:

   * If `people[left] + people[right] <= limit`, both can share one boat. Move both pointers (`left += 1`, `right -= 1`).
   * Else, the heaviest person (`people[right]`) must go alone, so move `right -= 1`.
4. In each case, we use **one boat** (`count += 1`).
5. Continue until all people are assigned to boats.

This greedy approach minimizes the number of boats by always attempting to pair the heaviest person with the lightest possible partner.

---

## Code with Comments

```python
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()  # Sort people by weight
        count = 0      # Number of boats used
        left = 0       # Pointer to lightest person
        right = len(people) - 1  # Pointer to heaviest person

        # While there are people left to place in boats
        while left <= right:
            if people[left] + people[right] <= limit:
                # Lightest and heaviest can share a boat
                left += 1
            # Heaviest person always goes in a boat (alone or paired)
            right -= 1
            count += 1

        return count
```

---

## Examples

### Example 1

**Input:**

```python
people = [1, 2], limit = 3
```

**Process:**

* `1 + 2 = 3` → Both share one boat.

**Output:**

```python
1
```

### Example 2

**Input:**

```python
people = [3, 2, 2, 1], limit = 3
```

**Process:**

* Pair `(1, 2)` → Boat 1
* Pair `(2)` alone → Boat 2
* Pair `(3)` alone → Boat 3

**Output:**

```python
3
```

### Example 3

**Input:**

```python
people = [3, 5, 3, 4], limit = 5
```

**Process:**

* Pair `(3)` alone → Boat 1
* Pair `(3)` alone → Boat 2
* Pair `(4)` alone → Boat 3
* Pair `(5)` alone → Boat 4

**Output:**

```python
4
```

---

## Complexity Analysis

* **Time Complexity:** `O(n log n)` → Sorting dominates.
* **Space Complexity:** `O(1)` → Constant extra space.
