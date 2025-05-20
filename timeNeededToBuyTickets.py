class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        i=0
        n = len(tickets)
        
        while tickets[k] !=0 :
            if tickets[i] == 0 :
                i = (i+1)%n
                continue
                
            tickets[i] -= 1
            time += 1
            i = (i+1)%n

        return time

        
# optimized version

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        total = 0

        for i, x in enumerate(tickets):
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total