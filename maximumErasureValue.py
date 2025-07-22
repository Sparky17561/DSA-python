# leetcode 1695. Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/

# 📘 Problem Statement:
# Given an array nums, find the maximum sum of a subarray that contains only unique elements.

# ✅ Example:

# nums = [4, 2, 4, 5, 6]

# Valid unique subarrays:

# [4, 2] → sum = 6

# [2, 4, 5, 6] → sum = 17 (maximum)

# [4, 5, 6] → sum = 15

# Expected Output: 17

# 🧠 Intuition:
# You're asked to find a sliding window where no duplicate values exist, and the sum is maximized.

# To do this:

# Use the two-pointer technique (left and right)

# Use a dictionary (window) to track the count of elements in the window

# Keep adding to the window from the right

# If you see a duplicate, shrink from the left until the duplicate is gone

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        window = {}     # Dictionary to keep track of elements in the current window
        left = 0        # Left pointer of the window
        max_t = 0       # Maximum sum found so far
        tot = 0         # Current sum of the window

        # Right pointer moves through the array
        for right in range(len(nums)):

            # If nums[right] is a duplicate, shrink window from left
            while nums[right] in window:
                window[nums[left]] -= 1       # Remove the element at left from window count
                tot -= nums[left]             # Subtract it from current sum
                if window[nums[left]] == 0:   # If it's fully removed, delete from window
                    del window[nums[left]]
                left += 1                     # Move left forward

            # Add current element to the window
            window[nums[right]] = window.get(nums[right], 0) + 1
            tot += nums[right]               # Add to current sum

            # Update max sum if needed
            max_t = max(max_t, tot)

        return max_t


# 🧪 Step-by-Step Walkthrough:
# Input:

# nums = [4, 2, 4, 5, 6]

# Iteration 1: right = 0, num = 4

# Not in window → add 4

# window = {4:1}, tot = 4, max_t = 4

# Iteration 2: right = 1, num = 2

# Not in window → add 2

# window = {4:1, 2:1}, tot = 6, max_t = 6

# Iteration 3: right = 2, num = 4

# 4 is duplicate → shrink from left

# remove 4 → window = {2:1}, tot = 2

# Add 4 again → window = {2:1, 4:1}, tot = 6, max_t = 6

# Iteration 4: right = 3, num = 5

# Not in window → add 5

# window = {2:1, 4:1, 5:1}, tot = 11, max_t = 11

# Iteration 5: right = 4, num = 6

# Not in window → add 6

# window = {2:1, 4:1, 5:1, 6:1}, tot = 17, max_t = 17

# ✅ Final Output:

# 17

# Time: O(n), because each element is added and removed at most once.

# Space: O(n), in the worst case when all elements are unique.