# Given an unsorted integer array nums, return the smallest missing positive integer.
# LeetCode 41: First Missing Positive
# O(n) time complexity and O(1) space complexity solution



class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]: # number should be inside range(1,size of nums) and also check if number is already in its index position if it is we dont need to evaluate
                correct_idx = nums[i]-1
                nums[i],nums[correct_idx] = nums[correct_idx],nums[i]


        for i in range(n):
            if nums[i] != i+1:  # [1,3,4] => positions are [0,1,2] => 1 == 0+1, 3 != 1+1 return 1+1
                return i+1

        return n+1

        