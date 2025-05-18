class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set()
        destinations = set()

        for path in paths:
            sources.add(path[0])
            destinations.add(path[1])

        for city in destinations:
            if city not in sources:
                return city



# can do with array too


class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = []
        destinations = []

        for path in paths:
            sources.append(path[0])
            destinations.append(path[1])

        for city in destinations:
            if city not in sources:
                return city
