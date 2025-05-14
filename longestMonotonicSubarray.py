class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 1
        res = 1
        increasing = 0 # neither increasing nor decreasing

        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]: #ascending sequence
                if increasing > 0:
                    current+=1  # increment if already ascending sequence
                else:
                    current=2 # increment current and change increasing flag to ascending
                    increasing=1
            elif nums[i-1] > nums[i]: # descending sequence
                if increasing < 0:
                    current+=1 
                else:
                    current=2
                    increasing=-1
            else: # if equal element
                current=1
                increasing=0
            res=max(res,current)

        return res
        