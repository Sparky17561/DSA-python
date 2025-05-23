class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        cnt1 = set(nums1)
        cnt2 = set(nums2)
        


        return [list(cnt1-cnt2),list(cnt2-cnt1)]
        

        