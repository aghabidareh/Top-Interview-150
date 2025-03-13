class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        prev0 = 2
        prev1 = 3

        for x in range(3, n):
            prev0, prev1 = prev1, prev0 + prev1

        return prev1