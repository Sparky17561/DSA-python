from collections import Counter
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        

        count = Counter(nums)
        for freq in count.values():
            if freq%2 != 0:
                return False

        return True

        