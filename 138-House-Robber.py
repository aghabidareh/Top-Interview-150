class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def check(ind):
            if ind < 0: return 0
            if DP[ind] != -1: return DP[ind]
            pick = nums[ind] + check(ind - 2)
            not_pick = 0 + check(ind - 1)
            DP[ind] = max(pick,not_pick)
            return max(pick, not_pick)
        DP = [-1] * n
        DP[0] = nums[0]
        return check(n-1)