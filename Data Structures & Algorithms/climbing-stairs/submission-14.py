class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1 
        for i in range(n): 
            l, r = r, l + r
        return l