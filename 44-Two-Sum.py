class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}

        for index , number in enumerate(nums):
            prefix = target - number

            if prefix in elements:
                return [elements[prefix] , index]

            elements[number] = index

        return []