class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return 0
        
        expected = sorted(heights)  # .sort() returns None after sorting which we cannot iterate thats why we use sorted() which helps us getting a sorted array which is iterable
        count = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count+=1
        
        return count