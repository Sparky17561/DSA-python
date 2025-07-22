# leetcode 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# 🧠 Intuition Behind the Logic:

# Water can only be trapped between bars.

# For each position, the water trapped = min(left_max, right_max) - current height

# This method avoids extra arrays by tracking lmax and rmax as we go from both sides inward.

# 🔍 Example Walkthrough

# Input:
# height = [0,1,0,2,1,0,1,3,2,1,2,1]


# Visualization:

# Position:      0  1  2  3  4  5  6  7  8  9 10 11
# Heights:       0  1  0  2  1  0  1  3  2  1  2  1
# Trapped Water: 0  0  1  0  1  2  1  0  0  1  0  0  = 6


# Explanation:

# At index 2: min(1,2) - 0 = 1

# At index 4: min(2,3) - 1 = 1

# At index 5: min(2,3) - 0 = 2

# At index 6: min(2,3) - 1 = 1

# At index 9: min(2,2) - 1 = 1

# → Total = 6

# ⏱️ Time and Space Complexity
# Time: O(n) → Each element is processed once.

# Space: O(1) → No extra arrays used.




class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Initialize two pointers: one from the left and one from the right
        l = 0
        r = len(height) - 1

        # Variables to keep track of the max height seen so far from the left and right
        lmax = 0
        rmax = 0

        # This will store the total trapped water
        drop = 0

        # Loop until the two pointers meet
        while l < r:
            # Always process the smaller height side first
            if height[l] < height[r]:
                # If current left height is greater than or equal to lmax, update lmax
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    # Water trapped = lmax - current height
                    drop += lmax - height[l]
                # Move left pointer rightward
                l += 1
            else:
                # Same logic, but for the right side
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    drop += rmax - height[r]
                # Move right pointer leftward
                r -= 1

        # Return the total water trapped
        return drop
