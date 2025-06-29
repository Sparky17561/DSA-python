
# StriverAtoZ
# we are given an array of integers and a target sum k.
# We need to find the length of the longest contiguous subarray that sums to k.
# non-negative integers are given in the array.
# We can use a sliding window approach to solve this problem efficiently.
class Solution:
    def longestSubarray(self, nums, k):
        i = 0
        res = 0
        maxL = 0

        for j in range(len(nums)):
            res += nums[j]

            # shrink window while sum > k
            while res > k and i <= j:
                res -= nums[i]
                i += 1

            if res == k:
                maxL = max(maxL, j - i + 1)

        return maxL
