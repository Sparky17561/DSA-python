#leetcode 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/
## Given a binary array nums, return the maximum length of a contiguous subarray with an equal number
# of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_map={0:-1}
        maxL = 0
        curr_sum=0

        for i,num in enumerate(nums):
            if num == 0:
                curr_sum+=-1
            else:
                curr_sum+=1
            
            if curr_sum in prefix_map:
                maxL = max(maxL,i-prefix_map[curr_sum])
            else:
                prefix_map[curr_sum] = i

        return maxL
        