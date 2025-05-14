class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        num1Idx ={n:i for i,n in enumerate(nums1)}
        res = [-1]*len(nums1)

        stack=[]

        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                val = stack.pop()
                idx = num1Idx[val]
                res[idx] = current
            if current in  num1Idx:
                stack.append(current)

        return res

