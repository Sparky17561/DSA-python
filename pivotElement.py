class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total =sum(nums)
        left_sum =0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
        return -1

        