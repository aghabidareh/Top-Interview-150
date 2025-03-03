class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size_of_array = len(nums)
        if size_of_array == 1:
            return nums[0]

        counter = 1
        nums.sort()

        for i in range(1, size_of_array):
            if nums[i - 1] == nums[i]:
                counter += 1
            else:
                if counter > size_of_array // 2:
                    return nums[i - 1]

        if counter > size_of_array // 2:
            return nums[i - 1]

        return None