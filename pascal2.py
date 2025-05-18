class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]

        for _ in range(rowIndex):
            next_row = [0]*(len(res)+1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row

        return res


        