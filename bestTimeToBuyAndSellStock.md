# Stock Buy and Sell - Maximum Profit

## Problem Statement

Given an array `prices` where `prices[i]` represents the price of a given stock on the *i-th* day, the task is to maximize profit by choosing **one day to buy** the stock and a **different day in the future to sell** it.

Return the maximum profit achievable. If no profit can be made, return `0`.

---

## Approach

We use a **two-pointer sliding window** technique:

* Maintain two pointers: `left` (buy day) and `right` (sell day).
* Initialize `left = 0` and `right = 1`.
* Loop while `right < len(prices)`:

  * If `prices[left] >= prices[right]`, it means the current `right` is a better day to buy, so move `left` to `right`.
  * Else, calculate profit = `prices[right] - prices[left]` and update the maximum profit.
  * Increment `right` in each step.
* Return the maximum profit found.

This ensures we always buy at the lowest price seen so far and sell at the highest profit possible after that.

---

## Code with Comments

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0             # Pointer for buying day
        right = left + 1     # Pointer for selling day
        maxi = 0             # Variable to store maximum profit

        # Traverse through the prices
        while right < len(prices):
            if prices[left] >= prices[right]:
                # Found a cheaper buying price, shift buying pointer
                left = right
                right += 1
            else:
                # Calculate profit and update maximum profit
                maxi = max(maxi, prices[right] - prices[left])
                right += 1

        return maxi
```

---

## Examples

### Example 1

**Input:**

```python
prices = [7, 1, 5, 3, 6, 4]
```

**Process:**

* Buy at `1`, Sell at `6` → Profit = `5`

**Output:**

```python
5
```

### Example 2

**Input:**

```python
prices = [7, 6, 4, 3, 1]
```

**Process:**

* Prices are decreasing → No profit possible.

**Output:**

```python
0
```

---

## Complexity Analysis

* **Time Complexity:** `O(n)` → Single traversal of the array.
* **Space Complexity:** `O(1)` → Constant extra space used.
