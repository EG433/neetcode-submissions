class Solution:
    def climbStairs(self, n: int) -> int:
        l, r = 1, 1
        # 1, 1, 2, 3, 5, 
        for i in range(n):
            temp = l
            l = r
            r = temp + l
        return l