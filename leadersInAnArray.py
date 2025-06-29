# StriverAtoZ
# Given an array of integers, we need to find all the leaders in the array.
# An element is a leader if it is greater than all the elements to its right side.
# The rightmost element is always a leader.

# Brute Force Approach:
class Solution:
    def leaders(self, nums):
        leader = []

        for i in range(len(nums)):
            is_leader = True
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    is_leader = False
                    break
            if is_leader:
                leader.append(nums[i])

        return leader





## Efficient Approach:# We can solve this problem in O(n) time complexity by traversing the array from right to
class Solution:
    def leaders(self, nums):
        leader = []
        max_from_right = nums[-1]
        leader.append(max_from_right)

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_from_right:
                max_from_right = nums[i]
                leader.append(max_from_right)

        return leader[::-1]
