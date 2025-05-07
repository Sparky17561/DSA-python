class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        nums2 = sorted(nums)

        count = 1
        maxi = 0

        for i in range(1,n):
            if nums2[i] != nums2[i-1]:
                if nums2[i] - nums2[i-1] == 1:
                    count +=1
                else:
                    maxi = max(maxi,count)
                    count=1
        
        return max(maxi,count)
        
        