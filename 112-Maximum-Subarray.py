class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_list = [nums[0]]
        for i in range(1,len(nums)):
            if sum_list[i-1] < 0:
                sum_list.append(nums[i])
            else:
                sum_list.append(sum_list[i-1]+nums[i])
        return max(sum_list)