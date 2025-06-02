# implement stack using two queues
from collections import deque
# leetcode 225
# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()
        
    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0