
# LeetCode Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers, indexed from 1, as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Your solution must use only constant extra space.
# O(n) time complexity and O(1) space complexity solution
# LeetCode 167: Two Sum II - Input Array Is Sorted


class Solution:
    def twoSum(self, numbers, target):
        
        left=0
        right=len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1,right+1]
            elif total < target:
                left+=1
            else:
                right-=1

        