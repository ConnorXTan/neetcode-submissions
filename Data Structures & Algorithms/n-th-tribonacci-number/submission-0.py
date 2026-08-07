class Solution:
    def tribonacci(self, n: int) -> int:
        current = 2
        n0 = 0
        n1 = 1
        n2 = 1
        if n == 0: return n0
        if n == 1: return n1
        if n == 2: return n2
        for i in range(n-2):
            current = n0 + n1 + n2
            n0 = n1 
            n1 = n2 
            n2 = current
        return (current)
        