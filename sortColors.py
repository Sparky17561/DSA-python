# Dutch National Flag Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res=[]
        low,mid,high=0,0,len(nums)-1

        if len(nums)==1:
            return res

        while mid <= high:
            if nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[low] = nums[low],nums[mid]
                low+=1
                mid+=1

        return res