class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 2:
                nums.remove(nums[i])
            else:
                i += 2
        return len(nums)