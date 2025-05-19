from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)  # automatically sets missing keys to 0
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2

        # Check if any character has an odd count left (can be placed in the center)
        for cnt in count.values():
            if cnt % 2:
                res += 1
                break

        return res
