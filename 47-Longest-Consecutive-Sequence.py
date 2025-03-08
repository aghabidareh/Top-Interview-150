class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        number_set = set(nums)

        for n in number_set:
            if (n - 1) not in number_set:
                length = 1
                while (n + length) in number_set:
                    length += 1
                longest = max(longest, length)

        return longest