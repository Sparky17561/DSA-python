# Given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = left+1
        maxi=0


        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right+=1
            else:
                maxi = max(maxi,prices[right]-prices[left])
                right+=1

        return maxi
        