
# Given a list of names and their corresponding heights, the task is to sort the names based on their heights in descending order.
# The solution involves creating a list of tuples where each tuple contains a name and its corresponding height.


class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = []

        i = 0
        while i < len(names):
            people.append((names[i], heights[i]))
            i += 1

        # Sort by height in descending order
        sorted_people = sorted(people, key=lambda item: item[1], reverse=True)

        # Extract only the names in sorted order
        result = []
        for name, height in sorted_people:
            result.append(name)

        return result
