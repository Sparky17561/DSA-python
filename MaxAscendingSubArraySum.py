class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=nums[0]
        maxi=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
            else:
                maxi = max(count,maxi)
                count = nums[i]

        return max(maxi,count)

        