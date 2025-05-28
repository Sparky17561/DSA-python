
# Given an array of people and a limit, this function calculates the minimum number of boats required to save all people.
# LeetCode 881: Boats to Save People

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        count=0
        left = 0
        right = len(people)-1

        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
            right-=1
            count+=1


        return count