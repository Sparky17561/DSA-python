
from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        actual=[]

        for i in range(len(nums)):
            actual.append(i+1)
        
        seta = set(actual)
        setb = set(nums)
        diff = list(seta - setb)

        for num in nums:
            if count[num] == 2:
                rep = num

        return [rep,diff[0]]
        