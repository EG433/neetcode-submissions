class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1 
        for i in range(n - 1): 
            l, r = r, l + r
        return r

        1, 1, 2, 3, 5