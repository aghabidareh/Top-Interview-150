class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        frequency = Counter(nums)
        size_of_array = len(nums)
        for (key, val) in frequency.items():
            if val > (size_of_array / 2):
                return key
        return None