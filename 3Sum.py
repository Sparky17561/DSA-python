# 3 things to note:
# 1. We are sorting the array first
# 2. We are using two pointers, one at the start and one at the end of the array
# 3. We are skipping duplicates to avoid duplicate triplets in the result
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# LeetCode 15: 3Sum
# O(n^2) time complexity and O(1) space complexity solution
# LeetCode Problem: https://leetcode.com/problems/3sum/

# first we sort the array , then we place a for loop and fix a number , inside that loop we use two pointer approach (Two sum II) to find the other two numbers that sum to zero with the fixed number. Now to update the left pointer we skip duplicates to avoid duplicate triplets in the result. The right pointer is updated when the sum is greater than zero and the left pointer is updated when the sum is less than zero. When we find a triplet that sums to zero, we append it to the result list and update both pointers while skipping duplicates. for skipping duplicates we check if the current number is equal to the previous number, if it is we skip it. This way we avoid duplicate triplets in the result. Finally we return the result list. We use while loop.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # if not first element and previous num equal to current (cauz we dont need duplicates)
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1
        return res

        