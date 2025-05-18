# similar to missing and repeating number problem

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        count = [0]*(n+1)

        for num in nums:
            count[num]+=1

        for i in range(1,n+1):
            if count[i] == 0:
                res.append(i)

        return res     