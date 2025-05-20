# 1608. Special Array With X Elements Greater Than or Equal X
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

class Solution(object):
    def specialArray(self, nums):
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            # Using expanded version
            count = 0
            for num in nums:
                if num >= mid:
                    count += 1


            if count == mid:
                return mid
            elif count > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
