# leetcode 2160. Sort the Jumbled Numbers

class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        def mapped_num(num):
            if num == 0:
                return mapping[0]

            multiplier = 1
            result = 0
            while num > 0:
                digit = num % 10
                mapped_digit = mapping[digit]
                result += mapped_digit * multiplier
                multiplier *= 10
                num //= 10   # Update num here!

            return result

        # Sort nums by their mapped value
        return sorted(nums, key=mapped_num)
