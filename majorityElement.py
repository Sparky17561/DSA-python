# brute force

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)

        if n == 1:
            return nums[0]
        hash1={}
        for num in nums:
            if num not in hash1:
                hash1[num] = 1
            else:
                hash1[num] += 1
                if hash1[num] > n//2:
                    return num

        
        
# optimal 

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        return nums[len(nums)//2]