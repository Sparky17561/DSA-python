🧾 Problem Statement
You are given two integer lists basket1 and basket2. You can perform swap operations to make the two baskets contain the same elements (in any order). Each swap has a cost, defined as the smaller of the two elements being swapped.

Your goal is to compute the minimum total cost to make the baskets identical. If it's not possible, return -1.

💡 Approach
Count the difference in frequency of each number between basket1 and basket2.

If any difference is odd, it's impossible to make the baskets equal (return -1).

Collect the items that need to be swapped (half of the absolute difference for each number).

Sort this swap list to optimize cost.

For each swap, choose the cheapest way:

Direct swap: use lst[i]

Indirect swap via cheapest element in both baskets: use 2 * mn

Accumulate the minimum of these two options into res.

✅ Code with Comments
python
Copy
Edit
from collections import defaultdict

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        count = defaultdict(int)

        # Count frequency differences between baskets
        for b in basket1:
            count[b] += 1
        for b in basket2:
            count[b] -= 1

        res = 0
        lst = []
        mn = float('inf')  # Track the smallest value overall

        # Build list of elements that need to be swapped
        for key, val in count.items():
            if val % 2 != 0:
                return -1  # Odd difference means it's impossible
            mn = min(mn, key)
            # Append half the excess value (since one swap fixes two positions)
            for _ in range(abs(val) // 2):
                lst.append(key)

        lst.sort()

        # Pick the cheaper of:
        # - Swapping lst[i] directly
        # - Swapping via the minimum element twice
        for i in range(len(lst) // 2):
            res += min(2 * mn, lst[i])

        return res
✅ Valid Test Case
python
Copy
Edit
basket1 = [1, 1, 4, 3]
basket2 = [2, 4, 2, 3]
Step-by-step:

Differences: {1: 2, 2: -2, 3: 0, 4: 0}

Values needing swap: [1, 2]

Cheapest value in both baskets: 1

Sorted list: [1, 2]

Compute result:

min(2 * 1, 1) = 1

Final result: 1

✅ Output: 1

❌ Invalid Test Case
python
Copy
Edit
basket1 = [1, 2, 3]
basket2 = [1, 2, 2]
Step-by-step:

Differences: {1: 0, 2: -1, 3: 1}

2 and 3 have odd differences

Therefore, cannot balance

❌ Output: -1

🧠 Time & Space Complexity
Time Complexity: O(n log n) — due to sorting the swap list

Space Complexity: O(n) — for frequency map and swap list

