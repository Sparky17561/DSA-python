# Koko Eating Bananas

## Intuition (short)

Koko has several piles of bananas and a deadline `H` hours. She chooses a single integer eating speed `K` (bananas/hour). For a pile of size `p`, she needs `ceil(p / K)` hours. We want the **minimum** `K` such that the total hours `sum(ceil(p / K)) <= H`.

This is a classic application of **binary search on the answer** (not on array indices):

* Rephrase the problem as: **find the minimal ****************`K`**************** such that ****************`feasible(K)`**************** is True**.
* `feasible(K)` = "Koko finishes within `H` hours".
* `feasible(K)` is monotonic: if `feasible(K)` is True, then any `K' > K` is also True. So binary search applies.

Search space:

* Lower bound `L = 1` (at least 1 banana/hour).
* Upper bound `R = max(piles)` (eating the biggest pile in one hour is the fastest needed).

Time complexity: each feasibility check is `O(n)` (sum over piles). We do `O(log M)` checks where `M = max(piles)`. So overall **O(n · log M)**. Space complexity: **O(1)** extra.

---

## Template mapping (how this fits the general binary-search template)

General template (find minimal `k` with `condition(k)` True):

```python
left, right = L, R
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left
```

Mapping for Koko:

* `k` → `speed` (bananas/hour)
* `condition(speed)` → `sum( ceil(pile / speed) ) <= H` (i.e., can finish within `H` hours)
* `L` = 1, `R` = max(piles)

We use an inclusive variant below (`while left <= right`) and keep an `ans` variable. That style is very explicit and easy to reason about:

* If `total_hours <= H`, record `ans = mid` and try smaller speeds (`right = mid - 1`).
* Otherwise, need a faster speed (`left = mid + 1`).

---

## Code (clean, commented, safe integer arithmetic)

```python
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int

        Returns the minimum integer speed K such that sum( ceil(pile / K) ) <= H.
        Uses binary search on K in the range [1, max(piles)].
        """

        # Binary-search bounds
        left = 1
        right = max(piles)      # upper bound (inclusive)
        ans = right             # best found candidate

        # We use integer math for ceil: ceil(a / b) == (a + b - 1) // b
        while left <= right:
            mid = (left + right) // 2   # candidate speed
            total_hours = 0

            # compute hours needed at speed = mid
            for pile in piles:
                # integer ceil division
                total_hours += (pile + mid - 1) // mid

                # small optimization: early exit if we already exceed h
                if total_hours > h:
                    break

            # If mid is feasible (total_hours <= h), try slower speeds
            if total_hours <= h:
                ans = mid
                right = mid - 1
            else:
                # mid too slow: need a larger speed
                left = mid + 1

        return ans
```

Notes about the implementation:

* We compute `ceil(pile / speed)` without floats using `(pile + speed - 1) // speed`. This avoids any float/integer-division pitfalls and is faster.
* We included an **early break** in the loop when `total_hours` already exceeds `h` to save time on large inputs.
* The binary search uses an inclusive `[left, right]` loop (`while left <= right`) and maintains `ans` explicitly.

---

## Example (step-by-step)

Input:

```
piles = [3, 6, 7, 11]
h = 8
```

Goal: minimal `K` so that `sum(ceil(pile / K)) <= 8`.

Binary-search iterations (high-level):

* `left = 1`, `right = 11` → `mid = 6`

  * hours = `ceil(3/6)+ceil(6/6)+ceil(7/6)+ceil(11/6)` = `1+1+2+2 = 6` → `6 <= 8` → feasible. Record `ans = 6`. Try slower: `right = 5`.
* `left = 1`, `right = 5` → `mid = 3`

  * hours = `ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3)` = `1+2+3+4 = 10` → `10 > 8` → not feasible. Need faster: `left = 4`.
* `left = 4`, `right = 5` → `mid = 4`

  * hours = `ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4)` = `1+2+2+3 = 8` → `8 <= 8` → feasible. Record `ans = 4`. Try slower: `right = 3`.

Loop ends (`left > right`). Final `ans = 4` (correct).

---

## Complexity

* Time: `O(n * log M)` where `n = len(piles)` and `M = max(piles)`.
* Space: `O(1)` extra.

---

## Common pitfalls & tips

* **Wrong division**: Do not use integer division with floats incorrectly. Prefer `(pile + speed - 1) // speed` to compute ceil without floats.
* **Off-by-one in bounds**: Be consistent with inclusive/exclusive `right`. The code above uses inclusive `right` and `while left <= right`.
* **Non-monotonic condition**: Binary search requires monotonicity. Make sure `feasible(k)` becomes no harder as `k` increases (true for Koko).

---


