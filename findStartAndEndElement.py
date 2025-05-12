# optimal soln 

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        
        def first_position(nums, target): 
            first = -1
            s = 0 
            end = n - 1 
            while s <= end: 
                m = (s + end) // 2 
                if target > nums[m]: 
                    s = m + 1  
                elif target == nums[m]: 
                    first = m 
                    end = m - 1  # move left
                else: 
                    end = m - 1  # corrected
            return first        

        def last_position(nums, target):
            last = -1
            s = 0 
            end = n - 1 
            while s <= end: 
                m = (s + end) // 2 
                if target > nums[m]: 
                    s = m + 1  
                elif target == nums[m]: 
                    last = m 
                    s = m + 1  # move right
                else: 
                    end = m - 1  # corrected
            return last         
        
        first = first_position(nums, target)
        last = last_position(nums, target)
        return [first, last]
    

# brute force 

class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                end = i
        return [start, end]
