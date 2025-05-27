from functools import cmp_to_key
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it as a string.
# LeetCode 179: Largest Number
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i,n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1,n2):
            if n1 + n2 > n2 +n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        return str(int(''.join(nums)))