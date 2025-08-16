# Stock Buy and Sell II - Maximum Profit with Multiple Transactions

## Problem Statement

Given an array `prices` where `prices[i]` represents the price of a stock on the *i-th* day, you are allowed to complete **as many transactions as you like** (i.e., buy one and sell one share of the stock multiple times).

You must sell the stock before buying again. Return the maximum profit you can achieve.

---

## Approach

We can maximize profit by taking advantage of **every increasing sequence** in prices:

* If today's price is greater than yesterday's, we can make a profit by buying yesterday and selling today.
* Instead of explicitly simulating multiple buy/sell operations, we simply accumulate the difference whenever `prices[i] > prices[i-1]`.
* This way, we capture all profitable upward trends.

This greedy strategy ensures we gain maximum profit without overcomplicating the logic.

---

## Code with Comments

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0   # Variable to store total profit

        # Traverse from day 1 to last day
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                # If today's price is higher, add the profit difference
                profit += prices[i] - prices[i - 1]

        return profit
```

---

## Examples

### Example 1

**Input:**

```python
prices = [7, 1, 5, 3, 6, 4]
```

**Process:**

* Buy at `1`, sell at `5` → Profit = `4`
* Buy at `3`, sell at `6` → Profit = `3`
* Total Profit = `7`

**Output:**

```python
7
```

### Example 2

**Input:**

```python
prices = [1, 2, 3, 4, 5]
```

**Process:**

* Buy at `1`, sell at `2` → Profit = `1`
* Buy at `2`, sell at `3` → Profit = `1`
* Buy at `3`, sell at `4` → Profit = `1`
* Buy at `4`, sell at `5` → Profit = `1`
* Total Profit = `4`

**Output:**

```python
4
```

### Example 3

**Input:**

```python
prices = [7, 6, 4, 3, 1]
```

**Process:**

* Prices keep falling → No profit.

**Output:**

```python
0
```

---

## Complexity Analysis

* **Time Complexity:** `O(n)` → Single pass through the prices.
* **Space Complexity:** `O(1)` → Constant space used.
