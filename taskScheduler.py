# leetcode 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

# 🧪 Example Walkthrough:

# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2

# Step-by-step:

# Frequency count:

# count = {"A": 3, "B": 3}
# max_freq = 3 (A and B both appear 3 times)

# max_count = 2 (A and B both have frequency = 3)

# Calculate slots:

# (total_slots) = (max_freq - 1) * (n + 1) + max_count
#               = (3 - 1) * (2 + 1) + 2
#               = 2 * 3 + 2
#               = 6 + 2 = 8


# Compare with len(tasks):

# max(len(tasks), total_slots) = max(6, 8) = 8

# ✅ Final Output:

# Output: 8

# 🧠 Explanation of schedule:

# You might visualize it like this:

# A B idle A B idle A B
# → Each 'A' is 2 units apart → constraint satisfied
# → 'idle' used only when needed
# → Total time = 8 units



class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        # Step 1: Count how many times each task appears
        count = {}  # Dictionary to store frequency of each task
        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] += 1

        # Step 2: Find the maximum frequency of any task
        max_freq = 0
        for freq in count.values():
            if freq > max_freq:
                max_freq = freq

        # Step 3: Count how many tasks have that maximum frequency
        max_count = 0
        for freq in count.values():
            if freq == max_freq:
                max_count += 1

        # Step 4: Calculate the least interval time
        # (max_freq - 1) = number of full groups or 'frames' between max frequent tasks
        # (n + 1) = length of each group: max task + n cooldowns
        # max_count = number of tasks with the same max frequency (they fill the last row)

        total_slots = (max_freq - 1) * (n + 1) + max_count

        # Step 5: Return the maximum of total tasks and the calculated slots
        # Why? Because if we have more tasks to fill all idle slots, no idles are needed
        return max(len(tasks), total_slots)
