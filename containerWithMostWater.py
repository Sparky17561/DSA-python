# you are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# LeetCode 11: Container With Most Water
# O(n) time complexity and O(1) space complexity solution


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        left = 0
        right = len(height)-1

        while left < right:
            maxarea = max(maxarea,(right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return maxarea


            

            
        