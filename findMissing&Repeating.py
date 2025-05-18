from collections import Counter
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        flat = []
        for row in grid:
            for num in row:
                flat.append(num)

        count = Counter(flat)


        repeating = missing = -1

        for i in range(1,n*n+1):
            if count[i] == 0 :
                missing = i
            elif count[i] > 1:
                repeating = i
            

        return [repeating,missing]
        
        