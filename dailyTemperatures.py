# leetcode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

# 🧪 Example Input:
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# ✅ Output:
# [1, 1, 4, 2, 1, 1, 0, 0]

# 🧠 Step-by-step Visual for First Few Days:
# i = 0 → 73 → stack = [0]

# i = 1 → 74 > 73 → pop 0, res[0] = 1 → stack = [] → push 1

# i = 2 → 75 > 74 → pop 1, res[1] = 1 → stack = [] → push 2

# i = 3 → 71 < 75 → push 3

# i = 4 → 69 < 71 → push 4

# i = 5 → 72 > 69 → pop 4, res[4] = 1 → 72 > 71 → pop 3, res[3] = 2 → push 5
# ...



class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Stack to store indices of temperatures that are waiting for a warmer day
        stack = []

        # Total number of days
        n = len(temperatures)

        # Initialize result array with 0s. Each index will store how many days to wait.
        res = [0] * n

        # Loop through each day's temperature
        for i in range(n):

            # While there's a previous temperature in stack AND current temperature is higher
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  # Get index of the colder day
                res[prev_index] = i - prev_index  # Calculate days waited for a warmer day

            # Add current day's index to the stack (waiting for a warmer day)
            stack.append(i)

        # Any indices left in the stack never had a warmer day ahead → remain 0 in result
        return res
