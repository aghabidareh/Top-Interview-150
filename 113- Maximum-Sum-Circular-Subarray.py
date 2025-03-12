class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minSum = nums[0]
        current_min = 0
        max_sum = nums[0]
        current_sum = 0
        total = 0
        for i in nums:
            current_sum = max(current_sum, 0)
            current_sum += i
            max_sum = max(current_sum, max_sum)
            current_min = min(current_min, 0)
            current_min += i
            minSum = min(minSum, current_min)
            total+=i
        if max_sum<0:
            return max_sum
        return max(total-minSum, max_sum)