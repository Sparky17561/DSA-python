## Given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# LeetCode 122: Best Time to Buy and Sell Stock II
# This problem allows for multiple transactions, meaning you can buy and sell as many times as you like.
# The goal is to maximize the total profit from these transactions.
# This solution iterates through the prices and adds to the profit whenever there is a price increase from one day to the next.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]

        return profit
        