# leetcode 136. Single Number
# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Bit manipulation is used to solve this problem efficiently.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=0

        for num in nums:
            index ^= num
        return index
        

        
        
