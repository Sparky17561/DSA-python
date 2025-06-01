# stack

# This code is for a baseball game scoring system.
# It processes a list of operations and calculates the total score.
# leetcode 682


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))  # Works for negatives too

        return sum(stack)
