class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        direction = {
            'N' : [0,1],
            'S' : [0,-1],
            'E' : [1,0],
            'W' : [-1,0]
        }

        visited = set()
        x,y=0,0 # initially

        for c in path:
            visited.add((x,y)) # pass as a tuple not list/array
            dx,dy = direction[c]
            x,y = x+dx,y+dy
            if (x,y) in visited:
                return True
        return False
        