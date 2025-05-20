# Given an array of integers, sort the array in increasing order based on the frequency of the elements.
# If two elements have the same frequency, sort them in decreasing order.
# Return the sorted array.


from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data = Counter(nums)
        res = []

        # Sort by frequency (ascending), then by number (descending)
        for key, value in sorted(data.items(), key=lambda item: (item[1], -item[0])):
            res.extend([key] * value)

        return res
