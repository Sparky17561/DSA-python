from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students = deque(students)
        count = 0

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.pop(0)
                count=0
            else:
                students.append(students.popleft())
                count+=1

        return count
            