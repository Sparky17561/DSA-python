# Sliding window
# It is a technique that uses a window to traverse through the array.
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        

# solution

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        L=0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False