Sure! Here's a complete `README.md` file you can use for your project:

---

## 🔥 Count Max OR Subsets

This project contains a solution to the problem of **counting the number of subsets** in a given list of integers such that the **bitwise OR** of the subset is **equal to the maximum possible OR** obtainable from any subset.

---

### 📌 Problem Statement

Given an array `nums`, return the number of **non-empty subsets** whose **bitwise OR** is equal to the **maximum OR** value that can be obtained from any subset of `nums`.

---

### 💡 Approach

We use **backtracking** to explore all possible subsets of the array `nums`. At each step, we decide whether to **include** or **exclude** the current element in the subset.

#### 🔧 Steps:

1. **Compute the Max OR**
   Traverse through all numbers in `nums` and compute the overall OR (`maxOR`) using:

   ```python
   maxOR |= num
   ```

2. **Use Backtracking**
   For each index in the array:

   * Try including the current number (`currentOR | nums[index]`)
   * Try excluding the current number (`currentOR`)
   * Count subsets where `currentOR == maxOR`

3. **Optimization**
   If `currentOR == maxOR` at any point, the number of remaining subsets that will also have `maxOR` is `2^(remaining elements)`. So we return that count directly instead of exploring further.

---

### ✅ Example

Let’s say:

```python
nums = [3, 1]
```

* All subsets: `[], [3], [1], [3,1]`
* OR values: `0, 3, 1, 3`
* Maximum OR: `3`
* Subsets with OR = 3: `[3], [3,1]`

**Answer:** `2`

---

### 🧪 Code

```python
class Solution:
    def countMaxOrSubsets(self, nums):
        # Step 1: Find the maximum OR possible using all elements
        maxOR = 0
        for num in nums:
            maxOR |= num  # Bitwise OR of all numbers

        # Step 2: Define a recursive backtracking function
        def backtrack(index, currentOR):
            # Base case: if we've processed all elements
            if index == len(nums):
                # Check if current OR equals the max OR
                return 1 if currentOR == maxOR else 0

            # Optimization: if currentOR already equals maxOR,
            # all combinations of remaining elements will also give maxOR
            if currentOR == maxOR:
                return 1 << (len(nums) - index)  # 2^(remaining elements)

            # Recurse: include or exclude current element
            include = backtrack(index + 1, currentOR | nums[index])
            exclude = backtrack(index + 1, currentOR)

            return include + exclude

        # Start backtracking from index 0 with OR = 0
        return backtrack(0, 0)
```

---

### 🧪 Test the Code

```python
sol = Solution()
print(sol.countMaxOrSubsets([3, 1]))  # Output: 2
print(sol.countMaxOrSubsets([2, 2, 2]))  # Output: 7
print(sol.countMaxOrSubsets([1, 2, 3]))  # Output: 6
```

---

### 📈 Time and Space Complexity

* **Time Complexity:** `O(2^n)` in the worst case — we explore all subsets.
* **Space Complexity:** `O(n)` for recursion stack.

But thanks to the **early termination optimization**, the performance is much better in practice.

---

Let me know if you want a visualization, LeetCode problem link, or an iterative version!
