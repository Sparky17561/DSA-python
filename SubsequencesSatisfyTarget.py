#leetcode 1498. Number of Subsequences That Satisfy the Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given
#-sum-condition/
# Given an array of integers nums and an integer target, return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target.
# Since the answer may be too large, return it modulo 10^9 + 7
# The solution uses a two-pointer technique and precomputes powers of 2 to efficiently count valid subsequences.
# The array is sorted to facilitate the two-pointer approach.
## Time Complexity: O(n log n) for sorting, O(n) for the two-pointer traversal.
# ## Space Complexity: O(n) for the power array.

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10**9 +7
        nums.sort()
        n = len(nums)

        power =[1]*n

        for i in range(1,n):
            power[i] = (power[i-1]*2)%mod

        left,right=0,n-1

        result=0

        while left<=right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right-left])%mod
                left+=1
            else:
                right-=1
        return result
        