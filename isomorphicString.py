class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # Check if c1 is already mapped
            if c1 in map_s_t:
                if map_s_t[c1] != c2:
                    return False
            else:
                map_s_t[c1] = c2

            # Check if c2 is already mapped (reverse mapping)
            if c2 in map_t_s:
                if map_t_s[c2] != c1:
                    return False
            else:
                map_t_s[c2] = c1

        return True
