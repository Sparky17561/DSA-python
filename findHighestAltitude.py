# leetcode 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/


class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        res=[0]
        prefix=0

        for i in range(len(gain)):
            prefix+= gain[i]
            res.append(prefix)

        return max(res)
        