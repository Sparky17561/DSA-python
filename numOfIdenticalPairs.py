class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        count={}

        for num in nums:
            if num in count:
                res += count[num]
                count[num]+=1
            else:
                count[num] = 1
        

        return res
    

    # mathematical solution
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        num_freq = Counter(nums)
        for freq in num_freq.values():
            count += (freq * (freq - 1)) // 2
        return count