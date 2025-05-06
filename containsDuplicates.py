class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check ={}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in check:
                return True
            else:
                check[nums[i]] =0
        return False