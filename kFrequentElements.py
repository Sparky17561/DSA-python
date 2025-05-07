class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        freq={}
        a=[]
        for i in range(0,n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        while k != 0:
            high = max(freq,key=freq.get)
            a.append(high)
            freq.pop(high)
            k-=1

        return a



        