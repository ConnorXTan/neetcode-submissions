# 1 1 2 3 5 
class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        for i in range(n - 1):
            temp = first
            first = second + first
            second = temp
        return first
