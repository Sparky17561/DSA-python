class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        n = len(s)

        for i in range(1, n):  # valid splits from 1 to n-1
            left = s[:i]
            right = s[i:]
            left_zeros = left.count('0')
            right_ones = right.count('1')
            score = left_zeros + right_ones
            max_score = max(max_score, score)

        return max_score
